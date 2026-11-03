---
name: climate-x-products
description: "Climate X's products: Spectra (physical risk → financial loss), Adapt and Adaptation Finance, Carta (asset maps for 18.7m companies), Infrastructure Screener. For each: what it does, who buys it, gaps and opportunities (my take), discovery questions. Use when discussing a product, a Climate X export, or feature ideas."
---

# Climate X products

Facts from climate-x.com (Nov 2026); "my take" = my inference, to test with customers. Company, method, regulation, competitors: `climate-x-company`.

**How they connect:** Carta (company → assets) → Spectra (assets → loss) → Adapt (loss → action, ROI) → Adaptation Finance (action → bank revenue). Screener = Spectra for infrastructure.

## Spectra
How much could my assets lose, under which scenario, when?
- **What:** search an address or upload a portfolio (up to 100k) → ratings A–G (accuracy, probability, severity), Expected Annual Loss (£, %), cVaR, portfolio score; 11 hazards, RCPs and SSPs to 2100. Web app, CSV, PDF, API. Pitch: "Replace outdated Power BI and Excel files"
- **Buyers:** banks (stress tests, ICAAP, capital, ECL, lending decisions, SS5/25 evidence), real estate, insurers, PE; partners (Mitie, IBD, Scaler, Nfq). User: risk analyst, not a climate expert
- **Proof:** Tier 1 bank, ~0.5m properties → provision figure; next: API in mortgage underwriting
- **Gaps (my take):** property damage ≠ bank loss (their own article: indirect losses 6–14× direct) · choices move the headline (scenario, year, hazards, defended, per-loan vs per-property) · "severe" moving from SSP5-8.5 to SSP3-7.0 · wide exports push people back into Excel · incumbents bundle with credit data
- **Opportunities (my take):** answers with their method (SS5/25 evidence by default) · analyst agent: question → confirmed choices → numbers from code · old vs new "severe" side by side · lender view (LTV, LGD, insurance → ECL, ICAAP) · underwriting via API · event impact · decision thresholds per customer (also guides the science team)
- **Questions:** last time a Spectra number went into a decision, what happened? · At what point does a risk change your decision, and why there? · When a number was challenged, what did you show? · How do you get from property damage to your book? · Which scenario do you report, and what changes as SSP5-8.5 retires? · What do you do with the export?

## Adapt and Adaptation Finance
What should I do about it, what does it cost, what's the ROI? Can a bank finance it?
- **What:** per-asset report in ~60s: pre-adaptation risk, cost, 1- and 10-year ROI, loss savings, post-adaptation risk. E.g. flood defences: loss £33,828 → £5,674, river flood E → A. ISO 14090/14091, EU Taxonomy
- **Adaptation Finance:** bank names clients → Carta maps assets → highest-ROI projects → risk engineers check → bank lends. "$2tn a year" gap. E.g. Hilton: 143 assets, $26.5m, ~$0.8m fees
- **Buyers:** real-estate owners (Aroundtown, CBRE), facilities partners (Mitie, Equans, IBD), banks (Triodos; corporate banking)
- **Gaps (my take):** cost and effectiveness assumptions vary by site · ROI depends on horizon, discount rate, scenario · avoided loss is hard to prove · a different buyer each time
- **Opportunities (my take):** resilience-linked loan pricing · capex optimiser within a budget · editable assumptions with source · relationship-manager flow: result → financing proposal · track realised value
- **Questions:** after a high-risk asset, what happens next, who decides to spend? · Last retrofit decision: what was the business case?

## Carta
Where are the assets of companies I lend to or invest in?
- **What:** asset maps for 18.7m public and private companies, subsidiaries incl. JVs >50%. Websites, job boards, registries, maps → classified, scored for materiality → AI + human review of every output → satellite checks on key sites → Spectra. Managed service, "days, not months", annual remap. UI shows confidence split (e.g. 90% high)
- **Buyers:** banks (corporate borrowers, provisions), investment banks (a top-3 bank), PE, insurers, advisers
- **Gaps (my take):** no complete golden set · missed sites understate risk, wrong ones cost trust · thin footprints for small firms · a managed service scales with people
- **Opportunities (my take):** provenance per site · evaluation on companies with known site lists (precision, recall) · self-serve for well-known companies · customer corrections feed the models · deal and credit pack · alerts when key sites change
- **Questions:** how do you assess a borrower's physical risk today, and how long? · Last time you relied on an asset list, how did you know it was complete?

## Infrastructure Screener
What's the risk to a site that spans more than a point?
- **What:** solar, wind, transmission, pipelines, water, roads, rail. Draw or upload the footprint → 11 hazards at sub-component level, time and scenario deltas → AI report, "every number traceable back to source". "95% faster than manual"
- **Buyers:** infrastructure investors, utilities, developers; investment committees
- **My take:** their clearest example of AI writing the story while every number traces to source; the same pattern fits bank reporting
- **Opportunities:** the traceable report for Spectra portfolios · knock-on effects across a network · project-finance covenant sensitivity
- **Questions:** how do you assess a site that spans kilometres today? · What does your investment committee need to trust a figure?
