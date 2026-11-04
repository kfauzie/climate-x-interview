---
name: pm-5-build
description: "Turn the agreed solution design into a working first version (MVP) on a branch: the customer's brand and product look, engine separate from the AI interpreter, synthetic data, tests from the test set, a check in a real browser, a PR and a no-install demo. Use when building or changing it."
---

# Build: the working first version

Input: `solution-design.md` (agreed screens, checks, test set). Output: `runs/run-N/build.md` and a PR. This is where the screens get full visual polish. Layout and content follow the principles and checklist in `pm-4-solution-design`; polish never adds elements.

## Look
- Clean B2B SaaS: generous spacing, clear hierarchy, consistent components, restrained colour
- **Brand:** font Graphik (Helvetica, Arial as fallbacks). Colours: red `#e01e1a` (darker `#a11b14` on hover), charcoal `#343a40`, off-white `#f9f9fa`, white panels
- **Product look:** light, white panels, thin dividers, small grey uppercase labels; scenario and year as rounded dropdowns in a side panel; red for active toggles; A–G ratings as coloured circles; large light-weight numbers; pill buttons; red only for the primary action
- Accessible: never colour alone, visible focus, works in light and dark and on a phone
- A page shared outside the company doesn't present itself as the company's product

## Build and check
- **Build** on a branch:
  - The engine (numbers, checks, method, rows) separate from the interpreter (input → choices, never a number)
  - No real data yet: a seeded synthetic file in the run, labelled as synthetic
  - Tests from the test set; run them after every change
  - Labels and verdicts generated from the numbers, never typed by hand
- **Check before showing anyone:** walk it end to end in a real browser and look at the screenshots. Then ask:
  - Can a first-time user tell in five seconds what the screen is for and what to do next?
  - Do the principles in `pm-4-solution-design` and the look above hold on the real screens?
  - Are the numbers right, and are the limits stated?
- **PR** with screenshots, how to run it and the test results
- For people who can't run it: a clickable demo built from the real UI that replays precomputed answers, with a note on what it can't do
- `build.md`: how it's built, how to run it, check results, the PR and demo links, feedback rounds, open items

## After the build
- **Test with users** (`pm-6-mvp-review`): they think aloud while I watch. Feedback goes back into the file it changes (a screen's content, inputs or checks → `solution-design.md`, its look → the build), logged as a round in `build.md`
- **Hand-off:** I turn the approved version into the PR myself, with tests: that PR is the spec. One PR per screen, behind a feature flag. The engineer reviews it and hardens it for production (sign-in, storage, monitoring); check in staging
- **Release and measure** against targets agreed in advance; iterate if it misses, scale if it hits

## Under time pressure
- Get a usable version in front of people early, then improve it
- Narrate what I'm building, what I'm leaving out, and why
- Leave time to finish: check the numbers and walk the flow once
