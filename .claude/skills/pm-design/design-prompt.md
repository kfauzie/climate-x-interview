# Design prompt (how to brief a design)

Use this to brief an AI design tool (e.g. Claude with a Figma connection) or a designer. Write it before generating any screens; update it after every round of user testing. With the prototype, it becomes the spec.

## Structure
- **Role:** "You are a skilled UI/UX designer designing <the flow> for <product>"
- **Users:** who they are, how technical, what they already know and use. E.g. "risk analysts at banks: financially literate, not necessarily experts in <domain>; they live in Excel"
- **Target outcome:** what a user must achieve in one session. E.g. "Answer one committee question and have it approved in one sitting"
- **Success measures:** task completion, time, manual edits, review time (from `SKILL.md` §2)
- **Grounding:** "Follow the design guide and only use terms and metrics from the glossary; **flag gaps instead of filling them**." Attach the design guide (components, colours, type), the glossary, and real product screenshots
- **Tone:** plain language; no jargon without explanation; the user's own terms
- **Shape:** e.g. "a guided, step-by-step flow with structured input", with consistent action placement
- **Trust requirements:** what must be visible (method, sources, uncertainty, limitations), what AI may and may not do
- **Steps:** for each step, the fields below, with a worked example

## Each step
| Field | What to write |
|---|---|
| Input | What the user brings or enters |
| Output | What the step produces and hands on |
| Happy path | A real example: what the user does and what the system says back |
| Edge cases | Insufficient input, partial match, wrong format, ambiguity, out of scope, user leaves midway, with the exact message shown |
| Acceptance criteria | Testable statements ("every item ends up either accepted or flagged; none silently dropped") |
| Hand-off | What passes to the next step |

## Worked example (a generic upload step)
- **Input:** a file of items with names and addresses
- **Output:** a confirmed list
- **Happy path:** user uploads a clean file of 200 items → "Found 200, all matched. Ready to continue?"
- **Edge cases:** no addresses → "I need an address for each item. Here's a template"; 12 ambiguous → "188 matched. 12 need a check: here they are"; wrong file type → list accepted formats; user leaves midway → progress saved, "Welcome back: you'd uploaded 200. Continue?"
- **Acceptance criteria:** accepts CSV and XLSX and rejects others with a clear message; every item is matched or flagged, none silently dropped; progress is saved after each upload
- **Hand-off:** confirmed list → next step
