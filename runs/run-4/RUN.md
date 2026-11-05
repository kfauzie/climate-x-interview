# Run 4

**Status:** prototype built (`build/mvp.html`; open with `tools/open_run.sh`); next: MVP review (pm-6)
**Synthetic for the prototype (labelled on screen):** EBITDA by site, CX Capital's past assessments, the example insurance policy, premium rules of thumb, other deals (`notebooks/synthetic_inputs.py` → `data/synthetic_inputs.json`)
**Checks:** `node build/test_mvp.js` (known answers), `node build/check_mvp.js` (headless click-through); design images from the build: `node build/capture_screens.js`
**Dataset:** `data/Climate X Sample Data.xlsx` (Spectra v2 export, 22 Meridian Group sites, 4 scenarios × 12 years)
**Context:** `notes/CX_Capital_context.md` (customer brief, an illustrative composite: CX Capital and Meridian are fictional); brand guideline now a skill: `climate-x-brand`
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- Note: the interview recording caught only the interviewer's microphone (headphones), so the transcript holds the interviewer's summaries, not the customer's words
- Discovery questions and interview notes: https://app.notion.com/p/40f8f31ef05f81ca90e3d909dfea71e8
- Solution concept: https://app.notion.com/p/40f8f31ef05f8195aa05dd2a5174a82e (numbers: `notebooks/concept_numbers.py`)

Everything below applies to **run 4 only**. Do not carry it into any other run.

## Customer (given for this run)
- **Organisation:** CX Capital, mid-market private equity, London. £6bn AUM, 3 funds, 24 portfolio companies; equity cheques £40m–£120m; holds of 4–7 years
- **Who we work with:** the central sustainability team (2 people on physical climate risk, 40–60 deals a year), reporting to an MD who sponsors the work but hasn't made it mandatory. No formal role in diligence, no authority over deal teams
- **Relationship with Climate X:** onboarded Q1 2025. Carta for portfolio monitoring; physical risk assessments run on request when a deal enters diligence. **Renewal due Q1 2027**
- **The deal:** Project Meridian. Target Meridian Group, diversified asset-heavy operations. EV £480m, equity £165m, **7-year hold**, 22 sites in 15 countries. **IC in four weeks**
- **How diligence works:** 4–6 weeks from kick-off to IC; IC paper drafted from week 4; 15+ workstreams in parallel, each with an owner and a RAG status; the IC paper has a standing ESG section

## Customer ask (given, word for word)
> The sustainability team has asked more than once whether the output can be made "more useful to the deal side." Unresolved.

*This is a wish, not a problem. Discovery should find what decision the deal team makes with the output, and why it doesn't change any decision today.*

## Account team observations (given)
- Assessments are requested inconsistently and usually late (11 of 60 deals last year)
- A deal exec asked what a letter grade meant in practice; the team couldn't answer from the export
- Hold period is not in what we send; it sits with the deal team
- No deal has been declined on physical climate grounds; findings, when acted on, go into the post-close 100-day plan

## What the context implies (inferred, test in discovery)
- **Two users:** the sustainability team produces the assessment; the deal team (and IC) decides. The deal team is the one to win over
- **The decision is per deal, at IC,** on price, terms or the 100-day plan, not on the portfolio
- **The export speaks in grades and hazard metrics; the deal side speaks in £, EV and the hold period**
- **Why now:** renewal in Q1 2027; usage is low (11 of 60 deals)

## Initial review (pm-1)
Code: `notebooks/initial_review.py`. Unless stated: 2030, middle scenario (SSP2-4.5), £ loss a year. 2030 is the nearest projection year to the middle of the 7-year hold.

**The data** (first five rows; 9 of 104 columns shown. The other 95 are the address, identifiers, building attributes, and the score, depth or intensity, range, reliability and £ loss for each of 11 hazards)
| Site | Country | Type | Year | Scenario | Overall grade | Coastal flood grade | Total £ loss a year | Replacement cost |
|---|---|---|---|---|---|---|---|---|
| Marina Boulevard | Singapore | Office | 2020 | SSP1-2.6 | A | F | £9,785,648 | £1,431,646,352 |
| Farringdon Road | UK | Office | 2020 | SSP1-2.6 | A | A | £23,202 | £13,249,148 |
| Wilton Place | Ireland | Office | 2020 | SSP1-2.6 | A | A | £7,916 | £13,073,271 |
| Devarabisanahalli Road | India | Office | 2020 | SSP1-2.6 | A | – | £8,185 | £1,581,343 |
| Martin Place | Australia | Office | 2020 | SSP1-2.6 | A | A | £2,096 | £109,502,741 |

**In two lines:** 1,056 rows, one per site × scenario × year (22 sites × 4 scenarios × 12 years, 2020 to 2100). Per site: address, type, age, floors, replacement cost (£2.55bn in total); per hazard: grade A–G, severity (e.g. flood depth in metres) with range, reliability and £ loss a year; then total £ loss and loss as % of replacement cost
**Data quality:** usable. Totals add up (hazard losses = total; % = total ÷ replacement cost); no repeated rows. Blank hazard grades carry £0 loss (guess: hazard not modelled there). 14 of 22 sites have age flagged "U" (guess: unknown/estimated). 3 sites have no city. All flood figures assume no flood defences. None of this changes the findings except the last, noted in finding 1

