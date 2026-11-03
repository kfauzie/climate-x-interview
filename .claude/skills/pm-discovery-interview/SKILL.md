---
name: pm-discovery-interview
description: "My approach to customer discovery interviews: principles, a 15-minute question plan, follow-up triggers, and a base template customised per run from the customer profile and data findings. Use when preparing, running or reviewing a discovery call."
---

# Discovery interview

Users tend to describe solutions; my job is to find the problem behind them.

Output: `runs/run-N/discovery-questions.md` from `template.md`, published to Notion. Never edit the template for one run.

## Principles
- **Problem, not solution:** no pitching, no "would you like X?". If they describe a solution, ask what it would let them do
- **Last real time:** anchor on a specific recent example. Each step: who, which tool, how long, handed to whom
- **Follow the data:** what goes in at each step, from where, in what shape, and what they do to it first
- **Find the bottleneck:** where time goes, where errors and rework happen. Rank by frequency × severity × who feels it
  - Once it's clear it hurts, that's enough. Ask "How's that been for you?" only on a cue ("it queues on my desk"), or when you need urgency for a deal
- **Who uses it vs who asks:** always ask who would use it day to day. If the askers wouldn't, the ask may not hold
- **ROI beyond time:** efficiency (hours, people, consultants) + decision value (what a late or wrong answer held up) + risk (a wrong number reaching the board or regulator)
- **Success and guardrail:** how they'd know it works; what must be true to trust it; who signs off, who could block
- **Why now:** "Is anything making this more pressing?" Don't name the deadline or rule first
- **Close:** recap in 3 points, biggest pain first → agree a review with the people they named → ask to email follow-ups → ask for real examples with their answers (for testing)

## Follow-up triggers
- "usually", "it depends" → "Tell me about the last time"
- "roughly", "sort of" → "What's the part I'm missing?" Don't relabel it and move on
- Simple step, suspiciously long → "Walk me through that step"
- Feature request → "What would that let you do that you can't today?"
- Why behind the why: "No time" → "not a priority" → the real reason

## Writing the questions
- Non-leading: turn a data finding into "how do you handle…", never reveal it. Tag `(from: finding)` for me only
- Their words (e.g. ICAAP, risk appetite), not ours (model, eval). "Check our answers against yours", not "eval"
- 15 min, 7 questions max: opening 2 min (1), workflow 8 min (3), value and trust 3 min (2), close 2 min (1)
- Merge, don't add. Max 1–2 data questions live; the rest under "Later" (ask if time, else email)
- Ask once: track what's been answered
- One-line hypothesis per section, so surprises stand out

## Per run
1. Quick research: the vendor's and customer's public material, the rules they answer to. For hypotheses and vocabulary only; never pitch it
2. Read `RUN.md` and the Profile findings
3. Fill the template: X = the task, plus the customer's audiences, cadence, tools, regulator
4. Add the 1–2 strongest data questions; fit the 15-minute plan
5. Save, then publish: new Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), `Run N: discovery questions (<customer>)`, with an empty `## Notes` at the end. Link it in `RUN.md`
6. After the call: notes → `notes/interview.md`, as is, with the page link
