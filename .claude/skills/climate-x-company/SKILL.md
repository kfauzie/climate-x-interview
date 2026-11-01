---
name: climate-x-company
description: "Background on Climate X the company: mission and values, funding, founders and advisers, stage, product line-up, methodology, regulation (PRA SS5/25, ECB, IFRS S2), banking use cases, partnerships, thought leadership, brand and product look, and competitors (Moody's RMS, Jupiter, S&P), with sources. Use for company context, market and competitive positioning, commercial, strategy or culture questions, regulatory context, or to check which claims are verified."
---

# Climate X: company brief

Updated 2026-11-01 from climate-x.com (read directly) and web search. Source tags: **[site]** climate-x.com, **[web]** press or third parties, **[prep]** my preparation notes, **[analysis]** my inference. Site claims are Climate X's own marketing: accurate as to what they say, not independently verified. ⚠️ marks conflicts.

## Mission, vision and values [site]
- **Vision:** "Make every location on Earth resilient." **Mission:** "Drive resilient capital, asset by asset"
- **Values:** (1) Win when our customers win: "customer outcomes, not just our output"; (2) Tell it like it is: candour and transparency; (3) Own everything you touch: "draft to done… step up before we're asked"; (4) Bet on ourselves and move: "build fast, and we build it right"; (5) Have each other's backs
- [analysis] These match the role: customer-outcome obsession, candour, end-to-end ownership, speed with quality. Useful for "why Climate X" and for the conversation with a co-founder

## Company
- UK-headquartered B2B climate-risk analytics. Co-founders Lukky Ahmed (CEO) and Kamil Kluza (COO in most sources, CPO in one ⚠️) [web]
- **Funding:** $18m Series A, June 2024, led by GV [web]. Investors listed on the site: GV, WTI, PropTech1, Unconventional Ventures, CommerzVentures, noa [site]. Tracxn: $24.9m in total [web]. No 2026 round found. Prep notes: between Series A and B, about 85 people, approaching profitability [prep]
- **Advisory board** [site]: Bob Wigley (Chair of UK Finance; ex-Chair Merrill Lynch EMEA; former Bank of England Court member), David Carlin (Head of Risk, UNEP FI), Jackie (20+ years in mortgages, OBE; conduct and regulation), Iván Markman (ex-Yahoo), Sunil Kappagoda (ex-BCG, Verifone APAC)
- **Science partners** [site]: CCRM (Oxford-originated consultancy), with Prof Stephan Harrison, Prof David Stainforth (co-founder of climateprediction.net), Dr Mike Harrison (ex-Met Office, WMO)
- **Scale claims** [site]: clients with "over $13.5 trillion" combined AUM; "trusted by G-SIBs"; Carta "trusted by a top 3 investment bank". The banking case study says target sectors hold "over $45tr in AUM" ⚠️ (a market figure, not a client figure)
- **Awards** [site]: Deloitte, Cog X, Digital Catapult, Founders Forum, Chartis "Rising Star", among others
- **Security and governance** [site]: ISO certifications, "InfoSec compliant", works "in accordance with the PRA's Model Risk Management (MRM) frameworks", independent model reviews

## Product line-up (detail in `climate-x-products`)
| Product | What it does [site] |
|---|---|
| **Spectra** | Physical climate risk turned into asset- and portfolio-level financial loss (web app, CSV upload, Enterprise API, PDF reports) |
| **Adapt** | Cost and ROI of adaptation measures per asset (pre/post-adaptation loss, 1- and 10-year ROI), report in about 60 seconds |
| **Carta** | Maps the physical assets and subsidiaries of 18.7m public and private companies; feeds Spectra. Run as a managed service |
| **Infrastructure Screener** | New app: screens spatially complex infrastructure (solar, wind, transmission, pipelines, water, roads, rail) against 11 hazards, with an AI-written report where "every number [is] traceable back to source" |
| **Adaptation Finance** | Offer for banks: find clients' highest-ROI resilience projects, risk-engineer due diligence, then finance them ("a $2 trillion opportunity") |
| **Enterprise API** | Programmatic access for hundreds of thousands of assets; CSV export to Tableau, Power BI, Qlik |

## Methodology [site]
- **IPCC framework:** hazard × vulnerability × exposure. "Glass-box methodology": full documentation with every report, plus confidence scores per hazard and regional accuracy
- **11 hazards (confirmed):** river, surface and coastal flooding (defended / undefended), wildfire, landslide, subsidence, North Atlantic storms, tropical cyclones, storm surge, drought, extreme heat. The "16 hazards" figure from a third-party profile is wrong
- **Scenarios:** RCP 2.6 / 4.5 / 6.0 / 8.5 and SSP1-2.6 / 2-4.5 / 3-7.0 / 5-8.5, in 5-year steps from 2020 to 2100
- **Outputs:** portfolio risk score and distribution; hazard ratings with accuracy (claimed up to 99%), probability and severity; Expected Annual Loss in money and %; climate value at risk (cVaR, confirmed by the Tier 1 bank case study; a third-party comparison saying otherwise is wrong)
- **Data:** CMIP5 and CMIP6 models, best-performing chosen per variable; damage curves by building use and hazard, calibrated by region; building database of 1.5bn assets (methodology and banking pages) or "over 2 billion" (Spectra page) ⚠️; resolution down to 10–30m; residential losses at flat or unit level
- **Model governance:** validated against historical events; peer-reviewed; independent model reviews within an MRM framework
- **Integration:** Fathom model integration for water, wind, fire and earth perils (Oct 2025) [web]

