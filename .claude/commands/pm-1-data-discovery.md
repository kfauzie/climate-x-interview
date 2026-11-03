---
name: pm-1-data-discovery
description: "Analyse a customer's dataset as a PM: what it is, what to trust, which choices change the answer, and what a product built on it must handle. Three modes: Profile (before the interview), Test (check what the customer said), Answer (one question, with every assumption stated)."
---

# Data discovery

The goal isn't the most interesting finding. It's knowing what to ask, what to trust, and what any product on this data has to handle.

## Modes
- **Profile** (before the interview): understand the data and turn patterns into questions. No conclusions yet
- **Test** (after the interview): check what the customer said against the data and sharpen the problem
- **Answer** (one question): answer it the way a trustworthy product should

## Ground rules
- Active run only: read its `RUN.md` first. Save the notebook to the run's `notebooks/`, and data notes and defaults to its `RUN.md`
- Every number comes from code, in a notebook, one step per cell
- Read the data provider's own documentation first. If others disagree with it, go with the original and flag it
- Mark anything inferred (meanings, units, intent) as inferred
- Plain language; explain any metric a non-expert wouldn't know
- Requirements, not solutions: no dashboards or agents unless asked
- Live: narrow early and time-box it. Profile is for knowing what to ask, not for exhausting the data

## Toolkit
- `python3 tools/cxlens.py profile <csv>`: decode, trust checks, swings and shape in about a second
- In Python: `import sys; sys.path.insert(0, 'tools'); import cxlens as cx`, then `cx.total`, `cx.count`, `cx.swing`, `cx.rise`, `cx.top_driver`, `cx.loss_rate_bp`, `cx.trust`
- Verdicts such as "same answer under 2 of 3 scenarios" come from `cx.swing`, never written by hand
- If `cx.load` raises `ShapeError`, the file doesn't fit; say so and analyse by hand

## Profile
1. **Frame:** who uses the data, which decisions it feeds, which rules govern them, and anything making it urgent
2. **Decode:** what a row is; counts; what each column means, including dimensions packed into column names; assumptions on anything ambiguous (units, annual or cumulative); any standard being replaced (e.g. a retiring scenario); how hard the raw file is to use, which is itself a product insight
3. **Trust:** do derived fields recompute? do values stay in bounds and in order (risk shouldn't fall as severity rises)? Count nulls, duplicates (including one entity on several rows), bad formats and outliers. For each issue: which answers it changes, and by how much
4. **Judgment calls:** every choice that changes the answer: which subset, which scenario or year, which metric (count, value or rate), counting unit, missing data, whose loss (the asset's or the lender's; direct or indirect). Change one at a time and measure the swing. This is why two people get different numbers from the same file
5. **Shape:** concentration (top entity, top 1%, top 10); segments by total and by rate, and where they disagree. Report observations, not "the key risk is"
6. **Limits:** 3–5 questions the data can't answer, and what data would. Always check the customer's own financial loss and comparison with last period
7. **Product implications:** turn each judgment call, trust issue and limit into a requirement (state assumptions, consistent defaults, disclose exclusions, refuse out-of-scope questions, keep an audit trail), including what the governing rules expect
8. **Questions:** pass the findings to `pm-2-discovery-interview`

## Test
1. List every claim and assumption from the notes, with who said it
2. Test each one: supported, not supported or unclear, with the number
3. What the data shows that they didn't mention
4. Contradictions first: they make the best follow-up questions
5. Problem statement: [user] needs to [decision] but currently [workaround], causing [impact]. Narrow and broad
6. Updated requirements, and the top 3 questions to close the gaps

## Answer
1. The question in data terms, with any ambiguity flagged
2. Every judgment call made and why (use the `RUN.md` defaults)
3. The answer, with the code and rows used
4. How it moves under the main alternatives
5. What the data can't answer, and the likely follow-ups

## Before presenting
- No headline number without its assumptions
- No duplicates or missing data handled silently
- No view on what matters most before the interview
- No data issue without the answers it affects
- Never two things changed in one comparison
- Open with 5 bullets: what the data is, the biggest judgment calls, trust issues, limits, what I concluded. Live: one line per step, so it can be narrated
