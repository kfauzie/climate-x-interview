# Run 3

**Status:** initial data review done; next: discovery questions (pm-2)
**Dataset:** `data/northwind_renewables_spectra_infra_2026-09.csv` (Spectra Infrastructure Screener export, September 2026)
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- (none yet)

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
"Rated E–G" means in 2050, central scenario (SSP2-4.5) unless stated. Severe = SSP5-8.5. Loss = £ expected loss a year.

**The data** (first five rows; 11 of 49 columns shown, the other 38 are the other hazards, scenarios and years)
| Site | Country | Region | Type | MW | Commissioned | Value | Location | Debt facility | River flood rating | River flood loss a year |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | UK | Teesside | battery | 38.0 | 2021 | £21.4m | footprint | A | E | £216,600 |
| S002 | UK | Scottish Borders | wind | 52.8 | 2023 | £69.0m | footprint | A | B | £64,300 |
| S003 | UK | Scottish Borders | wind | 89.7 | 2020 | £130.2m | footprint | A | B | £124,500 |
| S004 | UK | Essex | battery | 22.9 | 2015 | £13.8m | footprint | B | C | £42,100 |
| S005 | UK | Essex | battery | 39.8 | 2021 | £20.4m | point | B | C | £46,500 |

**In two lines:** 62 rows, one per site (38 UK, 24 Spain; 30 solar, 19 wind, 13 battery; £2.9bn, 3.2 GW, commissioned 2014–2024). Columns: site ID, country, region, type, capacity, year commissioned, value, location type (footprint or point), debt facility (A or B); then rating A–G and £ loss a year for river flood, surface water flood, extreme heat, wildfire and windstorm, under central and severe, for 2030 and 2050
**Usable:** yes. No duplicates; 3 sites have no wildfire scores. Guess: an Infrastructure Screener export, used for asset management and lender reporting

**Findings**
| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **A few sites carry the serious risk.** 8 of 62 sites are rated E–G, all for river flood. 7 of them are UK battery sites (7 of Northwind's 12 in the UK), in Teesside, Lincolnshire and Humberside. Together: 21% of the expected loss, 9% of the value | The risk that needs action may sit in a handful of sites, not across all 62 |
| 2 | **The scenario changes the picture.** Under the severe scenario, 24 sites are rated E–G (32% of the value), against 8 (9%). Extreme heat brings in 8 Spanish solar sites, which have no E–G rating under central. Expected loss: £46.6m a year against £24.1m | Which sites need attention depends on the scenario Northwind plans for |
| 3 | **Some scores are missing.** 3 sites have no wildfire scores: S001 and S010 (Teesside battery) and S032 (Scottish Borders wind). S001 and S010 are also among the 8 rated E–G | A blank could mean "no risk" or "not assessed"; any plan built on it inherits the gap |

**The questions they become**
1. The data shows 8 of your 62 sites are rated E–G, all for river flood, and 7 of them are UK battery sites. Does that match what you see?
   - What do you do about it?
2. The data shows 24 sites rated E–G under the severe scenario, against 8 under central. Does that match what you see?
   - What do you do about it?
3. The data shows three sites with no wildfire scores. Does that match what you see?
   - What do you do about it?

**Clarifications to confirm**
- Which scenario and year Northwind plans for, and whether the lenders ask for a particular one
- Whether E–G is the cut-off they use for "needs action"
- What a blank wildfire score means: no risk, or not assessed
- What "point" means for 16 sites (scored at one location, not the site's outline) and whether that's intended

**Checked, nothing found:** no duplicate sites; values per MW are consistent within each type; newer and older sites have similar loss rates (0.7–0.9% of value); point and footprint sites have similar loss rates; debt facility A holds 6 of the 8 E–G sites (£200m of £266m), but its loss rate is close to facility B's (0.87% against 0.76%)

**Follow-ups to ask Claude Code**
- Split the 8 E–G sites by debt facility and show what each facility's lenders would see
- Rerun each finding for 2030
- Rank all 62 sites by expected loss as a share of value, to see where a cut-off would fall
