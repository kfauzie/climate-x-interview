---
name: "pm-data-lens"
description: "Use when a PM analyses a dataset around customer discovery: surfaces judgment calls, product implications and discovery questions, not premature conclusions."
---

# PM data lens

Analyse data the way a product manager needs it: in service of a customer's decision and of what a product must do to support it. The goal is not the most interesting finding. It is knowing what to ask, what to trust, and what any product built on this data has to handle.

## Pick the mode
- **Profile** (default, no notes given): before discovery. Understand the data, surface patterns as questions, no conclusions
- **Test** (notes given): after discovery. Test what the customer said against the data and sharpen the problem
- **Answer** (question given): answer one customer question the way a trustworthy product should

## Rules for every mode
- Find the active run in CLAUDE.md, then read that run's `runs/run-N/RUN.md` for the customer, their decisions, the stakes, data notes and defaults. If unknown, say so rather than assume
- Run isolation: use only the active run's `data/` and `notes/`. Never read, reuse or cite another run's data, notes, notebooks, findings or defaults, even if the dataset looks similar
- Save outputs (notebooks, charts) in the active run's `notebooks/`. Record new data notes and defaults in that run's `RUN.md`, never in a skill or in CLAUDE.md
- Every number is computed in code. Never estimate or round in your head
- Work in a Jupyter notebook, one cell per step, so the reasoning is reviewable
- Mark anything inferred (column meanings, units, intent) as inferred
- Plain language. Explain any metric a non-technical customer would not know
- No solution recommendations (dashboards, agents, tools) unless asked. Product implications are requirements, not solutions

## Speed (live sessions)
- **Use the toolkit first:** `tools/cxlens.py` in the repo. `python3 tools/cxlens.py profile <csv>` gives decode, trust checks, one-at-a-time swings and shape in about a second. In Python: `import sys; sys.path.insert(0,'tools'); import cxlens as cx`, then `cx.load`, `cx.total`, `cx.count`, `cx.swing`, `cx.rise`, `cx.top_driver`, `cx.loss_rate_bp`, `cx.trust`
- **Verdicts come from code:** use the verdict returned by `cx.swing` / `cx.verdict` ("same answer under 2 of 3 scenarios") instead of writing one by hand. Never state that a choice changes the answer without that verdict
- **If `cx.load` raises `ShapeError`,** the file doesn't fit the wide layout: say so, and write the analysis by hand
- **Answer in chat first,** then save the notebook (cells calling the same `cx` functions) and commit once at the end of the step

## Profile mode

1. **Frame**
   - Who uses this data and which decisions it could feed, from the run's `RUN.md` or inputs. One line each

2. **Decode the data**
   - What one row represents, row and entity counts
   - Data dictionary: column groups, meaning, example value. For wide formats, decode the dimensions encoded in column names
   - Flag every ambiguous column with the assumption you made (units, time basis, annual vs cumulative)
   - Note how hard the raw structure is to use: this friction is itself a product insight

3. **Trust checks**
   - Internal consistency: derived fields recompute from their inputs, values respect expected bounds and orderings (e.g. risk should not fall as severity rises), ratings or bands are consistent
   - Quality: nulls, duplicates (including one entity across several rows), inconsistent formats, outliers. Count each precisely by sub-type
   - For each issue: which answers it changes, and by how much

4. **Judgment calls**
   - List every choice an analyst must make that changes the answer: which subset, which value of each dimension, which metric (count vs value vs rate), unit of aggregation, how to treat missing data
   - Isolate one dimension at a time, holding the others fixed, and quantify the swing. Do not mix two dimensions in one comparison
   - These explain why two people answering the same question get different numbers

5. **Shape of the data**
   - Concentration: share held by the top entity, top 1% and top 10. Name any single entity that dominates
   - Segment comparisons on both absolute and normalised basis (e.g. £ and rate per £), and say when they disagree
   - Report as observations, never as "the key risk is" or "you should focus on"

6. **Limits**
   - 3 to 5 questions a customer might reasonably ask that this data cannot answer, and what extra data would

7. **Product implications**
   - For each judgment call, trust issue and limit: what any product built on this data must do. For example: state assumptions in every answer, apply consistent defaults, disclose exclusions, refuse out-of-scope questions, keep an audit trail
   - Stay neutral on which product

8. **Discovery questions**
   - Follow the `discovery-interview` skill: its principles, and its template customised for this run, saved as the run's `discovery-questions.md`
   - 6 to 10 questions, each tied to a finding above
   - Non-leading: ask how the customer handles the issue, never reveal the finding or suggest a solution
   - Favour questions about real recent moments, who uses the numbers, and how they are checked and defended
   - If a template link is given, place each under its matching section and add them under a new heading "Data-informed questions" with "(from: finding)" after each. Edit nothing else. Never write to a master template; ask for a copy if unsure

## Test mode

1. Extract every claim, hypothesis and assumption from the notes, with who said it
2. Test each against the data: supported, not supported or unclear, with the number and one chart
3. What the data shows that the customer did not mention but would care about
4. Contradictions between what they said and what the data shows. Flag these first, they are the best follow-up questions
5. Problem statement: [user] needs to [decision] but currently [workaround], causing [impact]. Success = [measurable outcome]. A narrow version and a broad one
6. Updated product implications
7. Top 3 questions to ask next to close the biggest gaps

## Answer mode

1. Restate the question in data terms, and flag ambiguity
2. State every judgment call you made (subset, dimension values, metric, aggregation, missing data) and why. Use a documented default if the run's `RUN.md` has one
3. Give the answer, with the code and the rows used
4. Sensitivity: how the answer changes under the main alternative choices
5. What part of the question the data cannot answer
6. Likely follow-up questions

## Self-check before presenting
Fail and fix if any of these is true:
- A total or headline number without its assumptions stated
- Duplicates or missing data handled silently
- A conclusion about what matters most, before discovery
- A solution recommendation nobody asked for
- A number not produced by code
- An inferred column meaning presented as fact
- A data quality issue listed without saying which answers it affects
- Two dimensions changed at once in a comparison

## Output
- Start with 5 bullets: what the data is, the biggest judgment calls, trust issues, limits, and what you added or concluded
- Then the sections for the mode, short and scannable
- For live sessions: one sentence per step on the choice made and why, so it can be narrated