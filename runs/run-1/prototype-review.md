# Run 1: prototype review with Sarah Okafor

Made with the `pm-6-prototype-review` skill from `RUN.md`, `solution-concept.md`, `solution-detail.md`, `visual-design.md` and `notes/sarah-followup.md`. About 15 minutes.

**Who:** Sarah Okafor (Head of Climate Risk, decision owner), one of her analysts (day-to-day user), someone from model risk (gatekeeper; Sarah: "if it involves AI, someone from model risk should hear it early")
**Prototype:** the app on the `prototype/answer-with-method` branch, or the clickable demo (share the link before the session, or screen-share)
**Data, said plainly:** practice portfolio data and a made-up loan book. No real loan data until procurement signs
**Riskiest assumption to test** (from `solution-concept.md`): a step-by-step trace of each figure is enough for model risk to approve. Her model risk criteria: documented method, reproducible numbers, independent validation, a named owner

## 1. Recap the problem (1–2 min)
> "Last time you said it all runs through you, so you're the bottleneck: every answer comes to you to check the scenario and horizon, which loans are in or out, that it reconciles to the book, and that the write-up reads well. And the answers rarely end there: someone always asks about the severe scenario, and you start again. Have I got that right?"

## 2. Walkthrough (4–5 min): the credit committee question
> "We built something to test one idea: your analysts can answer these questions in one sitting, and you can check each one in minutes, because every answer carries its method. It doesn't calculate loss to the bank or produce slides yet. It runs on practice data."

| Step | What I show | What I say (her words) | Pain it addresses |
|---|---|---|---|
| 1 Ask | Paste "How many CRE loans have a flood rating of E or worse by 2050?", asked by Credit committee, audience Committee | "Your analyst pastes the question exactly as it came in. The audience sets your defaults from your methodology paper" | Askers' plain-English questions |
| 2 Confirm | The choices with where each came from; flags: scenario not stated (central used, your committee default), flood definition, the maturity exclusion from your write-up | "These are the choices you check today: scenario, horizon, which loans are in or out. Your analyst confirms them before anything is calculated. Changing your defaults needs a reason, and comes to you" | Deciding scenario, horizon and population (most of the 3 days) |
| 3 Answer | **4 of 235 CRE loans, £7.1m of £580.3m**; severe **8 loans, £17.0m**; 2030 "same count, different loans"; method note; checks; source rows | "This is the write-up your analysts do by hand, in the same fields. And the severe answer is already here, before anyone asks" | The write-up; "what about severe?" |
| 4 Review | Your screen: failed checks and changes to your defaults first, then the answer and the method note; approve | "This is what you'd see. Anything unusual is at the top; if nothing is, you read the note and approve" | Half a day of checking per big answer |
| 5 Follow-up | "What about the severe scenario?" → fast-track: only "Scenario: Central → Severe, 4 → 8 loans" | "When the follow-up comes, only the change comes back to you" | Follow-ups restarting the clock (2 extra days) |
| 6 A draft with slips | Replay a draft with three slips: present-day ratings instead of 2050, a stale export, no scenario stated → three failed checks | "Three small slips can move a number by a third. Each one is caught here before it reaches you" | Key-person risk; a wrong figure reaching the CRO or the PRA |

**Careful with step 6:** present it as a typical draft, not as the one she sent back. Don't say where it came from; her analyst may be in the room.

> Where AI is and isn't used: "The system reads the question and suggests the choices. Your analyst confirms them. Every number is then calculated from the files, the same way each time, and the method note shows exactly how."

## 3. Hands on (3 min): the analyst drives
- Second example: "How much of our 2024 and 2025 lending went into high subsidence areas?" Practice-data answer: **24.3% of 2024–25 lending vs 8.7% of the older book**, with origination taken from the loan system
- Ask them to think aloud. Optional: add a region on the Confirm screen. Note where they hesitate or ask "what does this mean?"

## 4. Questions (4–5 min)
1. **Problem fit (Sarah):** "If this had existed when the CRO's 2050 question came in, what would have happened differently?"
2. **Trust (Sarah):** "Would you sign off an answer from this screen? What would you need to see first?"
3. **Trust (model risk):** "What would you need before approving something like this? What's missing compared with what you'd normally review?" *(tests the riskiest assumption; don't list her four criteria for them)*
4. **Adoption (analyst):** "Of last month's questions, which would you have run through this, and which not?"
5. **Gaps:** "What's missing that would stop you using it?" Then: "Is that a must-have or a nice-to-have?"
6. **Next step:** "What would a pilot need to look like for you to say yes? Who else has to agree?"

*Hypotheses, so I notice surprises:* Sarah likes the review screen but wants the PRA grid (central and severe, 2030 and 2050) on one page and an export in her pack format. Model risk asks about version control, independent validation and who owns the defaults. The analyst asks what happens with questions outside the scope (loss to the bank, arrears).

## 5. Next steps (1–2 min)
- **Pilot shape to propose:** about 4 weeks; two analysts; last quarter's ~15 questions replayed, with the team's own answers as the test set; sample data first, real data once procurement signs; a validation pack for model risk (method, reproducibility, test results, named owner)
- Permission to send short follow-up questions (copying the analysts on anything about data)
- Ask for a few more past questions with the answers the team gave, to add to the test set

## If time allows
- "Would you be comfortable with a quick approval for a follow-up that only changes one thing, like the scenario?" *(confirms the fast-track decision)*
- "Which scenario do you treat as severe today, and does that change as the scenario sets are updated?" *(SSP5-8.5 is being retired; inferred mapping central = SSP245, severe = SSP585)*
- "Who should be able to change the defaults, and how should changes be recorded?"
- "Where does the answer need to end up: an email, an Excel tab, a slide?"

## Notes
