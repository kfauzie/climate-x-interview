# Run 1: problem and recommended solution (Sarah Okafor)

Made with the `problem-to-solution` skill from `RUN.md`, `notes/interview.md` and `notebooks/spectra_test.ipynb`. Numbers use run 1 defaults (SSP245, 2050, each property counted once) unless stated.

## 1. Problem
- **The ask:** "a customised report builder to help her team produce custom reports to answer any questions". In the call: "I want my analysts configuring reports in Spectra directly rather than wrestling with a spreadsheet of hundreds of columns." This is a solution; it targets the filtering step
- **The problem, in her words:** "It all runs through me, so I'm the bottleneck."

**Evidence**
- "The filtering itself took maybe an hour. The rest went on deciding which scenario and horizon to use, whether to include loans in arrears, and then writing up how we got the number" (notes, CRE flood example, about 3 days)
- "Every answer comes through me… one subtly wrong scenario choice and the number means something different. So things queue up on my desk"; checking "can take me half a day when it's a big one and I'm doing several a week" (notes)
- "Someone always comes back with, what about the severe scenario? And we start again" (notes); her CRO question took another 2 days of follow-ups
- Five of her example questions use the same few choices (loans, hazard, rating, scenario, year, grouping); 3 of 5 leave the scenario unstated (Test C4)
- Whether a choice matters depends on the question: the treasury rise is 2.74× under SSP585 vs 1.57× under SSP245, but her CRE flood count is 4 under SSP126 and SSP245 and 8 under SSP585 (Test C3)

**Problem statement**
- **Narrow:** Sarah needs each of her team's ~15 ad-hoc answers a month to be correct and defensible before it leaves the team, but today each is built by hand in Excel with choices made case by case and written up by hand, then queued for her check, causing 2–5 day turnarounds, follow-ups that restart the clock, and key-person risk
- **Broad:** the bank needs climate numbers that are consistent and defensible across all its audiences, but every answer depends on one-off analyst choices checked by one person

**Size (her estimates)**
- Efficiency: ~15 requests × 2–5 days = 30–75 analyst days a month (she said "roughly 45"), plus several half-days a week of her review
- Decision value: answers feed the CRO, credit committee, treasury, mortgage pricing and IR; a 2-day follow-up delays each of them. *Not quantified in the call: next time ask what a late answer held up*
- Risk: a wrong scenario choice reaching a senior audience or the PRA; all checking depends on one person

## 2. Options

| Criterion | A. Answer with its method (root problem) | B. Report builder (the ask) | C. Automate the risk committee pack (smallest) |
|---|---|---|---|
| What it is | Analyst types the question; tool shows the choices (defaults filled, unstated ones flagged); code computes the answer, writes the method note and shows one-change versions; Sarah reviews in a checklist view | Analysts pick filters and groupings in Spectra instead of Excel | The one repeating report, generated each quarter |
| Fixes the top pain? | **Yes:** targets her review (#1) and follow-ups (#2), and sets defaults (#3) | **Partly:** removes the ~1 hour of filtering; doesn't touch choosing, writing up or her check | **No:** 1 of ~15 requests a month |
| Customer value | Review time per answer, fewer follow-up rounds, consistent defaults | Some analyst hours | Small, predictable saving |
| Adoption | Analysts use it daily; Sarah reviews. Askers stay on email and Teams (they ask in plain English and won't use a tool) | Analysts; needs them to learn a new interface | None needed |
| Revenue (hypotheses) | Retention of an 18-month customer; expansion to more analysts and audiences; the same question shape applies to any bank on Spectra; differentiates on trust vs Moody's and Jupiter | Table stakes; competitors offer similar | Low |
| Conservative buyer | Every number from code with a full trace, matching "the same way my analysts write it up today"; model risk sees it early; runs on sample data until procurement signs | Same data handling, but no help with model risk's ask for a method trace | Easy to approve |
| Effort and risk | Medium. Risk: model risk's bar for "traceable" is higher than expected | Medium. Risk: faster cuts lengthen her queue | Small. Risk: too small to matter |

## 3. Recommendation: A, answer with its method
**Why:** it targets her stated bottleneck and the follow-up chain, and it meets model risk's condition directly ("computed by code and traceable"). It still delivers the ask: her analysts build the answers themselves.

**Narrowest version**
- **Users:** an analyst asks; Sarah reviews
- **Scope:** a count, a sum or a rise, filtered by loan type, hazard and rating, grouped by hazard or region, for a scenario and year. Covers all five of her examples. Refuses anything else with a plain message (e.g. "loss to the bank" needs LGD and insurance data that isn't in the file)
- **Steps:** (1) Ask in plain English → (2) Confirm the choices (defaults shown, unstated ones flagged) → (3) Answer: number, method note, source rows, one-change versions (other scenarios, year, counting basis) → (4) Review: checklist of what she checks today (scenario and year as asked, loans in and out, reconciles to the book, readable write-up) → approve or send back

**Deterministic vs AI**
- Code computes every number, the method note and the one-change versions (`tools/cxlens.py`)
- AI only turns the plain-English question into the structured choices, which are shown back for the analyst to confirm or edit
- A human checks twice: the analyst confirms the choices, and Sarah approves the answer

**Not yet:** loss to the bank (needs LGD and insurance data), joining the bank's own loan data (arrears, status) until procurement signs, PowerPoint export, free-form questions outside the scope

**Success criteria (proposed, to validate with her)**
- Target: one of her questions goes from asked to approved in one sitting; her review of a standard answer takes minutes, not up to half a day
- Guardrail: every figure traces to source rows, and the method note matches what her analysts would write
- Test set: her five example questions with toolkit-computed answers, plus the questions and outputs she's sending this week

**Riskiest assumption:** a step-by-step trace of each figure is enough for model risk to approve. The prototype tests it by showing Sarah and a model risk contact the trace for one figure and asking whether it would pass.

**Next step with the customer:** a working prototype (not slides) with Sarah, one analyst and someone from model risk, run on her example questions. Ask: "Would you sign off this answer from this screen? What's missing?"
