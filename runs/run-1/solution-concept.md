# Run 1: solution concept (Sarah Okafor)

From the discovery call transcript (Notion, "Run 1: discovery questions (Sarah Okafor) v2") and the run 1 practice data.

## 1. The problem
**What she asked for:** "If we could configure reports in Spectra ourselves, we'd be much quicker. Simple as that."

**The real problem:** Sarah's analysts need to answer ~15 plain-English questions a month from senior people, but today every answer needs judgement calls, a write-up, and Sarah's personal check, which makes each one take 3–4 days and makes her the bottleneck.

**Evidence** (discovery call)
- The slicing isn't the problem: "Not the slicing, that's an hour or so. It's deciding those choices, writing up how the number was produced so it stands up, and then waiting for me to review it."
- She's the bottleneck: "Everything has to come past my desk before it goes out, and there are about 15 of these a month."
- The askers won't use a tool: "They're senior. They ask in plain English by email or in meetings, and they'd never log into Spectra. It'd be my analysts using it."
- Choices aren't consistent: "We have defaults in a methodology paper I own, but every question's a bit different… And no, it's not perfectly consistent. That's partly why I check everything."
- It doesn't end at one answer: "Someone always comes back with, what about commercial property? Or what about the severe scenario? And we start the whole thing again."

**Impact**
- **Analysts:** "around 45 analyst days a month" (her estimate)
- **Sarah:** "a big chunk of mine", reading every line
- **Askers:** "decisions wait on us, so climate risk gets seen as a blocker"
- **The bank:** "a wrong number reaching the board or the PRA" is what worries her most

## 2. Solution ideas
| | A. Report builder (the ask) | B. Answer builder with Sarah's defaults and a write-up | C. Defaults checklist |
|---|---|---|---|
| What it is | Analysts filter and group the Spectra data in Spectra instead of Excel | Analysts build an answer with Sarah's defaults pre-set; the product writes the method, shows the other scenarios up front, and Sarah approves on one screen | Sarah's methodology as a one-page checklist and write-up template |
| How it solves the problem | Saves the hour of slicing | Removes the choosing, the write-up and most of her checking; follow-ups are already answered | Fewer inconsistent choices; still manual |
| User experience | A new tool for analysts; Sarah still checks everything | Analysts paste the question and confirm; Sarah reviews a draft in minutes; askers stay on email | A form to fill in |
| Effort | Medium | Medium | Small |

## 3. The recommended solution
**Recommendation: B.** It goes at the days of judgement, write-up and review, not the hour of slicing. It still gives her the builder she asked for, with her defaults built in. For later: projected balances (run-off), more data sources, PowerPoint.

**Workflow, with Treasury's question from the call** ("how much expected losses rise from 2030 to 2050 under the severe scenario")
- Treasury emails the climate risk team the question.
- The analyst pastes it into the product and picks "Treasury" as the asker.
- The product reads it as: expected loss, severe scenario, 2030 to 2050, all loans. Sarah's defaults fill the rest (exclusions, balances held flat).
- The product calculates: **£1.7m in 2030 → £4.7m in 2050, 2.81×** under severe. Central is shown next to it: 1.58×. Mortgages (2.70×) and CRE (2.88×) are one click away for the follow-up.
- The analyst checks, adds a note, and sends the draft to Sarah.
- Sarah sees what needs her attention first (any change from her defaults), checks the number and the method, and approves.
- The product drafts the reply and file; the analyst sends it to Treasury.

*(Practice data; balances held flat.)*

**What AI, code and people do**
- **AI** reads the plain-English question into choices (scenario, years, loans), each shown and editable
- **Code** calculates every number, writes the method from the choices, and checks them against Sarah's defaults
- **People:** the analyst confirms the choices; Sarah approves before anything goes out

**Success criteria**
- **Target:** "answers going out in a day rather than most of a week"
- **Mustn't get worse:** no wrong number reaches the board or the PRA; every figure traces back ("If I can't trace it, I won't use it")
- **Approvers need to see:** model risk, that "the numbers are computed by code, not made up by a model"; then IT, procurement and the CRO
- **Test cases:** Treasury's rise (2.81× severe, 1.58× central), plus her earlier example questions, with answers calculated by code

**Assumptions**
- Sarah's defaults can be written down well enough for the product to pre-set them
- Seeing the method and the changes from her defaults is enough for her to stop "reading every line"
- Balances held flat and mortgages and CRE combined by default are acceptable for a first version
