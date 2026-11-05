"""Run 3 initial review (pm-1): changed, concentrated, missing or odd. Every number in RUN.md comes from here."""
import pandas as pd
d = pd.read_csv('runs/run-3/data/northwind_renewables_spectra_infra_2026-09.csv')
H = ['flood_river', 'flood_surface', 'extreme_heat', 'wildfire', 'windstorm']; S = {'central': 'ssp245', 'severe': 'ssp585'}; BAD = list('EFG')
print(f'sites {len(d)}, unique {d.site_id.nunique()}, value £{d.asset_value_gbp.sum()/1e6:.0f}m, {d.capacity_mw.sum():.0f} MW, commissioned {d.commissioned.min()}-{d.commissioned.max()}')
print(d.groupby(['country', 'asset_type']).size().unstack(fill_value=0).to_dict('index'))
def loss(s, y, hz=H, f=d): return f[[f'{h}_{S[s]}_{y}_loss_gbp' for h in hz]].sum(axis=1)
def worst_bad(s, y, f=d): return f[[f'{h}_{S[s]}_{y}_rating' for h in H]].isin(BAD).any(axis=1)

print('\n# What changes (2030 -> 2050)')
for s in S:
    a, b = loss(s, '2030').sum(), loss(s, '2050').sum()
    print(f'{s}: total £{a/1e6:.1f}m -> £{b/1e6:.1f}m a year ({b/a:.2f}x); sites with any E-G: {worst_bad(s,"2030").sum()} -> {worst_bad(s,"2050").sum()}')
for h in H:
    a, b = d[f'{h}_ssp245_2050_loss_gbp'].sum(), d[f'{h}_ssp585_2050_loss_gbp'].sum()
    print(f'  {h:13} 2050 central £{a/1e6:.2f}m, severe £{b/1e6:.2f}m ({b/a:.2f}x)')
print('loss rate (central 2050, % of value) by commissioning:', {k: f'{loss("central","2050",f=g).sum()/g.asset_value_gbp.sum():.2%}' for k, g in d.groupby(pd.cut(d.commissioned, [2013, 2018, 2021, 2024], labels=['2014-18', '2019-21', '2022-24']), observed=True)})

print('\n# What is concentrated (central 2050)')
L = loss('central', '2050'); d['L'] = L; d['rate'] = L / d.asset_value_gbp
print(f'total £{L.sum()/1e6:.1f}m a year = {L.sum()/d.asset_value_gbp.sum():.2%} of value')
top = d.sort_values('L', ascending=False)
print(f'top 10 sites: {top.L.head(10).sum()/L.sum():.0%} of loss, {top.asset_value_gbp.head(10).sum()/d.asset_value_gbp.sum():.0%} of value')
print('share of loss by hazard:', {h: f'{d[f"{h}_ssp245_2050_loss_gbp"].sum()/L.sum():.0%}' for h in H})
print('by country x hazard (£m):'); print((d.groupby('country')[[f'{h}_ssp245_2050_loss_gbp' for h in H]].sum() / 1e6).round(2).rename(columns=lambda c: c.split('_ssp')[0]))
bad = worst_bad('central', '2050'); d['bad'] = bad
print(f'sites rated E-G on any hazard: {bad.sum()} of {len(d)}; which:', d[bad][['site_id', 'region', 'asset_type']].values.tolist())
for h in H: print(f'  E-G {h}: {d[f"{h}_ssp245_2050_rating"].isin(BAD).sum()}')
rf = d.flood_river_ssp245_2050_rating.isin(BAD)
print('river flood E-G by asset type:', d[rf].asset_type.value_counts().to_dict(), '| batteries total', (d.asset_type == 'battery').sum(), '| UK batteries E-G', (rf & (d.asset_type == 'battery') & (d.country == 'UK')).sum(), 'of', ((d.asset_type == 'battery') & (d.country == 'UK')).sum())
print('battery loss rate vs others:', {k: f'{g.L.sum()/g.asset_value_gbp.sum():.2%}' for k, g in d.groupby('asset_type')})
print('by debt facility:', {k: dict(sites=len(g), value=f'£{g.asset_value_gbp.sum()/1e6:.0f}m', loss=f'£{g.L.sum()/1e6:.1f}m', rate=f'{g.L.sum()/g.asset_value_gbp.sum():.2%}', bad=int(g.bad.sum())) for k, g in d.groupby('debt_facility')})
print('debt facility by country:', d.groupby(['debt_facility', 'country']).size().to_dict())

print('\n# What is missing or odd')
wf = d[[c for c in d.columns if c.startswith('wildfire')]].isna().all(axis=1)
print('no wildfire scores:', d[wf][['site_id', 'country', 'region', 'asset_type']].values.tolist())
print('location_type:', d.location_type.value_counts().to_dict(), '| point by asset type:', d[d.location_type == 'point'].asset_type.value_counts().to_dict())
print('point vs footprint loss rate:', {k: f'{g.L.sum()/g.asset_value_gbp.sum():.2%}' for k, g in d.groupby('location_type')})
print('value per MW (£m) by type:', d.assign(v=d.asset_value_gbp/d.capacity_mw/1e6).groupby('asset_type').v.describe()[['min', 'max']].round(2).to_dict('index'))
print('columns:', [c for c in d.columns if not any(c.startswith(h) for h in H)], '| metrics:', sorted({c.rsplit('_', 2)[-2] + '_' + c.rsplit('_', 1)[-1] if c.endswith('loss_gbp') else c.rsplit('_', 1)[-1] for c in d.columns if any(c.startswith(h) for h in H)}))

print('\n# First five rows (key columns)')
cols = ['site_id', 'country', 'region', 'asset_type', 'capacity_mw', 'commissioned', 'asset_value_gbp', 'location_type', 'debt_facility', 'flood_river_ssp245_2050_rating', 'flood_river_ssp245_2050_loss_gbp']
print(d[cols].head(5).to_string(index=False), f'\n{d.shape[1] - 2 - len(cols)} columns left out')

print('\n# Severe 2050: which hazards and sites are E-G')
sb = worst_bad('severe', '2050')
print({h: int(d[f'{h}_ssp585_2050_rating'].isin(BAD).sum()) for h in H})
print('E-G sites under severe by country/type:', d[sb].groupby(['country', 'asset_type']).size().to_dict())
print('E-G value share, central:', f'{d.asset_value_gbp[bad].sum()/d.asset_value_gbp.sum():.0%}', '| severe:', f'{d.asset_value_gbp[sb].sum()/d.asset_value_gbp.sum():.0%}')
print('E-G sites (central) by facility, value:', d[bad].groupby('debt_facility').asset_value_gbp.sum().div(1e6).round(0).to_dict())
print('8 E-G sites share of total loss (central 2050):', f'{d.L[bad].sum()/d.L.sum():.0%}')

print('\n# UK expected loss a year, central 2050, all hazards and wildfire only (blank = £0)')
uk = d[d.country == 'UK']
print(f"£{uk[[f'{h}_ssp245_2050_loss_gbp' for h in H]].fillna(0).sum().sum()/1e6:.1f}m total, wildfire £{uk.wildfire_ssp245_2050_loss_gbp.fillna(0).sum()/1e6:.2f}m")
