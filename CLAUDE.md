# Climate X interview: customer discovery workspace

Discovery workspace for a customer's climate physical-risk portfolio data. Use the `pm-data-lens` skill:
`/pm-data-lens` = Profile, `/pm-data-lens <notes>` = Test, `/pm-data-lens <question>` = Answer.

## Why this repo exists
Preparation for a live prototyping interview for a Principal PM role (senior IC) at Climate X. Confidential: keep this repo private.

## The session
- Live build session, remote with screen share, with **Kevin Luo** (leads product). Kevin hands over a real dataset of Climate X outputs during the session, possibly not this CSV, and asks for a new feature built on it
- **Kevin role-plays an enterprise customer.** Run live discovery on him first, get past the stated ask to the real workflow problem, and keep asking while building so every trade-off traces back to something he said
- Kamil Kluza (co-founder): the prep page lists him for the session, but that is wrong. Per the candidate, the session is with Kevin, and the conversation with Kamil only happens **if it goes well**. Kamil brings a founder's lens: commercial impact, product strategy, the Series B vision
- Considered for **Seat 1 (Customer & UX / Discovery)**: discovery-centric, with LLM familiarity as support. Frame value commercially (investment and lending decisions; ROI = time saved, consultant cost avoided, better decisions), not as safety
- Assessed on thinking and outcome, not polish. AI tools are encouraged
- What lands:
  - think out loud and narrate choices
  - take the work as far as something an engineer can review (a PR, not a spec)
  - make AI output trustworthy for regulated, decision-grade use (evals, golden datasets, human in the loop, thresholds, failure modes, the line between deterministic and AI)
  - keep the commercial thread: customer value, adoption, conservative enterprise buyers

## About Climate X
- B2B physical climate-risk data and analytics ("Google Maps for climate change"). Search any asset to see its physical-risk profile and quantified financial loss
- Products: Carta (company structure → subsidiaries → assets → risk), Spectra and Adapt (risk and revenue-impact modelling). This CSV appears to be a Spectra export (inferred from the filename)
- Customers: banks, asset managers, real estate, private equity. Growing in data centres and renewables
- Stage: between Series A and B, about 85 people, approaching profitability. Lean, flat, AI-native

More detail (products, methodology, banking use cases, competitors, sources): `docs/climate-x-brief.md`

## Customer context (for analysis)
- Customer: an enterprise customer role-played by Kevin. For this dataset, inferred to be a UK lender (residential mortgages plus CRE)
- Users of this data: [confirm in discovery] likely climate / credit risk team, reporting to risk committee and regulator
- Decisions it feeds: [confirm in discovery] likely PRA climate stress test / disclosure figures, lending appetite by region or property type, loans to review
- Stakes: regulated, decision-grade. Numbers must be defensible to auditors and regulators

## Session setup
At the start of every session, before any analysis, run `pip install -q -r requirements.txt && python3 -m ipykernel install --user`

## Live-session workflow with pm-data-lens
1. When the dataset arrives: `/pm-data-lens` (Profile) for a fast decode, trust checks and judgment calls → use the discovery questions on Kevin
2. Paste rough notes from Kevin's answers: `/pm-data-lens <notes>` (Test) → contradictions first, problem statement
3. Turn product implications into requirements for the feature, then build it to a reviewable PR

## Files
- `data/spectra_portfolio_export.csv`: vendor export, 2,000 loans on 1,880 properties, 81 columns
- `docs/climate-x-brief.md`: company and product research with sources
- `docs/role-brief.md`: the Principal PM role, the two seats, process, and how my experience maps to it
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
