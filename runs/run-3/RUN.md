# Run 3

**Status:** screens designed (`design/`); MVP built (`build/mvp.html`); next: the MVP review with Marcus
**Dataset:** `data/northwind_renewables_spectra_infra_2026-09.csv` (Spectra Infrastructure Screener export, September 2026)
**Build (MVP):** `build/mvp.html` (open from a local server in `runs/run-3/`); tests `build/test_mvp.js`, quick check `build/check_mvp.js`. Measure costs and loss cuts are a SYNTHETIC placeholder for Adapt, inside the file
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- MVP review questions: https://app.notion.com/p/40f8f31ef05f811fb967f6ee1b77b366
- Solution concept v2 (current): https://app.notion.com/p/40f8f31ef05f818eacecd7712f2c8851
- Solution concept v1: https://app.notion.com/p/40e8f31ef05f81cbadd2e063c7c8018c
- Discovery questions v5 (current): https://app.notion.com/p/40f8f31ef05f811bbce5ee59bee5fad8
- Discovery questions v4: https://app.notion.com/p/40f8f31ef05f8142a954dfb9c56b672d
- Discovery questions v3 (with call notes): https://app.notion.com/p/40e8f31ef05f819485c6de10d3e855be
- Discovery questions v2 (has a meeting notes block): https://app.notion.com/p/40e8f31ef05f81d1b5e8fcb7900a5853
- Discovery questions v1: https://app.notion.com/p/40e8f31ef05f81658eb1c6a31ed1de35

Everything below applies to **run 3 only**. Do not carry it into any other run.

## Customer (given for this run)
- **Name:** Marcus Bell
- **Role:** Head of Asset Management
- **Organisation:** Northwind Renewables, an infrastructure fund owning 62 operating sites: solar farms, onshore wind and battery storage, in the UK and Spain
- **Funding:** partly by two bank debt facilities (A and B)
- **Relationship with Climate X:** customer for about six months (Spectra Infrastructure Screener)

## Customer ask (given, word for word)
> "We need Adapt to give us a resilience plan for every one of our sites."

*This is a solution (an Adapt plan for every site), not a problem. Discovery should find what the plans are for, who acts on them, and what goes wrong today without them.*

## Initial review (pm-1)
**Terms used below.** Rated E–G: the worst three of Spectra's seven risk bands, A (lowest) to G (highest). Central scenario: SSP2-4.5, roughly today's climate policies. Severe scenario: SSP5-8.5, very high emissions. Expected loss: Spectra's average damage a year in £, across all possible events. MW (megawatts): the most power a site can deliver at once. Battery sites: large batteries that store electricity from the grid.

**The data** (first five rows; 11 of 49 columns shown, the other 38 are the other hazards, scenarios and years)
| Site | Country | Region | Type | Capacity (MW) | Commissioned | Value | Location | Debt facility | River flood rating, central 2050 | River flood expected loss a year, central 2050 |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | UK | Teesside | battery | 38.0 | 2021 | £21.4m | footprint | A | E | £216,600 |
| S002 | UK | Scottish Borders | wind | 52.8 | 2023 | £69.0m | footprint | A | B | £64,300 |
| S003 | UK | Scottish Borders | wind | 89.7 | 2020 | £130.2m | footprint | A | B | £124,500 |
| S004 | UK | Essex | battery | 22.9 | 2015 | £13.8m | footprint | B | C | £42,100 |
| S005 | UK | Essex | battery | 39.8 | 2021 | £20.4m | point | B | C | £46,500 |

**In two lines:** 62 sites, one per row (30 solar farms, 19 onshore wind farms, 13 battery sites; 38 in the UK, 24 in Spain; worth £2.93bn, commissioned 2014–2024). For each of 5 hazards (river flood, surface water flood, extreme heat, wildfire, windstorm), a rating and an expected loss under the central and severe scenarios, for 2030 and 2050; plus capacity, value, location type (footprint = scored over the site's outline, point = placed at one spot on the map) and debt facility (A or B).
**Data quality check:** no duplicate sites; 3 sites have no wildfire scores (S001, S010, S032); 16 sites are placed at one point rather than their outline. Neither changes the findings: wildfire is £0.42m of the UK's £14.1m expected loss a year (central, 2050), and point and outline sites have similar expected loss (0.85% and 0.81% of value a year).

**Findings**
| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **8 of 62 sites are rated E–G, all for river flood, under the central scenario in 2050.** 7 of the 8 are UK battery sites (out of Northwind's 12 UK battery sites), in Teesside, Lincolnshire and Humberside. They carry 21% of Northwind's expected loss but are 9% of its value. Battery sites expect to lose 1.50% of their value a year, against 0.77% for solar and 0.66% for wind | The sites that need action may be a handful, not all 62 |
| 2 | **Under the severe scenario in 2050, 24 sites are rated E–G, against 8 under central.** Extreme heat adds 8 Spanish solar farms that aren't rated E–G under central. Expected loss: £46.6m a year under severe, £24.1m under central | Which sites need action depends on which scenario Northwind plans for |

**The questions they become**
1. The data shows 8 of your 62 sites rated E–G for river flooding by 2050 under today's policies, and 7 of them are UK battery sites. What's behind that?
   - How do you handle the flood risk at those 8 sites today?
2. The data shows 24 sites rated E–G by 2050 if emissions stay very high, against 8 under today's policies. How do you decide which scenario to plan for?
   - What would change for you if you planned for very high emissions?

**Clarifications to confirm**
- Which scenario and year does Northwind use for planning, and does either lender (facility A or B) ask for a particular one?
- Which rating counts as "needs action" for Northwind: E–G, or another cut-off?
- For S001, S010 and S032, does a blank wildfire score mean no wildfire risk, or not assessed?

**Looked at, nothing to ask about**
- Sites commissioned 2014–18, 2019–21 and 2022–24 expect similar losses (0.86%, 0.73% and 0.88% of value a year, central 2050).
- Facility A and facility B sites expect similar losses (0.87% and 0.76% of value a year, central 2050).
- Site values are in line with capacity for each site type.

**Follow-ups to ask Claude Code**
- Show the 8 sites rated E–G under the central scenario, with their debt facility and expected loss
- Rerun both findings for 2030
- List all 62 sites from the highest to the lowest expected loss a year as a share of the site's value, to see where a cut-off for action would fall

## Claims from the interview, tested (`notebooks/concept_numbers.py`)
| Claim | Result |
|---|---|
| "It's really those few sites, not all 62" (the 8 rated E–G for river flood) | **Partly.** His own test ("below this range for every hazard under both scenarios") with E–G as the line leaves 24 sites needing a plan in 2050: 8 under central, 16 more under severe (8 Spanish solar, extreme heat) |
| Battery sites are on low land near rivers in Teesside and Humberside | **Supported:** 7 of the 8 sites rated E–G under central are UK battery sites, all in Teesside, Lincolnshire or Humberside |
| Some sites are a single pin, not the outline | **Supported:** 16 sites are scored at a single pin, including 3 of the 8 rated E–G (S014, S017, S038) |
| Teesside battery site flooded | Not testable (no flood history in the data); the 4 Teesside battery sites expect £216,600 to £728,900 a year of river flood loss by 2050 (central) |
