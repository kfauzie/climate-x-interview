"""Run 3 numbers for the solution concept."""
import pandas as pd
d = pd.read_csv('runs/run-3/data/northwind_renewables_spectra_infra_2026-09.csv')
H = ['flood_river', 'flood_surface', 'extreme_heat', 'wildfire', 'windstorm']; BAD = list('EFG')
def eg(s, y): return d[[f'{h}_{s}_{y}_rating' for h in H]].isin(BAD).any(axis=1)
both = eg('ssp245', '2050') | eg('ssp585', '2050')
print('screening test "no hazard rated E-G in 2050 under central or severe":', int((~both).sum()), 'pass,', int(both.sum()), 'need a plan')
print('central-only E-G 2050:', int(eg('ssp245','2050').sum()), '| severe-only adds:', int((eg('ssp585','2050') & ~eg('ssp245','2050')).sum()))
need = d[both]; print('needing a plan by country/type:', need.groupby(['country','asset_type']).size().to_dict())
print('missing wildfire among them:', need[need.wildfire_ssp245_2050_rating.isna()].site_id.tolist())
t = d[(d.region == 'Teesside')][['site_id','asset_type','asset_value_gbp','location_type','flood_river_ssp245_2050_rating','flood_river_ssp245_2050_loss_gbp','flood_river_ssp585_2050_loss_gbp']]
print(t.to_string(index=False))
c8 = d[eg('ssp245','2050')]
print('8 central E-G sites river flood loss a year central 2050: £', int(c8.flood_river_ssp245_2050_loss_gbp.sum()), '| point locations among them:', c8[c8.location_type=='point'].site_id.tolist())

# Bank document: the 24 sites (rated E-G in 2050 under severe), loss a year severe 2050, all hazards
sev = eg('ssp585', '2050'); print('severe set equals either-scenario set:', bool((sev == both).all()))
g = d[sev].copy()
g['loss'] = g[[f'{h}_ssp585_2050_loss_gbp' for h in H]].sum(axis=1)
g['eg_for'] = g.apply(lambda r: ', '.join(h for h in H if r[f'{h}_ssp585_2050_rating'] in BAD), axis=1)
g['central_eg'] = eg('ssp245', '2050')[sev]
print('total loss a year, 24 sites, severe 2050: £', int(g.loss.sum()))
print('point locations among the 24:', g[g.location_type == 'point'].site_id.tolist())
print(g.sort_values('loss', ascending=False)[['site_id', 'region', 'asset_type', 'eg_for', 'loss', 'location_type', 'central_eg']].to_string(index=False))
