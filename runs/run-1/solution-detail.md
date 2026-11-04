# Run 1: solution detail

From `solution-concept.md`: a report builder with Sarah's defaults, a method note it writes itself, her approval, and a drafted reply. **No AI in this version.** Numbers below are from the practice data and synthetic loan book.

## Success
- **Users:** analysts build answers; Sarah approves them. Askers never touch the product
- **Measures:** time from question to approved answer (target: a day) · Sarah's review time (target: minutes) · answers sent back · edits to the reply after approval (target: none)
- **Must stay true:** every number computed by code and rebuilt the same from its log · nothing sent without Sarah's approval

## Flow
| Step | Who | Screen | Ends in |
|---|---|---|---|
| 1. Build | Analyst | **Build the answer** | Calculate |
| 2. Answer | Analyst | **Answer** | Submit to Sarah |
| 3. Review | Sarah | **Review** | Approve, or send back |
| 4. Send | Analyst | **Send** | Reply sent from their own email, logged |

Askers email or Teams the question, as today. A follow-up ("what about severe?") reopens the answer with one change.

**Decisions to agree**
1. Question and options on one screen, not two: **recommend yes** (one less step; the question stays in view while picking)
2. No AI in the first version; the options are picked by hand: **yes** (agreed in the concept)
3. Fast-track review: a follow-up that changes one option, with all checks passing, shows Sarah only the change: **recommend yes**, confirm with her
4. The product drafts the reply; the analyst sends it from their own email: **recommend yes**
5. Numbers in the drafted reply can't be edited, only the words around them: **recommend yes**

## Screen 1 · Build the answer (analyst)
**Removes:** choosing scenario, horizon and loans case by case; the 1 hour of filtering in Excel.

| Input | Mandatory | Default | Source shown, one click away |
|---|---|---|---|
| Question, pasted as the asker wrote it | Yes | | The analyst |
| Who asked | No | | The analyst |
| Audience: Committee · PRA / stress · Other | Yes | | The analyst. Sets the defaults below |
| Measure: count of loans with balance · £ damage · share · rise | Yes | Count with balance | Default |
| Loans: CRE · mortgages · all | Yes | All | Default |
| Hazard: flood · subsidence · heat · wind | Yes | | The analyst |
| Rating: e.g. E or worse | Yes | E or worse | Default |
| Scenario: central · severe · low | Yes | Committee: central · PRA: central and severe | Her methodology paper, the audience's paragraph |
| Year: 2030 · 2050 | Yes | Committee: 2050 · PRA: 2030 and 2050 | Her methodology paper |
| Exclusions: in default · redeemed since the export · maturing before 2030 | No | In default, redeemed since the export | Her methodology paper |
| Count per: loan · property | Yes | Loan | Default |
| Group by: hazard · region · property type | No | | The analyst |
| Reason for a change from a default | Yes, for each change | | The analyst. Shown to Sarah |

**Checks** (rules, run as options change)
| Check | Failure |
|---|---|
| A year in the question (e.g. "by 2050") is among the years picked | **Warns:** "The question asks about 2050; you've picked 2030." Shown to Sarah |
| Every change from a default has a reason | **Blocks** Calculate until given |
| The hazard and year exist in the data | **Blocks:** "Present-day ratings aren't in this export: 2030 and 2050 only" |
| The question asks for loss to the bank | **Blocks** with the reason: "Needs default-loss and insurance data that isn't loaded. Damage to properties is available" |

**Edge cases**
- No audience picked → Calculate stays off: "Pick who it's for. It sets the default scenario and years"
- Two questions pasted in one → "This looks like 2 questions. Build them separately"
- Back from the Answer screen keeps every option

**Ends in:** Calculate. **Acceptance:** picking an audience sets its defaults; every option shows its source; nothing computes until Calculate.

## Screen 2 · Answer (analyst)
**Removes:** the write-up, and "what about severe?" starting it all again.

