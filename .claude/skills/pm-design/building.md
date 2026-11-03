# Building and checking the prototype

What worked in practice. Read with `SKILL.md` (philosophy, process, checklist).

## Build
- **Branch and PR:** build on a branch (`prototype/<name>`) and open a PR with what, why, how it works, data used, tests and what's not built. If `gh pr create` is blocked, open it through the REST API (`gh api repos/<owner>/<repo>/pulls`)
- **Structure:** a deterministic engine (every number, checks, method note, source rows), a separate interpreter (input → structured choices, never a number), a thin API, and a static front end. Reuse `tools/cxlens.py` where the data fits
- **Synthetic supporting data:** if the customer won't share real data yet, generate it with a seeded script inside the run (e.g. `runs/run-N/data/make_<thing>.py`) and label it SYNTHETIC everywhere it appears. Check that defaults don't wipe out most of it
- **Tests come from the design's test set,** plus the flow rules (reasons for departures, comments on failed checks, approvals, fast-tracks, reproducibility). Run them after every change
- **Walk it in a real browser** (Playwright) end to end, then at phone width and in dark mode, and look at screenshots before showing anyone. This catches what API tests miss: misleading verdicts, raw JSON in the UI, wrong plurals, broken back navigation
- **Verdicts and labels come from the numbers** (e.g. "same count, different loans"), never typed by hand
- **A clickable demo for people who can't run it:** build it from the real UI with an in-page mock API that replays precomputed answers, so the demo and the app never drift apart. Say clearly on the page what it can't do
- **Record each feedback round** in the run's `design.md`, and add any general lesson to this skill

## Check before showing anyone
- Run the **design review checklist** in `SKILL.md` §7 against the running prototype, not the mock-up
- Fix what the browser walk-through shows before polishing anything else
- Put the limitations **in the product** (an "about this answer" note or banner), not only in the README
