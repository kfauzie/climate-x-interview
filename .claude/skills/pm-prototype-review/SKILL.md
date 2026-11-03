---
name: pm-prototype-review
description: "Run a prototype review with the customer and their gatekeepers: what to test, a 15-minute script built on the customer's own example, questions, what to measure, and the per-run review page. Use after a prototype is built, before a demo, or when turning review feedback into the next design round."
---

# Prototype review

Not to sell it. To learn whether it solves the problem for the people who'd use and approve it.

Inputs (active run): `RUN.md`, `solution.md` (riskiest assumption), `design.md`, `notes/`, the prototype or demo. Output: `runs/run-N/prototype-review.md` (outline below), published to Notion.

## What I'm testing, in order
1. Problem fit: does it remove the pain, in their workflow?
2. Trust: would the owner and gatekeepers sign off an answer from it?
3. Adoption: who uses it, how often, what they'd stop doing
4. The riskiest assumption: confirmed, refuted or open

Who's there: decision owner, a day-to-day user, the gatekeeper behind the riskiest assumption. Ask who else; they often name the real blocker.

## 15 minutes
| | Time | |
|---|---|---|
| Recap | 1–2 min | Their words, biggest pain first. "Have I got that right?" |
| Walkthrough | 4–5 min | One of their own examples, end to end |
| Hands on | 3 min | They drive a second example, thinking aloud. I don't help unless stuck |
| Questions | 4–5 min | 5–6 max, fit and trust first |
| Next steps | 1–2 min | What a pilot would need, with whom, on what data |

## Script
- Start from their problem: "Last time you said… so we built something to test one idea"
- One line on what it is and isn't, and what data it runs on (say if synthetic)
- Their example, their terms, their defaults
- Tie each moment to a pain: "this is the check you said takes half a day"
- Show a failure on purpose: a case that went wrong, caught. Builds more trust than a perfect run
- Where AI is and isn't, plainly: "it reads the question; every number is calculated from the file"
- Pause after each key moment

## Questions
- Fit: "If this had existed last time, what would have been different?"
- Trust: "Would you sign off from this screen? What would you need first?" Gatekeeper: "What would you need to approve this?"
- Adoption: "Who'd use it, for what? What would you stop doing?"
- Gaps: "What would stop you using it?" → must-have or nice-to-have?
- Value: "How would you know in three months it was worth it?"
- Next: "What would a pilot need for you to say yes? Who has to agree?"
- Follow-ups: "What makes you say that?", "What did you expect to happen?"

## Measure, not just listen
- Hands-on: done unaided? how long? where they hesitated or misread? what they'd change before sending?
- Later rounds: compare options on completion and speed, not preference

## Rules
- Don't defend. A criticism is data: ask why, write it down
- No jargon ("calculated from the file", not "deterministic"); no promises ("let me take that back")
- Ask for follow-ups and test data (past questions with their answers; no real data until signed)

## `prototype-review.md` outline (per run)
- Who, prototype link, data (real / practice / synthetic), riskiest assumption
- Recap line in their words
- Walkthrough table: step · what I show · what I say · the pain it addresses (one row = a failure caught)
- AI line, hands-on example, 6 questions with hypotheses, pilot shape, "if time" questions
- `## Notes` at the end

## Per run
1. Write `prototype-review.md`; publish a new Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), `Run N: prototype review (<customer>)`; link it in `RUN.md`
2. After: notes → `notes/prototype-review-notes.md`, as is; feedback round → `design.md`; riskiest assumption → `solution.md`; general lessons → this skill or `pm-design`
