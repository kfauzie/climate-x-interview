---
name: pm-discovery-interview
description: "My approach to customer discovery interviews: principles, follow-up triggers, a 15-minute question plan and the base question template, customised per run from the customer profile and data findings. Use when preparing, running or reviewing a discovery call."
---

# Discovery interview

Users tend to describe solutions; my job is to find the problem behind them.

Output: `runs/run-N/discovery-questions.md` (the template below, customised), published to Notion.

## Principles
- **Problem, not solution:** no pitching, no "would you like X?". If they describe a solution, ask what it would let them do
- **Last real time:** anchor on a specific recent example. Each step: who, which tool, how long, handed to whom
- **Follow the data:** what goes in at each step, from where, in what shape, what they do to it first
- **Find the bottleneck:** where time goes, where errors and rework happen. Rank by frequency × severity × who feels it
  - Once it's clear it hurts, that's enough. "How's that been for you?" only on a cue ("it queues on my desk") or when I need urgency for a deal
- **Who uses it vs who asks:** always ask who'd use it day to day. If the askers wouldn't, the ask may not hold
- **ROI beyond time:** efficiency (hours, people, consultants) + decision value (what a late or wrong answer held up) + risk (a wrong number reaching the board or regulator)
- **Success and guardrail:** how they'd know it works; what must be true to trust it; who signs off, who could block
- **Why now:** "Is anything making this more pressing?" Don't name the deadline or rule first
- **Close:** recap in 3 points, biggest pain first → agree a review with the people they named → ask to email follow-ups → ask for real examples with their answers

## Follow-up triggers
- "usually", "it depends" → "Tell me about the last time"
- "roughly", "sort of" → "What's the part I'm missing?" Don't relabel it and move on
- Simple step, suspiciously long → "Walk me through that step"
- Feature request → "What would that let you do that you can't today?"
- Why behind the why: "No time" → "not a priority" → the real reason

## Writing the questions
- Non-leading: turn a data finding into "how do you handle…", never reveal it. Tag `(from: finding)` for me only
- Their words (e.g. ICAAP, risk appetite), not ours. "Check our answers against yours", not "eval"
- 15 min, 7 questions max: opening 2 min (1), walkthrough 8 min (3), value and trust 3 min (2), close 2 min (1)
- Merge, don't add. 1–2 data questions live; the rest under "Later" (ask if time, else email)
- Ask once; one-line hypothesis per section so surprises stand out

## Template
**Opening**
- Where is the need for X coming from? Tell me about the most recent requests
- Who would actually use X day to day? Would the people asking use it themselves?
- If not clear: Is anything making this more pressing right now?

**Walkthrough**
- Walk me through the last time you did X. Each step: who, which tool, how long
  - Do these come up again and again, or are they mostly new?
  - Where does most of the time go? What data goes in, from where?
  - What's the most painful part? → What do you check, and why?
  - At what point does <the risk> start to change a decision? Why there?

**Value and trust**
- How much does this cost you today? Besides time, what else? When an answer was late or wrong, what did it hold up?
- If this got better, how would you know?
- What would need to be true to trust <the answer> without <the painful step>?
- Who else signs it off, who could block it? When someone last challenged a number, what did you show them?

**Close**
- Recap, 3 points, biggest pain first. Anything I missed?
- I'll come back with something to review. Who else should be there?
- Can I email short questions in between?
- Could you share a few past requests and your team's answers? We'd check ours against yours

**Later** (if time, else email): the remaining data questions

## Per run
1. Quick research: vendor's and customer's public material, the rules they answer to. For hypotheses and vocabulary only
2. Read `RUN.md` and the Profile findings
3. Fill the template: X = the task; add their audiences, cadence, tools, regulator; add the 1–2 strongest data questions
4. Save; publish a new Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), `Run N: discovery questions (<customer>)`, empty `## Notes` at the end; link it in `RUN.md`
5. After the call: notes → `notes/interview.md`, as is, with the page link
