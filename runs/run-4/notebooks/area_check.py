"""Run 4: is the risk the asset or the area? Compare the two Singapore sites and coastal-flood sites."""
import pandas as pd
d = pd.read_excel('data/Climate X Sample Data.xlsx', 'Sample Data')
k = d[(d.Year==2030)&(d.Scenario=='ssp245')]
c = ['Asset ID','Street','City','Asset Type','Floor Count','Building Replacement Cost','Coastal Flood Score','Coastal Flood Severity Value (maximum depth (m))','Coastal Flood Loss','Total Building Loss','Total Loss Percentage','Physical Risk Score','Latitude','Longitude']
print(k[k.Country=='Singapore'][c].to_string())
print('\ncoastal flood grade by site:'); print(k[c[:3]+['Coastal Flood Score','Coastal Flood Loss']].sort_values('Coastal Flood Loss',ascending=False).head(6).to_string())
print('\nportfolio loss % (total loss / total rebuild cost):', round(k['Total Building Loss'].sum()/k['Building Replacement Cost'].sum(),4))
print('median site loss %:', round(k['Total Loss Percentage'].median(),4))
