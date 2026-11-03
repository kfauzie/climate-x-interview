# Run N: design for <the recommended solution>

<!-- Copy to runs/run-N/design.md. Fill each section in order and get agreement before moving on: flow → screens → test set → prototype. Delete these comments. -->

From `solution.md`, `notes/…` and any follow-up material the customer sent. Status: **<flow drafted / flow agreed / screens agreed / prototype built>**

## What's worth building
- **The pain it removes** (customer's words): …
- **The one job it does:** …
- **What it deliberately doesn't do (and why):** …
- **Where this could go** (one line): … **The slice we build now:** …

## Success, defined before designing
- **Users:** <role, how technical, how often>
- **Measures:** <task completion, time to a usable answer, manual edits, review time, override rate>, with targets to agree
- **Guardrail:** <what must stay true for them to trust it>
- **Where it breaks today:** <the step where time goes or errors happen>

## Who does what
- **Asker:** <who brings the question or need; do they use the tool?>
- **User:** <who works in the tool day to day>
- **Approver / owner:** <who signs off, and whose defaults or rules apply>
- **Gatekeepers:** <model risk, IT, procurement, audit, regulator: what each needs to see>

## User flow
```
<step> → <step> → <step> → …
```
1. **<Step>** (<who>): <what happens; what is computed vs interpreted vs decided by a person>
2. …

## Decisions
<!-- Each with a recommendation; record the answer. -->
1. <Decision>: **<agreed answer>**
2. …

## Design brief
<!-- From pm-design/design-prompt.md: role, users, target outcome, grounding (design guide, glossary, product screenshots; flag gaps), tone, trust requirements, steps. -->

## Screens
<!-- One block per screen. Use the customer's real examples for happy paths and a real failure they described for edge cases. -->
### Screen 1 · <name> (step <n>)
- **Input:** …
- **Output:** …
- **Happy path:** <a real example from the customer, with the expected result>
- **Edge cases:** …
- **Acceptance criteria:** …

## Test set
<!-- Expected answers computed by code on the run's data, never by hand. Include at least one real failure case and one out-of-scope case. -->
| Case | Expected |
|---|---|
| <customer example 1> | <computed answer> |
| <real failure the customer described> | <what must be flagged or blocked> |
| <out-of-scope request> | <refused, with the reason> |

## Limitations shown in the product
- <what the product says it won't do, where it says it, and why>

## Design review checklist
<!-- Run pm-design §7 against the running prototype; note any item that fails and what was done. -->

## Brand and look
- **Colours and fonts:** <values, and where they came from (site CSS, brand guide, the person)>
- **Product look and feel:** <conventions from real product screenshots>

## Feedback rounds
### Round 1 (<who>, <date>)
1. <what was said>
- Status: <recorded / implemented>; fixes found while testing: …

## Open items
- …
