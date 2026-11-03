---
name: pm-3-problem-to-solution-concept
description: "Turn discovery notes and data findings into a solution concept: a problem statement and the users, a recommendation on what's worth building: 2–3 options with trade-offs, one pick, a worked example from a real request, the narrowest slice, success criteria and the riskiest assumption. Use after the interview and the data Test, before design."
---

# Problem to solution concept

Start from the problem, not the feature request. Build the simplest thing that solves it, and only go more complex once that's been tested and falls short.

Inputs (active run only): `RUN.md` (customer, the ask word for word), `notes/interview.md`, the `pm-1-data-discovery` Test results; the company and product skills for background. Output: `runs/run-N/solution-concept.md`, shown in chat first. It gets screen-shared and narrated, so it's written to be followed at a glance (see Presenting it).

## 1. Problem
- The ask, word for word, and why it's a solution rather than a problem
- The problem in one line, in their words if possible ("It all runs through me")
- 3–5 pieces of evidence, each a quote or a number from code, with its source
- Statement: [user] needs to [job] but currently [workaround], causing [impact]. A narrow and a broad version
- Why now: a deadline, review or rule change, with its source. Or "none"
- Size: time and cost, decision value, and risk. Estimates marked as estimates

## 2. Users
Name them before any option: who uses it day to day, who approves the output, who asks but never touches it, and who has to sign it off. Design for the first two.

## 3. Options
Two or three, always including: the ask as stated, the option that hits the root problem, and the smallest useful thing (e.g. fix one report, or agree defaults).

Name each option by what it does for whom ("Analysts answer it themselves; the manager approves on one screen"), not a slogan.

| | A | B | C |
|---|---|---|---|
| Who uses it, who approves | | | |
| Fixes the top pain? | | | |
| Value to the customer | | | |
| Adoption: change needed | | | |
| Each gatekeeper condition | | | |
| Revenue (hypothesis) | | | |
| Fit with the vendor: reuses an existing product or pattern? | | | |
| Effort and risk | | | |

## 4. Pick
- Which, and why in two sentences: tied to the top pain and the gatekeeper's condition
- The one job it does and the action it ends in. Decision-ready beats a better report
- The narrowest slice: which of the users first, what it covers and refuses, the steps
- Where it could go, in one line. Think big, ship narrow
- What's left out for now, and why
- Where AI is used and where a person checks. Anything AI touches shows its source (the words in the request, the default and where it's written down, the data rows), confirmable in one click. AI never produces a number
- Gatekeeper conditions, one row each: how it's met, concretely, or "partly" / "not yet" with what's missing
- Success: a target, a guardrail, and test cases with known answers
- The riskiest assumption, and how the prototype will test it
- Next step: who sees the prototype, and what I'll ask them

## 5. Worked example
One real request from the notes, as a table: step | today (who, how long, what went wrong) | with the pick (who, what they see and click, the actual numbers from code). Last row: what the approver does and how long it took.

## Presenting it
- Open with one line: the problem, who it's for, the pick
- Tables over paragraphs; a few words per cell; one point per line
- Quotes cut to the words that carry them
- Bold only the decision and the key numbers
- Anything that doesn't change the decision goes

## Rules
- Evidence or it doesn't go in
- Say how, not that: never "met by design" or "seamless". Show the mechanism
- Don't just build the ask, and don't dismiss it: show how the pick still delivers it, or say what it doesn't
- Tag outside facts with their source; check the original when sources disagree
- Minutes, not tens of minutes: reuse the Test and Profile, don't re-analyse
