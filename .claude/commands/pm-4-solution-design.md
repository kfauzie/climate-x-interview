---
name: pm-4-solution-design
description: "Turn the solution concept into medium-fidelity screens, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before pm-5-build."
---

# Solution design

Before starting, read climate-x-products, climate-x-company and climate-x-role. Start from the workflow in the solution concept (the Notion page linked in `RUN.md`).

Output: the screen images, saved in runs/run-N/design/.

## Principles
1. **Know the user.** Put yourself in their shoes. They're intelligent and expert in their domain, but not technical. Use their own terms from the interview notes; don't invent labels. No technical or AI terms on screen.
2. **One step per screen.** Each screen does exactly one step of the workflow.
3. **Show only what matters.** Sensible defaults wherever possible, and a few clear options. Each fact appears once.
4. **Information hierarchy and progressive disclosure.** The key information is big and up front. Detail sits lower and smaller, or appears only when the user asks for it.
5. **Trust.** The user can see how each number was produced.
6. **Handle edge cases.** Missing data, unclear input, or something the product can't do: say so where it happens, and let the user clarify or pick the closest alternative.
7. **Make it enjoyable.** Serious, but with a little personality: friendly wording, a clear sense of progress, small moments of feedback (e.g. a short loading message, a clear "done").

## How to work
- Medium fidelity: real labels, greyscale plus one accent colour, no brand polish.
- Don't calculate anything for these static screens. Use realistic placeholder numbers. The real numbers are calculated with code in pm-5-build.
- Show only what a real user would see. No design notes on screen. The only exception is a ribbon at the top: "User: [role] · Job to be done: [job]".
- One screen first, the most important one. Get feedback before making the rest.
- If a screen takes more than a few minutes, it's too detailed.
- Before showing me, walk the flow once as the user and fix anything confusing.
