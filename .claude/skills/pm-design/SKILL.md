---
name: pm-design
description: "My product and UX design approach for AI products a non-technical user trusts and can act on: principles, then the process from user flow to a visual design (static images) to a clickable prototype that becomes the spec. Use when designing flows or screens, producing a visual design, building a prototype or applying design feedback."
---

# Design

Make it something a non-technical user can trust, understand at a glance and act on. One job, done well: it fits where they already work, explains itself, shows how it got every answer, and ends in a decision.

Input: `solution.md` (what to build, the slice, success criteria). Output: `runs/run-N/design.md`, a visual design, then a clickable prototype.

## Principles

### Every screen earns its place
- Each screen removes a pain the customer named. If it doesn't, cut it
- Rules, defaults and layout before AI
- The flow ends in an action (approve, send, change a decision), with the consequence next to it

### Trust
- Answer up front; the method and source rows one click away
- Honest about uncertainty: say "unsure" and why. Flag what's unstated, ambiguous or not in the data instead of guessing
- People stay in control: easy to review, override and configure. Their overrides become test cases
- AI interprets, code computes. AI turns messy input into choices the user confirms; it never shows a number
- Every value shows where it came from: the user, a default, or a change
- State the limits in the product: what it won't do, and a way to stop. A stated limit builds more trust than a hidden one
- Earn trust in stages: offline tests, then shadow mode beside the current process, then a pilot

### Ease of use
- Fits the workflow: where they already work, in the format they already send (email, spreadsheet, slide)
- Explains itself in one line ("Uses your committee defaults: central scenario, 2050")
- Pyramid: one headline, then detail, then the full method
- Their language and the product's own terms. Yes / no / unsure, not confidence scores. The AI should feel almost invisible
- Free text first; examples only pre-fill. Show what was understood and let them add what was missed
- Back keeps everything. Back bottom left, next bottom right, one primary action per step
- Warn rather than block when a reviewer will see it
- Defaults that can change have an owner and a change log

### Look
- Clean B2B SaaS: generous spacing, clear hierarchy, consistent components, restrained colour
- Looks like part of their product: copy conventions from real product screenshots, and real brand values from the source, never guessed
- Accessible: never colour alone, visible focus, works in light and dark and on a phone
- A page shared outside the company doesn't present itself as the company's product

## Process
1. **Success:** who the users are; how we'll measure it (task completion, time to a usable answer, edits, review time); what must stay true to trust it; where it breaks today
2. **Flow:** who does what (asker, user, approver, gatekeeper) and the steps. List the decisions to agree, each with my recommendation
3. **Visual design (static images first).** Key screens as polished, realistic mock-ups, not clickable:
   - Real content: their actual question, real numbers from code, their terms
   - The happy path, plus the one screen that matters most for trust (e.g. the review screen, or a failure being caught)
   - Made in Figma when connected, otherwise a static HTML mock rendered to PNG
   - **The images show only the product, exactly as the user would see it.** No annotations, numbered markers, side notes, "screen 1 of 3" labels, pain call-outs, design-check results or review comments. Anything about the design goes in `design.md`, never in the image
   - Review them with the user and agree before building anything clickable. Cheap to change now, expensive later
4. **Screen spec:** for each screen, input, output, happy path, edge cases with the exact message, acceptance criteria. A real failure the customer described is the main edge case
5. **Test set:** their examples, a real failure and an out-of-scope request, with expected answers computed by code
6. **Clickable prototype** (on a branch, PR at the end):
   - The engine (numbers, checks, method, rows) separate from the interpreter (input → choices, never a number)
   - No real data yet: a seeded synthetic file in the run, labelled as synthetic
   - Tests from the test set; run them after every change
   - Labels and verdicts generated from the numbers, never typed by hand
7. **Check before showing anyone** (results go in `design.md`, never on the screens): walk it end to end in a real browser and look at the screenshots. Then ask:
   - Can a first-time user tell in five seconds what the screen is for and what to do next?
   - Does each principle above hold on the real screens?
   - Are the numbers right, and are the limits stated?
8. **Test with users** (`pm-prototype-review`): they think aloud while I watch
9. **Hand-off:** the visual design and the screen spec are the spec. Rebuild with real components, one PR per screen with tests, behind a feature flag; an engineer reviews; check in staging
10. **Release and measure** against targets agreed in advance; iterate if it misses, scale if it hits

For people who can't run it: a clickable demo built from the real UI that replays precomputed answers, with a note on what it can't do.

## Under time pressure
- Get a usable version in front of people early, then improve it
- Narrate what I'm building, what I'm leaving out, and why
- Leave time to finish: check the numbers and walk the flow once

## `design.md` (per run)
Success · who does what · flow · decisions · visual design (images, plus the reasoning for each screen in text) · screen spec · test set · limits shown in the product · check results · brand values and their source · feedback rounds · open items
