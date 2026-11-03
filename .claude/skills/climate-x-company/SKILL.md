---
name: climate-x-company
description: "Climate X the company: snapshot, mission and values, methodology, regulation its customers face (PRA SS5/25), customers and proof points, partners, what it argues publicly, competitors, brand and product look. Facts from climate-x.com and press, with sources. Use for company, market, regulatory or competitive context."
---

# Climate X

From climate-x.com (read Nov 2026) unless marked (web) for press or third parties. Their claims, not independently verified. ⚠️ = sources disagree.

## Snapshot
- B2B physical climate-risk analytics, London. "Google Maps for climate change"
- Founders: Lukky Ahmed (CEO), Kamil Kluza (COO; CPO in one source ⚠️)
- $18m Series A, June 2024, led by GV (web). Also WTI, PropTech1, Unconventional Ventures, CommerzVentures, noa. ~$24.9m raised in total (web, Tracxn)
- Advisers: Bob Wigley (Chair, UK Finance), David Carlin (UNEP FI), a mortgage-industry OBE, Iván Markman, Sunil Kappagoda. Science partner: CCRM (Oxford-originated)
- Claims: clients with $13.5tn+ AUM; G-SIBs; a top-3 investment bank (Carta). ISO certified; works to PRA model risk management frameworks

## Mission and values
- Vision: "Make every location on Earth resilient." Mission: "Drive resilient capital, asset by asset"
- Values: win when customers win · tell it like it is · own everything you touch · bet on ourselves and move · have each other's backs

## Products (detail in `climate-x-products`)
- Spectra: physical risk → financial loss, asset and portfolio
- Adapt (+ Adaptation Finance): cost and ROI of adaptation; financing it through banks
- Carta: asset maps for 18.7m companies, as a managed service
- Infrastructure Screener: solar, pipelines, networks; AI report with every number traceable
- Access: web app, CSV, PDF reports, Enterprise API

## Method
- IPCC: hazard × vulnerability × exposure. Damage curves by building use and hazard, calibrated by region
- 11 hazards: river, surface, coastal flood (defended / undefended), wildfire (30m), landslide, subsidence, N. Atlantic storms, tropical cyclones, storm surge, drought, extreme heat
- Scenarios: RCP 2.6–8.5, SSP1-2.6 / 2-4.5 / 3-7.0 / 5-8.5; 5-year steps, 2020–2100
- Outputs: ratings A–G with accuracy (up to 99%), probability, severity; Expected Annual Loss (£, %); cVaR; portfolio score
- Data: CMIP5/6 models picked per variable; 1.5bn buildings (2bn on the Spectra page ⚠️); "glass-box" docs and confidence per hazard; independent model reviews
- Fathom model integration, Oct 2025 (web)

## Regulation
- **PRA SS5/25** (UK): in force Dec 2025, replaced SS3/19. Review window closed 3 June 2026 → supervisors can ask for gap analyses and evidence. Expects asset-level data (not postcodes), 2030/2050/2100 under several pathways, data lineage, proxies disclosed, scenario choice justified (central + tail), climate in ICAAP / ILAAP / ORSA
- ECB: first climate-risk penalty on a bank, Nov 2025
- Also: IFRS S2 / TCFD, CSRD / ESRS, EU Taxonomy, SB 261, AASB, CSDS, SEC

## Customers and proof
- Banks, insurers, real estate, PE and asset managers, consultancies, infrastructure
- Bank uses: stress tests, ICAAP, capital, ECL, annual reports, credit and lending decisions. Upload up to 100k addresses → PDF report
- Tier 1 bank case study: ~0.5m properties; cVaR for flood, storm, subsidence, heat; replaced a provider without subsidence → provision figure, rethink of where to lend. Next: Spectra API in mortgage underwriting
- Pitch lines: "Replace outdated Power BI and Excel files"; "no consultancy costs"

