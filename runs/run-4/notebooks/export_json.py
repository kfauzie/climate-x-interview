"""Turn the Spectra export into data/sites.json for the prototype: one object per site,
with per scenario x year: overall grade, total £ loss a year, loss %, and per hazard grade + £ loss."""
import json, pandas as pd
d = pd.read_excel('data/Climate X Sample Data.xlsx', 'Sample Data')
H = ['River Flood','Surface Flood','Coastal Flood','Subsidence','Landslide','Wildfires','Storms','Tropical Cyclones','Hail','Extreme Heat Days','Drought']
static = {'Street':'street','City':'city','Post Code':'postcode','Region':'region','Country':'country','Latitude':'lat','Longitude':'lon',
          'Asset Use':'use','Asset Type':'type','Age Category':'age','Floor Count':'floors','Building Replacement Cost':'replacement_cost','Gross Premise Area':'area_m2'}
nz = lambda v: None if pd.isna(v) else (v.item() if hasattr(v,'item') else v)
sites = []
for aid, g in d.groupby('Asset ID', sort=False):
    s = {'id': str(aid), **{k: nz(g.iloc[0][c]) for c, k in static.items()}, 'risk': {}}
    for _, r in g.iterrows():
        hz = {}
        for h in H:
            loss = r.get(h+' Loss')
            sev = [c for c in d.columns if c.startswith(h+' Severity Value')]
            hz[h] = {'grade': nz(r[h+' Score']), 'loss': nz(loss) if loss is not None else None,
                     'sev': (nz(r[sev[0]]) if sev else None)}
        s['risk'].setdefault(r.Scenario, {})[str(r.Year)] = {'grade': r['Physical Risk Score'], 'loss': int(r['Total Building Loss']),
                                                             'loss_pct': float(r['Total Loss Percentage']), 'hazards': hz}
    sites.append(s)
meta = {'scenarios': sorted(d.Scenario.unique().tolist()), 'years': sorted(int(y) for y in d.Year.unique()),
        'hazards': H, 'severity_units': {h: [c for c in d.columns if c.startswith(h+' Severity Value')][0].split('(',1)[1].rstrip(')') for h in H if any(c.startswith(h+' Severity Value') for c in d.columns)}, 'currency': 'GBP', 'flood_defences': 'Undefended', 'source': 'Spectra v2 export'}
json.dump({'meta': meta, 'sites': sites}, open('data/sites.json','w'), separators=(',',':'))
print(len(sites), 'sites;', meta['scenarios'], len(meta['years']), 'years')
