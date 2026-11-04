---
name: pm-3-problem-to-solution-concept
description: "Turn the discovery notes and data findings into a solution concept: the problem, two or three different solution ideas, and the recommended solution with its end-to-end workflow. Use after the discovery interview, before solution design."
---

# Problem to solution concept

Start from the problem, not the feature request. Recommend the simplest thing that solves it.

## Inputs
- Read climate-x-products, climate-x-company and climate-x-role for background.
- The interview notes: the Notes section of the Notion page "Run N: discovery questions (customer)" under 2nd round prep. Quote from it.
- Any answers from pm-1-data-discovery. Don't re-analyse the data.

## Output
Save to runs/run-N/solution-concept.md and publish it as a Notion page under 2nd round prep, titled "Run N: solution concept (customer)". Show it in chat first. It will be shared on screen, so keep it short.

## 1. The problem
- **What they asked for**, in their words
- **The real problem**, based on the interview notes: [user] needs to [job] but today [workaround], which causes [impact]. Quote their words where possible.
- **Evidence:** 3–5 bullets, each a quote from the interview notes or a number calculated from the data, saying where it came from
- **Impact:** one line per person affected (time, waiting, rework, risk to decisions). Mark estimates

## 2. Solution ideas
Two or three ideas that are genuinely different from each other. For each:
- What it is, in one line
- How it solves the problem
- User experience: how it fits their day
- Implementation effort: rough size

## 3. The recommended solution
- **Recommendation:** which idea and why, in one sentence. Compared with the original ask: what it covers, what it doesn't, and what's for later.
- **Workflow, end to end:** bullets in the form "[who] does [what] with [what]", from the moment the request arrives to the answer being sent, including steps outside the product. For example:
  - The CRO emails the climate risk team a question.
  - The analyst pastes the question into the product.
  - The product suggests the scenario, year and loans; the analyst confirms.
  - ...
  Use a real request from the interview notes if available, with real numbers calculated from the data.
- **AI vs code vs human:** decide who does each step based on what each does best. AI for flexibility (messy input, free text, interpretation), code for fixed logic (every number, rules, checks), and people for judgement and approval. Keep people in control: what AI and code should be visible and editable, and a person checks before anything goes out.
- **Success criteria:** how we'll know it works: a target, what mustn't get worse, what the people who approve it need to see, and test cases with known answers
- **Assumptions:** any belief that, if wrong, would make the solution fail

## Rules
- No claim without evidence: a quote or a calculated number
- Say how, not that: never "seamless" or "met by design"
- Plain words a stranger could follow
