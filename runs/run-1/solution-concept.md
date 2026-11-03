# Run 1: solution concept (Sarah Okafor)

Made with `pm-3-problem-to-solution-concept` from `RUN.md`, `notes/interview.md`, `notes/sarah-followup.md` and `notebooks/spectra_test.ipynb`. Practice-data numbers use central (`ssp245`, inferred) at 2050.

## 1. Problem
**The ask:** "customized report builder to help her team product custom reports to answer any questions that the team may have". In the call: "I want my analysts configuring reports in Spectra directly rather than wrestling with a spreadsheet of hundreds of columns." That's a solution, and it targets the hour of filtering, not the days around it.

**In her words:** "It all runs through me, so I'm the bottleneck."

**Evidence**
- "The filtering itself took maybe an hour. The rest went on deciding which scenario and horizon to use, whether to include loans in arrears, and then writing up how we got the number" (call; ~3 days end to end)
- "Honestly, it's the checking… things queue up on my desk"; "half a day when it's a big one and I'm doing several a week" (call)
- "Someone always comes back with, what about the severe scenario? And we start again" (call). The scenario changes some answers and not others: CRE flood E+ is 4 loans under central and 8 under severe; the treasury rise is 1.57× vs 2.74× (Test)
- A draft she sent back had three small slips (wrong horizon, stale export, no scenario stated) that "together inflated the count by about a third" (follow-up)
- Her write-ups already follow one shape (scenario, horizon, hazard, population, exclusions, data date, join), and her defaults are written down in a paper she owns (follow-up)

**Statement**
- **Narrow:** Sarah needs each of the ~15 ad-hoc answers a month to be right and defensible before it leaves the team, but each is built by hand in Excel with choices made case by case and written up by hand, then queued for her check, causing 2–5 day turnarounds, follow-ups that restart the clock, and key-person risk
- **Broad:** the bank needs climate numbers that are consistent and defensible across every audience (CRO, committees, pricing, treasury, IR, PRA), but every answer depends on one-off choices checked by one person

**Why now:** none stated by her. Background: PRA SS5/25 lets supervisors ask for evidence from June 2026 and expects justified scenario choices and documented lineage (`climate-x-company`).

**Size** (her estimates)
- Time: "roughly 45 analyst days a month", plus several half-days a week of her review
- Decisions: answers feed the CRO, credit committee, pricing and treasury; each follow-up adds ~2 days. Not quantified: what a late answer held up
- Risk: a wrong scenario or a stale export reaching a committee or the PRA; all checking rests on one person

## 2. Options
| | A. Answer with its method | B. Report builder (the ask) | C. Defaults + write-up template |
|---|---|---|---|
| What it is | Analyst pastes the question; it's read into choices with her defaults applied and gaps flagged; code computes the answer, method note, checks and one-change versions; Sarah reviews failures first | Analysts pick filters and groupings in Spectra instead of Excel | Her defaults and write-up fields as a one-page template and Excel checklist |
| Fixes the top pain? | **Yes:** her check, the follow-ups, the write-up | **Partly:** the hour of filtering only | **Partly:** fewer slips; still manual |
| Value to the customer | Review in minutes; follow-ups answered up front; same defaults every time | Some analyst hours; may lengthen her queue | Fewer send-backs |
| Adoption | Analysts daily, Sarah reviews; askers stay on email | Analysts learn a new tool | Easy, but relies on discipline |
| Gatekeepers (model risk: documented method, reproducible, validated, named owner) | Every number from code, reproducible from the log; method note per answer; Sarah owns the defaults | No method trace | Documents the method; nothing reproducible |
| Revenue (hypothesis) | Retention, more seats; repeatable for any bank on Spectra | Table stakes | None |
| Fit with Climate X | Built on the Spectra export and its ratings; "trust in every number" | Generic BI | Services, not product |
| Effort and risk | Medium. Risk: model risk's bar is higher | Medium. Risk: faster cuts, longer queue | Small. Risk: too small to matter |

## 3. Pick: A, answer with its method
**Why:** it goes at her bottleneck (the check and the follow-ups), and it meets model risk's condition by design: every number is computed and traceable. It still delivers the ask: analysts build answers themselves, within her defaults.

- **One job:** an answer Sarah can approve in minutes. Ends in **approve or send back**, then email text plus Excel
- **Narrowest slice:** one analyst and Sarah; counts, £ totals, shares and rises, filtered by loans, hazard and rating, grouped by hazard or region, for a scenario and year. Refuses loss to the bank (no default or insurance data) with the reason. Steps: Ask → Confirm → Answer → Review
- **Where it could go:** every audience gets numbers from one set of defaults, with a log ready for the PRA
- **Left out:** loss to the bank; real loan data until procurement signs (synthetic loan book instead); PowerPoint export; the quarterly committee pack
- **AI vs person:** AI only reads the question into choices; code computes everything; the analyst confirms the choices and Sarah approves the answer
- **Success:** target, one of her questions asked to approved in a day, her review in minutes; guardrail, every figure reproducible from its log entry and nothing sent unapproved; test cases, her three example questions, the treasury rise, the sent-back draft (must fail 3 checks), "loss to the bank" (refused)
- **Riskiest assumption:** a method note plus source rows per answer is enough for model risk. Test: show the trace for one figure to Sarah and a model risk contact and ask whether it would pass
- **Next step:** prototype on her own examples with Sarah, an analyst and model risk. Ask: "Would you sign off from this screen? What's missing?"
