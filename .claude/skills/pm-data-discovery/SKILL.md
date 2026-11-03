---
name: pm-data-discovery
description: "Analyse a customer's dataset as a PM: what it is, what to trust, which choices change the answer, and what a product built on it must handle. Three modes: Profile (before discovery), Test (check what the customer said), Answer (one question, answered the way a trustworthy product should)."
---

# Data discovery

Goal isn't the most interesting finding. It's knowing what to ask, what to trust, and what any product on this data has to handle.

## Modes
- **Profile** (no notes yet): understand the data, turn patterns into questions, no conclusions
- **Test** (notes given): check what the customer said against the data, sharpen the problem
- **Answer** (a question given): answer it with every assumption stated

## Ground rules
- Active run only: read `runs/run-N/RUN.md` first; never touch another run. Outputs → the run's `notebooks/`; data notes and defaults → its `RUN.md`
- Every number from code, never estimated. Notebook, one cell per step
- Check the data provider's own docs first (methodology, FAQs, case studies). If third parties disagree, go with the primary source and flag it
- Mark anything inferred (meanings, units, intent) as inferred
- Plain language; explain any metric a non-expert wouldn't know
- Requirements, not solutions. No dashboards or agents unless asked
- Live: narrow early and time-box. Profile is for knowing what to ask, not for exhausting the data

## Toolkit
- `python3 tools/cxlens.py profile <csv>` → decode, trust checks, swings, shape in ~1s
- In Python: `import sys; sys.path.insert(0, 'tools'); import cxlens as cx` → `cx.load`, `cx.total`, `cx.count`, `cx.swing`, `cx.rise`, `cx.top_driver`, `cx.loss_rate_bp`, `cx.trust`
- Verdicts come from `cx.swing` / `cx.verdict`, never written by hand
- `ShapeError` → the file doesn't fit; say so and analyse by hand
- Answer in chat first, then save the notebook, commit once

## Profile
1. **Frame:** who uses the data, which decisions it feeds, which rules govern them, and any why-now (deadline, review, standard being replaced)
2. **Decode:** what a row is; counts; data dictionary (decode dimensions packed into column names); assumptions on ambiguous columns (units, annual vs cumulative); standards in transition (e.g. a scenario being retired); how hard the raw file is to use (itself a product insight)
3. **Trust:** derived fields recompute; values respect bounds and order (risk shouldn't fall as severity rises); nulls, duplicates (incl. one entity on several rows), formats, outliers, each counted. For each issue: which answers it changes, by how much
4. **Judgment calls:** every choice that changes the answer: subset, dimension values, metric (count vs value vs rate), unit of aggregation, missing data, whose loss (asset vs lender; direct vs indirect), old vs new standard. Change one at a time, quantify the swing
   - This is why two people get different numbers from the same file
5. **Shape:** concentration (top entity, top 1%, top 10); segments on £ and on rate, and where they disagree. Observations, never "the key risk is"
6. **Limits:** 3–5 questions the data can't answer and what would. Always check: the customer's own financial loss; comparison with last period
7. **Product implications:** for each judgment call, trust issue and limit → a requirement (state assumptions, consistent defaults, disclose exclusions, refuse out-of-scope, audit trail). Map to what the governing rules expect (granularity, lineage, justified scenarios, reproducibility)
8. **Questions:** hand findings to `pm-discovery-interview`, tagged `(from: finding)`

## Test
1. Every claim and assumption from the notes, with who said it
2. Each tested: supported / not / unclear, with the number
3. What the data shows that they didn't mention
4. Contradictions first: the best follow-up questions
5. Problem statement: [user] needs to [decision] but currently [workaround], causing [impact]. Narrow and broad
6. Updated implications; top 3 questions to close the gaps

## Answer
1. The question in data terms; flag ambiguity
2. Every judgment call made and why (use `RUN.md` defaults)
3. The answer, with the code and rows used
4. How it moves under the main alternatives
5. What the data can't answer; likely follow-ups

## Before presenting
Fix if any is true:
- A headline number without its assumptions
- Duplicates or missing data handled silently
- A view on what matters most, before discovery
- A number not from code, or an inferred meaning stated as fact
- A data issue without the answers it affects
- Two dimensions changed in one comparison

## Output
- 5 bullets first: what the data is, biggest judgment calls, trust issues, limits, what I concluded
- Then the mode's sections, short. Live: one line per step, so it can be narrated
