"""Run 4 concept v2: insurance premiums over the hold. ASSUMPTIONS (to check with a broker, not data):
premium = expected loss (AAL) x 1.5-2.0 loading; premiums rise 5% a year (market trend); +50% after a claim (once)."""
import pandas as pd
d = pd.read_excel('data/Climate X Sample Data.xlsx', 'Sample Data')
sg = 1740500331
def aal_path(defended):
    x = d[d.Scenario=='ssp245'].copy()
    if defended: x.loc[x['Asset ID']==sg,'Total Building Loss'] -= x.loc[x['Asset ID']==sg,'Coastal Flood Loss']
    t = x.groupby('Year')['Total Building Loss'].sum().reindex(range(2020,2101)).interpolate()
    return t[list(range(2026,2033))]
for defended in (False, True):
    a = aal_path(defended)
    for load in (1.5, 2.0):
        p = [a[y]*load*1.05**(y-2026) for y in a.index]
        print('defended' if defended else 'undefended', 'load', load, 'AAL hold', round(a.sum()/1e6,1),
              'premium 2026', round(p[0]/1e6,1), '2032', round(p[-1]/1e6,1), 'hold total', round(sum(p)/1e6,1),
              'with one claim in 2028 (+50% from 2029)', round(sum(v*(1.5 if y>=2029 else 1) for v,y in zip(p,a.index))/1e6,1))
