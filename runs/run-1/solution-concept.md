# Run 1: solution concept

**Every answer waits for Sarah's check, so she's the bottleneck. Pick: her analysts draft answers in the product with her defaults, Sarah approves on one screen, and the product drafts the reply.**

## 1. Problem
**Ask:** "customized report builder… to answer any questions". A solution: it fixes the hour of filtering, not the days around it.

**In her words:** "It all runs through me, so I'm the bottleneck."

| Evidence | Source |
|---|---|
| Filtering "maybe an hour"; the rest of **~3 days** is choosing scenario and horizon, then writing up | Discovery call |
| Her check: **up to half a day**, "several a week" | Discovery call |
| "What about the severe scenario? And we start again." | Discovery call |
| The scenario can double the answer: CRE flood is **4 loans** central, **8** severe | Our analysis of her data |
| A draft she sent back: wrong horizon, stale export, no scenario stated | Her follow-up email |

**Problem statement:** Sarah needs each of ~15 answers a month to be right before it leaves the team, but each is built and written up by hand, then queued for her check, so answers take 2–5 days and every follow-up restarts the clock.

**Bigger problem behind it:** every audience should get numbers built the same way, but today each answer rests on one-off choices checked by one person.

**Why now:** none stated. The PRA can ask for evidence from June 2026.

**Impact on each user** (her estimates)

| Who | What it costs them today |
|---|---|
| Analysts | 2–5 days per answer, **~45 days a month**; a follow-up means starting again |
| Sarah | **Up to half a day** per check, several a week; nothing leaves without her |
| Askers (CRO, committees, treasury) | Wait 2–5 days, ~2 more per follow-up; decisions wait with them |
| The bank | A wrong scenario or stale export could reach a committee or the PRA |

## 2. Users and workflow

| Step | Who | What they do | What the product does |
|---|---|---|---|
| 1. Ask | CRO, committees, pricing, treasury, IR | Email or Teams, as today. **Never touch the product** | |
| 2. Draft | **Analyst** | Pastes the question, checks the choices, submits | Reads the question into choices, each with its source · computes the answer, method note, checks and the severe and 2030 versions |
| 3. Review | **Sarah** | Approves, or sends back with a comment | Shows failed checks first · logs her decision |
| 4. Send | Analyst | Sends it | **Drafts the reply email and the Excel file** |

Signs off the product once: model risk, IT, procurement, the CRO.

## 3. Options

| | **A. Analysts draft answers; Sarah approves; it drafts the reply** | B. Analysts build reports in Spectra (the ask) | C. Defaults + write-up template |
|---|---|---|---|
| Who uses, who approves | Analysts; Sarah in the tool | Analysts; Sarah by hand | Analysts; Sarah by hand |
| Fixes her check? | **Yes** | No | Partly |
| Value | Review in minutes; "severe?" answered up front | Analyst hours | Fewer send-backs |
| Change needed | Paste the question | Learn a report builder | Fill in a form |
| Model risk | Method note + log per answer | No trace | Method only |
| Revenue (hypothesis) | Retention, more seats | Table stakes | None |
| Fit with Climate X | Built on the Spectra export and A–G ratings | Generic BI | A service |
| Effort · risk | Medium · model risk wants more | Medium · longer queue | Small · too small |

## 4. Pick: A
**Why:** it removes her check as the bottleneck, and every number is computed and traceable, which is model risk's condition. Still the ask: analysts build answers themselves.

| | |
|---|---|
| Ends in | **Sarah approves** → reply email + Excel drafted for the analyst to send |
| First users | One analyst and Sarah |
| Covers | Counts, £ totals, shares, rises · by loans, hazard, rating · scenario and year |
| Refuses | "Loss to the bank": no default or insurance data. Says why |
| Later | One set of defaults behind every audience's numbers |
| Not yet | Real loan data (until procurement signs) · PowerPoint · the quarterly pack |

**AI only reads the question. Everything it touches has a source, one click away**

| Value | Source shown |
|---|---|
| Choice from the question | The words highlighted ("by 2050") |
| Default | Her methodology paper, the paragraph |
| Analyst's change | Their reason, flagged to Sarah |
| Any number | Code, never AI · click → the loan rows |

**Model risk's conditions**

| Condition | How |
|---|---|
| Documented method | Method note per answer, in her write-up fields |
| Reproducible | Each answer logged (choices, file dates, version); rebuild gives the same number |
| Independent validation | **Partly:** they get the code and a test set to run |
| Named owner | Sarah, per answer · **open:** owner of the tool |

| | |
|---|---|
| Target | Asked → approved **in a day**; her review **in minutes** |
| Guardrail | Nothing sent unapproved; every figure rebuilds the same |
| Test cases | Her 3 examples · treasury rise (2.74× severe) · sent-back draft fails 3 checks · "loss to the bank" refused |
| Riskiest assumption | Method note + source rows is enough for model risk → show them one figure's trace |
| Next | Prototype with Sarah, an analyst, model risk: "Would you sign off from this screen?" |

## 5. Example: "How many CRE loans have a flood rating of E or worse by 2050?"

| Step | Today | With A (practice data) |
|---|---|---|
| Ask | Email; analyst filters Excel, ~1 hour | Analyst pastes it, picks "Credit committee" |
| Choices | Analyst decides scenario, horizon, exclusions; writes up. Most of ~3 days | Shown with sources: 2050 ← "by 2050"; central ← her paper; "scenario not stated" flagged. Confirm |
| Answer | Built by hand | **4 of 235 CRE loans, £7.1m of £580.3m** · click → the 4 loans · severe: 8 loans, £17.0m |
| Slip | A draft used 2030, a stale export, no scenario | Caught: 3 failed checks shown first · drafted 4 of 236, £6.2m vs fixed 4 of 235, £7.1m |
| **Sarah** | Checks by hand, **up to half a day**; analyst writes the email | 6 of 6 checks pass → **approves in minutes** → reply email + Excel drafted |
