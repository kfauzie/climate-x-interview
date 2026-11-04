# Run 1: solution design

A report builder with Sarah's defaults, a method note it writes itself, her approval and a drafted reply. No AI in this version. Medium fidelity; numbers from the practice data and synthetic loan book. Source: `design/solution-design.html`.

## Walkthrough
One question all the way through: "For the stress test, how many CRE loans have a flood rating of E or worse?"
- **Analyst:** the stress-test team emails the question. I paste it in. It's read as CRE loans, flood E or worse; Sarah's stress-test standard fills in central and severe, 2030 and 2050. I see all four answers at once and the loans behind the worst case. The stress test covers the whole book, so I include loans maturing before 2030, give my reason, add a note and send the draft to Sarah
- **Sarah:** a draft is waiting. What needs my attention comes first: the analyst changed my standard, and with it severe 2050 is 8 loans rather than 5. I check the table and approve
- **Analyst:** it's approved. The reply with the table and the file are drafted; I send it

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
- **Inputs:** the question, typed loosely; AI reads it into choices, highlights the words it used and fills the rest from Sarah's defaults. AI never produces a number. Real example questions to start from. Asked by, with "+ Add person". Data: refresh the Spectra export, or upload a new loan book
- **Choices:** scenario, horizon, exclusions (common ones, or typed and read by AI) and method. Each shows its source; a change from Sarah's defaults is flagged for her
- **Not counted, in plain words, linked to the list:** loans in the Spectra export but not in the loan book; loans with no rating for that hazard and year
- **Edge cases:** warnings in red, where they happen: year doesn't match the question, stale data, a year not in the data, nothing matches, loss to the bank (refused, with the closest alternative)
- **Ends in:** Send draft to Sarah

## 2. Review the draft
![Review](design/review.png)

- **Removes:** half a day of checking someone else's numbers
- **Looks different from the draft:** addressed to Sarah, with what needs her attention first: changes from her standard (with their effect on the answer), flags and the analyst's note
- **More than one scenario or year:** one answer with a small table (central and severe × 2030 and 2050), reviewed once and sent as one email
- **Inputs:** a comment, required to send back
- **Ends in:** Approve, or Send back. Nothing goes out without her approval

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