**Shows**, headline first:
1. **4 of 235 CRE loans, £7.1m of £580.3m balance** · flood E or worse · 2050 · central
2. If one option changed: severe 8 loans, £17.0m ("doubles the answer") · 2030 4 loans, £6.2m ("same count, different loans") · per property: same answer
3. The loans counted, on screen; all rows in Excel
4. Method note in her write-up fields: scenario and horizon · hazard and rating · loans in and out · counting basis · data dates and the loan-book join · balance basis
5. About this answer: damage to properties, not loss to the bank · practice data

| Input | Mandatory | |
|---|---|---|
| Note to Sarah | Only if a check failed | Shown at the top of her review |

**Checks** (code)
| Check | Failure |
|---|---|
| Horizon matches the question | Warns. Shown first to Sarah; note required |
| Data fresh: export not older than the loan book, or redeemed loans excluded | Same |
| Unmatched loans listed (2 here) | Always listed on their own tab |
| Unscored loans listed (1 here) | Always listed |
| Counting basis stated | Always stated |

The method note always names the scenario, so the slip "didn't say which scenario" can't happen.

**Edge cases**
- Zero loans → shown as 0 with the options used, not an error
- Unscored loans affect the answer → "1 loan has no score for flood at 2050: excluded, listed on its own tab"

**Ends in:** Submit to Sarah. **Acceptance:** same options, same number, every time; clicking any number shows its rows; the note never leaves out scenario, years or data dates.

## Screen 3 · Review (Sarah)
**Removes:** half a day of checking.

**Shows**, most important first:
1. Failed checks, each in plain words with what it changes
2. Changes from her defaults, with the analyst's reasons
3. If checks failed: as built vs with the checks fixed (e.g. 4 of 236, £6.2m vs 4 of 235, £7.1m)
4. The answer, the one-change versions and the method note as they'll be sent
5. The loans, one click away

| Input | Mandatory | Default |
|---|---|---|
| Approve · Send back | Yes | |
| Comment | To send back, or to approve with a failed check | Pre-filled with the failed checks |

**Checks:** data changed since it was built → warns: "The Spectra export has changed since this was built. Rebuild?" · fast-track only when exactly one option changed from an approved answer and all checks pass.

**Ends in:** Approve, or Send back (reopens Screen 1 with her comment). **Acceptance:** nothing reaches Send without her approval; her decision is logged.

## Screen 4 · Send (analyst)
**Removes:** writing the reply and building the Excel by hand.

**Shows:** a drafted reply to the asker (headline answer, one line on the method, the severe version, Sarah as approver) and the Excel file (answer · loans counted · unmatched · excluded · method note).

| Input | Mandatory | Default |
|---|---|---|
| Reply text | Yes | Drafted; words editable, numbers locked |
| Mark as sent | Yes | |

**Ends in:** Copy reply and download Excel → sent from their own email → logged (who asked, built, approved; data dates; version). **Acceptance:** the reply's numbers always match the approved answer.

## Test set
| Case | Expected |
|---|---|
| Credit committee: CRE, flood E or worse, 2050, central | 4 of 235 loans, £7.1m of £580.3m · severe 8 loans, £17.0m |
| CRO: total by 2050, then by hazard and region | £3.31m central, £6.10m severe · subsidence and South East top under both |
| Mortgage pricing: 2024–25 lending, subsidence E to G, central 2050 | £52.3m, 24.3% of new lending vs 8.6% older · origination-source check flagged |
| Treasury: rise 2030 → 2050, severe | 2.74× (1.57× central) |
| Sent-back draft rebuilt: 2030 picked, redeemed loans included | 2 failed checks (horizon, freshness) · 4 of 236, £6.2m vs fixed 4 of 235, £7.1m |
| "Loss to the bank" | Refused with the reason |

## Limits shown in the product
- Damage to properties, not loss to the bank
- Practice data and a synthetic loan book until procurement signs
- Scenario names mapped central = SSP2-4.5, severe = SSP5-8.5 (to confirm with Sarah)
