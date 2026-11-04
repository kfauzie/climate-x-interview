---
name: pm-4-solution-design
description: "Turn the solution concept into medium-fidelity screens a reviewer can follow live: a walkthrough in the user's shoes, one screen per step, sensible defaults, the key number big and up front, edge cases handled where they happen. Each screen is a static mock with real numbers and a few lines on its inputs and checks. Most important screen first. Use after the solution concept, before the clickable prototype."
---

# Solution design

Input: `solution-concept.md`. Output: `runs/run-N/solution-design.md` plus the screen images, reviewed live and agreed before `pm-5-clickable-prototype`.

## Principles
1. **Know the user.** Put yourself in their shoes: write a short walkthrough ("I'm the [user], I've just received [trigger]. First I…, then I…"). They're intelligent and expert in their domain, but not technical. Use the language from the interview notes and their role. No technical or AI terms on screen
2. **One step per screen.** Each screen does exactly one step of the walkthrough
3. **Show only what matters.** Only what the user needs to provide or confirm for that step; everything else is gone or one click away. Sensible defaults wherever possible, so the user only confirms. A few sensible options, not a blank field or everything at once
4. **Information hierarchy.** The key information is big and up front. Details and supporting information sit lower, smaller and less prominent
5. **Trust.** Numbers are calculated, never written by the AI, and the user can see how each one was produced
6. **Handle edge cases.** Missing data, unclear input, or something the product can't do: say so where it happens, and let the user clarify or pick the closest alternative
7. **Test it, briefly.** Walk the main flow once as the user (a minute). Run AI personas and edge cases only on the most important screen, with a handful of cases. Note what you'd test with real users later

## Separate the product from the explanation
- The screen shows only what a real user would see in the real product. No design commentary, annotations or notes on how the AI works
- The only meta element on screen is the ribbon at the top: "User: [role] · Job to be done: [job]"
- Everything that explains the design goes in a few lines under the image: the pain it removes, inputs, checks, edge cases

## Screen checklist
- Inputs the user can see and check are at the top
- An output sits directly below its input and is the most prominent thing
- Each fact appears once; show, don't tell
- It's a draft until someone approves it

## Fidelity and speed
- Medium fidelity: real labels and real numbers from code, greyscale plus one accent colour, no brand polish
- One screen first, the most important one. Get feedback before making the rest
- If a screen takes more than a few minutes, it's too detailed

## Output: `solution-design.md`
- The walkthrough
- Flow: one table (step | who | screen | ends in)
- Each screen: the image, then a few lines: the pain it removes, inputs, checks, what it ends in
- Test set: the customer's examples, one real failure and one out-of-scope request, with expected answers computed by code
