# Run 1: clickable prototype

From `solution-detail.md` and `visual-design.md`. Status: **built; PR open**: https://github.com/kfauzie/climate-x-interview/pull/1

## How it's built
Code in `prototype/` (see its README for how to run and test it).
- `engine.py` computes every number, check, method note and source row; `interpret.py` reads the question into choices and never produces a number
- Practice data, plus a synthetic loan book (`data/make_loan_book.py`), labelled as such
- 21 tests from the test set in `solution-detail.md`
- Clickable demo for people who can't run it: `prototype/demo/build_demo.py`, replaying answers precomputed by the engine

## Feedback round 1 (from my review of the demo, 2026-11-01)
1. Ask is free text; examples only pre-fill it. Audience is a list plus "Other"
2. Confirm can add choices the AI didn't pick up (region, property type, origination year, balance band)
3. Back keeps everything
4. Back bottom left, forward bottom right, on every step
5. Modern B2B SaaS look: cleaner layout, clear hierarchy, consistent components
6. Climate X colours and type
7. Look of Climate X's own products

Status: **all 7 implemented**. Also fixed while testing: a follow-up keeps a change Sarah already approved and can still fast-track; a follow-up naming a year uses it for the horizon check; the scenario verdict lists the selected scenarios; "infx" for a zero answer now reads "ranges from 0 to N".

## Check before showing anyone (2026-11-03)
| Check | Result |
|---|---|
| Purpose and next step clear in five seconds | Pass |
| Every screen tied to a pain; ends in an action | Pass |
| One headline, detail on demand | Pass |
| Every number traceable from the screen | **Partial:** loans only in the Excel download |
| Limits stated at the decision | **Partial:** what it won't do isn't in the app |
| Unstated, ambiguous, out of scope flagged, not guessed | Pass |
| Their language, no AI jargon | Pass |
| Back keeps everything; actions in the same place | Pass |
| Errors and empty states say what to do | Pass |
| Belongs in the product | Pass |
| Numbers right | Pass: 21 tests, browser walk-through |

## Open items
- Bring the prototype in line with `visual-design.md`: the loans on screen, "About this answer", as drafted vs with the checks fixed, pre-filled send back (closes both partial checks)
