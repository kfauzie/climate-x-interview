# Run 1

**Status:** practice run. The data is synthetic, not real Climate X data
**Dataset:** `data/spectra_portfolio_export.csv` (Spectra-style UK loan portfolio export)
**Interview notes:** `notes/interview.md` (from Notion), `notes/sarah-followup.md` (her example questions, a sent-back case, defaults), `notes/mock-feedback.md`
**Solution:** `solution.md` (recommended: answer with its method)
**Design:** `design.md` (flow and screens agreed)
**Prototype:** `prototype/` at the repo root; synthetic loan book from `data/make_loan_book.py`
**Prototype review:** `prototype-review.md` (script and questions, made with `pm-prototype-review`)
**Notion review:** https://app.notion.com/p/40b8f31ef05f814e815fc95807769b0b (take review notes here)
**Test:** `notebooks/spectra_test.ipynb` (built by `notebooks/build_test.py`), chart `notebooks/test_cre_flood_by_scenario.png`
**Discovery questions:** `discovery-questions.md` (customised for Sarah and this dataset, 15-min version)
**Notion questions:** https://app.notion.com/p/40b8f31ef05f8114908bd8ada551932c (take call notes here)
**Analysis:** `notebooks/spectra_profile.ipynb` (Profile mode, built by `notebooks/build_profile.py`) and `notebooks/region_abs_vs_rate.png`

Everything below applies to **run 1 only**. Do not carry it into any other run.

## Customer ask (given, word for word)
> customized report builder to help her team product custom reports to answer any questions that the team may have

*This is a solution, not a problem. Discovery should find the questions behind it: which questions, from whom, how often, how they're answered today, and what makes that slow or risky.*

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

## Problem statement (from Test, run 1)
**Narrow:** Sarah (Head of Climate Risk) needs each ad-hoc physical-risk answer her team sends (about 15 a month) to be correct and defensible before it leaves the team. Today each one is built by hand in Excel, with the scenario, horizon and loan population chosen case by case and written up by hand, then queued for her personal check. That causes 2–5 day turnarounds (her estimate: about 45 analyst days a month, plus several half-days a week of her review time), follow-ups that restart the clock, and key-person risk.
Success (proposed, to validate): a standard-shape question answered and ready to review the same day; her review per answer cut from up to half a day to minutes because the method is stated and traceable; model risk approval.

**Broad:** The bank needs climate-risk numbers that are consistent and defensible across all its audiences (CRO, committees, pricing, treasury, IR, the PRA). Today every answer depends on case-by-case analyst choices checked by one person. That causes slow answers, key-person risk, and the chance that different audiences get numbers built on different assumptions.
Success (proposed): one agreed set of defaults; every figure traceable to source rows; numbers that reconcile across audiences; model risk sign-off.

**Key tension:** the ask (analysts configure reports themselves) targets the hour of filtering. The pain is the days of choosing, writing up and checking. A builder alone could increase her review queue.

## Profile findings (run 1, from the notebook)
- Baseline (defaults below): £3,313,709 annual expected loss to properties
- One-at-a-time swings vs baseline: SSP126 0.72×, SSP585 1.84×; 2030 0.64×; per-loan counting 1.021×; LTV-weighted "bank view" 0.47× (assumption)
- Missing scores: 45 loans (£19.3m balance); 39 mortgages, 6 CRE
- Concentration: top property P51627 (Retail, South East) is 12.77% of loss; top 1% of properties 31.78%; top 10 loans 15.41% of balance
- CRE is 72.99% of loss but loss rates are close (17.54 vs 16.21bp) under every scenario
- Residential lending from 2021–25 has a higher loss rate (17.55bp) than 2010–15 (14.66bp), with mix not controlled
- Subsidence is 53.6% of loss and the most scenario-sensitive (SSP585/SSP245 = 2.33×)

## Sarah's defaults (from her follow-up; her methodology paper, approved yearly by risk committee)
- Committee work: **central at 2050**, plus 2030 if asked about the near term
- PRA and stress work: **severe alongside central, at 2030 and 2050**
- Deviations need Sarah's approval
- INFERRED mapping to this file, to confirm: central = `ssp245`, severe = `ssp585`

## Default analysis choices (state them in every answer)
- Scenario SSP245, year 2050, all 4 hazards summed
- Count physical risk once per property (deduplicate on `property_id`)
- Missing scores: exclude, and disclose the count and the denominator used
- Report £ figures and loss rate (basis points of property value) together
