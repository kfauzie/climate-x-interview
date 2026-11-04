"""cxlens: a fast, reusable toolkit for pm-1-data-discovery on wide climate-risk exports.

General code only. It never stores run data, findings or defaults; those belong in each run's RUN.md.

Works on files whose risk columns follow  <hazard>_<scenario>_<year>_<metric>
(e.g. flood_ssp245_2050_loss_gbp). If the file doesn't match, load() raises
ShapeError and the analysis has to be written by hand instead.

CLI:
    python3 tools/cxlens.py profile <csv> [--out report.md]
Python:
    import sys; sys.path.insert(0, 'tools'); import cxlens as cx
    d = cx.load('runs/run-N/data/file.csv')
    cx.total(d, scenario='ssp245', year='2050')
    cx.count(d, where={'loan_type': 'Commercial real estate'}, hazard='flood', rating_at_least='E')
    cx.swing(d, cx.total, 'scenario')      # one dimension varied, the rest held at defaults
"""
from __future__ import annotations
import argparse, re, sys, time
from dataclasses import dataclass, field
import numpy as np
import pandas as pd

# Hazards can be one word or several (flood, flood_river, flood_surface); scenarios are one token (ssp245, central).
RISK_RE = re.compile(r'^(?P<hazard>[a-z]+(?:_[a-z]+)*)_(?P<scenario>[a-z]+\d*|[a-z0-9]+)_(?P<year>\d{4})_(?P<metric>[a-z_]+)$')


class ShapeError(ValueError):
    """The file doesn't match the expected wide layout. Fall back to a hand-written analysis."""


@dataclass
class Data:
    df: pd.DataFrame
    path: str
    row_id: str | None
    entity_id: str | None
    value_col: str | None
    balance_col: str | None
    segments: list[str]
    hazards: list[str]
    scenarios: list[str]
    years: list[str]
    metrics: list[str]
    risk_cols: list[str]
    defaults: dict = field(default_factory=dict)
    detected: dict = field(default_factory=dict)

    @property
    def entities(self) -> pd.DataFrame:
        """One row per entity (e.g. property), so entity-level risk is counted once."""
        return self.df.drop_duplicates(self.entity_id) if self.entity_id else self.df

    def col(self, hazard, scenario, year, metric):
        return f'{hazard}_{scenario}_{year}_{metric}'


def _order_scenarios(names):
    nums = [re.findall(r'\d+', n) for n in names]
    if all(nums):
        return sorted(names, key=lambda n: int(re.findall(r'\d+', n)[0])), True
    return sorted(names), False


