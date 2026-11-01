"""Self-test for cxlens on a tiny synthetic file with known answers (no run data).

python3 tools/test_cxlens.py
"""
import os, sys, tempfile
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cxlens as cx

rows = []
# p1 has two loans (shared entity); p2 has one loan with a missing flood 2050 block
for loan, prop, seg, bal, val in [('L1', 'p1', 'A', 50, 100), ('L2', 'p1', 'A', 20, 100), ('L3', 'p2', 'B', 100, 200)]:
    r = {'loan_id': loan, 'property_id': prop, 'segment': seg, 'balance_gbp': bal, 'property_value_gbp': val}
    for h, pct in [('flood', 1.0), ('wind', 0.5)]:
        for s, k in [('ssp126', 1), ('ssp245', 2), ('ssp585', 4)]:
            for y, t in [('2030', 1), ('2050', 2)]:
                p = pct * k * t / 10
                r[f'{h}_{s}_{y}_damage_pct'] = p
                r[f'{h}_{s}_{y}_loss_gbp'] = p / 100 * val
                r[f'{h}_{s}_{y}_rating'] = 'A' if p < 0.2 else ('C' if p < 0.8 else 'E')
    rows.append(r)
df = pd.DataFrame(rows)
for m in ('damage_pct', 'loss_gbp', 'rating'):
    for s in ('ssp126', 'ssp245', 'ssp585'):
        df.loc[df.loan_id == 'L3', f'flood_{s}_2050_{m}'] = None

with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, 't.csv'); df.to_csv(path, index=False)
    d = cx.load(path)
    assert (d.row_id, d.entity_id, d.value_col, d.balance_col) == ('loan_id', 'property_id', 'property_value_gbp', 'balance_gbp')
    assert d.scenarios == ['ssp126', 'ssp245', 'ssp585'] and d.defaults['scenario'] == 'ssp245' and d.defaults['year'] == '2050'
    # p1 loss at ssp245 2050: flood 0.4% of 100 + wind 0.2% of 100 = 0.6; p2: wind only 0.2% of 200 = 0.4
    assert abs(cx.total(d) - 1.0) < 1e-9
    assert abs(cx.total(d, dedup=False) - 1.6) < 1e-9          # p1 counted twice
    assert abs(cx.total(d, weight='ltv') - (0.6 * .5 + 0.6 * .2 + 0.4 * .5)) < 1e-9
    tr = cx.trust(d)
    assert tr['loss_recompute']['cells_off_by_more_than_1'] == 0 and tr['loss_recompute']['basis'] == 'pct/100'
    assert tr['ordering']['violations'] == 0
    assert tr['missing']['rows_with_missing'] == 1 and tr['missing']['by_hazard_year'] == {'flood 2050': 1}
    assert tr['shared_entities']['extra_rows'] == 1
    t, v = cx.swing(d, cx.total, 'scenario')
    assert list(t.answer.round(9)) == [0.5, 1.0, 2.0] and '3 different answers' in v
    assert 'Same answer' in cx.verdict([4, 4, 4])
    assert '2 values give the same answer' in cx.verdict([4, 4, 8])
    # shape error on a file without the wide pattern
    bad = os.path.join(tmp, 'bad.csv'); pd.DataFrame({'a': [1], 'b': [2]}).to_csv(bad, index=False)
    try:
        cx.load(bad); raise AssertionError('expected ShapeError')
    except cx.ShapeError:
        pass
print('cxlens self-test: all passed')
