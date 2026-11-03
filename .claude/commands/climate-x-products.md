---
name: climate-x-products
description: "Climate X's products: Spectra (physical risk as financial loss), Adapt and Adaptation Finance, Carta (asset maps for 18.7m companies), Infrastructure Screener. For each: what it does, who buys it, gaps, opportunities and discovery questions. Use when discussing a product, a Climate X export, or feature ideas."
---

# Climate X products

Facts from climate-x.com (November 2026). Gaps and opportunities are my own reading, to test with customers. Company, models and regulation: `climate-x-company`.

**How they connect:** Carta finds a company's assets → Spectra prices their risk → Adapt shows what to do and the return → Adaptation Finance lets a bank lend for it. The Screener is Spectra for sites that span more than a point.

## Spectra
*How much could my assets lose, under which scenario, and when?*
- **What it does:** search an address or upload up to 100k. Returns A–G ratings with accuracy, probability and severity, Expected Annual Loss in £ and %, climate value at risk, and a portfolio score. Web app, CSV, PDF reports and an API. Pitched as a replacement for "outdated Power BI and Excel files"
- **Who buys it:** banks (stress tests, capital planning, provisions, lending decisions), real estate, insurers, private equity, and partners such as Mitie and Nfq. The day-to-day user is a risk analyst, not a climate expert
- **Proof:** a Tier 1 bank ran it across about 0.5m properties to size a provision; next it wants the API inside mortgage underwriting
- **Gaps:**
  - Damage to a property isn't loss to the bank, which also depends on loan size, recovery and insurance
  - Choices move the headline (scenario, year, hazards, flood defences, counting per loan or per property), so two analysts can get two numbers
  - "Severe" is shifting from SSP5-8.5 to SSP3-7.0
  - Wide exports push people back into Excel
- **Opportunities:**
  - Every answer arrives with its method, ready as regulatory evidence
  - An analyst assistant: plain-English question → choices the analyst confirms → numbers from code
  - Old and new "severe" side by side during the switch
  - A lender view: property loss turned into loan impact for provisions and capital
  - Risk checks inside underwriting through the API
  - Customer-specific thresholds, which also tell the science team what to prioritise
- **Questions:**
  - The last time a Spectra number went into a decision, what happened?
  - At what point does a risk change your decision, and why there?
  - When a number was challenged, what did you show?
  - What do you do with the export once you've downloaded it?

## Adapt and Adaptation Finance
*What should I do about it, what will it cost, and is it worth it?*
- **What it does:** a per-asset report in about a minute: risk before, cost, return over 1 and 10 years, loss avoided, risk after. Example: flood defences cut a building's expected loss from £33,828 to £5,674. Based on ISO adaptation standards
- **Adaptation Finance:** a bank names its corporate clients; Carta maps their assets; Climate X finds the best-return resilience projects and checks them with risk engineers; the bank lends. Example: Hilton, 143 assets, $26.5m of lending
- **Who buys it:** property owners (Aroundtown, CBRE), facilities firms (Mitie, Equans), banks (Triodos)
- **Gaps:**
  - Cost and effectiveness vary by site
  - The return depends on horizon and scenario
  - Avoided loss is hard to prove afterwards
- **Opportunities:**
  - Loan pricing that rewards completed resilience work
  - The best mix of measures for a fixed budget
  - Editable assumptions with their source
  - A flow that turns a result into a financing proposal
- **Questions:**
  - After you spot a high-risk asset, what happens next, and who decides to spend?
  - In your last retrofit decision, what did the business case look like?

## Carta
*Where are the assets of the companies I lend to or invest in?*
- **What it does:** maps the sites and subsidiaries of 18.7m public and private companies. Pulls from websites, job boards, registries and maps; classifies and scores each site; a person reviews every result; satellite images confirm key sites; the results feed Spectra. Run as a service, delivered "in days, not months", remapped yearly
- **Who buys it:** banks (corporate borrowers), investment banks (including a top-3 bank), private equity, insurers
- **Gaps:**
  - No complete answer key to measure accuracy against
  - A missed site understates risk; a wrong one costs trust
  - Small firms have thin public footprints
  - A people-heavy service is hard to scale
- **Opportunities:**
  - Show the sources and confidence behind each site
  - Measure accuracy on companies whose site lists are known
  - Self-serve for well-known companies
  - Let customer corrections improve the maps
  - Alerts when key sites change
- **Questions:**
  - How do you assess a borrower's physical risk today, and how long does it take?
  - The last time you relied on an asset list, how did you know it was complete?

## Infrastructure Screener
*What's the risk to a site that spans more than a point?*
- **What it does:** for solar and wind farms, power lines, pipelines, water networks, roads and rail. Draw or upload the footprint; it screens 11 hazards down to each part of the site and writes a report in which "every number [is] traceable back to source"
- **Who buys it:** infrastructure investors, utilities, developers
- **Why it matters:** their clearest example of AI writing the story while every number traces back to source. The same pattern would work for bank reporting
- **Questions:**
  - How do you assess a site that spans kilometres today?
  - What does your investment committee need before it trusts a figure?
