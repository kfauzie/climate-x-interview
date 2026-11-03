---
name: pm-3-problem-to-solution-concept
description: "Turn discovery notes and data findings into a solution concept in three parts: the problem, the options ending in a recommendation and why, then the recommended solution in detail (workflow with a real example, scope, where AI is used and its sources, gatekeeper conditions, success, riskiest assumption). Use after the interview and the data Test, before design."
---

# Problem to solution concept

Start from the problem, not the feature request. Build the simplest thing that solves it, and only go more complex once that's been tested and falls short.

Inputs (active run only): `RUN.md` (customer, the ask word for word), `notes/interview.md`, the `pm-1-data-discovery` Test results; the company and product skills for background. Output: `runs/run-N/solution-concept.md`, shown in chat first. It gets screen-shared and narrated: three parts, two tables, short bullets.

## 1. Problem
- **The ask**, word for word, and why it's a solution rather than the problem
- **The problem in their words** ("It all runs through me")
- **Evidence:** 3–5 bullets, each a quote or a number from code, with its source in plain words ("discovery call", "her follow-up email", "our analysis of their data")
- **Problem statement:** [user] needs to [job] but currently [workaround], causing [impact]. Then one line on the bigger problem behind it, if there is one
- **Impact on each user:** one bullet per user (time, waiting, rework, risk to the decisions they feed). Estimates marked
- **Why now**, with its source, or "none stated"

## 2. Options, and which I recommend
Two or three: the ask as stated, the option that hits the root problem, and the smallest useful thing. Name each by what it does for whom, not a slogan. Options must differ in what they solve, not in how it's built (AI vs dropdowns is an implementation detail; pick the simpler one inside the option).

One table, options as columns: what it is (one line) · fixes the top pain? · value · adoption · what the gatekeepers need · revenue (hypothesis) · effort and risk.

**Recommendation:** which, and why in 2–3 sentences: the top pain, the gatekeeper's condition, and how it still delivers the ask (or what it doesn't).

## 3. The recommended solution
- **Workflow:** one table from the request to the answer delivered: step | who | what they do | what the product does | the real example. Show who never touches it, who uses it, who approves, and what the product hands back. Use one real request from the notes, with actual numbers from code. Then one line on who signs off the product
- **Scope:** what it covers, what it refuses (with the reason), what's not yet, and where it could go
- **AI and its sources:** what AI does, and nothing else. Anything AI touches shows its source (the words in the request, the default and where it's written, the data rows), one click away. AI never produces a number. Where a person checks
- **Gatekeeper conditions:** one bullet each, how it's met concretely, or "partly" / "not yet" with what's missing
- **Success:** a target, a guardrail, test cases with known answers
- **Riskiest assumption**, and how the prototype tests it
- **Next step:** who sees the prototype, and what I'll ask them

## Rules
- Evidence or it doesn't go in
- Say how, not that: never "met by design" or "seamless"
- Plain words a stranger can follow: no internal labels (mode names, file names, codes)
- Bold only the decision and the key numbers
- Don't just build the ask, and don't dismiss it
- Tag outside facts with their source
- Minutes, not tens of minutes: reuse the Test and Profile, don't re-analyse
