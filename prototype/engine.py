"""Deterministic engine for "answer with its method". Every number comes from here, never from the interpreter.

Inputs: a run folder with data/manifest.json (Spectra export + loan book, with as-at dates).
"""
from __future__ import annotations
import copy, json, os, sys
from dataclasses import dataclass, field, asdict
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
import cxlens as cx  # noqa: E402

RATINGS = list('ABCDEFG')

# Sarah's defaults, from her methodology paper (run notes). Scenario names are resolved through the manifest.
AUDIENCE_DEFAULTS = {
    'committee': {'scenarios': ['central'], 'years': ['2050']},
    'pra': {'scenarios': ['central', 'severe'], 'years': ['2030', '2050']},
    'other': {'scenarios': ['central'], 'years': ['2050']},
}
DEFAULT_EXCLUSIONS = {'in_default': True, 'redeemed': True, 'maturing_before': 2030}  # Sarah's write-ups leave these out
DEFAULTED_FIELDS = ['scenarios', 'years', 'exclusions', 'unit', 'origination_source']


@dataclass
class Choices:
    measure: str = 'count'                 # count | loss | rise | share
    loan_type: str | None = None           # None = all loans
    hazards: list = field(default_factory=list)   # [] = all hazards
    rating_min: str | None = None          # e.g. 'E' (inclusive)
    rating_max: str | None = None          # e.g. 'G'
    scenarios: list = field(default_factory=list)  # friendly names: central / severe / low
    years: list = field(default_factory=list)      # for rise: [from, to]
    unit: str = 'loans'                    # loans | properties
    originated: list | None = None         # e.g. [2024, 2025]
    origination_source: str = 'loan_book'  # loan_book | spectra
    exclusions: dict = field(default_factory=lambda: dict(DEFAULT_EXCLUSIONS))
    group_by: list = field(default_factory=list)   # e.g. ['hazard', 'region']
    filters: dict = field(default_factory=dict)    # added dimensions, e.g. {'region': ['South East'], 'property_type': ['Office']}

    @staticmethod
    def from_dict(d):
        c = Choices(); [setattr(c, k, copy.deepcopy(v)) for k, v in d.items() if hasattr(c, k)]; return c


def defaults_for(audience: str) -> dict:
    a = AUDIENCE_DEFAULTS.get(audience, AUDIENCE_DEFAULTS['other'])
    return {'scenarios': list(a['scenarios']), 'years': list(a['years']), 'exclusions': dict(DEFAULT_EXCLUSIONS),
            'unit': 'loans', 'origination_source': 'loan_book'}


def departures(choices: Choices, sources: dict, audience: str) -> list:
    """Analyst changes away from Sarah's defaults. Choices the asker stated (source 'question') are not departures."""
    dflt = defaults_for(audience); out = []
    for f in DEFAULTED_FIELDS:
        if sources.get(f) == 'analyst' and getattr(choices, f) != dflt[f]:
            out.append({'field': f, 'default': dflt[f], 'chosen': getattr(choices, f)})
    return out


class Book:
    """Loaded data for one run: Spectra export joined to the loan book."""

    def __init__(self, run_dir: str):
        m = json.load(open(os.path.join(run_dir, 'data', 'manifest.json')))
        self.manifest = m
        self.scen_map = {k: v for k, v in m['scenario_names'].items() if k != 'note'}
        self.d = cx.load(os.path.join(run_dir, 'data', m['spectra_export']['file']))
        self.book = pd.read_csv(os.path.join(run_dir, 'data', m['loan_book']['file']), dtype={'redeemed_date': str})
        self.export_as_at = m['spectra_export']['as_at']; self.book_as_at = m['loan_book']['as_at']
        s = self.d.df.copy()
        b = self.book.rename(columns={'balance_gbp': 'book_balance_gbp', 'loan_type': 'book_loan_type'})
        self.df = s.merge(b, on='loan_id', how='left', indicator=True)
        self.df['matched'] = self.df['_merge'] == 'both'
        self.df['book_origination_year'] = pd.to_numeric(self.df.origination_date.str[:4], errors='coerce')
        self.df['maturity_year'] = pd.to_numeric(self.df.maturity_date.str[:4], errors='coerce')
        self.unmatched_in_book = self.book[~self.book.loan_id.isin(s.loan_id)]

    def ssp(self, friendly):
        return self.scen_map.get(friendly, friendly)

    @property
    def hazards(self):
        return self.d.hazards


