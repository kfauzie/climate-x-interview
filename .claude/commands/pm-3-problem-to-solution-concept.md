---
name: pm-3-problem-to-solution-concept
description: "Turn the discovery notes and data findings into a solution concept: the problem, two or three different solution ideas, and the recommended solution with its end-to-end workflow. Use after the discovery interview, before solution design."
---

# Problem to solution concept

Start from the problem. Recommend the simplest thing that solves it.

## Inputs
- Read climate-x-products, climate-x-company and climate-x-role for background. Follow the communication guide in climate-x-role for everything you write.
- The interview notes: the Notes section of the Notion page "Run N: discovery questions (customer)" under 2nd round prep. Quote from the transcript, not the AI summary, which can get details wrong.
- Any answers from pm-1-data-discovery. Don't re-analyse the data.

## Output
Publish it as a Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled "Run N: solution concept (customer)". Give me the link (no summary in chat) and add it to `RUN.md`. It will be shared on screen, so keep it short.

## 0. Check for gaps first
Before writing anything, check the notes for gaps big enough to change which idea is recommended or the main workflow (e.g. who the user is, what the job is). Only then, show me the questions for the customer and wait. Detail choices (defaults, settings, methodology options) don't stop the work: make a sensible assumption, state it, and move on. It's a first prototype.

## 1. The problem
- **What they asked for**, in their words
- **The real problem**, based on the interview notes: [user] needs to [job] but today [workaround], which causes [impact]. Quote their words where possible.
- **Evidence:** 3–5 bullets, each a quote from the interview notes or a number calculated from the data, saying where it came from
- **Impact:** one line per person affected (time, waiting, rework, risk to decisions). Mark estimates

## 2. Solution ideas
Two or three ideas that are genuinely different from each other. For each:
- What it is, in one line
- **User:** does it solve the problem? How much of the pain does it remove (all, most, or a little)? Does it lead to a better commercial decision (where to invest, lend or adapt)? How does it fit their day?
- **Commercial:** does it fit Climate X's product strategy? Likely return: can we charge more, or does it help retention and renewal?
- **Effort:** rough size across engineering (how much to build), science (any new models needed), data (e.g. asset data to collect), and rollout (e.g. onboarding).

Mark user and commercial points as judgements unless backed by a quote or number.

## 3. The recommended solution
- **Recommendation:** which idea and why, in one or two sentences, weighing user, commercial and effort from section 2 and naming which tipped it. Compared with the original ask: what it covers, what it doesn't, and what's for later.
- **Workflow, end to end:** bullets in the form "[who] does [what] with [what]", from the moment the request arrives to the answer being sent, including steps outside the product. For example:
  - The CRO emails the climate risk team a question.
  - The analyst pastes the question into the product.
  - The product suggests the scenario, year and loans; the analyst confirms.
  - ...
  Use a real request from the interview notes if available, with real numbers calculated from the data. Show it handles the range of requests and follow-ups, not just the example or the defaults. Every input has a reason: it changes the answer, or it's needed to send it.
- **What AI, code and people do:** decide who does each step based on what each does best. AI for flexibility (messy input, free text, interpretation), code for fixed logic (every number, rules, checks), and people for judgement and approval. Keep people in control: what AI and code do is visible and editable, and a person checks before anything goes out.
- **Success criteria:** how we'll know it works: a target, what mustn't get worse, the time or consultant cost it saves, what the people who approve it need to see, and test cases with known answers
- **Assumptions:** any belief that, if wrong, would make the solution fail, each written as a question to ask in the MVP review

## Rules
- No claim without evidence: a quote or a calculated number
- For money decisions today (cost, payback), use the nearest year in the data, and show how it changes later; a far-off year alone suggests the problem can wait
- Only ask the customer what could change which idea or the main workflow. Everything else is a stated assumption.
- Say how, not that: never "seamless" or "met by design"