## Regulation (where Climate X sells into) [site]
- **PRA SS5/25** (UK): in force 3 December 2025, replaced SS3/19 entirely; 140 paragraphs over governance, risk management, scenario analysis, data, disclosures, banking and insurance. The six-month review window closed **3 June 2026**: supervisors can now ask for the gap analysis, remediation plan and evidence. Key data expectations: **asset-level, not postcode averages**; forward-looking to 2030, 2050 and 2100 under several pathways; data inventories with owners, lineage and uncertainties; proxies disclosed and justified. Scenario analysis must document methods and assumptions, justify scenario choice against IPCC / NGFS, cover a central case plus tail risks, and show how it drives decisions. Climate risk to be folded into ICAAP / ILAAP / ORSA
- **ECB:** first-ever penalty on a bank for failing to assess climate risk materiality (Nov 2025, per Climate X)
- Also: IFRS S2 / TCFD, CSRD / ESRS, EU Taxonomy, SB 261 (California), AASB (Australia), CSDS, SEC
- [analysis] For UK banks, SS5/25 is the "why now": the evidence, lineage and scenario-justification expectations map directly onto audit trails and stated assumptions

## Customers and use cases [site]
- **Industries:** banking, insurance, real estate, private equity and asset management, consultancies, infrastructure
- **Banking uses:** stress testing, annual reports, ICAAP, capital, ECL; collateral value and insurability; credit assessment and lending decisions; originations; portfolio comparison by region. Workflow: upload a CSV of up to 100k addresses, download a PDF report
- **Tier 1 bank case study:** a European digital bank with 180+ years' heritage (retail, business, agriculture) replaced a heritage provider that lacked subsidence and benchmarked poorly. It used Spectra cVaR data (flood, storm, subsidence, heat) under RCPs and SSPs at 5-year steps to 2100 for stress testing and back-book analysis of about 0.5m properties. Results: property-level risk, a $ provision quantification, a rethink of which postcodes to lend to. Next: Spectra via API inside **mortgage underwriting**, assessing each application in real time
- **Positioning lines on the site:** "Replace outdated Power BI and Excel files with an intuitive interface"; "no consultancy costs"; "know where to invest and where to sell"

## Partnerships and go-to-market [web, site]
- CBRE (expanded climate risk capabilities with Climate X; joint wildfire report), Aroundtown, IBD Group (Aug 2026), Mitie (Jun 2026), Scaler, Equans, Embark (US), Nfq (Spain, banks), Triodos Bank, Fathom (model integration)
- Pattern: direct enterprise sales plus partners and resellers who turn the data into services

