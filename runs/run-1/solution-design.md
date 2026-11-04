# Run 1: solution design

A report builder with Sarah's defaults, a method note it writes itself, her approval and a drafted reply. No AI in this version. Medium fidelity; numbers from the practice data and synthetic loan book. Source: `design/solution-design.html`.

## Walkthrough
- **Analyst:** I've just received an email from the credit committee: "How many CRE loans have a flood rating of E or worse by 2050?" I paste it in and pick who asked. The scenario, year and exclusions are already set to Sarah's standard, and the answer is there: 3 loans, £5.4m. I check the loans behind it, try severe to see if it matters, add a note and send the draft to Sarah
- **Sarah:** a draft is waiting. I read the question and the answer, glance at the loans and the method, and approve. If something's off, I change it or send it back with a comment
- **Analyst:** it's approved. The reply and the file are drafted; I read it and send

## Flow
| Step | Who | Screen | Ends in |
|---|---|---|---|
| 1 | Analyst | Draft | Send draft to Sarah |
| 2 | Sarah | Review the draft | Approve, or send back |
| 3 | Analyst | Send the answer | Send |

Askers (CRO, committees, pricing, treasury, IR) never touch it: they email the question and get the reply.

## 1. Draft
![Draft](design/draft.png)

- **Removes:** choosing scenario, horizon and loans by hand, the write-up, and "what about severe?" restarting it
- **Inputs:** question, asked by and data. Scenario, horizon and exclusions start on Sarah's standard for that asker, so the analyst only confirms; the horizon follows the question. Note to Sarah is optional
- **Edge cases, said where they happen:**
  - No year in the question → horizon starts on the asker's default, marked "Default"
  - A year not in the data ("present-day") → "This data has 2030 and 2050. Use 2030?"
  - Horizon or data doesn't match the question → shown on this screen, so the analyst fixes it before Sarah sees it
  - Nothing matches → "0 loans" with the controls still visible to widen it
  - Loss to the bank → "Can't calculate loss to the bank from this data. Show damage to properties instead?"
- **Ends in:** Send draft to Sarah. The number updates as the controls change

## 2. Review the draft
![Review](design/review.png)

- **Removes:** half a day of checking someone else's numbers
- **Inputs:** scenario, year and leave-out can be changed; a comment is required to send back
- **Ends in:** Approve, or Send back to the analyst with the comment. Nothing goes out without her approval

## 3. Send the answer
![Send](design/send.png)

- **Removes:** writing the reply and building the Excel by hand
- **Inputs:** the drafted reply, editable
- **Ends in:** Send. Logged with who asked, built and approved, the data dates and the version

## Test set
| Case | Expected |
|---|---|
| Credit committee: CRE, flood E or worse, 2050, central | 3 of 144 loans, £5.4m of £351.8m · severe 5 loans, £9.6m |
| CRO: total by 2050, by hazard and region | £3.31m central, £6.10m severe · subsidence and South East top under both |
| Mortgage pricing: 2024–25 lending, subsidence E to G | £52.3m, 24.3% of new lending vs 8.6% older · origination-source check flagged |
| Treasury: rise 2030 → 2050, severe | 2.74× (1.57× central) |
| Sent-back draft rebuilt (2030, redeemed loans included) | Analyst warned on Draft before sending: wrong year, stale data · 4 of 145, £6.2m vs 3 of 144, £5.4m when fixed |
| "Loss to the bank" | Refused with the reason |

The CRO, pricing and treasury figures are from the Spectra file alone; recompute them with the default exclusions when the prototype is rebuilt.

## Tested briefly
- **Main flow,** walked once as the analyst and as Sarah: each screen is one step; nothing asks for something the user doesn't have
- **Draft screen edge cases, checked against the engine:** no year in the question (falls back to 2050, 3 loans) · zero result (wind G at 2030: 0 of 144, £0) · years in the data (2030 and 2050 only)
- **Personas on the Draft screen:** a new analyst (does "Default" make clear it can be changed? likely yes, it sits beside the toggle) · Sarah (would she trust 3 loans without the full write-up on screen? test with her)
- **With real users later:** time from question to draft for an analyst; whether Sarah approves without opening Excel
