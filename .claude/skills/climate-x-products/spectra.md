
# Climate X Spectra

Source tags: **[site]** climate-x.com (read 2026-11-01; Climate X's own claims), **[web]** press or third parties, **[prep]** my preparation notes, **[analysis]** my inference. Present [analysis] items as hypotheses to test with the customer, never as facts.

## What it is [site]
- "Translate physical risk into actionable, asset-level financial loss metrics." Search by address or postcode, or upload a portfolio (CSV, up to 100k addresses), pick scenario settings, download a financial impact report. Web app, CSV export (Tableau, Power BI, Qlik) and Enterprise API for hundreds of thousands of assets
- **Hazards (11):** river, surface and coastal flooding (defended / undefended), wildfire (new global 30m model), landslide, subsidence, North Atlantic storms, tropical cyclones, storm surge, drought, extreme heat
- **Scenarios:** RCP 2.6 / 4.5 / 6.0 / 8.5 and SSP1-2.6 / 2-4.5 / 3-7.0 / 5-8.5, in 5-year steps from 2020 to 2100
- **Outputs:** portfolio physical risk score and risk distribution; hazard ratings A–G with accuracy (claimed up to 99%), probability and severity; **Expected Annual Loss** in money and %; climate value at risk (cVaR, used by the Tier 1 bank case study); PDF reports at asset and portfolio level; residential losses down to flat or unit
- **Method:** IPCC hazard × vulnerability × exposure; damage curves by building use and hazard, calibrated by region; CMIP5/CMIP6 models chosen per variable; building data on 1.5bn (or "over 2bn") assets ⚠️ with type and replacement cost; "glass-box" documentation and confidence scores with every report; independent model reviews within an MRM framework; Fathom integration [web]
- **Positioning:** "Replace outdated Power BI and Excel files with an intuitive interface that's as easy to use as Google Maps"; "no consultancy costs"

## Customers and users
- **Banks** [site]: climate and credit risk teams. Uses named on the site: stress testing, annual reports, **ICAAP**, capital, **ECL**, collateral value and insurability, credit assessment and lending decisions, originations, regional comparison. Regulation: **PRA SS5/25**, ECB, IFRS S2, EU Taxonomy, CSRD
- **Tier 1 bank case study** [site]: about 0.5m-property book; stress test and back-book analysis using cVaR for flood, storm, subsidence and heat; switched from a provider without subsidence; led to a provision figure and a review of where to lend. **Next step: Spectra API in mortgage underwriting**, scoring each application in real time
- **Real estate** [site, web]: CBRE, Aroundtown; disclosure, acquisition and resilience planning
- **Insurers, PE and asset managers, consultancies, infrastructure** [site]
- **Partners** [web]: Mitie, IBD Group, Scaler, Equans, Nfq, Embark
- Typical user: a risk analyst or sustainability lead, financially literate, not necessarily a climate expert [prep]

## Value proposition
- **For the buyer:** a defensible, asset-level view of physical risk in money terms, for lending, investment and disclosure decisions, without consultants [site]
- **ROI as Climate X frames it:** time saved, consultant cost avoided, better decisions ("know where to invest and where to sell") [site, prep]
- **Why now for UK banks:** SS5/25 expects asset-level (not postcode) data, forward-looking horizons, documented lineage and justified scenarios; supervisors can ask for evidence since 3 June 2026 [site]

## Strengths [analysis, built on site]
- Financial loss, not just hazard scores; consistent in-house models across all 11 hazards
- Global coverage from one building database, including replacement cost, so customers can start without their own asset data
- Full scenario × horizon grid to 2100, including defended / undefended flood
- Glass-box documentation and MRM alignment answer the regulator's black-box concern
- Several ways in: self-serve app, CSV, API, partners

## Weaknesses and risks [analysis]
- **Property loss ≠ bank loss:** outputs are damage to the asset. Banks need loan impact (LTV, LGD, insurance, default) for ECL and capital. Climate X's own article says indirect losses run 6–14× direct damage, so a direct-damage figure understates exposure
- **Judgment calls move the headline:** scenario, horizon, hazard set, defended or not, per-loan vs per-property counting, missing data. Each can shift a total by a large multiple; two analysts can report different numbers from the same export
- **Scenario set in transition:** SSP5-8.5 is retiring under CMIP7 (Climate X's own guidance: SSP3-7.0 for continuity plus tail overlays). Customers whose "severe" default is SSP5-8.5 need a managed change
- **Wide exports are hard to use:** dozens of hazard × scenario × year × metric columns need reshaping, which is where Excel and Power BI work creeps back in
- **Incumbents bundle:** Moody's and S&P attach climate data to credit data; Climate X has to win on depth, usability and trust

## Opportunities (hypotheses to test in discovery) [analysis]
1. **Answers with their method (SS5/25 evidence):** every figure with scenario, horizon, population, exclusions, data dates and lineage stated, reproducible, with an audit trail. Matches the regulator's lineage expectations and Climate X's "glass box" stance
2. **Analyst agent:** plain-English questions turned into structured choices (shown back for confirmation), answers computed in code with cited rows. AI interprets, code computes. Climate X already uses "every number traceable back to source" for the Infrastructure Screener
3. **Scenario transition support:** show answers under the old and new "severe" (SSP5-8.5 vs SSP3-7.0 plus overlay) side by side, with the change documented for the methodology owner
4. **Lender view and provisions:** property loss to loan-level impact with customer-supplied LTV, LGD and insurance, and an indirect-loss uplift where justified. Feeds ECL and ICAAP
5. **Underwriting via API:** the case study's next step. Real-time checks on new mortgage applications against the bank's risk appetite thresholds
6. **Event impact:** when a flood or storm hits, which assets and loans are exposed, and by how much
7. **Decision thresholds per customer:** at what rating or loss does a risk change this customer's lending, pricing or investment decision? Configurable thresholds, and a signal to the science team about which models to prioritise
8. **Partner-ready outputs:** views partners can resell without climate expertise

## Discovery questions (non-leading)
- Walk me through the last time a Spectra number went into a decision or a report. Who used it and what did they do?
- At what point does a risk start to change your decision? Why there? Is it the same across portfolios?
- When someone challenged one of these numbers, what did you show them?
- How do you get from damage to the property to an impact on your book, or on provisions?
- Which scenario and horizon do you report, how did you justify it, and what happens as SSP5-8.5 retires?
- What do you do with the export after downloading it?

## Related
- Company, regulation and competitors: the `climate-x-company` skill
- Role and positioning: the `climate-x-role` skill
- Data analysis method: the `pm-data-discovery` skill
