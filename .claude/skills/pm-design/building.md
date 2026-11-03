# Building and checking the prototype

## Build
- Branch `prototype/<name>` → PR with what, why, how, data, tests, not built. If `gh pr create` is blocked: `gh api repos/<owner>/<repo>/pulls`
- Structure: deterministic engine (numbers, checks, method note, rows) + interpreter (input → choices, never a number) + thin API + static front end. Reuse `tools/cxlens.py` where it fits
- No real data yet → seeded script in the run (`runs/run-N/data/make_<thing>.py`), labelled SYNTHETIC everywhere. Check defaults don't exclude most of it
- Tests = the design's test set + flow rules (reasons, comments, approvals, fast-tracks, same input → same number). Run after every change
- Labels and verdicts from the numbers, never typed by hand
- Clickable demo for people who can't run it: the real UI + an in-page mock that replays precomputed answers, so they never drift apart. Say on the page what it can't do

## Check
- Walk it in a real browser (Playwright): end to end, phone width, dark mode, then look at the screenshots. Catches what API tests miss: misleading verdicts, raw JSON, wrong plurals, back that loses work
- Run the checklist in `SKILL.md` on the running prototype
- Limits in the product (an "about this answer" note), not only the README
- Log feedback in the run's `design.md`; general lessons back into the skill
