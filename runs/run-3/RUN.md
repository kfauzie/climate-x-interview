# Run 3

**Status:** discovery questions ready; next: the interview
**Dataset:** `data/northwind_renewables_spectra_infra_2026-09.csv` (Spectra Infrastructure Screener export, September 2026)
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- Discovery questions v3 (current): https://app.notion.com/p/40e8f31ef05f819485c6de10d3e855be
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
**Scenarios:** central = SSP2-4.5 (middle of the road, roughly today's policies); severe = SSP5-8.5 (very high emissions). **Years:** 2030 and 2050. **Hazards:** river flood, surface water flood, extreme heat, wildfire, windstorm. **Rating:** A (lowest risk) to G (highest); E–G are the worst three of the seven bands. **Expected loss:** Spectra's average damage per year, in £.

**The data** (first five rows; 11 of 49 columns shown, the other 38 are the other hazards, scenarios and years)
| Site | Country | Region | Type | Capacity (MW) | Commissioned | Value | Location | Debt facility | River flood rating, central 2050 | River flood expected loss a year, central 2050 |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | UK | Teesside | battery | 38.0 | 2021 | £21.4m | footprint | A | E | £216,600 |
| S002 | UK | Scottish Borders | wind | 52.8 | 2023 | £69.0m | footprint | A | B | £64,300 |
| S003 | UK | Scottish Borders | wind | 89.7 | 2020 | £130.2m | footprint | A | B | £124,500 |
| S004 | UK | Essex | battery | 22.9 | 2015 | £13.8m | footprint | B | C | £42,100 |
| S005 | UK | Essex | battery | 39.8 | 2021 | £20.4m | point | B | C | £46,500 |

**In two lines:** 62 sites, one per row: 30 solar farms, 19 onshore wind farms and 13 battery sites (large batteries that store electricity from the grid and release it later); 38 in the UK, 24 in Spain; worth £2.9bn in total, commissioned 2014–2024. Capacity is in MW (megawatts: the most power a site can deliver at once). Each site also has its location type (footprint = scored over the site's outline, point = scored at one spot), its debt facility (A or B), and a rating and expected loss for each hazard, scenario and year.
**Data quality check:** no duplicate sites; 3 sites have no wildfire scores (S001, S010, S032); 16 sites are scored at one spot rather than their outline. Neither changes the findings: wildfire is a small part of the UK risk, and spot and outline sites show a similar level of risk.

**Findings**
| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **A few sites carry the worst ratings.** Under the central scenario in 2050, 8 of 62 sites are rated E–G, all for river flood. 7 of the 8 are UK battery sites (out of 12 UK battery sites), in Teesside, Lincolnshire and Humberside. Together they're 21% of Northwind's expected loss but 9% of its value | The risk that needs action may sit in a handful of sites, not across all 62 |
| 2 | **The scenario changes which sites are rated E–G.** In 2050, 24 sites are rated E–G under the severe scenario, against 8 under central. Extreme heat adds 8 Spanish solar farms that aren't rated E–G under central. Expected loss: £46.6m a year under severe, £24.1m under central | Which sites need attention depends on the scenario Northwind plans for |

**The questions they become**
1. The data shows 8 of your 62 sites rated E–G for river flooding by 2050, and 7 of them are UK battery sites. What's behind that?
   - How do you handle the flood risk at those sites today?
2. The data shows 24 sites rated E–G by 2050 under the severe scenario, against 8 under central. How do you decide which scenario to plan for?
   - What would change for you if it were the severe one?

**Clarifications to confirm**
- Which scenario and year do you use for planning, and do your lenders ask for a particular one?
- Which rating counts as "needs action" for you?
- For the three sites with no wildfire score: does a blank mean no risk, or not assessed?

**Looked at, nothing to ask about**
- Newer and older sites have a similar level of risk.
- Sites in debt facilities A and B have a similar level of risk.
- Site values are in line with their size for each type of site.

**Follow-ups to ask Claude Code**
- Show the 8 sites rated E–G under central, with which debt facility each is in
- Rerun the findings for 2030
- List all 62 sites from highest to lowest expected loss compared with what each site is worth, to see where a sensible cut-off for action would fall