def _rating_mask(frame, col, lo, hi):
    r = frame[col]
    m = r.notna()
    if lo: m &= r >= lo
    if hi: m &= r <= hi
    return m


def _population(bk: Book, c: Choices):
    """Apply loan type, origination and exclusions. Returns (included, excluded, unmatched)."""
    df = bk.df
    unmatched = df[~df.matched]
    pop = df[df.matched]
    excluded = []
    ex = c.exclusions or {}
    if ex.get('in_default'):
        m = pop.status == 'in default'; excluded.append(pop[m].assign(reason='in default')); pop = pop[~m]
    if ex.get('redeemed'):
        m = pop.status == 'redeemed'; excluded.append(pop[m].assign(reason=f'redeemed after the export date')); pop = pop[~m]
    if ex.get('maturing_before'):
        m = pop.maturity_year < ex['maturing_before']; excluded.append(pop[m].assign(reason=f"matures before {ex['maturing_before']}")); pop = pop[~m]
    if c.loan_type:
        pop = pop[pop.loan_type == c.loan_type]
        unmatched = unmatched[unmatched.loan_type == c.loan_type]
    for col, vals in (c.filters or {}).items():
        if vals:
            pop = pop[pop[col].isin(vals)]; unmatched = unmatched[unmatched[col].isin(vals)]
    excl = pd.concat(excluded) if excluded else df.iloc[0:0]
    if c.loan_type and len(excl):
        excl = excl[excl.loan_type == c.loan_type]
    for col, vals in (c.filters or {}).items():
        if vals and len(excl):
            excl = excl[excl[col].isin(vals)]
    return pop, excl, unmatched


def _orig_col(c: Choices):
    return 'book_origination_year' if c.origination_source == 'loan_book' else 'origination_year'


def _value(bk: Book, c: Choices, scen: str, year: str):
    """The headline value for one scenario and year. Returns a dict of numbers."""
    pop, _, _ = _population(bk, c)
    hz = c.hazards or bk.hazards
    S = bk.ssp(scen)
    if c.measure == 'count':
        cols = [bk.d.col(h, S, year, 'rating') for h in hz]
        frame = pop.drop_duplicates('property_id') if c.unit == 'properties' else pop
        hit = np.zeros(len(frame), bool)
        for col in cols:  # worst rating across the selected hazards
            hit |= _rating_mask(frame, col, c.rating_min, c.rating_max).to_numpy()
        return {'n': int(hit.sum()), 'of_n': int(len(frame)), 'balance': float(frame.loc[hit, 'balance_gbp'].sum()),
                'of_balance': float(frame.balance_gbp.sum())}
    if c.measure in ('loss', 'rise'):
        e = pop.drop_duplicates('property_id')
        L = e[[bk.d.col(h, S, year, 'loss_gbp') for h in hz]].sum(axis=1, min_count=1)
        out = {'loss': float(L.sum())}
        for g in c.group_by:
            if g == 'hazard':
                out['by_hazard'] = {h: float(e[bk.d.col(h, S, year, 'loss_gbp')].sum()) for h in hz}
            elif g in e.columns:
                out[f'by_{g}'] = {k: float(v) for k, v in L.groupby(e[g]).sum().sort_values(ascending=False).items()}
        return out
    if c.measure == 'share':
        oc = _orig_col(c)
        new = pop[pop[oc].isin(c.originated or [])]; old = pop[pop[oc] < min(c.originated or [9999])]
        cols = [bk.d.col(h, S, year, 'rating') for h in hz]
        def hi(frame):
            m = np.zeros(len(frame), bool)
            for col in cols: m |= _rating_mask(frame, col, c.rating_min, c.rating_max).to_numpy()
            return m
        nb, ob = new.loc[hi(new), 'balance_gbp'].sum(), old.loc[hi(old), 'balance_gbp'].sum()
        return {'balance': float(nb), 'share': float(nb / new.balance_gbp.sum()) if len(new) else np.nan,
                'of_balance': float(new.balance_gbp.sum()), 'older_share': float(ob / old.balance_gbp.sum()) if len(old) else np.nan}
    raise ValueError(f'unknown measure {c.measure}')


def _key(c: Choices, v: dict):
    return {'count': 'n', 'loss': 'loss', 'share': 'share'}.get(c.measure, 'loss')


def _plural(n, one, many):
    return f'{n:,} {one if n == 1 else many}'


