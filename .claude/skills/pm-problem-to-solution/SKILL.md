---
name: pm-problem-to-solution
description: "Turn discovery notes and data findings into a problem statement and a recommendation on what's worth building: 2–3 options with trade-offs, one pick, the narrowest slice, success criteria and the riskiest assumption. Use after the interview and the data Test, before design."
---

# Problem to solution

Start from the problem, not the feature request. Build the simplest thing that solves it, and only go more complex once that's been tested and falls short.

Inputs (active run only): `RUN.md` (customer, the ask word for word), `notes/interview.md`, the `pm-data-discovery` Test results; the company and product skills for background. Output: `runs/run-N/solution.md`, shown in chat first. Keep it to one screen; it gets narrated live.

## 1. Problem
- The ask, word for word, and why it's a solution rather than a problem
- The problem in one line, in their words if possible ("It all runs through me")
- 3–5 pieces of evidence, each a quote or a number from code, with its source
- Statement: [user] needs to [job] but currently [workaround], causing [impact]. A narrow and a broad version
- Why now: a deadline, review or rule change, with its source. Or "none"
- Size: time and cost, decision value, and risk. Estimates marked as estimates

## 2. Options
Two or three, always including: the ask as stated, the option that hits the root problem, and the smallest useful thing (e.g. fix one report, or agree defaults).

| | A | B | C |
|---|---|---|---|
| Fixes the top pain? | | | |
| Value to the customer | | | |
| Adoption: who uses it, change needed | | | |
| What gatekeepers need, and how it's met | | | |
| Revenue (hypothesis) | | | |
| Fit with the vendor: reuses an existing product or pattern? | | | |
| Effort and risk | | | |

## 3. Pick
- Which, and why in two sentences: tied to the top pain and the gatekeeper's condition
- The one job it does and the action it ends in. Decision-ready beats a better report
- The narrowest slice: who uses it, what it covers and refuses, the steps
- Where it could go, in one line. Think big, ship narrow
- What's left out for now, and why
- Where AI is used and where a person checks
- Success: a target, a guardrail, and test cases with known answers
- The riskiest assumption, and how the prototype will test it
- Next step: who sees the prototype, and what I'll ask them

## Rules
- Evidence or it doesn't go in
- Don't just build the ask, and don't dismiss it: show how the pick still delivers it, or say what it doesn't
- Design for who'll use it, not who asked
- Tag outside facts with their source; check the original when sources disagree
- Minutes, not tens of minutes: reuse the Test and Profile, don't re-analyse
