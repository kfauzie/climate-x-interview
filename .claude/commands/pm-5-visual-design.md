---
name: pm-5-visual-design
description: "Turn the agreed solution detail into a visual design (static images of the key screens, product only, one screen first), then a clickable prototype on a branch with a PR. Use when producing the visual design, building the prototype or applying design feedback."
---

# Visual design, then the clickable prototype

Input: `solution-detail.md` (agreed) and the design principles in `pm-4-solution-detail`. Output: `visual-design.md` with images, then `clickable-prototype.md` and the PR.

## Look
- Clean B2B SaaS: generous spacing, clear hierarchy, consistent components, restrained colour
- Looks like part of their product: copy conventions from real product screenshots, and real brand values from the source, never guessed
- Accessible: never colour alone, visible focus, works in light and dark and on a phone
- A page shared outside the company doesn't present itself as the company's product

## Visual design (`visual-design.md`)
Key screens as polished, realistic static images, not clickable:
- Real content: their actual question, real numbers from code, their terms
- The happy path, plus the one screen that matters most for trust (e.g. the review screen, or a failure being caught)
- Made in Figma when connected, otherwise a static HTML mock rendered to PNG
- **One screen first.** Make the most important screen (usually the answer), show it, and make the others while the user reviews it. Their feedback on it shapes the rest
- **The images show only the product, exactly as the user would see it.** No annotations, numbered markers, side notes, "screen 1 of 3" labels, pain call-outs, design-check results or review comments. Reasoning goes in `visual-design.md`, never in the image
- `visual-design.md`: the images, the reasoning for each screen, brand values and their source
- Agree all of them with the user before building anything clickable. Cheap to change now, expensive later

## Clickable prototype (`clickable-prototype.md`, then PRs)
- **Build** on a branch:
  - The engine (numbers, checks, method, rows) separate from the interpreter (input → choices, never a number)
  - No real data yet: a seeded synthetic file in the run, labelled as synthetic
  - Tests from the test set; run them after every change
  - Labels and verdicts generated from the numbers, never typed by hand
- **Check before showing anyone:** walk it end to end in a real browser and look at the screenshots. Then ask:
  - Can a first-time user tell in five seconds what the screen is for and what to do next?
  - Do the principles in `pm-4-solution-detail` and the look above hold on the real screens?
  - Are the numbers right, and are the limits stated?
- **PR** with screenshots, how to run it and the test results
- For people who can't run it: a clickable demo built from the real UI that replays precomputed answers, with a note on what it can't do
- `clickable-prototype.md`: how it's built, how to run it, check results, the PR and demo links, feedback rounds, open items

## After the prototype
- **Test with users** (`pm-6-prototype-review`): they think aloud while I watch. Feedback goes back into the file it changes (a screen's inputs or checks → `solution-detail.md`, its look → `visual-design.md`), logged as a round in `clickable-prototype.md`
- **Hand-off:** solution detail plus visual design are the spec. Rebuild with real components, one PR per screen with tests, behind a feature flag; an engineer reviews; check in staging
- **Release and measure** against targets agreed in advance; iterate if it misses, scale if it hits

## Under time pressure
- Get a usable version in front of people early, then improve it
- Narrate what I'm building, what I'm leaving out, and why
- Leave time to finish: check the numbers and walk the flow once