def _money(x):
    return f'£{x/1e6:,.1f}m' if abs(x) >= 1e5 else f'£{x:,.0f}'


def _scen_label(s):
    return {'central': 'central', 'severe': 'severe', 'low': 'low-emissions'}.get(s, s)


def headline(bk: Book, c: Choices, scen, year, v=None):
    v = v or _value(bk, c, scen, year)
    sub = (c.loan_type + ' ' if c.loan_type else '').replace('Commercial real estate ', 'CRE ').replace('Residential mortgage ', 'mortgage ')
    where = '; '.join(f"{', '.join(v)}" for v in (c.filters or {}).values() if v)
    if where: sub = f'{sub}'; band_suffix = f' in {where}'
    else: band_suffix = ''
    unit = 'properties' if c.unit == 'properties' else 'loans'
    hz = ', '.join(c.hazards) if c.hazards else 'all hazards'
    band = (f'rated {hz} {c.rating_min} or worse' if c.rating_min and not c.rating_max else
            f'rated {hz} {c.rating_min} to {c.rating_max}' if c.rating_min else hz)
    if c.measure == 'count':
        return f"{v['n']:,} of {v['of_n']:,} {sub}{unit}{band_suffix}, {_money(v['balance'])} of {_money(v['of_balance'])} balance, {band} at {year} ({_scen_label(scen)})"
    if c.measure == 'loss':
        return f"{_money(v['loss'])} annual expected damage to properties{band_suffix}, {hz}, {year} ({_scen_label(scen)})"
    if c.measure == 'share':
        yrs = ' and '.join(str(y) for y in c.originated or [])
        return f"{_money(v['balance'])}, {v['share']:.1%} of {yrs} lending{band_suffix} ({_money(v['of_balance'])}), {band} at {year} ({_scen_label(scen)}), vs {v['older_share']:.1%} of the older book"
    return ''


