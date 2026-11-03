---
name: pm-problem-to-solution
description: "Turns a run's interview notes and data analysis into a summarised problem and a recommended solution: problem statement, 2–3 options with evidence-based trade-offs (customer value, adoption, revenue, how a conservative buyer gets comfortable), one pick, its narrowest version, success criteria and the riskiest assumption. Use after discovery and the pm-data-discovery Test, before design or prototyping, or when asked what to build and why."
---

# Problem to solution

Inputs, all from the **active run only** (see CLAUDE.md run rules):
- `runs/run-N/RUN.md`: customer profile, the ask (word for word), defaults, Profile findings
- `runs/run-N/notes/interview.md`: summary and transcript
- The pm-data-discovery **Test** results (claims tested, contradictions, problem statement). If Test hasn't been run, run it first

Background, general knowledge only: the company, product and role skills for this engagement (here `climate-x-company`, `climate-x-products`, `climate-x-role`): the vendor's positioning, existing products and patterns, stated next steps, the regulation its customers face, and competitors.

Output: show it in chat first, then save to `runs/run-N/solution.md` and commit once. Keep it to one screen where possible; it gets narrated live.

## Steps

### 1. Problem (from evidence, not the ask)
- **The ask**, word for word, and why it's a solution, not a problem
- **The problem** in one line, in the customer's words where possible ("It all runs through me")
- **Evidence:** 3–5 bullets, each a quote from the notes or a number from the data (with its source: notes, Test claim ID or Profile finding). No unsourced claims
- **Problem statement:** [user] needs to [job] but currently [workaround], causing [impact]. Narrow and broad versions. Reuse Test's statement if it still holds
- **Why now:** any deadline, supervisory review or standard change that makes this urgent, with its source. If none, say so
- **Size (ROI, three parts):** efficiency (time, people, consultants), decision value (what a slow or wrong answer held up or changed), risk and reputation. Mark estimates as estimates

### 2. Options (2–3)
Always include:
- **The ask as stated**, evaluated honestly
- **The option that targets the root problem**
- **The smallest useful thing** (e.g. fix one repeating report, or agree defaults)

For each: one-line description, which pain it fixes (by rank from the notes), and a row in this table:

| Criterion | What to write |
|---|---|
| Fixes the top pain? | Yes / partly / no, with the evidence |
| Customer value | Against the three ROI parts |
| Adoption | Who uses it day to day (asker vs user), fit with their tools and workflow (e.g. Excel, PowerPoint), behaviour change needed |
| Revenue for the vendor | Retention or renewal, expansion (more users, teams, products), reuse across similar customers, differentiation from competitors. Also any **new revenue for the customer** (e.g. a product they can sell or finance). Mark as hypotheses |
| Fit with the vendor's direction | Matches its public positioning and stated next steps (e.g. from case studies); **reuses an existing product or pattern** rather than inventing one; helps customers with the why-now rules |
| Conservative buyer | What their gatekeepers (model risk, IT, procurement, audit, regulator) need, and how this option meets it: code-computed numbers, audit trail, staged rollout, no real data until signed |
| Effort and risk | Rough build size; what could make it fail |

### 3. Recommendation
- **Pick one** and say why in two sentences, tied to the top pain and the gatekeeper's condition
- **Narrowest version:** who uses it, the scope (which questions or cases it covers, which it refuses), and the steps or screens in order
- **Where it could go:** one line on the bigger version this slice leads to (think big, ship narrow)
- **The action it ends in:** the decision the user takes at the end, and its financial or operational consequence. Decision-ready, not a better report
- **Deterministic vs AI:** what code computes (every number), what AI does (e.g. interpret a plain-English question into structured choices, shown back for confirmation) and where a human checks
- **What we won't build yet,** and why
- **Success criteria:** a target (from the customer's words or a proposed number to validate), a guardrail (what must stay true for them to trust it) and a test set (real or sample cases with known answers)
- **Riskiest assumption** and how the prototype tests it
- **Next step with the customer:** who sees the prototype, and what you ask them

## Rules
- **Evidence or it doesn't go in.** Every claim about the customer cites the notes; every number comes from the Test or Profile (computed by code, e.g. `tools/cxlens.py`), never estimated by hand
- **Don't just build the ask, and don't dismiss it.** Show how the pick still delivers what they asked for, or say plainly what it doesn't deliver and why
- **Who asks vs who uses.** Design for the person who would use it day to day, and say who that is
- **Speak the customer's language** in anything they'll see. No model, LLM or eval jargon
- **Stay solution-neutral until step 2.** The problem section must stand on its own
- **Reuse before inventing.** Check the vendor's own products and published patterns first; an option that extends an existing pattern is easier to sell and build
- **Source external facts.** Tag them ([site] the vendor's own pages, [web] third parties); when sources conflict, check the primary source and say which you used
- **Time:** this should take minutes, not tens of minutes. Use the existing Test and Profile outputs; don't re-analyse unless a claim needs a number that's missing
