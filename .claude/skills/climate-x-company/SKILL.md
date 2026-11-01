---
name: climate-x-company
description: "Background on Climate X the company: funding, founders, stage, products at a glance, methodology, banking use cases, partnerships, go-to-market and competitors (Moody's RMS, Jupiter, S&P), with sources. Use for company context, market and competitive positioning, commercial or strategy questions, or to check which claims are verified."
---

# Climate X: company brief

Compiled 2026-11-01 from web search results and my preparation notes. Most product claims come from Climate X's own marketing and are **unverified**. Points where sources conflict are marked ⚠️.

## Company
- UK-headquartered B2B physical climate-risk analytics company. Co-founders: Lukky Ahmed (CEO) and Kamil Kluza (COO in most sources, CPO in one ⚠️)
- Funding: $18m Series A in June 2024, led by GV (Google Ventures). Tracxn lists $24.9m in total, including CommerzVentures and Pale Blue Dot. Stated use of the round: expansion in Europe, North America and APAC. No 2026 round found. Prep notes: between Series A and B, about 85 people, approaching profitability
- Named clients (company-reported): Goldman Sachs, CBRE, Deloitte. Also claims clients with more than $13.5tn in combined AUM

## Brand (from climate-x.com's own CSS, fetched 2026-11-01)
- **Font:** Graphik (a commercial typeface from Commercial Type), with Helvetica and Arial as fallbacks
- **Colours:** brand red `#e01e1a` (hover and darker red `#a11b14`), charcoal text `#343a40`, off-white background `#f9f9fa`, white surfaces `#ffffff`
- **Product look and feel** (Spectra and Carta screenshots on climate-x.com): light UI with white panels and hairline grey dividers (Carta also has a dark map view with teal); small grey uppercase section labels ("Settings", "Risk dashboard"); settings as rounded dropdowns (SSP scenario, year) at the top of a side panel, with a red active state on toggles (Undefended / Defended); rating letters A–G in circular badges coloured by severity; large light-weight numbers for headline figures; fully rounded pill buttons with icons; red reserved for primary actions, active states and callouts; compact tables (Rating, Severity, Probability, Accuracy; "Acute" / "Chronic" group headers in red)
- Use in prototype code for Climate X. On a page published for others, don't present it as Climate X's own product (see `pm-design`)

## Products
- **Spectra**: asset- and portfolio-level physical risk
  - Outputs: hazard-specific risk ratings, annual losses in £ and as % of value, climate-adjusted VaR (cVaR) out to 2100
  - Hazard count varies by source: 11 (company site) vs 16 (third-party profile) ⚠️
  - One third-party comparison says Spectra lacks probabilistic modelling, custom return periods and CVaR. This conflicts with Climate X's own cVaR claims and may be out of date ⚠️
- **Adapt**: models the cost and ROI of adaptation measures (retrofits, flood defences, heat resilience)
- **Carta**: maps a company's structure, subsidiaries and assets, and the risk that flows through them (source: prep notes only; no public source found ⚠️)
- Recent launch: a global asset-level wildfire model at 30m resolution

## Methodology (as Climate X describes it)
- Damage curves: link hazard severity to damage, specific to building use and hazard, and calibrated by region
- Downscaled multi-model climate projections, combined with proprietary vulnerability data and geospatial hazard models
- Building database of about 1.5bn assets worldwide, with building type and replacement cost
- Fathom integration (Oct 2025) for water, wind, fire and earth perils, described as "the most defensible global model stack"
- Alignment claims: NGFS pathways, EU Taxonomy, ECB / IFRS frameworks, central-bank stress tests, TCFD

## Banking use cases
- Climate impact on **collateral value and insurability**
- Regulatory **stress testing and scenario analysis** (central banks, the ECB, and by implication the PRA in the UK)
- Case study: a European Tier 1 bank used Spectra cVaR loss data for stress testing and analysis of its existing loan book
- Triodos Bank: Spectra and Adapt built into risk management for SME lending
- Nfq (Spanish consultancy, 2025): resells Climate X data to banking clients

