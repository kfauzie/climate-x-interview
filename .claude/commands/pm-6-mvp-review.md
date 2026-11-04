---
name: pm-6-mvp-review
description: "Generate quick follow-up questions to confirm the working version solves the customer's problem: checks on the assumptions and on data scenarios it must handle. Use before showing the working version to the customer."
---

# MVP review

The goal is to confirm the solution works for the customer, not to sell it.

Before starting, read climate-x-products, climate-x-company and climate-x-role. Use the solution concept (problem, workflow, assumptions) and the working version.

## Generate the questions
Three questions, plus one optional, in this order. Each specific to this case.

1. **Does it solve the problem?** Whether the team could have used it for their last real request (one request, not all of them), e.g. "Could your team have used this for the last question you got?"
2. **Trust and sign-off.** What the approver needs before an answer goes out, e.g. "What would you need to see before you'd approve an answer from this and send it out?"
3. **Real examples for testing.** "Could you send us a sample of recent [requests], with the answers your team sent? We'd use them to test it."
4. **Defaults (optional, last).** Whether the choices it made for them are the ones their team would make, marked *(Optional)*, naming each default, not a list of categories, e.g. "By default, it counts mortgages and CRE together, leaves out loans in default, redeemed or maturing before 2030, and holds balances at today's level. Would your team use the same defaults?"

Only add another question for an assumption if it would change the main workflow.

## Check the sample yourself, don't ask
When the sample arrives, test it against the working version and check:
- Which requests it can't answer, and which hit gaps in the data
- Whether the sample covers enough cases (different askers, scenarios, years, loan groups). If not, ask for more

## Rules
- Open questions, with no hint of the answer you expect
- Plain language, in the customer's own terms. Follow "Writing anything the customer sees" in climate-x-role: name the exact thing, no shorthand from our notes, explain only what's new to them
- Only ask what could change the solution
- Short and easy to follow on first hearing: one idea per question
- No overlap: value, method and sign-off questions easily ask the same thing. Keep one question per area and merge the rest

## Save
Publish the questions as a Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled "Run N: MVP review (customer)", with an empty Notes section at the end. Always give me the link to the new page, and add it to `RUN.md`.
