---
name: pm-4-solution-design
description: "Turn the solution concept into screens in Climate X's brand, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before pm-5-build."
---

# Solution design

Before starting, read climate-x-products, climate-x-company and climate-x-role. Start from the workflow in the solution concept (the Notion page linked in `RUN.md`).

Output: the screen images, saved in runs/run-N/design/.

## Principles
1. **Know the user.** Put yourself in their shoes. They're intelligent and expert in their domain, but not technical. Use their own terms from the interview notes; don't invent labels. No technical or AI terms on screen. Explain domain terms wherever they appear, in a few words (e.g. "central (today's policies)"). Labels use roles, not people's names ("Send for approval", not "Send to Sarah"), so it works for any team; greeting the signed-in user by name is fine.
2. **One step per screen.** Each screen does exactly one step of the workflow.
3. **Show only what matters.** Sensible defaults wherever possible, labelled "Default", and a few clear options. Each fact appears once. Every input earns its place: it changes the answer or who gets it. Keep secondary actions (send back, cancel) out of the spot where users expect Back.
4. **Information hierarchy and progressive disclosure.** The key information is big and up front. Detail sits lower and smaller, or appears only when the user asks for it. Details go in a table, one fact per row (label | value), never a paragraph. Links and buttons say exactly what they open or do ("Show the rise by hazard", not "See where it comes from").
5. **Trust.** The user can see how each number was produced. Assumptions and counts get a short explanation on hover: what it means, and how the number was reached (e.g. "2,000 loans, 148 left out by the rules above, 20 not in the loan book: 1,832").
6. **Handle edge cases.** Missing data, unclear input, or something the product can't do: say so where it happens, and let the user clarify or pick the closest alternative.
7. **Make it enjoyable.** Serious, but with a little personality: friendly wording, a clear sense of progress, small moments of feedback (e.g. a short loading message, a clear "done").

## How to work
- Look: clean, delightful B2B SaaS in Climate X's brand: font Graphik (Helvetica, Arial as fallbacks); red #e01e1a, charcoal #343a40, off-white #f9f9fa, white panels. Red only for the main action. Don't rely on colour alone: pair it with text or an icon.
- Don't calculate anything for these static screens. Use realistic placeholder numbers. The real numbers are calculated with code in pm-5-build.
- Show only what a real user would see. No design notes on screen. The only exception is a ribbon at the top: large, in its own colour (not the brand red) so it reads as a label, with an icon for the user, "User: [role]" on top and "Job to be done: [job]" underneath.
- One screen first, the most important one. Get feedback before making the rest.
- If a screen takes more than a few minutes, it's too detailed.
- Before showing me, walk the flow once as the user and fix anything confusing.
