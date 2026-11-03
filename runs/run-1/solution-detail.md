# Run 1: solution detail, "answer with its method"

From `solution-concept.md`, `notes/interview.md` and `notes/sarah-followup.md`. Status: **agreed**. Next: `visual-design.md`.

## Success
- **Users:** the analyst builds the answer; Sarah approves it. Askers never use the tool
- **Measures:** time from question to an approved answer; Sarah's review time; answers sent back; edits after approval (target: none)
- **Must stay true:** every number from code, reproducible from the log; nothing sent without Sarah's approval

## Who does what
- **Askers** (CRO, committees, pricing, treasury, IR): stay on email and Teams
- **Analyst:** builds the answer in the tool
- **Sarah:** owns the defaults (her methodology paper) and approves every answer
- **Model risk:** sees the method and test results, not the daily flow

## Flow
```
[0 Quarterly setup] → 1 Ask → 2 Confirm → 3 Answer → 4 Sarah reviews → Send & log
                                                         ↑                    │
                                                         └── Follow-up ───────┘
```
- **Quarterly setup** (analyst): load the Spectra export and the loan book; record each file's date; join on loan ID; list unmatched loans. Sarah's defaults are set yearly from her methodology paper
- **Send and log:** email text plus Excel; log who asked, built and approved, the data dates and the version
- **Follow-up:** reopen and change one choice. One change from the asker, within defaults, all checks passing → fast-track review: Sarah sees only what changed

## Decisions
1. Askers stay on email; only the analyst and Sarah use the tool: **yes**
2. Question input: **AI reads it into choices, the analyst confirms**; a form is the fallback. AI never touches a number
3. Fast-track review for one-change follow-ups: **yes** (to confirm with Sarah)
4. Output: **email text plus Excel**, as today: **yes**
5. Prototype scope: Ask, Confirm, Answer, Review and follow-up on the practice data, with a small synthetic loan book for the join, exclusions and freshness check; setup simulated; sending as a log only: **yes**

## Every screen
- Plain risk language: no "model", "LLM" or "eval"
- The data dates (Spectra export, loan book) in the header; a step indicator (Ask → Confirm → Answer → Review)
- Back bottom left keeps everything; the one forward action bottom right

## Screen 1 · Ask
**Removes:** retyping and losing the asker's wording.

| Input | Mandatory | Default | Source |
|---|---|---|---|
| Question, as the asker wrote it | Yes | none | Analyst pastes it (free text; examples only pre-fill) |
| Audience: Committee / PRA-stress / Other (free text) | Yes | none | Analyst |
| Who asked | No | none | Analyst (free text) |

**Checks**
| Check | On failure |
|---|---|
| Question has more than one word | Blocks: "Add the question as the asker wrote it" |
| Audience picked | Blocks, with why: "It sets the default scenario and years" |
| One question per request | Warns: "This looks like 2 questions. Split them?" |

**Ends in:** Continue → Confirm.
**Acceptance:** the audience's defaults show before continuing (Committee: central, 2050; PRA-stress: central and severe, 2030 and 2050); the original wording is kept unchanged on every later screen and in the log.

## Screen 2 · Confirm
**Removes:** deciding scenario, horizon and which loans by hand, and guessing what the asker meant.

AI reads the question into the rows below; each is tagged *from the question*, *default* or *changed by analyst*.

| Input | Mandatory | Default | Source |
|---|---|---|---|
| Measure (count of loans with balance, £ damage, share, rise) | Yes | Count with balance | Question |
| Loans (CRE, mortgages, all) | Yes | All | Question |
| Hazard and rating threshold | Yes | none | Question |
| Counting basis (per loan / per property) | Yes | Per loan | Default |
| Scenario | Yes | Audience default (Committee: central) | Default unless stated |
| Year (2030 / 2050) | Yes | Audience default (Committee: 2050) | Question, else default |
| Exclusions | No | In default; redeemed since the export | Default; her write-ups suggest more (e.g. maturing before 2030) |
| Added choices (region, property type, origination year, balance band) | No | none | Analyst, "+ Add a choice" |
| Reason for a departure from the defaults | Yes, when the analyst departs | none | Analyst |