**Findings**
| # | Finding | Why it might matter (guess) |
|---|---|---|
| 1 | **One site carries three-quarters of the risk.** The Singapore office (Marina Boulevard) loses £9.9m a year of the £13.2m total (75%), mostly coastal flood (£9.1m). The top three sites (Singapore, Milan car park, Tokyo retail) are 94%. Flood is modelled undefended | The deal's climate question is one site, not 22. Whether that site is defended changes the answer |
| 2 | **The overall grade hides the £.** Singapore is graded **A** overall (coastal flood F) yet loses £9.9m a year; the Maidstone house is graded **E** and loses £0.26m. The grade follows loss as a share of the building's value (0.7% vs 13.8%). 20 of 22 sites are graded A | A deal team reading grades would see "all fine" and miss the biggest loss |
| 3 | **Over the 7-year hold, the risk is today's risk, not future risk.** Loss a year rises 0.4% from 2025 to 2035, and no site changes grade before 2050 in any scenario. The scenarios only split after 2080 (2100: £14.3m middle vs £25.6m worst case). Over the hold that's about £92m in total (2026–2032), against an EV of £480m | The case is about price and terms now, not long-term scenarios. Long-term views matter for the buyer at exit |
| 4 | **The data has no link to the deal's money.** It has replacement cost (£2.55bn, 5.3× the £480m EV) but no market value, revenue, ownership or lease, or hold period | £ loss can't yet be put next to EV, EBITDA or the business plan without the deal team's figures |

**The questions they become**
1. The data shows one site, the Singapore office, carries 75% of the expected loss. What's behind that?
   - How do you handle a single site like that in diligence today?
2. The data shows that site graded A overall while it loses £9.9m a year. What's behind that?
   - How do you explain a grade to the deal team today?
3. The data shows the expected loss barely changes over a 7-year hold. What's behind that?
   - How do you decide which years and scenarios go into the IC paper today?
4. The data shows £92m of expected loss over the hold, with no value or revenue to compare it to. What's behind that?
   - How do you turn climate findings into something the deal team can price today?

**Clarifications to confirm**
- Which year and scenario they show the deal team, and whether they use the hold period
- Whether Meridian owns or leases the sites (replacement cost is 5.3× EV)
- Whether the Singapore site has flood defences (the figures assume none)
- What a blank hazard grade means: not modelled, or no risk

**Looked at, nothing to ask about:** wildfire and landslide (£0); storms and tropical cyclones (<1% of loss); the four scenarios agree until 2080; asset IDs, coordinates and replacement cost are consistent across rows

**Follow-ups to ask Claude Code**
- Rerun findings 1 and 3 with Singapore defended (excluding coastal flood) to see how much the answer depends on it
- Express each site's loss as a share of an assumed value or EBITDA, once the deal team gives one
- Show what changes at exit (2033) for a buyer looking to 2050 or 2100

## For the solution (pm-3 onwards)
- **The customer is the Head of Sustainability (he).** Solve his biggest problem (guess: his team's work doesn't change deals; 11 of 60 deals, none changed). The deal team is his audience, not our customer
- **One push, simple and elegant:** one click in Spectra gives him a one-page deal-ready summary to send: £ over the hold against EV, the one site that drives it, what to check before IC, a RAG status. Minimal inputs (EV, hold period, prefilled); everything else a stated assumption. Better outcome for him: the deal team asks for it and acts on it (credibility without authority)
- Design around the deal's money: compare loss with **EV (£480m; equity £165m, ~£315m debt)** and add it up over the **hold period (7 years, ~2026–2033)**; show the exit view (risk from 2033 on) separately
- Hold period as an input (prefilled 7 years from 2026, editable), answer updates instantly. For Meridian it mainly scales the total (5y ~£66m, 7y ~£92m, 10y ~£132m, middle scenario: yearly loss is flat before 2050). Inputs that move the answer more: who bears the Singapore loss (owned/leased/insured), flood defences on/off, the exit view. Scenario: default middle, worst case one click away

## Data structure for later steps (structure only, no design decided)
- **Dimensions:** 22 sites × 4 scenarios (SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5) × 12 years (2020, 2025, 2030 … 2050, 2060 … 2100). Hold-period years: 2026–2032 fall between 2025, 2030 and 2035 (interpolate)
- **Per site (fixed):** ID, address, city, country, lat/lon, use, type, age, floors, replacement cost (£), floor area
- **Per site × scenario × year:** overall grade A–G, total £ loss a year, loss % of replacement cost; for each of 11 hazards a grade and (9 of them) a £ loss. Heat and drought have grades but no £ loss. A blank grade = £0 (guess: not modelled)
- **Not in the data, would come from the deal team:** hold period, value or EBITDA per site, ownership/lease, flood defences
- **Ready to use:** `data/sites.json` (made by `notebooks/export_json.py`): `{meta, sites:[{id, city, …, risk:{ssp245:{"2030":{grade, loss, loss_pct, hazards:{"Coastal Flood":{grade, loss}}}}}}]}`
- **Build kit (pre-installed):** `build/vendor/` Leaflet 1.9.4 and Chart.js 4.4.1 (local, works offline); `build/shoot.js <page> <outdir>` screenshots each `[data-screen]` and hides `.no-export`; Playwright and Chromium checked (about 3s a run)
