"""Numbers used in the run 4 solution concept."""
import pandas as pd
d = pd.read_excel('data/Climate X Sample Data.xlsx', 'Sample Data')
sg = 1740500331
k = d[(d.Year==2030)&(d.Scenario=='ssp245')]
r = k[k['Asset ID']==sg].iloc[0]
print('SG coastal depth m', r['Coastal Flood Severity Value (maximum depth (m))'], r['Coastal Flood Severity Lower Bound'], r['Coastal Flood Severity Upper Bound'], 'grade', r['Coastal Flood Score'])
print('SG loss', r['Total Building Loss'], 'coastal', r['Coastal Flood Loss'], 'pct', r['Total Loss Percentage'])
def hold(s, drop_sg_coastal=False, n=7):
    x = d[d.Scenario==s].copy()
    if drop_sg_coastal: x.loc[x['Asset ID']==sg,'Total Building Loss'] -= x.loc[x['Asset ID']==sg,'Coastal Flood Loss']
    t = x.groupby('Year')['Total Building Loss'].sum().reindex(range(2020,2101)).interpolate()
    return t[list(range(2026,2026+n))].sum()
for s in ['ssp245','ssp585']:
    print(s, 'hold 7y', round(hold(s)/1e6,1), 'excl SG coastal', round(hold(s,True)/1e6,1))
print('2030 total', k['Total Building Loss'].sum(), 'excl SG coastal', k['Total Building Loss'].sum()-r['Coastal Flood Loss'])
print('share of EV 480m:', round(hold('ssp245')/480e6,3), round(hold('ssp245',True)/480e6,3))
