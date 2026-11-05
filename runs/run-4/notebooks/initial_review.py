"""Run 4 initial review. Every number in RUN.md comes from this script."""
import pandas as pd
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40)
d = pd.read_excel('data/Climate X Sample Data.xlsx', 'Sample Data')
H = ['River Flood','Surface Flood','Coastal Flood','Subsidence','Landslide','Wildfires','Storms','Tropical Cyclones','Hail']
print('rows', len(d), 'assets', d['Asset ID'].nunique(), 'dup asset-year-scen', d.duplicated(['Asset ID','Year','Scenario']).sum())
# checks
d['sum_h'] = d[[h+' Loss' for h in H]].sum(axis=1)
print('total = sum of hazards:', (d['sum_h']-d['Total Building Loss']).abs().max())
print('loss % = total/replacement:', (d['Total Building Loss']/d['Building Replacement Cost']-d['Total Loss Percentage']).abs().max())
print('per-unit = total/volume:', (d['Total Building Loss']/d['Unit/Flat Volume']-d['Total Loss per Unit/Flat']).abs().max())
static = ['Building Replacement Cost','Asset Type','Country','Age Category']
print('static cols constant per asset:', (d.groupby('Asset ID')[static].nunique()>1).sum().to_dict())
a = d.drop_duplicates('Asset ID').set_index('Asset ID')[['City','Country','Asset Type','Asset Use','Building Replacement Cost','Floor Count','Unit/Flat Volume','Age Category','Age Category Flag','Gross Premise Area Flag']]
key = lambda y,s: d[(d.Year==y)&(d.Scenario==s)].set_index('Asset ID')
for y in [2025,2030,2035,2050]:
    k = key(y,'ssp245'); a[f'loss{y}'] = k['Total Building Loss']; a[f'grade{y}'] = k['Physical Risk Score']
a['pct2030'] = key(2030,'ssp245')['Total Loss Percentage']
a['top_hazard'] = key(2030,'ssp245')[[h+' Loss' for h in H]].idxmax(axis=1).str.replace(' Loss','')
a = a.sort_values('loss2030', ascending=False)
print(a.to_string())
print('\nportfolio replacement cost', a['Building Replacement Cost'].sum())
for y in [2025,2030,2035,2050]:
    t = a[f'loss{y}'].sum(); print(y,'ssp245 total loss/yr', t, 'top1 share', round(a[f'loss{y}'].max()/t,3), 'top3 share', round(a[f'loss{y}'].nlargest(3).sum()/t,3))
print('top asset share of replacement cost', round(a['Building Replacement Cost'].max()/a['Building Replacement Cost'].sum(),3))
# by hazard, 2030 ssp245
k = key(2030,'ssp245'); print('\nby hazard 2030 ssp245\n', (k[[h+' Loss' for h in H]].sum()/k['Total Building Loss'].sum()).round(3).sort_values(ascending=False))
# scenario x year
pv = d.pivot_table(index='Year', columns='Scenario', values='Total Building Loss', aggfunc='sum'); print('\n', pv)
# grade vs loss%
print('\ngrade vs loss % (2030 ssp245):\n', k.groupby('Physical Risk Score')['Total Loss Percentage'].describe()[['count','min','max']])
print(k[['City','Asset Type','Physical Risk Score','Total Building Loss','Total Loss Percentage']].sort_values('Total Loss Percentage',ascending=False).to_string())
# grade changes within hold (2025 -> 2035) by scenario
for s in ['ssp126','ssp245','ssp370','ssp585']:
    g = d[d.Scenario==s].pivot(index='Asset ID', columns='Year', values='Physical Risk Score')
    print(s,'grade changes 2025->2035:', (g[2025]!=g[2035]).sum(), ' 2025->2050:', (g[2025]!=g[2050]).sum())
# blanks
for h in ['Coastal Flood','Storms','Tropical Cyclones','Drought']:
    b = d[d[h+' Score'].isna()]
    print(h, 'blank rows', len(b), 'assets', b['Asset ID'].nunique(), 'loss on blank rows', b[h+' Loss'].sum() if h+' Loss' in d else 'n/a', list(b['Country'].unique())[:8])
print('flags', a['Age Category Flag'].value_counts().to_dict(), a['Gross Premise Area Flag'].value_counts().to_dict())
print('missing city/postcode assets', d[d.City.isna()]['Asset ID'].nunique())

print('\n--- part 2 ---')
H2 = [h+' Loss' for h in H]
for aid in [1740500331, 1740501107, 1740501298, 1772801990]:
    r = k.loc[aid]; print(aid, r['City'], {h:int(r[h]) for h in H2 if r[h]>0}, 'grades', {h:r[h.replace(' Loss',' Score')] for h in H2 if r[h]>0})
# 7-year hold 2026-2032 (IC now, exit ~2033), loss/yr interpolated linearly between projection years
yrs = range(2026, 2033)
for s in ['ssp245','ssp585']:
    t = d[d.Scenario==s].groupby('Year')['Total Building Loss'].sum()
    t = t.reindex(range(2020,2101)).interpolate()
    print(s, 'hold-period loss 2026-32', int(t[list(yrs)].sum()))
print('EV 480m, equity 165m; replacement cost / EV', round(a['Building Replacement Cost'].sum()/480e6,2))
print('Hong Kong/Brasil missing city:', d[d.City.isna()][['Asset ID','Country']].drop_duplicates().to_string())
