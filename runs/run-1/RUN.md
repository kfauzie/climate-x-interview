# Run 1

**Status:** practice run. The data is synthetic, not real Climate X data
**Dataset:** `data/spectra_portfolio_export.csv` (Spectra-style UK loan portfolio export)
**Interview notes:** none yet. Save Notion notes for this run in `notes/`
**Discovery questions:** `discovery-questions.md` (customised for Sarah and this dataset, 15-min version)
**Notion questions:** https://app.notion.com/p/40b8f31ef05f8114908bd8ada551932c (take call notes here)
**Analysis:** `notebooks/spectra_profile.ipynb` (Profile mode) and `notebooks/region_abs_vs_rate.png`

Everything below applies to **run 1 only**. Do not carry it into any other run.

## Customer profile (given for this run)
- **Name:** Sarah Okafor
- **Role:** Head of Climate Risk
- **Organisation:** large UK bank, regulated by the PRA. Retail mortgages plus commercial lending, including commercial real estate
- **Background:** about 12 years in credit risk before moving into climate risk. Sharp, commercially minded, fluent in risk and regulatory language (stress tests, ICAAP, risk appetite). Lives in Excel and PowerPoint. Not technical: has heard of APIs and LLMs, never used either directly
- **Team:** three analysts, who do the hands-on data work
- **Reports to:** the CRO
- **Fields questions from:** CRO and risk committee, credit committee, mortgage pricing, treasury, sustainability reporting, investor relations, the PRA
- **Relationship with Climate X:** customer for about 18 months. Receives Spectra outputs for the full mortgage and CRE book each quarter

## What the profile implies (inferred, test in discovery)
- **Two users:** Sarah (buyer and decision owner, defends the numbers) and her three analysts (prepare them). Their needs may differ
- **Outputs must land in Excel and PowerPoint,** in risk and regulatory language. No API or LLM jargon
- **Seven audiences:** the same data probably gets cut differently for each, which is where inconsistent numbers can creep in
- **Quarterly cadence for about 18 months (about 6 deliveries):** quarter-on-quarter change and reconciliation may matter
- **PRA, ICAAP and stress tests:** answers must be defensible, with assumptions and an audit trail
- **Credit risk background:** she is likely to think in terms of loan-level impact (LTV, LGD, risk appetite) rather than property damage

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
