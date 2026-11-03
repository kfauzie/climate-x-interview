---
name: pm-design
description: "Product and UX design from a recommended solution to a usable prototype: a design philosophy for AI products non-technical users can trust and act on, judgement on what is worth building, success defined before designing, user flow before screens, a design prompt, screens with inputs, outputs, edge cases and acceptance criteria, a design review checklist, think-aloud testing, and how the prototype becomes the spec. Use when deciding what to build, designing flows or screens, writing a design prompt, building or reviewing a prototype UI, or applying design feedback."
---

# PM design

**The point of view:** design what is worth building, then make it something a non-technical user can trust, understand at a glance and act on. A good product does one job very well; it fits where people already work, explains itself, shows how it got every answer, and ends in a decision, not a report.

Input: the run's `solution.md` (the pick, its narrowest version, success criteria). Output: the run's `design.md` from **`template.md`**, then the prototype. Supporting files: **`design-prompt.md`** (how to brief a design), **`building.md`** (how to build and check the prototype). Never edit the templates for a single run, and never reuse another run's design.

## 1. Decide what's worth building
- **Start from the problem, not the feature request.** Name the pain each screen removes, in the customer's words. If a screen doesn't tie to a pain, cut it
- **The simplest thing that solves it.** Try rules, defaults and clear layout before AI; add complexity only when the simple version is tested and falls short
- **One job, done well.** A focused tool that does one thing reliably beats a broad one nobody trusts. Say plainly what it doesn't do
- **Decision-ready, not a better report.** Every flow ends in an action the user can take (approve, send, change a decision), with the financial or operational consequence next to it
- **Think big, ship narrow.** Show where this could go (one line, or a roadmap), then build the narrowest slice that proves the riskiest assumption
- **Design for the person who uses it, not the person who asked.** Askers and users are often different people

## 2. Define success before designing
- **Who the users are** (role, how technical, how often they'll use it) and **what success means to them**, as measures: task completion, time to a usable answer, manual edits or corrections, review time, how often outputs are overridden
- **A guardrail:** what must stay true for them to trust it (e.g. every number traceable, nothing silently dropped)
- **Where it breaks today:** the step where time goes, errors happen or people give up. That's where the design must be strongest

## 3. Trust: AI products for non-technical users
- **Show the reasoning for every outcome.** A top-level answer up front, with the method, inputs and source rows one click away
- **Be honest about uncertainty.** Say "unsure" and why, and still summarise what is known, so the expert can decide. Flag what's unstated, ambiguous or not in the data rather than guessing
- **Keep humans in control.** Easy to review, override and configure. Overrides and corrections feed back into the test set
- **AI interprets; code computes.** AI turns messy input into structured choices the user confirms; every number comes from deterministic code. A model never shows or estimates a number
- **Make provenance visible.** Each figure traces to its inputs, settings and source rows from the screen itself, not only in an export. Tag where each value came from (from the user, a default, changed by the user)
- **Earn trust gradually.** Offline tests on known answers → shadow mode beside the current process → pilot → scale. Design the screens each stage needs (e.g. a side-by-side comparison for shadow mode)
- **Visible safety nets and explicit limits.** Show what the product will and won't do, a way to stop or roll back, and a targeted scope. A clearly stated limitation builds more trust than a hidden one

## 4. Easy to use
- **Fit the existing workflow.** Show up where people already work and produce what they already send (email text, a spreadsheet tab, a slide), in their format
- **Explain what the product does, in the product.** A one-line banner or empty state that says what will happen ("Answers use your committee defaults: central scenario at 2050"), repeated in settings and help
- **Pyramid structure.** Summary first, detail on demand: one headline number, then supporting detail, then the full method and rows
- **Speak their language.** Their terms and the product's own vocabulary (metric names, ratings, settings); plain labels like yes / no / unsure instead of confidence scores, models or prompts. The AI should feel almost invisible
- **Free text first; examples are defaults.** Examples pre-fill a field, never replace it; option lists include "Other" with free text
- **Show what was understood, and let the user add to it,** not only accept or change what was detected
- **Navigation never loses work.** Back keeps everything entered
- **Consistent action placement.** Back (secondary) bottom left, the forward action (primary) bottom right, one primary action per step
- **Warn rather than block** where a reviewer will see it, unless the step would produce something wrong
- **Defaults that can change have an owner and a history.** Configurable, owned by a named person, versioned, with a change log; during a transition, show old and new side by side

## 5. Visual craft
- **Modern B2B SaaS feel:** generous spacing, clear hierarchy, consistent components (buttons, inputs, tags, panels), restrained colour, a step indicator for multi-step flows, status shown with chips and colour as well as text
- **Match the company's product UI, not just its website:** study real product screenshots for layout, components, colour use and how numbers and ratings are shown, and reuse those conventions so the prototype looks like part of the product
- **Use the real brand** (palette and fonts) from the source (site CSS, brand guide, the person); never guess. A page published for others must not impersonate the company (no logo, no brand name as the product name) unless confirmed for its internal use
- **Accessible and responsive:** never colour alone for meaning, visible focus states, light and dark, phone width

## 6. Process
1. **Align on the user flow before screens:** who does what (asker, user, approver, gatekeeper), the steps, and the decisions to agree, each with a recommendation
2. **Brief the design** with `design-prompt.md`: role, users, target outcome, grounding (design guide, glossary; flag gaps instead of filling them), tone, and each step's input, output, happy path, edge cases, acceptance criteria and hand-off
3. **Screens:** the customer's real examples as happy paths, a real failure they described as the main edge case
4. **Test set** with expected answers computed by code
5. **Prototype** (see `building.md`), then run the design review checklist below
6. **Test with users using think-aloud:** don't explain; ask them to say what they're thinking as they use it. In later rounds compare options on task completion and speed (see `pm-prototype-review`)
7. **The prototype and the updated design prompt become the spec:** rebuild each screen with the product's real components, one PR per screen with tests for the happy path and edge cases, behind a feature flag; an engineer reviews architecture, security and scale; check in staging against the acceptance criteria
8. **Release and measure** against the success measures from §2, with targets agreed in advance; iterate if it misses, scale if it hits
9. **Record every feedback round** in `design.md`, and fold general lessons into this skill

## 7. Design review checklist (before showing anyone)
- [ ] Can a first-time, non-technical user tell **in five seconds** what the screen is for and what to do next?
- [ ] Does every screen tie to a named pain, and does the flow **end in an action**?
- [ ] Is there **one headline**, with detail on demand?
- [ ] Can every number be **traced** to its inputs and rows from the screen?
- [ ] Are **uncertainty, assumptions and limitations** visible where the decision is made?
- [ ] Is anything unstated, ambiguous or out of scope **flagged** rather than guessed?
- [ ] Is every label in the **user's language**, with no model or AI jargon?
- [ ] Does **back** keep everything, and are actions in the **same place** on every step?
- [ ] Do **errors and empty states** say what happened and how to fix it?
- [ ] Does it look like it **belongs in the product** (components, vocabulary, brand)?
- [ ] Does it work in **light and dark**, at **phone width**, with a **keyboard**?
- [ ] Is it **finished to something credible**: checked, usable end to end, limits stated, rather than half-built?

## Under time pressure (live builds, short sprints)
- **Get a usable version in front of people early,** then improve it. A working, honest slice beats a perfect plan
- **Narrow the analysis early;** don't let data exploration eat the build
- **Narrate the choices:** what you're building, what you're leaving out, and why
- **Save time to finish:** check the numbers, walk the flow once end to end, and state the limitations
