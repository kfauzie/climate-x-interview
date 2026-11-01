---
name: pm-design
description: "Principles for designing and prototyping a product from a recommended solution: user flow first, then screens with inputs, outputs, edge cases and acceptance criteria, then a prototype. Use when designing screens or flows, building or reviewing a prototype UI, or applying design feedback."
---

# PM design

Input: the run's `solution.md` (the pick, its narrowest version, success criteria). Output: the run's `design.md` (flow, decisions, screens, test set, feedback rounds), then the prototype.

## Process
1. **Align on the user flow before screens.** Who does what (asker vs user vs approver vs gatekeeper), the steps in order, and the decisions to agree, each with a recommendation. Record the agreed flow and decisions in `design.md`
2. **Then screens.** For each: input, output, happy path (use the customer's real example questions), edge cases (use a real failure they described), acceptance criteria
3. **Then the test set**, with expected answers computed by code
4. **Then the prototype.** Every number from deterministic code; AI only where it interprets, and never shows a number
5. **Record every feedback round** in `design.md` (what was said, status), and fold the general lessons into this skill

## Interaction principles
- **Inputs are free text first; examples are defaults.** Example questions or values pre-fill the field; they never replace it. Lists of options always include "Other" with free text
- **Show what was understood, and let the user add to it.** When the system interprets input (e.g. a question into choices), the user can edit each item **and add items it missed**, not only accept or change what was detected
- **Navigation never loses work.** Going back keeps everything entered; nothing resets unless the user asks
- **Consistent action placement.** Back (secondary) at the bottom left, the forward action (primary) at the bottom right, on every step. One primary action per step
- **Tag where each value came from** (from the user, a default, changed by the user) when trust matters
- **Warn rather than block** where a reviewer will see it, unless the step would produce something wrong

## Visual principles
- **Modern B2B SaaS feel:** clean layout with generous spacing, a clear hierarchy (one headline number, then supporting detail), consistent components (buttons, inputs, tags, panels), restrained colour, a step indicator for multi-step flows, and status shown with chips and colour, not only text
- **Match the company's product UI, not just its website:** study real product screenshots (product pages, demo videos, docs) for layout, components, how colour is used and how numbers and ratings are shown, and reuse those conventions so the prototype looks like it belongs in their product
- **Use the customer's or company's brand** (colour palette and fonts) when the prototype is for them. Get the real values from the brand source (site CSS, brand guide, or the person); never guess them. If they can't be fetched, say so and ask
- **Brand use and publishing:** a company's branding belongs in the prototype code. A page published for others to view should not impersonate the company (no logo, no brand name as the product's name) unless the person confirms it's for that company's internal use
- **Both light and dark, and phone width,** for anything published as a page
