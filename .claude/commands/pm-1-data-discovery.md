---
name: pm-1-data-discovery
description: Look at a customer's data before and during discovery to find the findings worth putting in front of them, and turn each into an interview question. Two modes: Initial review (before the interview) and Answer (test a claim or answer one question).
---

# Data discovery

The goal is to give the PM questions they couldn't ask without the data. People talk more when they react to their own numbers than to hypotheticals.

Before starting, read climate-x-products, climate-x-company and climate-x-role.

## Ground rules
- Every number is calculated by running code, never estimated by reading the file. Keep the code so each number can be traced.
- Mark anything guessed (meanings, units, intent) as a guess.
- Plain, specific words. Use the customer's own name for their organisation, not a category ("[Company]", not "the company"). Say "mortgage application" or "loan application", never just "application".
- Say "the output", not "the number": there isn't always a number.
- Stay generic: look for patterns, not for a known story.
- Don't over-analyse. Data quality is a sanity check, not the task.

## Initial review (before the interview)
About a minute. Find what to ask, not everything.

1. **Understand the file.** What one row is, how many rows, the key columns (identifiers, descriptors, risk measures), the dimensions packed into column names (hazards, scenarios, years), and anything ambiguous (units, yearly or cumulative, what a blank means). Guess which product it came from and what decisions it likely feeds, marked as a guess.
2. **Look for three kinds of finding:**
   - **What's changed:** recent vs older records, by count and by value.
   - **What's concentrated:** one hazard, area, segment or asset carrying most of it.
   - **What's missing or odd:** gaps, duplicates, stale or unscored records, and what the data can't answer. Treat oddities as clues to past mistakes or workarounds.
   For each, check whether the scenario or year choice changes the picture.
3. **Report 2 to 5 findings.** Only as many as are real; never pad. If nothing is relevant to the customer's need, say so.

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
1. **Findings.** Each a plain-words headline with one number and what it's compared against.
2. **Why it might matter.** One line each, labelled as a guess.
3. **The question it becomes.** It names the problem, never the requested solution or who would use it. One question per line:
   - "The data shows X. Does that match what you see?"
   - "What do you do about it?"
4. **Clarifications to confirm.** Ambiguities such as which scenario or year, units, what a blank means.
5. **Checked, nothing found.** One line.
6. **Follow-ups the PM can ask Claude Code.** Two or three ways to dig further.
7. **The data in two lines,** and whether it's usable in one line.
8. **The first five rows,** as a table. If the file is wide, show the identifiers, the descriptors and one set of risk measures, and say how many columns are left out.