## Recent partnerships (show where the go-to-market is heading)
- IBD Group (Aug 2026): real-estate resilience plans and disclosures
- Mitie (Jun 2026): powers Mitie's UK Climate Change Risk Assessment service
- Scaler (2026): CRE sustainability performance
- Aroundtown and Equans: real-estate portfolios and estates
- Embark (US): California climate disclosure advisory
- Pattern: growth through **partners and resellers** (consultancies, facilities managers) as well as direct sales

## Competitive landscape
- **Moody's** (including RMS): ranked #1 in Chartis Physical & Infrastructure Risk50 2025. Incumbent, bundled with credit data
- **Jupiter Intelligence**: positions on "investment-grade" analytics and model transparency for regulators. Claims 25% of top US banks
- **S&P Global** (acquired The Climate Service), plus XDI, EarthScan, AccuWeather, Mitiga
- Consolidation: the big rating agencies are buying smaller players
- The theme regulators keep raising: **black-box models**. Supervisors want projections they can check

## Implications (inferred)
- Customer datasets will probably resemble Spectra outputs: ratings, £ and % annual loss, possibly cVaR, by hazard × scenario × horizon
- A banking customer's pain will likely sit between the export and a number they can defend: choosing scenarios, aggregating to portfolio level, linking to collateral and LGD, and explaining the model to a regulator
- The way to stand out from Moody's and Jupiter is trust and explainability. The feature should show its assumptions, cite the rows it used and keep an audit trail, which fits the deterministic-plus-AI split
- Commercial angle: partners and resellers need outputs that non-experts can use (a consultancy or a facilities manager turning data into a plan). Ask the customer who else sees these numbers

## Discovery angles from this research
- "When your regulator or auditor last asked how a number was produced, what did you show them?"
- "How do you get from property-level loss to an impact on the loan book?"
- "Which scenario set do you have to use: NGFS, SSPs, or the PRA's?"
- "Who outside your team uses these outputs, and in what form?"

## Sources
- climate-x.com pages: [Spectra](https://climate-x.com/spectra), [Methodology](https://www.climate-x.com/spectra/methodology), [Banking](https://www.climate-x.com/industries/banking), [Banking case study](https://www.climate-x.com/case-study-climate-risk-for-banking), [Real estate](https://www.climate-x.com/industries/real-estate), [FAQs](https://www.climate-x.com/faqs), [Series A](https://www.climate-x.com/articles/press-releases/series-a), [Mitie](https://www.climate-x.com/articles/press-releases/climate-x-and-mitie-partner-to-help-organisations-build-climate-resistance), [IBD Group](https://www.climate-x.com/articles/press-releases/climate-x-ibd-group-partnership)
- Funding: [Finextra](https://www.finextra.com/newsarticle/44382/google-ventures-leads-18-million-round-in-climate-x), [ESG Today](https://www.esgtoday.com/climate-risk-assessment-platform-climate-x-raises-18-million/), [Tracxn](https://tracxn.com/d/companies/climate-x/__VpG6gSK3ixZ_aPDED1BGjZ06ZZiqI5pdfLwGsMRe5iE)
- Partners: [Triodos (FinTech Global)](https://fintech.global/2025/01/13/climate-x-links-with-triodos-bank-to-enhance-climate-resilience-for-smes/), [Nfq](https://nfq.uk/new-corporate-partnership-climate-x/)
- Third party: [Mitiga platform comparison](https://www.mitigasolutions.com/compare/best-climate-risk-platforms-compared), [Moody's Chartis ranking](https://www.moodys.com/web/en/us/insights/physical-transition-risk/moodys-ranked-1-in-chartis-physical-and-infrastructure-risk50-2025.html), [Jupiter (Business Wire)](https://www.businesswire.com/news/home/20250723646042/en/Jupiter-Intelligence-Establishes-New-Standard-for-Investment-Grade-Climate-Analytics), [Trellis](https://trellis.net/article/climate-risk-analytics-software-scene-expanding/)
