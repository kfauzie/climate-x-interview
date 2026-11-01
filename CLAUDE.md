# Climate X interview: customer discovery workspace

Discovery workspace for a customer's climate physical-risk portfolio data. Use the `pm-data-lens` skill:
`/pm-data-lens` = Profile, `/pm-data-lens <notes>` = Test, `/pm-data-lens <question>` = Answer.

## Customer context
- Customer: [unknown, fill in]
- Users of this data: [unknown, inferred: climate / credit risk team at a UK lender]
- Decisions this data feeds: [unknown, inferred: climate stress tests and disclosures, lending policy by region or property type, loan review]
- Stakes: [unknown]

## Files
- `data/spectra_portfolio_export.csv`: vendor export, 2,000 loans on 1,880 properties, 81 columns
- `notebooks/spectra_profile.ipynb`: Profile-mode analysis (trust checks, judgment calls, discovery questions)

## Data notes
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
