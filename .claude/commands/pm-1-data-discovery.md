---
name: pm-1-data-discovery
description: "Look at a customer's data before and during discovery: what it is, whether it's usable, what it can't answer, and which questions it raises for the customer. Two modes: Initial review (before the interview) and Answer (test a claim or answer one question)."
---

# Data discovery

The goal is better questions for the customer, not a full analysis. Every finding should end in something to ask.

Before starting, read climate-x-products, climate-x-company and climate-x-role.

## Ground rules
- Every number is calculated by running code, never estimated by reading the file. Keep the code so each number can be traced.
- Mark anything guessed (meanings, units, intent) as a guess
- Plain language
- Don't over-analyse. Data quality is a sanity check, not the task

## Initial review (before the customer interview)
1 minute max. A quick read to find what to ask, not a full analysis.

1. **Who uses this, and for what?** Using climate-x-products, guess which product it came from and which decisions it likely feeds (e.g. a bank's Spectra export: stress tests, provisions, lending or pricing; Adapt: which resilience work to fund). Mark it as a guess to confirm with the customer.
2. **What's in the file?**
   - What one row is (e.g. one loan, one property, one site) and how many rows
   - The key columns, grouped: identifiers (e.g. loan ID, address), descriptors (e.g. asset type, region, balance), and risk measures (e.g. rating, damage %, £ loss)
   - The dimensions packed into column names: which hazards, scenarios and years
   - Anything ambiguous: units, yearly or cumulative, what a blank means
3. **Is it usable?** A quick sanity check only: missing values, duplicates, anything obviously wrong. Note only issues that would change an answer.
4. **What stands out, and what can't it answer?** Two or three patterns worth asking about (e.g. where the risk is concentrated, a segment that looks different), plus what this data can't tell you (e.g. loss to the bank, change since last quarter).
5. **What should I ask?** Turn each finding from steps 1–4 into a question about the customer's real work. Pass these to pm-2-discovery-interview.
   - From step 1 (likely use) → "When did you last use this for a decision? What happened?"
   - From step 2 (anything ambiguous) → "When someone asks for a number, which scenario and year do you use, and who decided?"
   - From step 3 (usability issues) → "When the data has gaps like this, what do you do?"
   - From step 4, what stands out → "Most of the risk sits in X. Does that match what you see? Does it change anything?"
   - From step 4, what it can't answer → "Do you ever get asked about Y? How do you answer it today?"

## Answer (after the customer interview, or any time)
Test a claim the customer made, or answer one question. One at a time.

1. The claim or question in data terms, with anything ambiguous flagged
2. The choices made and why
3. The result, with the code and rows used. For a claim: supported, not supported or unclear
4. Anything surprising or contradicting what they said, as a follow-up question

## Tools
- `python3 tools/cxlens.py profile <csv>`: quick summary of the file in about a second
- In Python: `import sys; sys.path.insert(0, 'tools'); import cxlens as cx` (cx.total, cx.count, cx.swing, cx.top_driver, cx.trust)
- If cx.load raises ShapeError, the file doesn't fit; analyse by hand

## Output
- Questions for the customer: only those whose answer could change the product. As many as that is, often one to three, sometimes none. A table: the question in plain words | why ask (the finding, with its number) | how the answer would change the product
- The data in two lines: rows and what one row is; the key columns; which hazards, scenarios and years
- Whether it's usable, in one line
