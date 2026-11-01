---
name: discovery-interview
description: "Principles and a base template for customer discovery interview questions, customised for each run from its dataset and customer profile. Use when drafting, customising or reviewing discovery questions, preparing for a customer call or the live session, or deciding follow-ups during an interview."
---

# Discovery interview

The base template is `template.md` in this skill (source: the Discovery Question template in my Notion). It is generic. **Customise it for each run** using that run's `RUN.md` (customer profile, data notes) and its data-discovery Profile findings. Save the result as `runs/run-N/discovery-questions.md`. Never edit `template.md` for a single run, and never reuse another run's customised questions.

## Principles
1. **Problem, not solution.** Ask what happens and why it hurts. Do not pitch, suggest features or ask "would you like X?". If they describe a solution, ask what problem it would solve
2. **Go specific and map the workflow.** Anchor on the *last real time* they did the task. Get each step: who does it, with what tool, how long it takes, and what is handed to whom. Write the workflow down as you go
3. **Find the data.** For each step: what data goes in, where it comes from (system, vendor, spreadsheet, person), what format, how often, and what they do to it before use
4. **Find the most painful problems.** Listen for where the time goes, where errors and rework happen, and emotion ("I dread…", "every quarter we…"). Rank pains by frequency × severity × who feels it
   - Once it's clear something hurts and you've found the bottleneck, that's enough to prototype. **Don't add a separate "how does it land on you" question by default.** "What's the most painful part?" already does most of the work
   - Ask about personal impact only in two situations:
     - **They drop a cue** ("not a great look", "it queues on my desk"). That's an invitation: a quick "How's that been for you?" takes five seconds. Skipping a cue is the miss, not skipping the question
     - **You need urgency** (a real deal, not a short interview): "I'm worried a wrong number reaches the regulator" or "an analyst might leave" tells you whether they'll push it through IT and procurement or let it drift
5. **Push further on:**
   - general answers ("usually", "it depends") → "Tell me about the last time"
   - hedges ("roughly", "sort of", "should be fine") → "What's the part I'm missing?" Never relabel the answer in your own words and move on; the hidden step is usually behind the hedge
   - seemingly simple steps that take suspiciously long → "Walk me through that step. Where does the time go?"
   - the why behind the why: keep asking until you reach the root cause
6. **Measure potential ROI, always beyond time and cost.** Time saved alone undersells it. Cover all three parts, and get a number or a real example for each:
   - **Efficiency:** hours per cycle × people × cycles per year, consultant spend avoided
   - **Decision value:** which decisions the answer feeds (lending, pricing, risk appetite, investment) and what a late or wrong answer did to one. "When an answer was late or wrong, what decision did it hold up or change?"
   - **Risk and reputation:** a wrong figure reaching the regulator or the board, capital or provisioning impact, being seen as a blocker. "Besides time, what else does it cost you?"
   This matches how Climate X frames value: time saved, consultant cost avoided, better business decisions
7. **Have ideas on success criteria.** What would "this works" look like to them: a target metric, and what they would need to see to trust the output (the guardrail)
8. **Map who else is involved.** Who prepares, reviews, signs off, consumes and challenges the output. Who could block adoption. Who to bring into the next conversation
   - **Always ask "Who would actually use it?"** Separate the people asking the questions from the people who would use the thing asked for. If the askers wouldn't use it, the ask may not hold
9. **Close with clear next steps:**
   - Recap in **three points at most, leading with the biggest pain** (often a person or bottleneck), not with volume or stats. Then ask what was missed
   - Agree a prototype review with them and the other key stakeholders and users named in the call
   - Ask permission to send short ad-hoc questions in between, and how (email, Teams)
   - Ask for any data useful for evals and testing (sample outputs, past reports, real cases where they were challenged), and send it over

## Rules when writing questions
- **Non-leading.** Never reveal a data finding or hint at the answer. Turn a finding into a question about how they handle that situation ("How do you treat a property that secures more than one loan?", not "You're double counting properties")
- **Tag each data-informed question** with `(from: <finding>)` so the link to the analysis stays visible to me, not to the customer
- **Speak their language.** Use the customer's terms from the profile (e.g. ICAAP, risk appetite, LTV for a bank) and avoid ours (model, LLM, API, training, eval) unless they use them first. Say "check our answers against yours", not "eval"
- **Ask once.** Keep track of what has been answered and don't ask it again (e.g. volume). If an answer covered a later question, skip it
- **Time budget: about 15 minutes of live Q&A by default** (the rest of the session goes on synthesis, design and the prototype). Plan **7 questions at most**: Opening 2 min (1 question), Workflow 8 min (3), Value and trust 3 min (2), Close 2 min (1). Use sub-probes only when an answer is vague
- **Merge, don't add.** Fold baseline, guardrail and sign-off into combined questions. The baseline question must still reach beyond time: combine efficiency with decision value or risk in one question. Pick the 1–2 data-informed questions with the biggest effect on the answer for the live list
- **Everything else goes under "Later"**: asked only if time is left, otherwise sent by email after the call, using the permission asked for in the close

## How to customise for a run
1. Read the run's `RUN.md` (customer profile, data notes) and its Profile findings
2. Fill the template placeholders: `X` = the task the data feeds, `<the process>`, `<the climate risk>`, `<the answer>`, `<the painful step>`
3. Add role-specific angles from the profile: their audiences, cadence, tools, team, regulator
4. Add data-informed questions under the matching section, tagged `(from: finding)`
5. Fit the 15-minute budget: 7 live questions with minutes per section, the rest under "Later". Write a one-line hypothesis per section for what you expect to hear (so you notice surprises)
6. Save to `runs/run-N/discovery-questions.md`
7. **Publish to Notion**, where the note-taking assistant runs (see below)

## Publishing to Notion (every run)
- Create a new page under **2nd round prep** (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled `Run N: discovery questions (<customer name>)`
- Content: the run's `discovery-questions.md`, plus an empty `## Notes` section at the end for the call
- Record the page link in the run's `RUN.md` (**Notion questions:** line)
- If the questions change, update that run's page. Never edit the master Discovery Question template page, and never reuse another run's page
- After the call, save the notes back to the run's `notes/` folder as markdown, with the page link
