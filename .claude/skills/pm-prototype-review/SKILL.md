---
name: pm-prototype-review
description: "Prepares and runs a prototype review with the customer and their stakeholders: a short script that explains the product through the customer's own example, non-leading questions that test the problem fit, trust, adoption and the riskiest assumption, how to capture feedback, and a per-run review page in Notion. Use after a prototype is built, when preparing a demo or review session, or when turning review feedback into the next design round."
---

# Prototype review

Inputs, all from the **active run** (see CLAUDE.md run rules): `RUN.md` (customer, ask, problem statement), `solution.md` (the pick, success criteria, riskiest assumption), `design.md` (flow, screens, test set), the customer's follow-up material in `notes/`, and the prototype or its clickable demo.

Output: `runs/run-N/prototype-review.md` from **`template.md` in this skill**, published to a new Notion page (see below). Never edit `template.md` for a single run, and never reuse another run's review.

## What a review is for
Not to sell the prototype: to learn whether it solves the problem, for the people who would use and approve it. Four things to find out, in order of importance:
1. **Problem fit:** does it remove the pain they described, in their own workflow?
2. **Trust:** would the approver and the gatekeepers sign off an answer from it? What's missing?
3. **Adoption:** who would use it day to day, how often, and what would they stop doing?
4. **The riskiest assumption** from `solution.md`: confirmed, refuted or still open

## Who should be there
- The decision owner, a day-to-day user, and the gatekeeper whose condition is the riskiest assumption (e.g. model risk, compliance, IT). Ask the customer who else should see it; they often name the real blocker

## Time budget (about 15 minutes by default)
| Part | Time | What happens |
|---|---|---|
| 1. Recap the problem | 1–2 min | Their words, biggest pain first. "Have I got that right?" |
| 2. Walkthrough | 4–5 min | One of **their own** examples, end to end. Narrate what they'd do, not how it's built |
| 3. Hands on (if possible) | 3 min | They drive with a second example while thinking aloud. Don't help unless stuck |
| 4. Questions | 4–5 min | 5–6 questions max, problem fit and trust first |
| 5. Next steps | 1–2 min | What would make them pilot it, with whom, on what data |

## The script (how to explain the product)
- **Start from their problem, not the product.** "Last time you said … So we built something to test one idea: …"
- **One sentence on what it is and isn't.** What it does, what it deliberately doesn't do yet (and why), what data it runs on (say plainly if it's practice or synthetic)
- **Use their example and their words.** Their real question, their terms (metrics, audiences, regulator), their defaults
- **Show the moments that map to their pain,** and say which pain each one addresses ("this is the check you said takes half a day")
- **Show a failure on purpose.** A case they described that went wrong, and how the prototype catches it. Builds more trust than a perfect run
- **Say where AI is and isn't used,** in their language ("the system reads the question; every number is calculated from the file, and you see how")
- **Stop talking and let them react.** Pause after each key moment

## Questions (non-leading, behaviour-focused)
- **Problem fit:** "If this had existed last time, what would have happened differently?" "Where would this fit in your week?"
- **Trust:** "Would you sign off this answer from this screen? What would you need to see first?" To the gatekeeper: "What would you need to approve something like this?"
- **Adoption:** "Who on your team would use this, and for what?" "What would you stop doing?"
- **Gaps:** "What's missing that would stop you using it?" "Where would this break for you?"
- **Value:** "How would you know in three months that it was worth it?" (beyond time: decisions, risk)
- **Next step:** "What would a pilot need to look like for you to say yes? Who has to agree?"
- Follow-ups: "What makes you say that?", "Tell me more about…", "What would you expect to happen here?"

## Rules
- **Don't defend or explain away.** When they criticise, ask why and write it down. A criticism is data
- **Watch, don't only listen.** Note where they hesitate, misread a screen or ask "what does this mean?": those are design findings
- **Separate "nice to have" from "won't use it without".** Ask which one each request is
- **No jargon:** say "check our answers against yours", not "eval"; "calculated from the file", not "deterministic"
- **Don't promise dates or features.** "Let me take that back" is enough
- **Ask permission for follow-ups and for test data** (sample questions with their own answers, no real data until signed)

## After the review
- Save the notes to `runs/run-N/notes/prototype-review-notes.md` (from Notion, as is, with the page link)
- Record a **feedback round** in the run's `design.md` (what was said, by whom, status) and update the riskiest assumption in `solution.md`
- Fold any general lesson into this skill or `pm-design`

## Publishing to Notion (every run)
- New page under **2nd round prep** (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled `Run N: prototype review (<customer>)`
- Content: the run's `prototype-review.md`, plus an empty `## Notes` section at the end for the note-taking assistant
- Record the page link in the run's `RUN.md` (**Notion review:** line). Never reuse another run's page
