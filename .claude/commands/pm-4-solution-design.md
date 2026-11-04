---
name: pm-4-solution-design
description: "Turn the solution concept into medium-fidelity screens a reviewer can follow live: each key screen as a realistic static mock (real content and numbers, real states, no brand polish), with its inputs, checks and edge cases in a few lines underneath. One screen first. Includes my design principles for AI products a non-technical user trusts and can act on. Use after the solution concept, before the clickable prototype."
---

# Solution design

Make it something a non-technical user can trust, understand at a glance and act on. One job, done well: it fits where they already work, explains itself, shows how it got every answer, and ends in a decision.

Input: `solution-concept.md`. Output: `runs/run-N/solution-design.md` plus the screen images, reviewed live with the user and agreed before `pm-5-clickable-prototype`. Concrete enough to react to in the moment; quick enough to change while they watch.

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
- Every value shows where it came from (the user's words, a default and where it's written, the data rows), and one click confirms it
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

## Medium fidelity
- Real layout, real labels, their question and real numbers from code
- Real states on the screen itself: defaults with their source, a warning, a blocked action, an empty or zero result. Mandatory inputs marked as the product would ("Required")
- Greyscale plus one accent colour, system font, no icons, shadows or brand polish. That comes in the clickable prototype
- **Only the product, as the user would see it.** No annotations, numbered markers, side notes or design commentary in the image
- Static HTML rendered to PNG, all screens in one file; Figma when connected
- **One screen first:** the most important one (usually the answer), shown while the others are made. Its feedback shapes the rest
- About 10 minutes for the set. If a screen takes longer, it's too detailed

## What goes in `solution-design.md`
1. **Flow:** one table, step | who | screen | ends in. Who never touches it. Decisions to agree, each with my recommendation
2. **Each screen**, in flow order:
   - The image
   - Removes: the pain it takes away, in one line
   - Inputs: required or optional, the default, and its source (the user, a default and where it's written, read by AI)
   - Checks: what's checked, and whether a failure blocks or warns, with the exact message
   - Ends in: the action, and what must always be true
3. **Test set:** their examples, a real failure and an out-of-scope request, with expected answers computed by code
4. **Limits** the product states, and what it refuses

Keep the text under each image to a few lines. If it needs more, the screen is doing too much.
