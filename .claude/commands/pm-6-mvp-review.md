---
name: pm-6-mvp-review
description: "Generate quick follow-up questions to confirm the working version solves the customer's problem: checks on the assumptions and on data scenarios it must handle. Use before showing the working version to the customer."
---

# MVP review

The goal is to confirm the solution works for the customer, not to sell it.

Before starting, read climate-x-products, climate-x-company and climate-x-role. Follow the communication guide in climate-x-role for everything you write. Use the solution concept (problem, workflow, assumptions), from the Notion page linked in `RUN.md`, fetched fresh every time, and the working version.

## Plan the evaluation first
Before writing question 3, work out what the AI part needs to be tested on:
- What the AI does (from the solution concept), e.g. reading a question and suggesting choices
- What "right" looks like for each output, e.g. the choices a team member would have made
- Which cases matter most: common requests, tricky wording, and ones it should refuse or flag
- How many examples are needed to trust it, roughly

Then ask for exactly that.

## Generate the questions
Three questions, plus one optional, in this order. Each specific to this case.

1. **Does it solve the problem?** Whether the team could have used it for their last real request (one request, not all of them), e.g. "Could your team have used this for the last question you got?"
2. **Trust and sign-off.** What the approver needs before an answer goes out, e.g. "What would you need to see before you'd approve an answer from this and send it out?"
3. **Real examples for testing.** Ask for the sample the evaluation needs, in their terms, naming the tricky cases specifically, e.g. "Could you send us 20 or so recent [requests], with the answers your team sent? Please include a few unusual ones, like a scenario or year you rarely use, or ones where the right answer wasn't obvious and your team had to make a judgement call. We'd use them to test it."
4. **Defaults (optional, last).** Whether the choices it made for them are the ones their team would make, marked *(Optional)*, naming each default, not a list of categories, e.g. "By default, it [does A], [leaves out B] and [assumes C]. Would your team use the same defaults?"

Only add another question for an assumption if it would change the main workflow.

## Check the sample yourself, don't ask
When the sample arrives, test it against the working version and check:
- Which requests it can't answer, and which hit gaps in the data
- Whether the sample covers enough cases (e.g. different askers, scenarios, years, segments). If not, ask for more

## Rules
- Open questions, with no hint of the answer you expect
- In the customer's own terms
- Only ask what could change the solution
- Short and easy to follow on first hearing: one idea per question
- No overlap: value, method and sign-off questions easily ask the same thing. Keep one question per area and merge the rest

## Save
Publish the questions as a Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled "Run N: MVP review (customer)", with an empty Notes section at the end. Always give me the link to the new page, and add it to `RUN.md`.
