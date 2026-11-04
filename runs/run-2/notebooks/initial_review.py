"""Run 2 initial review (pm-1): changed, concentrated, missing or odd. Every number in RUN.md comes from here."""
import pandas as pd
d = pd.read_csv('runs/run-2/data/harbourside_mortgage_book_spectra_2026-10.csv', parse_dates=['origination_date'])
H = ['flood_river', 'flood_coastal', 'flood_surface', 'subsidence']; S = {'central': 'ssp245', 'severe': 'ssp585'}; BAD = list('EFG')
u = d.sort_values('origination_date').drop_duplicates('loan_id', keep='last')      # latest row per loan
scored = u[f'subsidence_ssp245_2050_rating'].notna()
print(f'rows {len(d)}, loans {len(u)}, balance £{u.balance_gbp.sum()/1e6:.0f}m, completed {u.origination_date.min():%b %Y} to {u.origination_date.max():%b %Y}')

def share(frame, hz, s, y='2050'):
    f = frame[frame[f'{hz[0]}_{S[s]}_{y}_rating'].notna()]
    bad = f[[f'{h}_{S[s]}_{y}_rating' for h in hz]].isin(BAD).any(axis=1)
    return bad.mean(), f.balance_gbp[bad].sum() / f.balance_gbp.sum()

print('\n# What has changed: completed since 2024 vs before (rated E-G in 2050)')
rec, old = u[u.origination_date >= '2024-01-01'], u[u.origination_date < '2024-01-01']
for hz in [[h] for h in H] + [H]:
    for s in S:
        (rc, rv), (oc, ov) = share(rec, hz, s), share(old, hz, s)
        print(f'{"+".join(hz) if len(hz) < 4 else "any hazard":14} {s:8} recent {rc:5.1%} of loans / {rv:5.1%} of balance | before {oc:5.1%} / {ov:5.1%}')
print('by year completed, subsidence E-G share of balance (central 2050):',
      {y: f'{share(u[u.origination_date.dt.year == y], ["subsidence"], "central")[1]:.0%}' for y in range(2019, 2027)})

print('\n# What is concentrated (central 2050)')
loss = {h: u[f'{h}_ssp245_2050_loss_gbp'].sum() for h in H}; tot = sum(loss.values())
print('share of expected loss a year by hazard:', {h: f'{v/tot:.0%}' for h, v in loss.items()}, f'total £{tot/1e6:.1f}m')
sub = u[u.subsidence_ssp245_2050_rating.isin(BAD)]
by = sub.groupby('postcode_district').balance_gbp.sum().sort_values(ascending=False)
print(f'subsidence E-G: {len(sub)} loans, £{sub.balance_gbp.sum()/1e6:.0f}m; top 5 districts hold {by.head(5).sum()/by.sum():.0%} of it: {list(by.head(5).index)}')
print('top 5 districts share of all lending balance:', f'{u[u.postcode_district.isin(by.head(5).index)].balance_gbp.sum()/u.balance_gbp.sum():.0%}')
print('subsidence E-G share of balance by channel:', {c: f'{share(u[u.channel == c], ["subsidence"], "central")[1]:.0%}' for c in ['Broker', 'Direct']})
print('by new build:', {c: f'{share(u[u.new_build == c], ["subsidence"], "central")[1]:.0%}' for c in ['Y', 'N']})

print('\n# What is missing or odd')
print('loans with no Spectra scores:', int((~scored).sum()), f'(£{u.balance_gbp[~scored].sum()/1e6:.0f}m); completed from', u[~scored].origination_date.min().date(), '| last scored completion', u[scored].origination_date.max().date())
dup = d[d.loan_id.duplicated(keep=False)].sort_values(['loan_id', 'origination_date'])
print('loan IDs on two rows:', dup.loan_id.nunique(), '| differ in:', [c for c in d.columns if dup.groupby('loan_id')[c].nunique(dropna=False).max() > 1])
print('balance counted twice if rows are summed: £', round(d.balance_gbp.sum() - u.balance_gbp.sum()))
print('no property value or LTV:', int(u.ltv.isna().sum()))
print('columns:', [c for c in d.columns if not any(c.startswith(h) for h in H)])

print('\n# First five rows (key columns)')
cols = ['loan_id', 'origination_date', 'postcode_district', 'property_type', 'new_build', 'channel', 'balance_gbp', 'ltv',
        'subsidence_ssp245_2050_rating', 'subsidence_ssp245_2050_damage_pct', 'subsidence_ssp245_2050_loss_gbp']
print(d[cols].head(5).to_string(index=False), f'\n{d.shape[1] - len(cols)} columns left out')