def compute(bk: Book, c: Choices, question_years=None, question_text='') -> dict:
    scen_list = c.scenarios or ['central']
    years = c.years or [bk.d.years[-1]]
    res = {'grid': [], 'versions': [], 'checks': [], 'method_note': [], 'drivers': {}}
    if c.measure == 'rise':
        y0, y1 = (years + years)[:2] if len(years) >= 2 else (bk.d.years[0], years[-1])
        for s in scen_list:
            a, b = _value(bk, c, s, y0)['loss'], _value(bk, c, s, y1)['loss']
            res['grid'].append({'scenario': s, 'year': f'{y0}→{y1}', 'value': b / a if a else None,
                                'text': f'{_scen_label(s)}: {_money(a)} in {y0} → {_money(b)} in {y1} = {b/a:.2f}× (+{b/a-1:.0%})'})
        res['headline'] = res['grid'][0]['text']
        others = [s for s in bk.scen_map if s not in scen_list]
        vals = [res['grid'][0]['value']]
        for s in others:
            a, b = _value(bk, c, s, y0)['loss'], _value(bk, c, s, y1)['loss']
            res['versions'].append({'change': f'scenario → {_scen_label(s)}', 'text': f'{b/a:.2f}×', 'value': b / a})
            vals.append(b / a)
        res['versions_verdict'] = cx.verdict(vals, 'scenario')
    else:
        for s in scen_list:
            for y in years:
                v = _value(bk, c, s, y)
                res['grid'].append({'scenario': s, 'year': y, 'value': v[_key(c, v)], 'detail': v, 'text': headline(bk, c, s, y, v)})
        main = res['grid'][0]
        res['headline'] = main['text']
        if c.measure == 'loss':
            res['drivers'] = {k: v for k, v in main['detail'].items() if k.startswith('by_')}
        # one-change versions: other scenarios, other year, other counting unit
        s0, y0, base = main['scenario'], main['year'], main['value']
        groups = []; bal = {}
        sv = [(s, _value(bk, c, s, y0)) for s in bk.scen_map if s not in scen_list]
        if sv:
            for s, v in sv:
                res['versions'].append({'change': f'scenario → {_scen_label(s)}', 'text': headline(bk, c, s, y0, v), 'value': v[_key(c, v)]})
        # scenario verdict covers the selected scenarios (in the grid) and the others, at the main year
        sel = [g for g in res['grid'] if g['year'] == y0]
        if len(sel) + len(sv) > 1:
            groups.append(('scenario', [g['value'] for g in sel] + [v[_key(c, v)] for _, v in sv]))
            bal['scenario'] = [g['detail'].get('balance') for g in sel] + [v.get('balance') for _, v in sv]
        yv = [(y, _value(bk, c, s0, y)) for y in bk.d.years if y not in years]
        for y, v in yv:
            res['versions'].append({'change': f'year → {y}', 'text': headline(bk, c, s0, y, v), 'value': v[_key(c, v)]})
        if yv:
            groups.append(('year', [base] + [v[_key(c, v)] for _, v in yv]))
            bal['year'] = [main['detail'].get('balance')] + [v.get('balance') for _, v in yv]
        if c.measure == 'count':
            c2 = copy.deepcopy(c); c2.unit = 'properties' if c.unit == 'loans' else 'loans'
            v = _value(bk, c2, s0, y0)
            res['versions'].append({'change': f'count {c2.unit} instead', 'text': headline(bk, c2, s0, y0, v), 'value': v['n']})
            groups.append(('counting unit', [base, v['n']]))
            bal['counting unit'] = [main['detail'].get('balance'), v.get('balance')]
        res['verdicts'] = {}
        for g, vals in groups:
            v = cx.verdict(vals, g)
            b = [x for x in bal.get(g, []) if x is not None]
            if c.measure == 'count' and len(set(vals)) == 1 and len(set(round(x) for x in b)) > 1:
                v = f'Same count for every {g} ({vals[0]:,}), but different loans: balance ranges {_money(min(b))}–{_money(max(b))}'
            res['verdicts'][g] = v
        if c.measure == 'loss' and len(scen_list) and 'by_hazard' in main['detail']:
            tops = {s: max(_value(bk, c, s, y0)['by_hazard'].items(), key=lambda kv: kv[1])[0] for s in bk.scen_map}
            res['verdicts']['top hazard'] = 'Same top hazard in every scenario' if len(set(tops.values())) == 1 else f'Top hazard changes with scenario: {tops}'
    res['checks'] = checks(bk, c, question_years, question_text)
    res['method_note'] = method_note(bk, c)
    pop, excl, unm = _population(bk, c)
    res['counts'] = {'included': int(len(pop)), 'excluded': int(len(excl)), 'unmatched': int(len(unm)), 'unscored': _unscored(bk, c, pop)}
    if c.measure in ('count', 'share') and c.rating_min:
        sel = source_rows(bk, c)['Counted']
        rc = [x for x in sel.columns if x.endswith('_rating')]
        worst = sel[rc].max(axis=1) if rc else None
        res['rows'] = [{'loan_id': r.loan_id, 'property_type': r.property_type, 'region': r.region, 'balance': float(r.balance_gbp),
                        'rating': (worst.loc[i] if worst is not None else '')} for i, r in sel.sort_values('balance_gbp', ascending=False).head(25).iterrows()]
        res['rows_total'] = int(len(sel))
    return res


def _unscored(bk, c, pop):
    hz = c.hazards or bk.hazards
    cols = [bk.d.col(h, bk.ssp(s), y, 'rating') for h in hz for s in (c.scenarios or ['central']) for y in (c.years or [bk.d.years[-1]])]
    return int(pop[cols].isna().any(axis=1).sum())


def checks(bk: Book, c: Choices, question_years=None, question_text='') -> list:
    out = []
    qy = [str(y) for y in (question_years or [])]
    yrs = [str(y) for y in (c.years or [])]
    miss = [y for y in qy if y not in yrs]
    out.append({'name': 'Horizon matches the question', 'ok': not miss,
                'detail': f"Question asks about {', '.join(qy)}; answer uses {', '.join(yrs) or 'nothing'}" if miss else
                ('Matches ' + ', '.join(qy) if qy else 'Question names no year; default used')})
    stale = bk.export_as_at < bk.book_as_at
    red = int((bk.df.matched & (bk.df.status == 'redeemed')).sum())
    inc = not (c.exclusions or {}).get('redeemed')
    out.append({'name': 'Data is fresh', 'ok': not (stale and inc and red),
                'detail': (f'Spectra export ({bk.export_as_at}) is older than the loan book ({bk.book_as_at}); '
                           + (f'{red} loans redeemed since then are INCLUDED' if inc else f'{red} loans redeemed since then are excluded')) if stale else 'Export and loan book are from the same date'})
    out.append({'name': 'Scenario stated', 'ok': bool(c.scenarios),
                'detail': ', '.join(_scen_label(s) for s in c.scenarios) if c.scenarios else 'No scenario chosen: the note would not say which scenario was used'})
    pop, excl, unm = _population(bk, c)
    out.append({'name': 'Unmatched loans listed', 'ok': True, 'detail': f'{_plural(len(unm), "loan", "loans")} in the Spectra export not found in the loan book; excluded and listed on their own tab'})
    out.append({'name': 'Unscored loans listed', 'ok': True, 'detail': f'{_plural(_unscored(bk, c, pop), "loan has", "loans have")} no score for the hazard and year used; excluded from counts and listed'})
    out.append({'name': 'Counting basis stated', 'ok': bool(c.unit), 'detail': f'Counted per {c.unit[:-1] if c.unit else "?"}' + ('; £ damage counted once per property' if c.measure in ('loss', 'rise') else '')})
    if c.originated:
        out.append({'name': 'Origination date source', 'ok': c.origination_source == 'loan_book',
                    'detail': 'From the loan system, as your method says' if c.origination_source == 'loan_book' else 'From the Spectra export; your method takes origination from the loan system'})
    return out


