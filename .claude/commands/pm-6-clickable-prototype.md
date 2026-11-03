---
name: pm-6-clickable-prototype
description: "Turn the agreed solution detail and visual design into a working clickable prototype on a branch: engine separate from the AI interpreter, synthetic data, tests from the test set, a check in a real browser, a PR and a no-install demo. Use when building or changing the prototype."
---

# Clickable prototype

Input: `solution-detail.md` (screens, checks, test set) and `visual-design.md` (agreed images). Output: `runs/run-N/clickable-prototype.md` and a PR.

- **Build** on a branch:
  - The engine (numbers, checks, method, rows) separate from the interpreter (input → choices, never a number)
  - No real data yet: a seeded synthetic file in the run, labelled as synthetic
  - Tests from the test set; run them after every change
  - Labels and verdicts generated from the numbers, never typed by hand
- **Check before showing anyone:** walk it end to end in a real browser and look at the screenshots. Then ask:
  - Can a first-time user tell in five seconds what the screen is for and what to do next?
  - Do the principles in `pm-4-solution-detail` and the look in `pm-5-visual-design` hold on the real screens?
  - Are the numbers right, and are the limits stated?
- **PR** with screenshots, how to run it and the test results
- For people who can't run it: a clickable demo built from the real UI that replays precomputed answers, with a note on what it can't do
- `clickable-prototype.md`: how it's built, how to run it, check results, the PR and demo links, feedback rounds, open items

## After the prototype
- **Test with users** (`pm-7-prototype-review`): they think aloud while I watch. Feedback goes back into the file it changes (a screen's inputs or checks → `solution-detail.md`, its look → `visual-design.md`), logged as a round in `clickable-prototype.md`
- **Hand-off:** solution detail plus visual design are the spec. Rebuild with real components, one PR per screen with tests, behind a feature flag; an engineer reviews; check in staging
- **Release and measure** against targets agreed in advance; iterate if it misses, scale if it hits

## Under time pressure
- Get a usable version in front of people early, then improve it
- Narrate what I'm building, what I'm leaving out, and why
- Leave time to finish: check the numbers and walk the flow once
