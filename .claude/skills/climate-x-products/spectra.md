
# Climate X Spectra

Confidence tags: **[public]** from Climate X marketing or press (unverified), **[prep]** from my preparation notes, **[analysis]** my inference. Present [analysis] items as hypotheses to test with the customer, never as facts.

## What it is
- Search any asset worldwide and see its physical-risk profile and quantified financial loss, on a map (the "Google Maps for climate change") [public]
- Outputs: hazard ratings, annual loss in £ and % of value, climate-adjusted VaR (cVaR) out to 2100 [public]. ⚠️ A third-party comparison says Spectra lacks cVaR and probabilistic modelling. Unresolved
- Hazards: 11 (company) vs 16 (third party) ⚠️. New 30m-resolution wildfire model [public]
- Method: damage curves by building use and hazard, calibrated by region; downscaled multi-model projections; database of about 1.5bn buildings with type and replacement cost; Fathom integration for water, wind, fire and earth perils [public]
- Framework claims: NGFS, ECB, IFRS, EU Taxonomy, TCFD, central-bank stress tests [public]

## Customers and users
- **Banks:** climate risk and credit risk teams. Use cases: collateral value and insurability, regulatory stress tests, reviewing the existing loan book. Examples: a European Tier 1 bank, Triodos (SME lending) [public]
- **Real estate:** portfolio owners and CRE firms (Aroundtown, CBRE). Disclosure and resilience planning [public]
- **Asset managers and PE:** investment screening [prep]. Clients claimed to hold over $13.5tn AUM [public]
- **Channel partners:** consultancies and facilities firms (Mitie, IBD Group, Scaler, Equans, Nfq, Embark) who turn the data into services for their own clients [public]
- Typical user: a risk analyst or sustainability lead. Financially literate, not necessarily a climate expert [prep]

## Value proposition
- **For the buyer:** a defensible, asset-level view of physical risk in money terms. That supports lending, investment and disclosure decisions without hiring consultants
- **ROI as Climate X frames it:** time saved, consultant cost avoided, better business decisions. Lead with commercial decisions (investment, lending, pricing), not safety [prep]

## Strengths [analysis, built on public]
- Turns hazard into **money**, by building type, which is what finance users need. Many tools stop at a hazard score
- **Global coverage** from a single building database, including replacement cost. Customers don't need their own asset data to start
- **Scenario × horizon** grid (SSPs, 2030–2100) suits regulatory scenario analysis
- Partner and reseller channel widens reach beyond direct enterprise sales
- AI-native, lean team that can ship quickly against slower incumbents

## Weaknesses and risks [analysis]
- **Black-box concern:** regulators and auditors want model transparency, which is Jupiter's selling point. Every number needs its assumptions, version and source visible
- **Property loss ≠ lender loss:** exports give damage to the asset. Banks need impact on the loan (LTV, LGD, insurance, default). Shown in the practice data: weighting by LTV alone gave 0.47× the property-level total
- **Judgment calls move the headline:** scenario, horizon, hazard set, per-loan vs per-property counting, missing data. In the practice data the SSP585 total was 1.84× the SSP245 total, and 2030 was 0.64× 2050. Two analysts can report different numbers from the same export
- **Wide exports are hard to use:** 72 columns of hazard × scenario × year × metric need reshaping before anyone can answer a question
- **Incumbents bundle:** Moody's and S&P attach climate data to credit data they already sell; S&P buys smaller players. Climate X has to win on depth, usability and trust

## Opportunities (hypotheses to test in discovery) [analysis]
1. **Reporting with an audit trail** (compliance, banks): portfolio figures with every assumption stated, default choices, exclusions disclosed, a version stamp. Answers "defend this number to the PRA"
2. **Analyst agent** (decisions, any segment): ask in plain English ("which CRE loans in the South East have subsidence rated E or worse in 2050?"), get answers computed in code, with cited rows and the judgment calls made. AI interprets the question; deterministic code computes the answer
3. **Event impact** (operational, insurers and lenders): when a flood or storm hits, which assets and loans are exposed, and by how much. Turns a once-a-year analysis into a recurring workflow
4. **Lender view:** translate property loss into loan-level impact using customer-supplied LTV, LGD and insurance assumptions. Closes the gap competitors also have
5. **Decision thresholds per customer:** the hail question. At what rating or loss does a risk change *this* customer's lending, pricing or investment decision? Configurable thresholds and alerts, and a signal to the science team about which models to prioritise
6. **Partner-ready outputs:** packaged views partners can resell without climate expertise

## Discovery questions (non-leading)
- Walk me through the last time a Spectra number went into a decision or a report. Who used it and what did they do?
- At what point does a risk start to change your decision? Why there? Is it the same across portfolios?
- When someone challenged one of these numbers, what did you show them?
- How do you get from damage to the property to impact on your book today?
- Which scenario and horizon do you report on, and who decides?
- What do you do with the export after downloading it?

## Related
- Company and competitor research: the `climate-x-company` skill
- Role and positioning: the `climate-x-role` skill
- Data analysis method: the `pm-data-lens` skill
