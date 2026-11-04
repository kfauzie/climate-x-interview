# Run 1: solution design

A report builder with Sarah's defaults, a method note it writes itself, her approval and a drafted reply. No AI in this version. Medium fidelity; numbers from the practice data and synthetic loan book. Source: `design/solution-design.html`.

## Flow
| Step | Who | Screen | Ends in |
|---|---|---|---|
| 1 | Analyst | Build the answer | Calculate |
| 2 | Analyst | Answer | Submit to Sarah |
| 3 | Sarah | Review | Approve, or send back |
| 4 | Analyst | Send the reply | Sent from their own email, logged |

Askers (CRO, committees, pricing, treasury, IR) never touch it: they email the question and get the reply.

**Decisions to agree**
1. Question and options on one screen: **recommend yes**
2. No AI in this version: **yes** (agreed in the concept)
3. Fast-track review: a follow-up with one changed option and all checks passing shows Sarah only the change: **recommend yes**, confirm with her
4. The product drafts the reply; the analyst sends it from their own email: **recommend yes**
5. Numbers in the reply can't be edited: **recommend yes**

## 1. Build the answer
![Build](design/build.png)

- **For:** analyst, to turn the asker's question into the right choices
- **Removes:** choosing scenario, horizon and loans case by case, and the hour of filtering
- **Shows:** one sentence of what will be calculated, then only what needs attention. All options sit behind "Change options", collapsed
- **Inputs:** question and who it's for are required. Who it's for sets her defaults (committee: central, 2050, leaving out loans in default, redeemed since the export and maturing before 2030). Words in the question are matched to options by rules, not AI, and tagged "From the question"; those need no reason. A reason is needed only to depart from her defaults
- **Checks:**
  - Asker didn't name a scenario → **notes**: "The asker didn't say which scenario. Using central, your committee default"
  - Year picked doesn't match the question → **warns**: "The question asks about 2050; you've picked 2030"
  - A departure from her defaults without a reason → **blocks** Calculate
  - Not in the data → **blocks**: "Present-day ratings aren't in this export: 2030 and 2050 only"
  - Loss to the bank → **blocks**: "Needs default-loss and insurance data that isn't loaded"
- **Ends in:** Calculate. Back from the Answer keeps every option

## 2. Answer
![Answer](design/answer.png)

- **For:** analyst, to check the answer before it goes to Sarah
- **Removes:** the write-up, and "what about severe?" starting it all again
- **Inputs:** a note to Sarah, required only if a check failed
- **Checks:** horizon matches the question and data is fresh → **warn**, shown first to Sarah. Unmatched and unscored loans are always listed. The method note always names the scenario, so that slip can't happen
- **Ends in:** Submit to Sarah. Same options, same number, every time; any number clicks through to its rows

## 3. Review (Sarah)
![Review](design/review.png)

Shown with her sent-back case, rebuilt: 2030 picked, redeemed loans included.
- **For:** Sarah, to approve or send back in minutes
- **Removes:** half a day of checking
- **Inputs:** approve or send back (required); a comment, required to send back or to approve with a failed check, pre-filled with the failed checks
- **Checks:** data changed since it was built → **warns**: "The Spectra export has changed since this was built. Rebuild?"
- **Ends in:** Approve, or send back to Build with her comment. Nothing reaches Send without her approval

## 4. Send the reply
![Send](design/send.png)

- **For:** analyst, to send the approved answer to the asker
- **Removes:** writing the reply and building the Excel by hand
- **Inputs:** the reply (drafted; words editable, numbers locked)
- **Ends in:** Copy reply, Download Excel, Mark as sent → logged: who asked, built and approved, data dates, version

## Test set
| Case | Expected |
|---|---|
| Credit committee: CRE, flood E or worse, 2050, central | 3 of 144 loans, £5.4m of £351.8m · severe 5 loans, £9.6m |
| CRO: total by 2050, by hazard and region | £3.31m central, £6.10m severe · subsidence and South East top under both |
| Mortgage pricing: 2024–25 lending, subsidence E to G | £52.3m, 24.3% of new lending vs 8.6% older · origination-source check flagged |
| Treasury: rise 2030 → 2050, severe | 2.74× (1.57× central) |
| Sent-back draft rebuilt | 2 failed checks · 4 of 145, £6.2m vs fixed 3 of 144, £5.4m |
| "Loss to the bank" | Refused with the reason |

The CRO, pricing and treasury figures are from the Spectra file alone; recompute them with the default exclusions when the prototype is rebuilt.

## Limits shown in the product
- Damage to properties, not loss to the bank
- Practice data and a synthetic loan book until procurement signs
- Central = SSP2-4.5, severe = SSP5-8.5 (to confirm with Sarah)
