---
name: climate-x-products
description: "Context on Climate X's products: Spectra (physical risk as financial loss, incl. the Infrastructure Screener module), Adapt, Adaptation Finance, and Carta (asset maps for 18.7m companies). Use when a build involves one or more of these products. Background only: don't build features from this file unless asked."
---

# Climate X products

Facts from climate-x.com (November 2026). Company, models and regulation: `climate-x-company`.

**How they connect:** Carta finds a company's assets → Spectra prices their risk → Adapt shows what to do and the return → Adaptation Finance lets a bank lend for it.

## Spectra
*How much could my assets lose, under which scenario, and when?*

- **What it does:** search an address or upload up to 100k. Returns A–G ratings with accuracy, probability and severity, Expected Annual Loss in £ and %, climate value at risk, and a portfolio score. 11 hazards; CMIP6 SSP scenarios; flood defences can be toggled. Web app, CSV, PDF reports and an API.
- **Who buys it:** banks (stress tests, capital planning, provisions, lending decisions), real estate, insurers, private equity, and partners such as Mitie and Nfq. The day-to-day user is a risk analyst, not a climate expert.
- **Example:** a Tier 1 bank ran it across about 0.5m properties to size a provision.

### How Spectra works
- **The model:** follows the IPCC disaster-risk framework: risk = hazard × exposure × vulnerability.
  - **Hazard:** how likely and how severe an extreme weather event is at that location (e.g. a 1-in-100-year flood depth).
  - **Exposure:** what's there: the asset and its value.
  - **Vulnerability:** how much damage the hazard does to that kind of asset, depending on type (building, infrastructure), use (residential, commercial, office) and properties (age, materials).
- **Expected Annual Loss (EAL):** the average damage per year, adding up all possible events weighted by their probability. Shown in £, and as % of the asset's value. Example: an EAL of 0.5% on a £1m building means about £5,000 a year on average.
- **Climate projections (CMIP6 SSPs):** CMIP6 is the global set of climate models behind the latest IPCC report. SSPs (Shared Socioeconomic Pathways) are emissions scenarios: SSP1 low, SSP2 middle of the road, SSP3 high, SSP5 very high. Spectra offers SSP1, 2, 3 and 5, plus the older CMIP5 RCPs (2.6, 4.5, 6.0, 8.5). Climate X picks the best-performing models for each hazard and downscales them to asset level.
- **Data:** remote sensing, public databases and machine learning for loss modelling.
- **Trust:** validated by replaying past events against real-world losses; confidence scores per hazard; methodology and regional accuracy included with every report; works within the PRA's Model Risk Management framework.
- **To check:** how the A–G bands are set, and the exact list of 11 hazards.

### Infrastructure Screener (Spectra module)
- **What it does:** for sites that span more than a point: solar and wind farms, power lines, pipelines, water networks, roads and rail. Draw or upload the footprint; it screens 11 hazards down to each part of the site and produces a report where every number traces back to source.
- **Who buys it:** infrastructure investors, utilities, developers.

## Adapt
*This asset is at risk. What should I do, what will it cost, and is it worth it?*

- **What it does:** for one asset, suggests resilience measures (e.g. flood defences) and shows, in about a minute: the risk before, the cost of the measure, the loss it avoids, the return over 1 and 10 years, and the risk after. Based on ISO adaptation standards.
- **Example:** a building has an expected loss of £33,828 a year from flooding. With flood defences, it drops to £5,674. So the measure avoids about £28,000 a year; if it costs less than that over its life, it pays for itself.
- **Who buys it:** property owners (Aroundtown, CBRE), facilities firms (Mitie, Equans).

## Adaptation Finance
*Which resilience projects could my bank lend for?*

- **What it is:** a way for banks to find new lending. Instead of only measuring climate risk in their book, they lend clients the money to reduce it.
- **How it works:**
  1. The bank names its corporate clients.
  2. Carta maps each client's sites.
  3. Spectra and Adapt find the sites at risk and the resilience projects with the best return.
  4. Risk engineers check the projects.
  5. The bank offers the client a loan to pay for them.
- **Example:** Hilton: 143 assets mapped and assessed, leading to $26.5m of resilience lending.
- **Who buys it:** banks (e.g. Triodos).

## Carta
*Where are a company's physical assets?*

- **Why it matters:** banks lend to companies, not addresses. To assess a company's climate risk, you first need to know where its factories, offices and warehouses are, and companies rarely publish a full list.
- **What it does:** maps the sites and subsidiaries of 18.7m public and private companies, using websites, job boards, registries and maps. Each site is classified (e.g. factory, office) and scored; a person reviews every result; satellite images confirm key sites. The site list then goes into Spectra.
- **How it's delivered:** as a service, "in days, not months", remapped yearly.
- **Example (illustrative):** a bank wants the physical risk of a manufacturing borrower. Carta finds its sites across several countries; Spectra rates each one; the bank sees which sites drive the risk.
- **Who buys it:** banks (corporate borrowers), investment banks, private equity, insurers.
