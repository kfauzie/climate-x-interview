---
name: pm-1-data-discovery
description: Look at a customer's data before and during discovery to find two or three findings worth putting in front of them, and turn each into an interview question. Two modes: Initial review (before the interview) and Answer (test a claim or answer one question).
---

# Data discovery

The goal is better questions for the customer, not a full analysis. The data's job is to give questions that couldn't be asked without it. People talk more when they react to their own numbers than to hypotheticals.

Before starting, read climate-x-products, climate-x-company and climate-x-role.

## Ground rules
- Every number is calculated by running code, never estimated by reading the file. Keep the code so each number can be traced.
- Mark anything guessed (meanings, units, intent) as a guess.
- Plain language. No jargon.
- Don't over-analyse. Data quality is a sanity check, not the task.
- Stay generic: look for patterns, not for any specific story.

## Initial review (before the interview)
About a minute. Find what to ask, not everything.

1. **Understand the file.** What one row is, how many rows, the key columns (identifiers, descriptors, risk measures), the dimensions packed into column names (hazards, scenarios, years), and anything ambiguous (units, yearly or cumulative, what a blank means). Guess which product it came from and what decisions it likely feeds, marked as a guess.
2. **Look for three kinds of finding:**
   - **What's changed:** recent vs older records, this period vs last, by count and by value.
   - **What's concentrated:** one hazard, area, segment or asset carrying most of the risk or value.
   - **What's missing or odd:** gaps, duplicates, stale or unscored records, and what the data can't answer. Treat each oddity as a clue to a past mistake or a manual workaround.
   For each, check whether the scenario or year choice changes the picture materially.
3. **Pick the two or three findings most likely to matter to the customer.** Prefer findings that are large, surprising, or that the customer could act on, and that test the ask: findings the ask would fix, and findings it wouldn't reach.

## Answer (after the interview, or any time)
Test a claim the customer made, or answer one question. One at a time.
1. The claim or question in data terms, with anything ambiguous flagged
2. The choices made and why (e.g. scenario, year, by count or by value)
3. The result, with the code and rows used. For a claim: supported, not supported or unclear
4. Anything surprising or contradicting what they said, as a follow-up question

## Tools
- `python3 tools/cxlens.py profile <csv>`: quick summary of the file
- In Python: `import sys; sys.path.insert(0, 'tools'); import cxlens as cx` (cx.total, cx.count, cx.swing, cx.top_driver, cx.trust)
- If cx.load raises ShapeError, the file doesn't fit; analyse by hand

## Output (one page, for the PM to react to)
1. **Findings (three at most).** Each as a headline in plain words with one number and what it's compared against. E.g. "Recent records are riskier: 17% rated E–G, against 12% before."
2. **Why it might matter.** One line per finding, labelled as a guess.
3. **The question it becomes.** One per finding, tied to what the customer asked for, so the answer tells you whether the ask solves what the data shows. In the form: "The data shows X. Does that match what you see? How would [the ask] have changed that?" Keep it open: no hint of the answer you expect.
4. **Checked, nothing found.** One line, so gaps aren't mistaken for things skipped.
5. **Follow-ups to ask me.** Two or three ways to dig further (e.g. split by area, rerun under the severe scenario, compare by value instead of count).
6. **The data in two lines.** Rows and what one row is; key columns; hazards, scenarios and years. Then whether it's usable, in one line.
