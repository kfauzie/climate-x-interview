---
name: pm-design
description: "My product and UX design approach: how to make an AI product a non-technical user trusts and can act on. Principles (trust, ease of use, craft), the process from user flow to screens to a prototype that becomes the spec, and a review checklist. Use when designing flows or screens, briefing a design, building a prototype UI or applying design feedback."
---

# Design

Make it something a non-technical user can trust, understand at a glance and act on. One job, done well: fits where they already work, explains itself, shows how it got every answer, ends in a decision.

Input: `solution.md` (the pick, the slice, success criteria). Output: `runs/run-N/design.md` from `template.md`, then the prototype. Also: `design-prompt.md` (briefing a design), `building.md` (building and checking it).

## Principles

### Worth building
- Every screen removes a named pain, in the customer's words. If it doesn't, cut it
- Rules, defaults and layout before AI
- Ends in an action (approve, send, change a decision), with the consequence next to it
- Design for who uses it, not who asked

### Trustworthy
- **Reasoning for every outcome:** answer up front, method and source rows one click away
- **Honest about uncertainty:** say "unsure" and why, still summarise what's known. Flag what's unstated, ambiguous or not in the data; never guess
- **Humans in control:** easy to review, override, configure. Overrides feed the test set
- **AI interprets, code computes:** AI turns messy input into choices the user confirms; a model never shows a number
- **Provenance visible:** each figure traces to its inputs and rows on screen; each value tagged (from the user / default / changed)
- **Earn trust gradually:** offline tests → shadow mode → pilot → scale, with the screens each stage needs
- **Limits stated in the product:** what it won't do, a way to stop, a narrow scope. A stated limit builds more trust than a hidden one

### Easy to use
- **Fit the workflow:** where they already work, in the format they already send (email, Excel tab, slide)
- **Explains itself:** one line in the product on what will happen ("Uses your committee defaults: central scenario, 2050")
- **Pyramid:** one headline, then detail, then the full method
- **Their language:** their terms and the product's vocabulary; yes / no / unsure, not confidence scores. The AI should feel almost invisible
- **Inputs:** free text first, examples only pre-fill; "Other" always available. Show what was understood and let them add what was missed
- **Flow:** back keeps everything; back bottom left, next bottom right, one primary action per step; warn rather than block when a reviewer will see it
- **Changeable defaults** have an owner, a version and a change log; in a transition, old and new side by side

### Craft
- Clean B2B SaaS: spacing, clear hierarchy, consistent components, restrained colour, status as chips as well as text
- Looks like part of the product: copy conventions from real product screenshots, not the marketing site
- Real brand values from the source, never guessed. A published page doesn't impersonate the company
- Accessible: not colour alone, visible focus, light and dark, phone width

## Process
1. **Success first:** users, measures (task completion, time to a usable answer, edits, review time, overrides), guardrail, where it breaks today
2. **Flow before screens:** who does what (asker, user, approver, gatekeeper), the steps, decisions to agree, each with my recommendation
3. **Brief** (`design-prompt.md`): users, target outcome, grounding (design guide, glossary; flag gaps, don't fill them), each step's input, output, happy path, edge cases, acceptance criteria
4. **Screens:** their real examples as happy paths; a real failure they described as the main edge case
5. **Test set:** expected answers from code
6. **Prototype** (`building.md`), then the checklist below
7. **Think-aloud with users:** don't explain; they say what they're thinking. Later rounds: compare options on completion and speed (`pm-prototype-review`)
8. **Prototype + brief = the spec:** rebuild with real components, one PR per screen with tests, behind a feature flag; engineer reviews; check in staging
9. **Release and measure** against targets agreed in advance → iterate or scale
10. **Log each feedback round** in `design.md`; general lessons back into this skill

## Checklist (before showing anyone)
- [ ] Non-technical user knows in 5 seconds what the screen is for and what to do next
- [ ] Every screen ties to a pain; the flow ends in an action
- [ ] One headline; detail on demand
- [ ] Every number traceable from the screen
- [ ] Uncertainty, assumptions and limits visible where the decision is made
- [ ] Unstated, ambiguous, out-of-scope flagged, not guessed
- [ ] Their language, no AI jargon
- [ ] Back keeps everything; actions in the same place
- [ ] Errors and empty states say what to do
- [ ] Looks like part of the product
- [ ] Light, dark, phone width, keyboard
- [ ] Finished to something credible: checked, end to end, limits stated

## Under time pressure
- Usable version in front of people early, then improve
- Narrow the analysis early; don't let it eat the build
- Narrate what I'm building, leaving out, and why
- Leave time to finish: check numbers, walk the flow once, state the limits
