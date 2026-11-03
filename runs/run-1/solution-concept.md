# Run 1: problem and recommended solution (Sarah Okafor)

From the discovery call, Sarah's follow-up email and our analysis of her (practice) data. Numbers use central scenario, 2050, unless stated.

## 1. Problem
- **The ask:** "customized report builder to help her team product custom reports to answer any questions that the team may have". In the call: "I want my analysts configuring reports in Spectra directly rather than wrestling with a spreadsheet of hundreds of columns." This is a solution, and it targets the hour of filtering, not the days around it
- **The problem, in her words:** "It all runs through me, so I'm the bottleneck."

**Evidence**
- "The filtering itself took maybe an hour. The rest went on deciding which scenario and horizon to use, whether to include loans in arrears, and then writing up how we got the number" (discovery call; about 3 days end to end)
- "Every answer comes through me… one subtly wrong scenario choice and the number means something different"; checking "can take me half a day when it's a big one and I'm doing several a week" (discovery call)
- "Someone always comes back with, what about the severe scenario? And we start again" (discovery call); her CRO question took another 2 days
- The scenario matters for some questions and not others: CRE flood E or worse is **4 loans** central and **8** severe; the treasury rise is 1.57× central and 2.74× severe (our analysis of her data)
- A draft she sent back had a wrong horizon, a stale export and no scenario stated (her follow-up email)

**Problem statement:** Sarah needs each of her team's ~15 answers a month to be right and defensible before it leaves the team, but each is built by hand in Excel, with choices made case by case and written up by hand, then queued for her check. Answers take 2–5 days, follow-ups restart the clock, and everything depends on her.

Behind it: every audience (CRO, committees, pricing, treasury, IR, the PRA) should get numbers built the same way, but today each rests on one-off choices.

**Impact on each user** (her estimates)
- **Analysts:** 2–5 days per answer, roughly **45 days a month**; a follow-up means starting again
- **Sarah:** up to **half a day** per check, several a week; nothing leaves without her
- **Askers:** wait 2–5 days, about 2 more per follow-up; their decisions wait too
- **The bank:** a wrong scenario or stale export could reach a committee or the PRA

**Why now:** none stated. The PRA can ask banks for evidence from June 2026.

## 2. Options, and which I recommend
| | A. Analysts draft answers in the product; Sarah approves on one screen | B. Analysts build their own reports in Spectra (the ask) | C. The quarterly risk committee pack, automated |
|---|---|---|---|
| What it is | Analyst pastes the question; the product shows the choices with her defaults and flags gaps; code computes the answer, method note and severe and 2030 versions; Sarah approves; the product drafts the reply | Analysts pick filters and groupings in Spectra instead of Excel | The one repeating report, generated each quarter |
| Fixes the top pain? | **Yes:** her check, the follow-ups and the write-up | Partly: the hour of filtering; not the choosing, write-up or her check | No: 1 of ~15 requests a month |
| Value | Her review in minutes; follow-ups answered up front; same defaults every time | Some analyst hours | A small, predictable saving |
| Adoption | Analysts daily; Sarah approves; askers stay on email | Analysts learn a new interface | None needed |
| What model risk needs | Every number from code, with a method note and a log per answer | No method trace | Easy to approve |
| Revenue (hypothesis) | Keeps an 18-month customer; more seats and audiences; repeatable for any bank on Spectra | Table stakes | Low |
| Effort and risk | Medium. Risk: model risk's bar is higher than we think | Medium. Risk: faster reports, longer queue on her desk | Small. Risk: too small to matter |

**Recommendation: A.** It goes at what she called the bottleneck, her check and the follow-ups that restart it, and every number is computed by code and traceable, which is model risk's condition. It still delivers the ask: her analysts build the answers themselves, within her defaults.

## 3. The recommended solution
**Workflow**, with her credit committee question: "How many CRE loans have a flood rating of E or worse by 2050?"

| Step | Who | What they do | What the product does | In the example (practice data) |
|---|---|---|---|---|
| 1. Ask | CRO, committees, pricing, treasury, IR | Email or Teams, as today. Never touch the product | | Credit committee emails the question |
| 2. Draft | **Analyst** | Pastes the question, checks the choices, submits | Reads the question into choices, each with its source; computes the answer, method note, checks and the other versions | 2050 ← "by 2050"; central ← her paper; "scenario not stated" flagged. **4 of 235 CRE loans, £7.1m of £580.3m**; severe 8 loans, £17.0m |
| 3. Review | **Sarah** | Approves, or sends back with a comment | Shows failed checks first; logs her decision | 6 of 6 checks pass; approves in minutes. The slipped draft would show its 3 failed checks first |
| 4. Send | Analyst | Sends it | **Drafts the reply email and the Excel file** | Email text plus the 4 loans |

Model risk, IT, procurement and the CRO sign off the product once.

**Scope**
- Covers: counts, £ totals, shares and rises, by loans, hazard and rating, for a scenario and year. All of her example questions
- Refuses, with the reason: "loss to the bank" (needs default and insurance data that isn't loaded)
- Not yet: real loan data until procurement signs (a synthetic loan book stands in), PowerPoint, the quarterly pack
- Could go: one set of defaults behind every audience's numbers

**AI and its sources**
- AI only reads the question into choices. Each shows its source, one click away: the words in the question, the default and the paragraph of her methodology paper, or the analyst's change and reason
- AI never produces a number. Code computes every number, the method note and the other versions; clicking a number shows the loan rows behind it
- A person checks twice: the analyst confirms the choices, Sarah approves the answer

**Model risk's conditions** (her follow-up email)
- Documented method: a method note per answer, in her write-up fields
- Reproducible: each answer logged with its choices, file dates and version; rebuilding it gives the same number
- Independent validation: **partly**. They get the code and a test set to run; the validation is theirs
- Named owner: Sarah, for each answer. **Not yet:** who owns the product itself

**Success** (to validate with her)
- Target: a question goes from asked to approved in a day; her review takes minutes, not half a day
- Guardrail: nothing is sent unapproved; every figure rebuilds the same
- Test cases: her three example questions, the treasury rise, the sent-back draft (must fail 3 checks), "loss to the bank" (refused)

**Riskiest assumption:** a method note and the source rows are enough for model risk. The prototype tests it by showing Sarah and a model risk contact the trace for one figure.

**Next step:** a working prototype on her own examples with Sarah, an analyst and someone from model risk. Ask: "Would you sign off this answer from this screen? What's missing?"
