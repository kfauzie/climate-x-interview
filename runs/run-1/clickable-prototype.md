# Run 1: clickable prototype

From `solution-design.md`. Status: **rebuilt to the agreed three screens; PR open**: https://github.com/kfauzie/climate-x-interview/pull/1

## What it does
**Draft** (analyst) → **Review** (Sarah) → **Send** (analyst)
- **Draft:** paste the question and pick who asked. Scenario, horizon and exclusions start on Sarah's standard for that asker; the answer (e.g. **3 loans · £5.4m**) updates live as the toggles change, with the loans behind it. Warnings (year doesn't match the question, stale data) show here, and need a note to Sarah
- **Review:** Sarah sees the question, the analyst's note, the answer, the loans and what the write-up adds. She can change scenario, horizon or exclusions, then approves or sends back with a comment
- **Send:** the reply and the Excel file are drafted from the approved answer; Send logs who asked, built and approved, and the data dates

## How it's built
Code in `prototype/` (its README says how to run and test it).
- `engine.py` computes every number, check, write-up line and loan row. Default exclusions now include loans maturing before 2030
- `interpret.py` reads the question into the starting options by rules, not AI. It never produces a number
- `app.py`: preview mode (recalculates without asking for reasons, for the live toggles) and a send step
- Practice data plus a synthetic loan book (`data/make_loan_book.py`), labelled as such
- 23 tests, all passing

## Run it
```bash
python3 -m uvicorn prototype.app:app --port 8000
```
Then open http://localhost:8000. Tests: `python3 -m pytest prototype/tests -q`.

## Checks (2026-11-04)
| Check | Result |
|---|---|
| Main flow end to end in a browser | Pass: Draft → Review → Approve → Send → Sent, no page errors |
| Toggles update the answer | Pass: severe 5 loans · £9.6m; 2030 4 loans · £6.2m |
| Edge cases | Pass: "loss to the bank" refused with the reason; total-loss question shows hazards and regions; zero result shows 0 |
| Each fact once; their words | Pass: Horizon, Excludes, write-up; data dates shown once |
| Phone width | Pass |
| Numbers right | Pass: 23 tests |

Fixed during the check: clicking "Send draft to Sarah" while still in the question box lost the click; the write-up box repeated the data dates.

## Feedback rounds
- **Round 1 (2026-11-01, my review of the old demo):** free text, add choices, back keeps state, button placement, B2B look, Climate X colours and type. Carried into the rebuild
- **Round 2 (2026-11-04, solution design):** builder instead of AI reading the question; Build and Answer merged into Draft; checks shown to the analyst; Sarah reviews the answer, not a checklist; one Send button

## Open items
- Rebuild the no-install demo (`prototype/demo/build_demo.py`); the fixed version isn't published yet
- Recompute the CRO, pricing and treasury figures in the test set with the new default exclusions
- Fast-track review for one-change follow-ups is still in the API but not on screen
