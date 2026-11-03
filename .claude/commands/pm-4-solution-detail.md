---
name: pm-4-solution-detail
description: "Turn the solution concept into what each screen does: the flow, who does what, and per screen its inputs (mandatory or not, default, source), what it shows, the checks it runs, edge cases and acceptance criteria. Includes my design principles for AI products a non-technical user trusts and can act on. Use after the solution concept, before any visual design."
---

# Solution detail

Make it something a non-technical user can trust, understand at a glance and act on. One job, done well: it fits where they already work, explains itself, shows how it got every answer, and ends in a decision.

Input: `solution-concept.md`. Output: `runs/run-N/solution-detail.md`, agreed with the user before `pm-5-visual-design`.

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

## What goes in `solution-detail.md`
- **Success:** who the users are; how we'll measure it (task completion, time to a usable answer, edits, review time); what must stay true to trust it
- **Flow:** who does what (asker, user, approver, gatekeeper) and the steps. Decisions to agree, each with my recommendation
- **Each screen:**
  - Purpose: the pain it removes
  - Inputs: each one mandatory or optional, its default, and where the value comes from (the user, a default, read by AI)
  - What it shows, headline first
  - Checks performed: what's checked, and whether a failure blocks or warns
  - Edge cases, with the exact message. A real failure the customer described is the main one
  - The action it ends in, and acceptance criteria
- **Test set:** their examples, a real failure and an out-of-scope request, with expected answers computed by code
- **Limits** the product states, and what it refuses
