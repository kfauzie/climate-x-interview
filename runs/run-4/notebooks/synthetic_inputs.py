"""SYNTHETIC inputs for the run 4 prototype (not real data): EBITDA per site, CX Capital's past assessments,
an example flood insurance policy and premium rules of thumb. Writes data/synthetic_inputs.json."""
import json
sites = json.load(open('data/sites.json'))['sites']
total_ebitda = 60_000_000          # assumed: EV £480m at 8x EBITDA
sg = '1740500331'
rest = [s for s in sites if s['id'] != sg]
w = {s['id']: s['replacement_cost'] ** 0.5 for s in rest}
ebitda = {sg: 12_000_000}
for s in rest:
    ebitda[s['id']] = round((total_ebitda - 12_000_000) * w[s['id']] / sum(w.values()), -4)
ebitda[rest[0]['id']] += total_ebitda - sum(ebitda.values())   # make it add up exactly
past = [0.4, 0.9, 1.2, 1.8, 2.3, 2.9, 3.4, 4.1, 5.6, 7.2, 11.5]  # AAL as % of EBITDA, 11 deals
out = {
  'label': 'SYNTHETIC for the prototype: not real data',
  'deal': {'name': 'Project Meridian', 'company': 'Meridian Group', 'ev': 480_000_000, 'hold_years': 7, 'hold_start': 2026, 'ic_date': '3 Dec 2026'},
  'ebitda_by_site': ebitda,
  'past_deals_aal_pct_ebitda': past,
  'premium': {'loading_low': 1.5, 'loading_high': 2.0, 'after_claim_low': 1.25, 'after_claim_high': 2.0},
  'example_policy': {'file': 'SG_office_flood_policy.pdf', 'site': sg, 'hazard': 'Coastal Flood', 'covers_flood': True,
                     'limit_per_event': 50_000_000, 'excess_per_event': 1_000_000, 'valid_until': '31 Mar 2028', 'last_covered_year': 2027,
                     'pages': {'covers': 4, 'limit': 6, 'excess': 6, 'valid': 1}},
  'other_deals': [{'name': 'Project Atlas', 'status': 'IC in 6 weeks', 'dot': 'green'}, {'name': 'Project Kestrel', 'status': 'not started', 'dot': 'grey'}],
}
out['premium'].update({'yearly_rise': 0.05, 'after_claim': 0.5, 'claim_year': 2028})   # assumed: market trend, one claim
out['defences'] = {sg: {'status': 'Suggested from public sources · to verify', 'items': [
  {'what': 'Marina Barrage (dam across the mouth of Marina Channel)', 'who': "PUB, Singapore's national water agency", 'standard': 'Design standard: to verify with PUB'},
  {'what': 'Coastal protection along Marina Bay', 'who': 'Singapore government (long-term coastal protection programme)', 'standard': 'Protection level at this site: to verify'}]}}
json.dump(out, open('data/synthetic_inputs.json', 'w'), indent=1)
print('EBITDA total', sum(ebitda.values()), 'SG', ebitda[sg])
