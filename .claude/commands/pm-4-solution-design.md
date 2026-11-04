---
name: pm-4-solution-design
description: "Turn the solution concept into medium-fidelity screens a reviewer can follow live: a walkthrough in the user's shoes, one screen per workflow step, each a static mock with real numbers and a few lines on its inputs and checks. Most important screen first. Use after the solution concept, before the clickable prototype."
---

# Solution design

Input: `solution-concept.md`. Output: `runs/run-N/solution-design.md` plus the screen images, reviewed live and agreed before `pm-5-clickable-prototype`.

## Principles
1. **Put yourself in the user's shoes.** Before designing, write a short walkthrough: "I'm the [user], I've just received [trigger]. First I…, then I…". The screens follow it
2. **One screen, one workflow step.** Each screen does exactly one step of the walkthrough
3. **Guide, don't overwhelm.** Small steps. Ask one thing at a time, and offer a few real options rather than a blank field or everything at once
4. **Just enough.** Only what that step needs; everything else is gone or one click away. Every element earns its place
5. **Information hierarchy.** What the user most needs to see or check comes first, at the top and largest. Detail sits lower or one click away
6. **Smart, not technical.** The user is intelligent and expert in their domain, but not technical. Use their words, don't over-explain, hide the technical and AI machinery entirely
7. **Trust.** Every number comes from code and shows where it came from. When the product can't do something, it says so in its own voice, at the moment it matters
8. **Test it, briefly.** Walk the main flow once as the user (a minute). Run AI personas and edge cases only on the most important screen, with a handful of cases. Note what you'd test with real users later

## Separate the product from the explanation
- The screen shows only what a real user would see in the real product. No design commentary, annotations or notes on how the AI works
- The only meta element on screen is the ribbon at the top: "User: [role] · Job to be done: [job]"
- Everything that explains the design goes in a few lines under the image

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
