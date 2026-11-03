# Run 1: solution concept

**In one line:** Sarah is the bottleneck because every answer waits for her check. **Pick: analysts answer questions themselves with her defaults; Sarah approves each one on a single review screen.**

## 1. Problem
**Ask:** "customized report builder" → a solution. It fixes the hour of filtering, not the days around it.
**Problem:** "It all runs through me, so I'm the bottleneck."

| Evidence | Source |
|---|---|
| Filtering ~1 hour; the rest of **~3 days** is choosing scenario and horizon, then writing up | Call |
| Her check: **up to half a day**, several a week | Call |
| "What about severe?" restarts it. CRE flood: **4 loans** central → **8** severe | Call, data |
| Sent-back draft: 3 small slips, count up "by about a third" | Follow-up |

**Size:** ~45 analyst days a month, plus her review (her estimate)
**Why now:** none stated. PRA can ask for evidence from June 2026

## 2. Users
| Role | Who | Uses the tool? |
|---|---|---|
| **Builds answers** | 3 analysts | Daily |
| **Approves** | Sarah | Every answer |
| Asks | CRO, committees, pricing, treasury, IR | No: email in, email + Excel out |
| Signs off the tool | Model risk, IT, procurement, CRO | Once |

## 3. Options
| | **A. Analysts answer; Sarah approves on one screen** | B. Analysts build reports in Spectra (the ask) | C. Defaults + write-up template |
|---|---|---|---|
| Fixes her check? | **Yes** | No | Partly |
| Fixes "what about severe?" | **Yes**, shown up front | No | No |
| Change for analysts | Paste the question | Learn a report builder | Fill in a form |
| Model risk | Method + log per answer | No trace | Method only |
| For Climate X | Retention; repeats for any bank on Spectra | Table stakes | A service, not product |
| Effort | Medium | Medium | Small |
| Main risk | Model risk wants more | Faster reports, longer queue | Too small to matter |

## 4. Pick: A
- **Ends in:** Sarah approves or sends back → email + Excel to the asker
- **Covers:** counts, £ totals, shares, rises · by loans, hazard, rating · scenario and year
- **Refuses:** "loss to the bank" (no default or insurance data), with the reason
- **Still delivers the ask:** analysts build answers themselves
- **Not yet:** real loan data (until procurement signs), PowerPoint, the quarterly pack
- **Later:** one set of defaults behind every audience's numbers

**AI only reads the question. Everything it touches has a source, one click away**
| Choice | Source shown |
|---|---|
| From the question | The words highlighted ("by 2050") |
| A default | Her methodology paper, the paragraph |
| Changed by the analyst | Their reason, flagged to Sarah |
| Any number | Code, never AI. Click → the loan rows |

**Model risk's four conditions**
| Condition | How |
|---|---|
| Documented method | Method note per answer, in her write-up fields |
| Reproducible | Each answer logged (choices, file dates, version); rebuild gives the same number |
| Independent validation | **Partly:** they get the code and a test set to run |
| Named owner | Sarah per answer. **Open:** owner of the tool |

**Success:** asked → approved in a day; her review in minutes. **Guardrail:** nothing sent unapproved.
**Riskiest assumption:** method note + source rows is enough for model risk → show them one figure's trace.
**Next:** prototype with Sarah, an analyst and model risk: "Would you sign off from this screen?"

## 5. Example: "How many CRE loans have a flood rating of E or worse by 2050?"
| Step | Today | With A (practice data) |
|---|---|---|
| Ask | Email; analyst filters Excel, ~1 hour | Analyst pastes it, picks "Credit committee" |
| Choices | Analyst decides scenario, horizon, exclusions; writes up. Most of ~3 days | Shown with sources: 2050 ← "by 2050"; central ← her paper. "Scenario not stated" flagged. Confirm |
| Answer | By hand | **4 of 235 CRE loans, £7.1m of £580.3m** · click → the 4 loans · severe: 8 loans, £17.0m |
| Check | Sarah, up to half a day | 6 of 6 checks pass; Sarah approves in minutes |
| When it goes wrong | A draft used 2030, a stale export and no scenario | Those 3 shown first: drafted 4 of 236, £6.2m vs fixed 4 of 235, £7.1m · "Send back" pre-filled |
