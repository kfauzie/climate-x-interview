# Run N: design for <the recommended solution>

<!-- Copy to runs/run-N/design.md. Fill each section in order and get agreement before moving on: flow → screens → test set → prototype. Delete these comments. -->

From `solution.md`, `notes/…` and any follow-up material the customer sent. Status: **<flow drafted / flow agreed / screens agreed / prototype built>**

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

## Brand and look
- **Colours and fonts:** <values, and where they came from (site CSS, brand guide, the person)>
- **Product look and feel:** <conventions from real product screenshots>

## Feedback rounds
### Round 1 (<who>, <date>)
1. <what was said>
- Status: <recorded / implemented>; fixes found while testing: …

## Open items
- …
