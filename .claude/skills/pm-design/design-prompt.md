# Design brief

For briefing an AI design tool (e.g. Claude with Figma) or a designer. Written before any screens; updated after each round of user testing. With the prototype, it becomes the spec.

## Brief
- **Role:** "You are a skilled UI/UX designer designing <the flow> for <product>"
- **Users:** who, how technical, what they already use. E.g. "risk analysts at banks: financially literate, not domain experts; live in Excel"
- **Target:** what they achieve in one session. E.g. "answer one committee question and get it approved in one sitting"
- **Success:** task completion, time, edits, review time
- **Grounding:** "Follow the design guide; only use terms from the glossary; flag gaps instead of filling them." Attach the guide, the glossary, product screenshots
- **Tone:** plain language, their terms
- **Shape:** e.g. guided steps with structured input; back bottom left, next bottom right
- **Trust:** what must be visible (method, sources, uncertainty, limits); what AI may and may not do

## Each step
| | |
|---|---|
| Input | what the user brings |
| Output | what the step produces |
| Happy path | a real example and what the system says back |
| Edge cases | too little input, partial match, wrong format, ambiguous, out of scope, leaves midway, with the exact message |
| Acceptance | testable: "every item matched or flagged; none silently dropped" |
| Hand-off | what passes to the next step |

## Example: upload a list
- Input: file with names and addresses → output: confirmed list
- Happy: clean file, 200 items → "Found 200, all matched. Ready to continue?"
- Edge: no addresses → "I need an address for each. Here's a template"; 12 ambiguous → "188 matched. 12 need a check: here they are"; wrong type → accepted formats; leaves midway → "Welcome back: you'd uploaded 200. Continue?"
- Acceptance: CSV and XLSX only, clear message otherwise; every item matched or flagged; progress saved after each upload