## Thought leadership (what Climate X is arguing publicly) [site]
- **"Your bank's physical risk provisions are probably wrong"**: direct-damage-only models miss most of the loss; indirect impacts (revenue loss, supply chain, business interruption) run **6–14×** direct damage (Climate X's own analysis about 6×; MSCI about 14×). Calls for "Gen 2" models that quantify financial loss and map full corporate asset hierarchies (Carta). Claims about a third of G-SIBs are building this
- **CMIP7 and the retirement of RCP8.5 / SSP5-8.5:** the new "High" scenario is lower; use **SSP3-7.0** for continuity and add tail overlays for stress tests; current pathway is about 2.6°C, i.e. near **SSP2-4.5**; "scenarios are inputs, not predictions"; model choice matters as much as scenario
- **Wildfire with CBRE:** indirect exposure (power shutoffs, smoke, insurance withdrawal) touches far more assets than direct burn; 3.4m US premises at high risk now, about 3.6m by 2040 under SSP2-4.5
- **Engineering:** "Querying 240 terabytes of global hazard data in real time" at 30m resolution
- [analysis] The public stance is "glass box, financial loss not hazard scores, beyond direct damage". A prototype that shows its method, traces every number and separates property damage from bank loss fits the company's own narrative

## Brand (from climate-x.com's own CSS) [site]
- **Font:** Graphik (commercial typeface from Commercial Type), with Helvetica and Arial as fallbacks
- **Colours:** brand red `#e01e1a` (hover and darker red `#a11b14`), charcoal text `#343a40`, off-white background `#f9f9fa`, white surfaces `#ffffff`
- **Product look and feel** (Spectra, Adapt and Carta screenshots): light UI with white panels and hairline grey dividers (Carta also has a dark map view with teal); small grey uppercase section labels ("Settings", "Risk dashboard"); settings as rounded dropdowns (SSP scenario, year) at the top of a side panel, with a red active state on toggles (Undefended / Defended, Flood Defences on/off); rating letters A–G in circular badges coloured by severity; large light-weight numbers for headline figures; fully rounded pill buttons with icons; red reserved for primary actions, active states and callouts; compact tables (Rating, Severity, Probability, Accuracy; "Acute" / "Chronic" headers in red); "Pre-Adapt" vs "Post-Adapt" side-by-side panels in Adapt
- Use in prototype code for Climate X. On a page published for others, don't present it as Climate X's own product (see `pm-design`)

## Competitive landscape [web]
- **Moody's** (including RMS): ranked #1 in Chartis Physical & Infrastructure Risk50 2025; bundled with credit data
- **Jupiter Intelligence:** "investment-grade" analytics and model transparency for regulators; claims 25% of top US banks
- **S&P Global** (bought The Climate Service), XDI, EarthScan, AccuWeather, Mitiga
- Climate X's counter-positioning [site]: in-house models consistent across all hazards, glass-box documentation, financial loss rather than hazard scores, MRM alignment, self-serve speed instead of consultants

## Implications (inferred) [analysis]
- Customer datasets will look like Spectra outputs: ratings, £ and % annual loss (EAL), possibly cVaR, by hazard × scenario × horizon, often with defended / undefended flood
- A UK bank's pain sits between the export and a number it can defend under SS5/25: choosing and justifying scenarios, aggregating to portfolio level, getting from property damage to bank loss, documenting lineage
- Scenario choice is shifting: SSP5-8.5 is retiring; SSP3-7.0 and tail overlays become the "severe" case. Defaults built on SSP5-8.5 need a review path
- Commercial angles: the case study's "next step" is underwriting via API; Adaptation Finance turns risk into bank revenue; partners need outputs non-experts can use

## Discovery angles [analysis]
- "When your regulator or auditor last asked how a number was produced, what did you show them?"
- "How do you get from property-level loss to an impact on the loan book, or to provisions?"
- "Which scenarios do you report, and how did you justify them? What changes as SSP5-8.5 retires?"
- "What did the SS5/25 gap analysis say about your data?"
- "Who outside your team uses these outputs, and in what form?"

## Sources
- climate-x.com (fetched 2026-11-01): [Home](https://www.climate-x.com/), [Values](https://www.climate-x.com/values), [About us](https://www.climate-x.com/about-us), [Spectra](https://www.climate-x.com/spectra), [Methodology](https://www.climate-x.com/spectra/methodology), [Adapt](https://www.climate-x.com/adapt), [Carta](https://www.climate-x.com/carta), [Infrastructure Screener](https://www.climate-x.com/products/infrastructure-climate-risk-screener), [Adaptation Finance](https://www.climate-x.com/adaptation-finance), [Banking](https://www.climate-x.com/industries/banking), [Banking case study](https://www.climate-x.com/case-studies/climate-risk-for-banking), [SS5/25](https://www.climate-x.com/regulation/ss5-25), [FAQs](https://www.climate-x.com/faqs), [Provisions article](https://www.climate-x.com/articles/industry/your-physical-risk-provisions-are-probably-wrong), [CMIP7 guide](https://www.climate-x.com/articles/industry/a-guide-to-cmip7-climate-scenerios), [CBRE wildfire report](https://www.climate-x.com/wildfire-risk-and-the-new-real-estate-calculus), [Mitie](https://www.climate-x.com/articles/press-releases/climate-x-and-mitie-partner-to-help-organisations-build-climate-resistance), [IBD Group](https://www.climate-x.com/articles/press-releases/climate-x-ibd-group-partnership)
- Funding: [Finextra](https://www.finextra.com/newsarticle/44382/google-ventures-leads-18-million-round-in-climate-x), [ESG Today](https://www.esgtoday.com/climate-risk-assessment-platform-climate-x-raises-18-million/), [Tracxn](https://tracxn.com/d/companies/climate-x/__VpG6gSK3ixZ_aPDED1BGjZ06ZZiqI5pdfLwGsMRe5iE)
- Partners: [Triodos (FinTech Global)](https://fintech.global/2025/01/13/climate-x-links-with-triodos-bank-to-enhance-climate-resilience-for-smes/), [Nfq](https://nfq.uk/new-corporate-partnership-climate-x/)
- Third party: [Moody's Chartis ranking](https://www.moodys.com/web/en/us/insights/physical-transition-risk/moodys-ranked-1-in-chartis-physical-and-infrastructure-risk50-2025.html), [Jupiter (Business Wire)](https://www.businesswire.com/news/home/20250723646042/en/Jupiter-Intelligence-Establishes-New-Standard-for-Investment-Grade-Climate-Analytics), [Trellis](https://trellis.net/article/climate-risk-analytics-software-scene-expanding/), [Mitiga comparison](https://www.mitigasolutions.com/compare/best-climate-risk-platforms-compared) (its cVaR claim is contradicted by Climate X's case study)
