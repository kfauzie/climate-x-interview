---
name: pm-problem-to-solution
description: "Turn discovery notes and data findings into a problem statement and a recommendation on what's worth building: 2–3 options with evidence-based trade-offs, one pick, the narrowest slice, success criteria and the riskiest assumption. Use after the interview and the data Test, before design."
---

# Problem to solution

Start from the problem, not the feature request. Simplest thing that solves it; only go more complex once the simple version is tested and falls short.

Inputs (active run only): `RUN.md` (customer, the ask word for word), `notes/interview.md`, the `pm-data-discovery` Test results. Background: the company and product skills. Output: `runs/run-N/solution.md`, in chat first. One screen; it gets narrated live.

## 1. Problem
- **The ask**, word for word, and why it's a solution, not a problem
- **The problem** in one line, their words if possible ("It all runs through me")
- **Evidence:** 3–5 bullets, each a quote or a number from code, with its source
- **Statement:** [user] needs to [job] but currently [workaround], causing [impact]. Narrow and broad
- **Why now:** deadline, review or rule change, sourced. Or "none"
- **Size:** efficiency + decision value + risk. Estimates marked as estimates

## 2. Options (2–3)
Always: the ask as stated, the option that hits the root problem, the smallest useful thing (e.g. fix one report, agree defaults).

| | Option A | Option B | Option C |
|---|---|---|---|
| Fixes the top pain? | yes / partly / no + evidence | | |
| Customer value | efficiency, decisions, risk | | |
| Adoption | who uses it, fit with their tools, change needed | | |
| Revenue (hypothesis) | retention, expansion, reuse across customers, new revenue for the customer | | |
| Gatekeepers | what model risk / IT / procurement / regulator need, and how it's met | | |
| Fit with the vendor | positioning, stated next steps, an existing pattern to reuse | | |
| Effort and risk | build size, what could make it fail | | |

## 3. Pick
- **Which and why:** two sentences, tied to the top pain and the gatekeeper's condition
- **One job it does**, and the action it ends in (approve, send, change a decision) with its consequence. Decision-ready beats a better report
- **Narrowest slice:** who uses it, what it covers and refuses, the steps
- **Where it could go:** one line. Think big, ship narrow
- **Not yet:** what's left out, and why
- **AI vs code:** code computes every number; AI only interprets; where a human checks
- **Success:** a target (their words or a number to validate), a guardrail, a test set with known answers
- **Riskiest assumption**, and how the prototype tests it
- **Next step:** who sees the prototype, and what I ask them

## Rules
- Evidence or it doesn't go in: quotes from the notes, numbers from code
- Don't just build the ask, and don't dismiss it. Show how the pick still delivers it, or say what it doesn't
- Design for who uses it, not who asks
- Reuse before inventing: check the vendor's existing products and patterns
- External facts tagged by source; check the primary source when they conflict
- Minutes, not tens of minutes: reuse Test and Profile, don't re-analyse
