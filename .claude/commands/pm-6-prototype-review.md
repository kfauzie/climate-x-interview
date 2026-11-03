---
name: pm-6-prototype-review
description: "Run a prototype review with the customer and their gatekeepers: what to test, a 15-minute script built on the customer's own example, questions, what to measure, and the per-run review page. Use before showing a prototype, or when turning review feedback into the next design round."
---

# Prototype review

Not to sell it. To learn whether it solves the problem for the people who'd use and approve it.

Inputs (active run): `RUN.md`, `solution-concept.md` (the riskiest assumption), `solution-detail.md`, `visual-design.md`, `clickable-prototype.md`, `notes/`, the prototype. Output: `runs/run-N/prototype-review.md`, published to Notion.

## What I'm testing, in order
1. Problem fit: does it remove the pain, in their workflow?
2. Trust: would the owner and the gatekeepers sign off an answer from it?
3. Adoption: who would use it, how often, and what they'd stop doing
4. The riskiest assumption: confirmed, refuted or still open

Invite the decision owner, a day-to-day user, and the gatekeeper behind the riskiest assumption. Ask who else should come; they often name the real blocker.

## 15 minutes
1. **Recap** (1–2 min): their words, biggest pain first. "Have I got that right?"
2. **Walkthrough** (4–5 min): one of their own examples, end to end
3. **Hands on** (3 min): they try a second example and think aloud. I don't help unless they're stuck
4. **Questions** (4–5 min): 5–6 at most, fit and trust first
5. **Next steps** (1–2 min): what a pilot would need, with whom, on what data

## Script
- Start from their problem: "Last time you said… so we built something to test one idea"
- One line on what it does and doesn't do, and what data it runs on (say if it's synthetic)
- Use their example, their terms and their defaults
- Tie each moment to a pain: "this is the check you said takes half a day"
- Show a failure being caught on purpose. It builds more trust than a perfect run
- Say plainly where AI is used: "it reads the question; every number is calculated from the file"
- Pause after each key moment and let them react

## Questions
- Fit: "If this had existed last time, what would have been different?"
- Trust: "Would you sign off from this screen? What would you need first?" To the gatekeeper: "What would you need to approve this?"
- Adoption: "Who would use it, for what? What would you stop doing?"
- Gaps: "What would stop you using it?" Then: must-have or nice-to-have?
- Value: "How would you know in three months that it was worth it?"
- Next: "What would a pilot need for you to say yes? Who has to agree?"
- Follow-ups: "What makes you say that?" "What did you expect to happen?"

## Watch, don't just listen
- During hands-on: did they finish unaided, how long did it take, where did they hesitate or misread, what would they change before sending?
- In later rounds, compare options on completion and speed, not on which they say they prefer
- Don't defend. A criticism is data: ask why and write it down
- No jargon, no promises ("let me take that back")

## Per run
1. Write `prototype-review.md`: who's coming, prototype link, data used, riskiest assumption, the recap line, a walkthrough table (what I show, what I say, the pain it addresses; one row is a failure being caught), the AI line, the hands-on example, the questions with my hypotheses, the pilot I'll propose, and a `## Notes` section
2. Publish it as a new Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled `Run N: prototype review (<customer>)`. Link it in `RUN.md`
3. After the review: save the notes to `notes/prototype-review-notes.md` as they are; log a feedback round in `clickable-prototype.md` and update the file each change belongs to; update the riskiest assumption in `solution-concept.md`