def load(path, **override) -> Data:
    """Load a wide export and detect its structure. Pass overrides (row_id=..., entity_id=..., value_col=...) if detection is wrong."""
    df = pd.read_csv(path)
    risk = [c for c in df.columns if RISK_RE.match(c)]
    if len(risk) < 4:
        raise ShapeError(f'Only {len(risk)} columns match <hazard>_<scenario>_<year>_<metric>. Write this analysis by hand.')
    unread = [c for c in df.columns if re.search(r'_\d{4}_', c) and c not in risk]
    if unread:  # never silently misread risk columns as categories
        raise ShapeError(f'{len(unread)} columns look like risk columns but do not match the layout (e.g. {unread[:3]}). Write this analysis by hand.')
    parts = pd.DataFrame([RISK_RE.match(c).groupdict() for c in risk])
    scen, ordered = _order_scenarios(sorted(parts.scenario.unique()))
    other = [c for c in df.columns if c not in risk]
    ids = [c for c in other if c.endswith('_id') or c == 'id']
    row_id = next((c for c in ids if df[c].is_unique), None)
    entity_id = next((c for c in ids if not df[c].is_unique), None)
    num = [c for c in other if pd.api.types.is_numeric_dtype(df[c])]
    value_col = next((c for c in num if 'value' in c), None)
    balance_col = next((c for c in num if any(k in c for k in ('balance', 'exposure', 'outstanding'))), None)
    segs = [c for c in other if (pd.api.types.is_string_dtype(df[c]) or df[c].dtype == object) and c not in ids and 2 <= df[c].nunique() <= 20]
    d = Data(df=df, path=path, row_id=override.get('row_id', row_id), entity_id=override.get('entity_id', entity_id),
             value_col=override.get('value_col', value_col), balance_col=override.get('balance_col', balance_col),
             segments=override.get('segments', segs), hazards=sorted(parts.hazard.unique()), scenarios=scen,
             years=sorted(parts.year.unique()), metrics=sorted(parts.metric.unique()), risk_cols=risk)
    d.detected = {'scenarios_ordered_by_number': ordered}
    mid = d.scenarios[len(d.scenarios) // 2]
    loss_metric = next((m for m in d.metrics if m.startswith('loss')), None)
    d.defaults = {'scenario': mid, 'year': d.years[-1], 'hazards': d.hazards, 'dedup': True, 'loss_metric': loss_metric}
    return d


# ---------- core calculations (deterministic) ----------

def _filter(d: Data, frame: pd.DataFrame, where: dict | None):
    if not where:
        return frame
    m = pd.Series(True, index=frame.index)
    for k, v in where.items():
        m &= frame[k].isin(v) if isinstance(v, (list, tuple, set)) else (frame[k] == v)
    return frame[m]


def total(d: Data, scenario=None, year=None, hazards=None, dedup=None, where=None, metric=None, weight=None):
    """Sum of a loss metric across hazards. dedup=True counts each entity once. weight='ltv' multiplies by balance/value (an assumption)."""
    df_ = d.defaults
    scenario = scenario or df_['scenario']; year = year or df_['year']; hazards = hazards or df_['hazards']
    dedup = df_['dedup'] if dedup is None else dedup; metric = metric or df_['loss_metric']
    # LTV weighting is a per-loan share of the entity's loss, so it always works on rows, never deduplicated entities
    frame = _filter(d, d.df if (weight == 'ltv' or not dedup) else d.entities, where)
    s = frame[[d.col(h, scenario, year, metric) for h in hazards]].sum(axis=1, min_count=1)
    if weight == 'ltv':
        s = s * frame[d.balance_col] / frame[d.value_col]
    return float(s.sum())


def count(d: Data, hazard, rating_at_least, scenario=None, year=None, where=None, unit='rows', measure=None):
    """How many rows (or entities) have hazard rating >= a band. measure='balance' sums the balance instead."""
    scenario = scenario or d.defaults['scenario']; year = year or d.defaults['year']
    frame = _filter(d, d.entities if unit == 'entities' else d.df, where)
    r = frame[d.col(hazard, scenario, year, 'rating')]
    hit = frame[r >= rating_at_least]
    if measure == 'balance':
        return float(hit[d.balance_col].sum())
    return int(len(hit))


def loss_rate_bp(d: Data, by: str, **kw):
    """Loss as basis points of entity value, by segment (absolute and normalised side by side)."""
    e = d.entities
    out = []
    for g, frame in e.groupby(by):
        L = total(d, where={by: g}, **kw)
        V = float(frame[d.value_col].sum())
        out.append([g, len(frame), V, L, L / V * 1e4 if V else np.nan])
    t = pd.DataFrame(out, columns=[by, 'entities', 'value', 'loss', 'rate_bp']).set_index(by)
    t['share_loss'] = t.loss / t.loss.sum(); t['share_value'] = t.value / t.value.sum()
    t['rank_loss'] = t.loss.rank(ascending=False).astype(int); t['rank_rate'] = t.rate_bp.rank(ascending=False).astype(int)
    return t.sort_values('loss', ascending=False)


def swing(d: Data, fn, dim: str, values=None, **fixed):
    """Vary ONE dimension (scenario, year, dedup, hazards, weight, unit), hold the rest fixed. Returns a table and a computed verdict."""
    if values is None:
        values = {'scenario': d.scenarios, 'year': d.years, 'dedup': [True, False],
                  'hazards': [[h] for h in d.hazards], 'unit': ['rows', 'entities'], 'weight': [None, 'ltv']}[dim]
    base_kw = dict(fixed)
    rows = []
    for v in values:
        kw = dict(base_kw); kw[dim] = v
        rows.append(['none' if v is None else ('+'.join(v) if isinstance(v, list) else v), fn(d, **kw)])
    t = pd.DataFrame(rows, columns=[dim, 'answer'])
    ref_kw = dict(base_kw)
    ref = fn(d, **ref_kw) if dim not in base_kw else None
    ref = ref if ref else t.answer.iloc[len(t) // 2]
    t['x_ref'] = (t.answer / ref).round(3) if ref else np.nan
    return t, verdict(t.answer.tolist(), dim)


def verdict(values, dim='choice'):
    """Plain-language verdict computed from the numbers, so claims are never over- or understated by hand."""
    vals = [v for v in values if v is not None and not (isinstance(v, float) and np.isnan(v))]
    distinct = len(set(round(v, 6) for v in vals))
    if distinct == 1:
        return f'Same answer for every {dim} ({vals[0]:,.6g}): this choice does not change the answer'
    lo, hi = min(vals), max(vals)
    same = len(vals) - distinct + 1 if distinct < len(vals) else 0
    if lo:
        msg = f'{distinct} different answers across {len(vals)} {dim} values; highest is {hi / lo:.2f}x the lowest'
    else:
        msg = f'{distinct} different answers across {len(vals)} {dim} values; ranges from 0 to {hi:,.6g}'
    if same:
        msg += f'; {same} values give the same answer'
    return msg


def rise(d: Data, scenario, year_from, year_to, **kw):
    a, b = total(d, scenario=scenario, year=year_from, **kw), total(d, scenario=scenario, year=year_to, **kw)
    return {'from': a, 'to': b, 'ratio': b / a if a else np.nan}


def top_driver(d: Data, by: str, **kw):
    """Which hazard or segment drives the total, and whether that answer is stable across scenarios."""
    out = {}
    for s in d.scenarios:
        kw2 = dict(kw); kw2['scenario'] = s
        if by == 'hazard':
            out[s] = max(d.hazards, key=lambda h: total(d, hazards=[h], **kw2))
        else:
            out[s] = loss_rate_bp(d, by, **kw2).loss.idxmax()
    stable = len(set(out.values())) == 1
    return out, ('Same driver in every scenario' if stable else 'Driver changes with scenario')


# ---------- trust checks ----------

def trust(d: Data) -> dict:
    df, r = d.df, {}
    dmg = next((m for m in d.metrics if 'damage' in m or 'pct' in m), None)
    lm = d.defaults['loss_metric']
    if dmg and lm and d.value_col:
        diffs = {}
        for basis, f in (('pct/100', 1 / 100), ('fraction', 1)):
            mx = 0.0; off = 0
            for h in d.hazards:
                for s in d.scenarios:
                    for y in d.years:
                        x = (df[d.col(h, s, y, lm)] - df[d.col(h, s, y, dmg)] * f * df[d.value_col]).abs()
                        mx = max(mx, x.max()); off += int((x > 1).sum())
            diffs[basis] = (off, mx)
        best = min(diffs, key=lambda k: diffs[k][0])
        r['loss_recompute'] = {'basis': best, 'cells_off_by_more_than_1': diffs[best][0], 'max_diff': round(float(diffs[best][1]), 2)}
    if 'rating' in d.metrics and dmg:
        long = pd.concat([pd.DataFrame({'r': df[d.col(h, s, y, 'rating')], 'v': df[d.col(h, s, y, dmg)]})
                          for h in d.hazards for s in d.scenarios for y in d.years], ignore_index=True).dropna()
        b = long.groupby('r').v.agg(['min', 'max', 'count'])
        overlaps = int(sum(b['max'].iloc[i] >= b['min'].iloc[i + 1] for i in range(len(b) - 1)))
        r['rating_bands'] = {'bands': b.round(4).to_dict('index'), 'overlapping_bands': overlaps}
    if dmg:
        viol = 0; checks = 0
        for h in d.hazards:
            for s in d.scenarios:
                for a, bb in zip(d.years, d.years[1:]):
                    viol += int((df[d.col(h, s, bb, dmg)] < df[d.col(h, s, a, dmg)]).sum()); checks += 1
            if d.detected.get('scenarios_ordered_by_number'):
                for y in d.years:
                    for a, bb in zip(d.scenarios, d.scenarios[1:]):
                        viol += int((df[d.col(h, bb, y, dmg)] < df[d.col(h, a, y, dmg)]).sum()); checks += 1
        r['ordering'] = {'violations': viol, 'checks': checks, 'scenario_order_known': d.detected.get('scenarios_ordered_by_number')}
    nn = df[d.risk_cols].isna(); miss = nn.any(axis=1)
    blocks = nn[miss].T.groupby(lambda c: tuple(RISK_RE.match(c).group('hazard', 'year'))).all().T
    r['missing'] = {'rows_with_missing': int(miss.sum()), 'share': float(miss.mean()),
                    'attribute_nulls': int(df.drop(columns=d.risk_cols).isna().sum().sum()),
                    'by_hazard_year': {f'{k[0]} {k[1]}': int(v) for k, v in blocks.sum().items() if v},
                    'balance_affected': float(df.loc[miss, d.balance_col].sum()) if d.balance_col else None}
    if d.entity_id:
        m = df[d.entity_id].value_counts(); sh = m[m > 1]
        r['shared_entities'] = {'entities_with_multiple_rows': int(len(sh)), 'rows_on_them': int(sh.sum()),
                                'extra_rows': int(len(df) - df[d.entity_id].nunique()),
                                'rows_per_shared_entity': {int(k): int(v) for k, v in sh.value_counts().sort_index().items()}}
    if 'postcode' in df.columns:
        pc = df.postcode.astype(str); ok = pc.str.fullmatch(r'[A-Z]{1,2}\d[A-Z\d]? \d[A-Z]{2}')
        bad = pc[~ok]; norm = pc.str.strip().str.upper().str.replace(' ', '')
        r['postcodes'] = {'non_standard': int((~ok).sum()), 'stray_spaces': int((bad != bad.str.strip()).sum()),
                          'lowercase': int((bad.str.strip() != bad.str.strip().str.upper()).sum()),
                          'no_inner_space': int((~bad.str.strip().str.contains(' ')).sum()),
                          'invalid_after_normalising': int((~norm.str.fullmatch(r'[A-Z]{1,2}\d[A-Z\d]?\d[A-Z]{2}')).sum())}
    if d.balance_col and d.value_col:
        ltv = df[d.balance_col] / df[d.value_col]
        r['bounds'] = {'ltv_min': round(float(ltv.min()), 3), 'ltv_max': round(float(ltv.max()), 3), 'ltv_over_100pct': int((ltv > 1).sum()),
                       'balance_max_over_median': round(float(df[d.balance_col].max() / df[d.balance_col].median()), 1)}
    return r


def concentration(d: Data, **kw):
    out = {}
    if d.balance_col:
        s = d.df[d.balance_col].sort_values(ascending=False); k = int(np.ceil(len(s) * .01)); T = s.sum()
        top = d.df.loc[s.index[0]]
        out['balance'] = {'top_row': top[d.row_id] if d.row_id else s.index[0], 'top_share': s.iloc[0] / T,
                          'top_1pct_share': s.head(k).sum() / T, 'top_10_share': s.head(10).sum() / T, 'k_1pct': k}
    lm = kw.get('metric') or d.defaults['loss_metric']
    e = d.entities.copy()
    sc = kw.get('scenario', d.defaults['scenario']); yr = kw.get('year', d.defaults['year'])
    L = e[[d.col(h, sc, yr, lm) for h in d.hazards]].sum(axis=1).sort_values(ascending=False); T = L.sum()
    k = int(np.ceil(len(L) * .01)); top = e.loc[L.index[0]]
    out['loss'] = {'top_entity': top[d.entity_id] if d.entity_id else L.index[0], 'top_share': L.iloc[0] / T,
                   'top_1pct_share': L.head(k).sum() / T, 'top_10_share': L.head(10).sum() / T, 'k_1pct': k,
                   'top_entity_attrs': {c: (top[c].item() if hasattr(top[c], 'item') else top[c]) for c in d.segments + ([d.value_col] if d.value_col else [])}}
    return out


# ---------- one-shot profile report ----------

def profile(d: Data) -> str:
    t0 = time.time(); L = []
    w = L.append
    df = d.df
    w(f'# cxlens profile: `{d.path}`\n')
    w(f'- Rows: {len(df):,} | columns: {df.shape[1]} | risk columns: {len(d.risk_cols)}')
    w(f'- Row id: `{d.row_id}` ({df[d.row_id].nunique() if d.row_id else "-"} unique) | entity id: `{d.entity_id}` ({df[d.entity_id].nunique() if d.entity_id else "-"} unique)')
    w(f'- Value: `{d.value_col}` | balance: `{d.balance_col}` | segments: {", ".join(f"`{s}`" for s in d.segments)}')
    w(f'- Dimensions: hazards {d.hazards} × scenarios {d.scenarios} × years {d.years} × metrics {d.metrics}')
    w(f'- Defaults used below (state them with every number): scenario `{d.defaults["scenario"]}`, year `{d.defaults["year"]}`, all hazards summed, each entity counted once\n')
    for s in d.segments:
        w(f'  - `{s}`: {df[s].value_counts().to_dict()}')
    w('\n## Trust checks')
    for k, v in trust(d).items():
        w(f'- **{k}**: {v}')
    w('\n## Judgment calls (one dimension at a time)')
    base = total(d); w(f'- Baseline total `{d.defaults["loss_metric"]}`: **{base:,.0f}**')
    for dim in ['scenario', 'year', 'dedup', 'hazards'] + (['weight'] if d.balance_col and d.value_col else []):
        t, v = swing(d, total, dim)
        w(f'- **{dim}**: ' + '; '.join(f'{a}: {b:,.0f} ({x}×)' for a, b, x in t.itertuples(index=False)) + f'  → {v}')
    w('\n## Shape')
    c = concentration(d)
    for k, v in c.items():
        w(f'- **{k}**: ' + ', '.join(f'{a}: {b:.2%}' if isinstance(b, float) and b < 1.5 else f'{a}: {b}' for a, b in v.items()))
    for s in d.segments:
        t = loss_rate_bp(d, s)
        flips = t[(t.rank_loss - t.rank_rate).abs() >= 3]
        w(f'\n**By `{s}`** (abs vs rate):')
        w(t[['entities', 'loss', 'share_loss', 'share_value', 'rate_bp', 'rank_loss', 'rank_rate']].round(3).to_markdown())
        if len(flips):
            w(f'- Ranks disagree by 3+ places: {", ".join(f"{i} (£ #{int(r.rank_loss)}, rate #{int(r.rank_rate)})" for i, r in flips.iterrows())}')
    hz = pd.DataFrame({h: [total(d, scenario=s, hazards=[h]) for s in d.scenarios] for h in d.hazards}, index=d.scenarios)
    w('\n**Loss by hazard × scenario** (latest year):'); w(hz.round(0).astype(int).to_markdown())
    w(f'\n_Computed in {time.time() - t0:.1f}s by cxlens. Frame, limits, implications and questions are judgment: write them from this._')
    return '\n'.join(L)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['profile']); ap.add_argument('csv'); ap.add_argument('--out')
    a = ap.parse_args()
    try:
        rep = profile(load(a.csv))
    except ShapeError as e:
        sys.exit(f'ShapeError: {e}')
    if a.out:
        open(a.out, 'w').write(rep)
    print(rep)
