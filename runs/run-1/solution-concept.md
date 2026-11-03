# Run 1: solution concept

**Every answer waits for Sarah's check, so she's the bottleneck. For her 3 analysts and Sarah: analysts answer questions themselves with her defaults; Sarah approves each on one screen.**

## 1. Problem
**Ask:** "customized report builder… to answer any questions". A solution: it fixes the hour of filtering, not the days around it.

**In her words:** "It all runs through me, so I'm the bottleneck."

| Evidence | Source |
|---|---|
| Filtering "maybe an hour"; rest of **~3 days** is choosing scenario and horizon, then writing up | Call |
| Her check: **up to half a day**, "several a week" | Call |
| "What about the severe scenario? And we start again." CRE flood: **4 loans** central, **8** severe | Call, Test |
| Sent-back draft: wrong horizon, stale export, no scenario stated | Follow-up |

| Statement | |
|---|---|
| Narrow | Sarah needs each of ~15 answers a month right before it leaves the team, but each is built and written up by hand, then queued for her check: 2–5 days, follow-ups restart the clock |
| Broad | The bank needs the same defensible numbers for every audience, but each answer rests on one-off choices checked by one person |

| | |
|---|---|
| Why now | None stated. PRA can ask for evidence from June 2026 (`climate-x-company`) |
| Size | ~45 analyst days a month + her review (her estimate) · each follow-up ~2 days · risk: a wrong scenario reaching a committee or the PRA |

## 2. Users
| Role | Who | Uses it? |
|---|---|---|
| **Builds answers** | 3 analysts | Daily |
| **Approves** | Sarah | Every answer |
| Asks | CRO, committees, pricing, treasury, IR | No: email in, email + Excel out |
| Signs off the tool | Model risk, IT, procurement, CRO | Once |

## 3. Options
| | **A. Analysts answer; Sarah approves on one screen** | B. Analysts build reports in Spectra (the ask) | C. Defaults + write-up template |
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
| Ends in | **Sarah approves or sends back** → email + Excel to the asker |
| First users | One analyst and Sarah |
| Covers | Counts, £ totals, shares, rises · by loans, hazard, rating · scenario and year |
| Refuses | "Loss to the bank": no default or insurance data. Says why |
| Steps | Ask → Confirm → Answer → Review |
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
| **Sarah** | Checks by hand, **up to half a day** | 6 of 6 checks pass → **approves in minutes** |
