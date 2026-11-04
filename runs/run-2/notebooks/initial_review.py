"""Run 2 initial review: every number in RUN.md comes from this script."""
import pandas as pd
d = pd.read_csv('data/harbourside_mortgage_book_spectra_2026-10.csv', parse_dates=['origination_date'])
H = ['flood_river', 'flood_coastal', 'flood_surface', 'subsidence']; S = ['ssp245', 'ssp585']; Y = ['2030', '2050']
print('rows', len(d), 'unique loans', d.loan_id.nunique(), 'columns', d.shape[1])
dup = d[d.loan_id.duplicated(keep=False)]
print('duplicate loan ids', dup.loan_id.nunique(), '| identical rows:', d.duplicated().sum())
print('origination', d.origination_date.min().date(), 'to', d.origination_date.max().date())
print('postcode_district examples', d.postcode_district.drop_duplicates().head(5).tolist(), 'unique', d.postcode_district.nunique())
miss = d[[c for c in d.columns if c.endswith('_rating')]].isna().all(axis=1)
print('loans with no Spectra scores at all:', int(miss.sum()), '| no property value / LTV:', int(d.ltv.isna().sum()))
print('no scores, by origination year:', d[miss].origination_date.dt.year.value_counts().sort_index().to_dict())
print('duplicate rows differ in:', [c for c in d.columns if d[d.loan_id.duplicated(keep=False)].groupby('loan_id')[c].nunique(dropna=False).max() > 1])
u = d.drop_duplicates('loan_id')
print('balance £m', round(u.balance_gbp.sum() / 1e6, 1), '| broker share', round((u.channel == 'Broker').mean(), 3))
# recent lending: proxy for applications that reach offer
for p in ['2025-11-01', '2026-04-01']:
    r = u[u.origination_date >= p]; print(f'originated since {p}:', len(r))
print('loans per month, last 12 months:', round(len(u[u.origination_date >= '2025-11-01']) / 12, 1))
# ratings an underwriter could see: worst rating across hazards, per scenario and year
order = {c: i for i, c in enumerate('ABCDEFG')}
def worst(s, y): return u[[f'{h}_{s}_{y}_rating' for h in H]].apply(lambda r: max((x for x in r if isinstance(x, str)), key=order.get, default=None), axis=1)
for s in S:
    for y in Y:
        w = worst(s, y); poor = w.isin(list('EFG'))
        print(f'{s} {y}: worst rating E-G on any hazard: {poor.sum()} loans ({poor.mean():.1%}), £{u.balance_gbp[poor].sum()/1e6:.0f}m balance')
w = worst('ssp245', '2050'); u = u.assign(worst245_2050=w)
print('which hazard drives E-G (ssp245 2050):', {h: int(u[f'{h}_ssp245_2050_rating'].isin(list('EFG')).sum()) for h in H})
print('loss £ a year by hazard, ssp245 2050:', {h: round(u[f'{h}_ssp245_2050_loss_gbp'].sum()) for h in H})
print('loss £ a year by hazard, ssp585 2050:', {h: round(u[f'{h}_ssp585_2050_loss_gbp'].sum()) for h in H})
# do the 4 hazards x 2 scenarios x 2 years give one loan different answers?
lo = pd.concat([worst(s, y) for s in S for y in Y], axis=1).dropna()
spread = lo.apply(lambda r: max(order[x] for x in r if isinstance(x, str)) - min(order[x] for x in r if isinstance(x, str)), axis=1)
print('loans whose worst rating differs by 2+ bands across scenario/year:', int((spread >= 2).sum()))
# recent vs older lending, and new build
rec = u.origination_date >= '2024-01-01'
for name, m in [('since 2024', rec), ('before 2024', ~rec), ('new build', u.new_build == 'Y'), ('not new build', u.new_build == 'N')]:
    print(f'{name}: {m.sum()} loans, E-G (ssp245 2050) {u.worst245_2050[m].isin(list("EFG")).mean():.1%}')
hi = (u.ltv > 0.85) & u.worst245_2050.isin(list('EFG'))
print('LTV over 85% and rated E-G (ssp245 2050):', int(hi.sum()), f'£{u.balance_gbp[hi].sum()/1e6:.1f}m')
top = u.groupby('postcode_district').agg(n=('loan_id', 'size'), poor=('worst245_2050', lambda x: x.isin(list('EFG')).sum())).sort_values('poor', ascending=False).head(5)
print('districts with most E-G loans:', top.to_dict('index'))
print('share of E-G loans in top 5 districts:', round(top.poor.sum() / u.worst245_2050.isin(list('EFG')).sum(), 3))
sc = u[[c for c in u.columns if c.endswith('_rating')]].notna().any(axis=1)
print('2026 originations:', int((u.origination_date.dt.year == 2026).sum()), '| of them unscored:', int(((u.origination_date.dt.year == 2026) & ~sc).sum()))
print('latest scored origination:', u[sc].origination_date.max().date(), '| earliest unscored:', u[~sc].origination_date.min().date())
# Headline candidate: share of new lending (by balance) rated E-G for subsidence, central vs severe, 2050
for since in ['2024-01-01', '2026-03-01']:
    n = u[u.origination_date >= since]
    for s in S:
        poor = n[f'subsidence_{s}_2050_rating'].isin(list('EFG'))
        print(f'since {since}, {s} 2050: subsidence E-G {poor.sum()} loans, {n.balance_gbp[poor].sum() / n.balance_gbp[n[f"subsidence_{s}_2050_rating"].notna()].sum():.1%} of scored balance')
