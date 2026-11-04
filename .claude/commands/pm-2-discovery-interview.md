---
name: pm-2-discovery-interview
description: "My approach to customer discovery interviews: how I run them, follow-up triggers, how I write the questions, and a 15-minute question template customised per run from the customer profile and data findings. Use when preparing, running or reviewing a discovery call."
---

# Discovery interview

Users tend to describe solutions; my job is to find the problem behind them.

Output: `runs/run-N/discovery-questions.md` (the template below, customised), published to Notion.

## How I run it
- **Problem, not solution:** no pitching and no "would you like X?". If they describe a solution, ask what it would let them do
- **The last real time:** anchor on a specific recent example. For each step: who, which tool, how long, handed to whom
- **Follow the data:** what goes in at each step, where it comes from, and what they do to it first
- **Find the bottleneck:** where the time goes, where errors and rework happen. Once it's clear it hurts, that's enough. Ask "How's that been for you?" only when they drop a cue ("it queues on my desk")
- **Who uses it vs who asks:** the people asking for answers often aren't the ones who'd use a tool. If the askers wouldn't use it, the ask may not hold
- **Value beyond time:** time and cost, the decisions a slow or wrong answer held up, and the risk of a wrong number reaching the board or the regulator

## Follow-up triggers
- "usually", "it depends" → "Tell me about the last time"
- "roughly", "sort of" → "What's the part I'm missing?" Don't restate it and move on
- A simple step that takes suspiciously long → "Walk me through that step"
- A feature request → "What would that let you do that you can't today?"
- Keep asking why: "no time" → "not a priority" → the real reason

## Writing the questions
- Non-leading: turn a data finding into "how do you handle…", never reveal it. Tag it `(from: finding)` for me only
- Their words (e.g. ICAAP, risk appetite), not ours. "Check our answers against yours", not "eval"
- 15 minutes, 7 questions at most: opening 2 min (1), walkthrough 8 min (3), value and trust 3 min (2), close 2 min (1)
- At most 1–2 data questions live; the rest go under "Later", asked if there's time or sent by email
- Ask each thing once. Write a one-line hypothesis per section so surprises stand out

## Template
**Opening**
- Where is the need for X coming from? Tell me about the most recent requests
- Who would use X day to day? Would the people asking use it themselves?
- Is anything making this more pressing right now? (don't name the deadline or rule first)

**Walkthrough**
- Walk me through the last time you did X: who, which tool, how long
  - Do these come up again and again, or are they mostly new?
  - Where does most of the time go? What data goes in, and from where?
  - What's the most painful part? → What do you check, and why?
  - At what point does <the risk> start to change a decision? Why there?

**Value and trust**
- What does this cost you today? Besides time, what else? When an answer was late or wrong, what did it hold up?
- If this got better, how would you know?
- What would need to be true for you to trust <the answer> without <the painful step>?
- Who else signs it off, and who could block it? When someone last challenged a number, what did you show them?

**Close**
- Recap in three points, biggest pain first. Anything I missed?
- I'll come back with something to review. Who else should be there?
- Can I email you short questions in between?
- Could you share a few past requests and the answers your team gave? We'd check ours against them

**Later**: the remaining data questions

## Per run
1. Quick research: the vendor's and customer's public material and the rules they answer to. For hypotheses and vocabulary only, never to pitch
2. Read the run's `RUN.md` and the questions from the data's initial review
3. Fill the template: X is the task; add their audiences, cadence, tools and regulator; add the 1–2 strongest data questions
4. Save it, then publish a new Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled `Run N: discovery questions (<customer>)`, with an empty `## Notes` section at the end. Link it in `RUN.md`
5. After the call, save the notes to `notes/interview.md` as they are, with the page link