**Checks**
| Check | On failure |
|---|---|
| Unstated choice | Warns, default applied: "The asker didn't say which scenario. Using central (committee default)" |
| Ambiguous term | Warns: "'Flood': this file has one flood measure. Your write-ups combine river and coastal. Confirm that's the same" |
| Not in the data | Blocks, with what's available: "Present-day ratings aren't in this export (2030 and 2050 only)" |
| Out of scope | Refused with the reason and an alternative: "Loss to the bank needs default-loss and insurance data that isn't loaded. Show damage to properties instead?" |
| Analyst departs from the defaults on their own | Needs a reason; marked "Needs Sarah's approval". A choice the asker stated isn't a departure |
| AI can't read the question | Falls back to the same rows as an empty form, saying which parts it couldn't read |

**Ends in:** Confirm and calculate → Answer.
**Acceptance:** nothing is computed until the analyst confirms; every choice shows its source; every departure carries a reason to Sarah; the AI never shows or estimates a number here.

## Screen 3 · Answer
**Removes:** the write-up, and the "what about severe?" round trip.

| Input | Mandatory | Default | Source |
|---|---|---|---|
| Confirmed choices | Yes | from Confirm | Confirm |
| Note to Sarah | Only if a check failed | none | Analyst |

**Shows**, headline first:
1. The answer in her shape: "4 of 235 CRE loans, £7.1m of £580.3m balance, rated flood E or worse, 2050, central"
2. If one choice changed, each with a computed verdict: severe 8 loans, £17.0m ("doubles the answer"); 2030 4 loans, £6.2m ("same count, different loans")
3. Method note in her write-up fields, ready to paste: scenario and horizon, hazard, population, exclusions, counting basis, data dates and join result, balance basis
4. The loans counted, on screen; all rows as Excel (unmatched and excluded loans on their own tabs)
5. Settings used, and "About this answer": damage to properties, not loss to the bank; practice data; what it can't answer

**Checks** (all computed)
| Check | On failure |
|---|---|
| Horizon matches the question | Warns; goes first on Sarah's screen; note required |
| Data fresh: export not older than the loan book, redeemed loans excluded | Same |
| Scenario stated | Same |
| Unmatched loans listed | Same |
| Unscored loans listed | Same |
| Counting basis stated | Same |

**Ends in:** Submit to Sarah.
**Acceptance:** every number comes from code and the same inputs give the same number; the method note never omits scenario, years or data dates; zero results show as 0 with the choices; the sent-back draft produces 3 failed checks.

## Screen 4 · Sarah's review
**Removes:** half a day of checking someone else's numbers.

| Input | Mandatory | Default | Source |
|---|---|---|---|
| Decision: approve / send back | Yes | none | Sarah |
| Comment | Yes to send back, or to approve with failed checks | Pre-filled with the failed checks | Sarah |

**Shows**, most important first: failed checks and departures (with the analyst's reasons) → as drafted vs with the checks fixed → one-change versions → method note as it will be sent → source rows.

**Checks**
| Check | On failure |
|---|---|
| Data unchanged since the answer was built | Warns: "Data has changed since this was built. Rebuild?" |
| Fast-track: exactly one change, from the asker, all checks pass | Otherwise full review |

**Ends in:** Approve → email text plus Excel, logged; Send back → reopens at Confirm with her comment.
**Acceptance:** nothing is sent without her approval; every approved answer can be rebuilt from its log entry with the same number.

## Test set
Values from the practice data; the committee case with the synthetic loan-book join from `prototype/engine.py`, the rest from the Spectra file with `tools/cxlens.py` (central = `ssp245`, severe = `ssp585`, inferred).

| Case | Expected |
|---|---|
| Credit committee: CRE flood E or worse, 2050, central | 4 of 235 loans, £7.1m of £580.3m (Spectra file alone: 4 of 243, £7,148,900 of £594,232,500); severe 8 loans, £17.0m |
| CRO: total by 2050, then hazard and region | £3,313,709 central; £6,099,020 severe; subsidence and South East top under both |
| Mortgage pricing: 2024–25 lending, subsidence E–G, central 2050 | £52,312,700, 24.26% of new lending vs 8.58% older; origination-source check flagged |
| Treasury: rise 2030 → 2050, severe | 2.74× (vs 1.57× central) |
| Sent-back draft: present-day ratings, stale export, no scenario | 3 failed checks; can't be approved without a comment |
| Out of scope: "loss to the bank" | Refused with the reason; offers damage to properties |

## Open items
- Confirm the scenario mapping: central = `ssp245`, severe = `ssp585` (inferred)
- Confirm with Sarah that she'd accept fast-track review for follow-ups
