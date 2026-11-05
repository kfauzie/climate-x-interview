---
name: pm-4-solution-design
description: "Turn the solution concept into screens in Climate X's brand, one per workflow step, that a reviewer can follow live. Most important screen first. Use after the solution concept, before pm-5-mvp-build."
---

# Solution design

Before starting, read climate-x-products, climate-x-company and climate-x-role. Follow the communication guide in climate-x-role for everything you write. Start from the workflow in the solution concept (the Notion page linked in `RUN.md`).

Output: the screen images, saved in runs/run-N/design/.

## Principles
1. **Decision first.** The product exists to help someone make a commercial decision. If a screen has a recommended decision, it's at the top, with the reason right under it.
2. **Know the user.** They're intelligent and expert in their domain, but not technical. Use their own terms from the interview notes; don't invent labels. No technical or AI terms on screen. Labels use roles, not people's names, so it works for any team.
3. **One step per screen.** Each screen does exactly one step of the workflow. When the next step belongs to someone else, make the hand-over clear.
4. **Show only what matters.** Sensible defaults, labelled "Default", and a few clear options. Each fact appears once. Every input earns its place: it changes the answer or who gets it.
5. **Information hierarchy and progressive disclosure.** The key information is big and up front. Detail sits lower and smaller, or appears only when asked.
6. **Trust.** The user can see how each number was produced, and where every choice came from (their input, a default, or changed by them).
7. **Handle edge cases.** Missing data, unclear input, or something the product can't do: say so where it happens, and let the user clarify or pick the closest alternative. When something is wrong, let them fix it right there, then redo whatever depends on it.
8. **Make it enjoyable.** Serious, but with a little personality: friendly wording, a sense of progress, small moments of feedback.

## How to work
- **Look:** clean, delightful B2B SaaS in Climate X's brand: font Graphik (Helvetica, Arial as fallbacks); red #e01e1a, charcoal #343a40, off-white #f9f9fa, white panels. Red only for the main action. Soft tints for status (green done, amber needs attention, blue selected or informational). Colour is never the only signal: a warning also says "Warning", a done state also shows a tick.
- **Layout details:** details in a table (label | value), not a paragraph. A line explaining a heading sits right under it, smaller and lighter. Hover explanations for assumptions and counts. Source tags on choices, one colour per kind. Notes and warnings look different from content.
- **Actions:** one primary button per screen (filled); others secondary (outline). Links and buttons say what they do. Secondary actions (send back, cancel) stay out of the Back position.
- **Borrow patterns:** for each step, find the closest comparable product and borrow what fits, and say which. E.g. Typeform or TurboTax for guided flows; Stripe for numbers with their source one click away; Linear for calm hierarchy.
- **No calculations:** use realistic placeholder numbers. Don't check against the data or report mismatches. Real numbers come in pm-5-mvp-build.
- **Prototype frame:** every screen fills the window, with a ribbon at the top (large, blue, an icon, "User: [specific role]" and "Job to be done: [job]", equally large) and a clickable chevron step bar with the current step highlighted. Leave both out of anything exported (e.g. PDFs). No other design notes on screen.
- **Process:** one screen first, the most important one. Get feedback before making the rest. If a screen takes more than a few minutes, it's too detailed. Before showing me, walk the flow once as the user and fix anything confusing.
