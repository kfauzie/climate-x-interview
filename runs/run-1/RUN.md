# Run 1

**Status:** practice run. The data is synthetic, not real Climate X data
**Dataset:** `data/spectra_portfolio_export.csv` (Spectra-style UK loan portfolio export)
**Interview notes:** none yet. Save Notion notes for this run in `notes/`
**Analysis:** `notebooks/spectra_profile.ipynb` (Profile mode) and `notebooks/region_abs_vs_rate.png`

Everything below applies to **run 1 only**. Do not carry it into any other run.

## Customer context (inferred for this dataset)
- Customer: an enterprise customer, inferred to be a UK lender (residential mortgages plus CRE)
- Users of this data: [confirm in discovery] likely climate / credit risk team, reporting to risk committee and regulator
- Decisions it feeds: [confirm in discovery] likely PRA climate stress test / disclosure figures, lending appetite by region or property type, loans to review
- Stakes: regulated, decision-grade. Numbers must be defensible to auditors and regulators

## Data notes
- 2,000 loans on 1,880 properties, 81 columns
- One row = one loan. `property_id` repeats: 112 properties carry 232 loans, and the property's risk is repeated on each loan
- Risk columns are `<hazard>_<scenario>_<year>_<metric>`
  - hazards: flood, subsidence, heat, wind
  - scenarios: ssp126, ssp245, ssp585
  - years: 2030, 2050
  - metrics: rating, damage_pct, loss_gbp
- Verified: `loss_gbp = damage_pct / 100 * property_value_gbp`
- Verified rating bands on damage_pct (%): A <0.02, B <0.05, C <0.1, D <0.2, E <0.4, F <0.8, G >=0.8
- INFERRED (unconfirmed): damage_pct is percent of property value, and loss is an annual expected loss to the property, not to the lender. Valuation date unknown
- Missing: 45 loans each lack one hazard × year in all 3 scenarios
- Postcodes: 159 badly formatted. Normalise (trim, uppercase, inner space) before any join

## Default analysis choices (state them in every answer)
- Scenario SSP245, year 2050, all 4 hazards summed
- Count physical risk once per property (deduplicate on `property_id`)
- Missing scores: exclude, and disclose the count and the denominator used
- Report £ figures and loss rate (basis points of property value) together