## Partners
- CBRE, Aroundtown, IBD Group (Aug 2026), Mitie (Jun 2026), Scaler, Equans, Embark, Nfq, Triodos, Fathom (web)
- Pattern: direct sales + partners who turn the data into services

## What they argue publicly
- Bank provisions are too low: direct-damage models miss indirect losses 6–14× larger → "Gen 2" models with financial loss and full asset hierarchies
- CMIP7 retires SSP5-8.5 → use SSP3-7.0 + tail overlays; current path ≈ SSP2-4.5; "scenarios are inputs, not predictions"
- Wildfire (with CBRE): indirect exposure (power, smoke, insurance) reaches far more assets than burns
- Real-time queries over 240TB of hazard data at 30m

## Competitors (web)
- Moody's RMS (#1 Chartis 2025, bundled with credit data), Jupiter (model transparency; "25% of top US banks"), S&P (bought The Climate Service), XDI, EarthScan, Mitiga
- Climate X's answer: in-house models across all hazards, glass-box docs, financial loss not hazard scores, self-serve speed

## Brand and product look
- Graphik (Helvetica, Arial fallback). Red `#e01e1a` (hover `#a11b14`), charcoal `#343a40`, off-white `#f9f9fa`, white panels
- Product UI: light, white panels, hairline dividers, small grey uppercase labels; settings (scenario, year) as rounded dropdowns in a side panel; red active toggles (defended / undefended); A–G ratings as coloured circles; big light-weight numbers; pill buttons; red only for primary and active; compact tables; Adapt shows pre vs post side by side
- Brand in prototype code only; a published page doesn't present itself as Climate X

## My take
- Customer data will look like Spectra output: ratings, EAL, maybe cVaR, by hazard × scenario × year
- A UK bank's pain sits between the export and a number it can defend under SS5/25: scenario choice, aggregation, property damage → bank loss, lineage
- "Severe" is moving from SSP5-8.5 to SSP3-7.0; defaults need an owner and a change path
- Their own story (glass box, financial loss, traceable AI reports) is the bar for anything I build

## Sources
- climate-x.com: [home](https://www.climate-x.com/), [values](https://www.climate-x.com/values), [about](https://www.climate-x.com/about-us), [Spectra](https://www.climate-x.com/spectra), [methodology](https://www.climate-x.com/spectra/methodology), [Adapt](https://www.climate-x.com/adapt), [Carta](https://www.climate-x.com/carta), [Screener](https://www.climate-x.com/products/infrastructure-climate-risk-screener), [Adaptation Finance](https://www.climate-x.com/adaptation-finance), [banking](https://www.climate-x.com/industries/banking), [case study](https://www.climate-x.com/case-studies/climate-risk-for-banking), [SS5/25](https://www.climate-x.com/regulation/ss5-25), [FAQs](https://www.climate-x.com/faqs), [provisions](https://www.climate-x.com/articles/industry/your-physical-risk-provisions-are-probably-wrong), [CMIP7](https://www.climate-x.com/articles/industry/a-guide-to-cmip7-climate-scenerios), [CBRE wildfire](https://www.climate-x.com/wildfire-risk-and-the-new-real-estate-calculus)
- Web: [Finextra](https://www.finextra.com/newsarticle/44382/google-ventures-leads-18-million-round-in-climate-x), [Tracxn](https://tracxn.com/d/companies/climate-x/__VpG6gSK3ixZ_aPDED1BGjZ06ZZiqI5pdfLwGsMRe5iE), [Triodos](https://fintech.global/2025/01/13/climate-x-links-with-triodos-bank-to-enhance-climate-resilience-for-smes/), [Nfq](https://nfq.uk/new-corporate-partnership-climate-x/), [Moody's Chartis](https://www.moodys.com/web/en/us/insights/physical-transition-risk/moodys-ranked-1-in-chartis-physical-and-infrastructure-risk50-2025.html), [Jupiter](https://www.businesswire.com/news/home/20250723646042/en/Jupiter-Intelligence-Establishes-New-Standard-for-Investment-Grade-Climate-Analytics)