def method_note(bk: Book, c: Choices) -> list:
    hz = ' and '.join(c.hazards) if c.hazards else 'all four hazards (' + ', '.join(bk.hazards) + ')'
    scen = ' and '.join(f'{_scen_label(s)} ({bk.ssp(s)})' for s in c.scenarios) if c.scenarios else 'NOT STATED'
    pop, excl, unm = _population(bk, c)
    ex = c.exclusions or {}
    exl = [x for x, on in [('loans in default', ex.get('in_default')), ('loans redeemed after the export date', ex.get('redeemed')),
                           (f"loans maturing before {ex.get('maturing_before')}", ex.get('maturing_before'))] if on]
    lines = [f"Scenario: {scen}. Horizon: {', '.join(c.years) if c.years else 'NOT STATED'}.",
             f"Hazards: {hz}" + (f"; rated {c.rating_min}{' to ' + c.rating_max if c.rating_max else ' or worse'}, worst rating across the hazards per loan." if c.rating_min else '.'),
             f"Population: {c.loan_type or 'all loans'}" + ''.join(f"; {k.replace('_', ' ')}: {', '.join(v)}" for k, v in (c.filters or {}).items() if v) + (f", originated {' and '.join(map(str, c.originated))} (origination date from the {'loan system' if c.origination_source == 'loan_book' else 'Spectra export'})" if c.originated else '') + '.',
             f"Excludes: {', '.join(exl) if exl else 'nothing'} ({len(excl)} loans).",
             f"Counting: per {c.unit[:-1]}" + ('; £ damage counted once per property even where it secures several loans.' if c.measure in ('loss', 'rise') else '.'),
             f"Data: Spectra export as at {bk.export_as_at}, joined to the loan book as at {bk.book_as_at} on loan ID; {len(unm)} loans didn't match and are listed separately.",
             "Balances are current balances, with no allowance for repayment." if c.measure in ('count', 'share') else
             "£ figures are annual expected damage to the properties, not loss to the bank."]
    return lines


def source_rows(bk: Book, c: Choices) -> dict:
    pop, excl, unm = _population(bk, c)
    keep = ['loan_id', 'property_id', 'loan_type', 'property_type', 'region', 'balance_gbp', 'status', 'origination_date', 'maturity_date']
    hz = c.hazards or bk.hazards
    rcols = [bk.d.col(h, bk.ssp(s), y, m) for h in hz for s in (c.scenarios or ['central']) for y in (c.years or [bk.d.years[-1]]) for m in ('rating', 'loss_gbp')]
    sel = pop
    if c.measure in ('count', 'share') and c.rating_min:
        m = np.zeros(len(pop), bool)
        s, y = bk.ssp((c.scenarios or ['central'])[0]), (c.years or [bk.d.years[-1]])[0]
        for h in hz: m |= _rating_mask(pop, bk.d.col(h, s, y, 'rating'), c.rating_min, c.rating_max).to_numpy()
        sel = pop[m]
    return {'Counted': sel[keep + rcols], 'Excluded': excl[[k for k in keep if k in excl.columns] + ['reason']] if len(excl) else excl,
            'Unmatched': unm[['loan_id', 'property_id', 'loan_type', 'balance_gbp']], 'Unscored': pop[pop[rcols].isna().any(axis=1)][keep + rcols]}
