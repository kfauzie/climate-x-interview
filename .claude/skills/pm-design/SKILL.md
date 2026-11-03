---
name: pm-design
description: "My product and UX design approach: how to make an AI product a non-technical user trusts and can act on. Principles, the process from success measures to user flow to a prototype that becomes the spec, a review checklist, and the per-run design doc. Use when designing flows or screens, building a prototype UI or applying design feedback."
---

# Design

Make it something a non-technical user can trust, understand at a glance and act on. One job, done well: fits where they already work, explains itself, shows how it got every answer, ends in a decision.

Input: `solution.md` (the pick, the slice, success criteria). Output: `runs/run-N/design.md` (outline at the end), then the prototype.

## Principles

### Worth building
- Every screen removes a named pain, in the customer's words. If it doesn't, cut it
- Rules, defaults and layout before AI
- Ends in an action (approve, send, change a decision), with the consequence next to it
- Design for who uses it, not who asked

### Trustworthy
- **Reasoning for every outcome:** answer up front, method and source rows one click away
- **Honest about uncertainty:** say "unsure" and why. Flag what's unstated, ambiguous or not in the data; never guess
- **Humans in control:** easy to review, override, configure. Overrides feed the test set
- **AI interprets, code computes:** AI turns messy input into choices the user confirms; a model never shows a number
- **Provenance visible:** each figure traces to its inputs and rows on screen; each value tagged (from the user / default / changed)
- **Earn trust gradually:** offline tests → shadow mode → pilot → scale
- **Limits in the product:** what it won't do, a way to stop, a narrow scope. A stated limit builds more trust than a hidden one

### Easy to use
- **Fit the workflow:** where they already work, in the format they already send (email, Excel tab, slide)
- **Explains itself:** one line on what will happen ("Uses your committee defaults: central scenario, 2050")
- **Pyramid:** one headline, then detail, then the full method
- **Their language:** their terms, the product's vocabulary; yes / no / unsure, not confidence scores. The AI should feel almost invisible
- **Inputs:** free text first, examples only pre-fill, "Other" always there. Show what was understood; let them add what was missed
- **Flow:** back keeps everything; back bottom left, next bottom right, one primary action per step; warn rather than block when a reviewer will see it
- **Changeable defaults** have an owner, a version and a change log; in a transition, old and new side by side

### Craft
- Clean B2B SaaS: spacing, hierarchy, consistent components, restrained colour, status as chips as well as text
- Looks like part of the product: copy conventions from real product screenshots, not the marketing site
- Real brand values from the source, never guessed. A published page doesn't impersonate the company
- Accessible: not colour alone, visible focus, light and dark, phone width

## Process
1. **Success first:** users, measures (task completion, time to a usable answer, edits, review time, overrides), guardrail, where it breaks today
2. **Flow before screens:** who does what (asker, user, approver, gatekeeper), the steps, decisions to agree, each with my recommendation
3. **Brief the design** (for Claude with Figma, or a designer):
   - Users, target outcome for one session, tone
   - Grounding: design guide, glossary, product screenshots. "Flag gaps, don't fill them"
   - Each step: input, output, happy path, edge cases with the exact message, acceptance criteria, hand-off. E.g. upload: "Found 200, all matched" / "188 matched, 12 need a check: here they are" / every item matched or flagged, none silently dropped
4. **Screens:** their real examples as happy paths; a real failure they described as the main edge case
5. **Test set:** expected answers from code
6. **Build** (on a branch `prototype/<name>`, PR at the end):
   - Engine (numbers, checks, method note, rows) separate from the interpreter (input → choices, never a number); thin API; static front end
   - No real data yet → seeded script in the run, labelled SYNTHETIC; check defaults don't exclude most of it
   - Tests = test set + flow rules; same input → same number. Run after every change
   - Labels and verdicts from the numbers, never typed by hand
7. **Check:** walk it in a real browser (end to end, phone, dark), look at screenshots, run the checklist below. Catches what tests miss: misleading labels, raw JSON, back that loses work
8. **Think-aloud with users:** don't explain; they say what they're thinking (`pm-prototype-review`). Later: compare options on completion and speed
9. **Prototype + brief = the spec:** real components, one PR per screen with tests, behind a feature flag; engineer reviews; check in staging
10. **Release and measure** against targets agreed in advance → iterate or scale. Log each feedback round in `design.md`; general lessons back into this skill

For people who can't run it: a clickable demo from the real UI with an in-page mock of precomputed answers, so the two never drift apart. Say on the page what it can't do.

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
- Usable version early, then improve
- Narrow the analysis early; don't let it eat the build
- Narrate what I'm building, leaving out, and why
- Leave time to finish: check numbers, walk the flow once, state the limits

## `design.md` outline (per run)
- **Success:** users, measures, guardrail, where it breaks today
- **Who does what:** asker, user, approver, gatekeepers (what each needs)
- **Flow:** steps, each marked computed / interpreted / decided by a person
- **Decisions:** each with the agreed answer
- **Screens:** input, output, happy path, edge cases, acceptance
- **Test set:** their examples, a real failure, an out-of-scope request, expected answers from code
- **Limits shown in the product**
- **Checklist result:** what failed, the fix
- **Brand and look:** values and source; product conventions
- **Feedback rounds:** who, when, what was said, status
- **Open items**
