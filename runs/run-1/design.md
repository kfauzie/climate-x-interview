# Run 1: design for option A, "answer with its method"

From `solution.md`, `notes/interview.md` and `notes/sarah-followup.md`. Status: **user flow agreed**; screens next.

## Who does what
- **Askers** (CRO, committees, pricing, treasury, IR): stay on email and Teams; never use the tool
- **Analyst:** builds the answer in the tool
- **Sarah:** owns the defaults (her methodology paper) and approves every answer
- **Model risk:** sees the method and test results, not the daily flow

## User flow (agreed)
```
[0 Quarterly setup] → 1 Request → 2 Interpret → 3 Confirm → 4 Compute & check → 5 Submit → 6 Sarah reviews → 7 Send & log
                                                                                                    ↑                      │
                                                                                                    └── 8 Follow-up ───────┘
```
0. **Quarterly setup** (analyst): load the Spectra export and the loan book; record each file's date; run the loan-ID join; list unmatched loans; flag staleness. Sarah's defaults configured yearly from her methodology paper
1. **Request** (analyst): paste the question as written; pick the audience (committee / PRA-stress / other), which sets the defaults
2. **Interpret** (AI, shown back, never applied silently): question → choices (measure, loans, hazard and rating threshold, aggregation, scenario and horizon, exclusions, data date). Flags: unstated (default applied), ambiguous, out of scope (refused with the reason)
3. **Confirm** (analyst): accept or edit. Edits outside the methodology are marked "needs Sarah's approval", with a reason
4. **Compute and check** (code only): answer in her shape; method note in her write-up fields; one-change versions with computed verdicts; checks (horizon, freshness, scenario stated, unmatched and unscored loans, counting basis); source rows as Excel
5. **Submit** (analyst): add context, send to Sarah
6. **Sarah reviews:** answer, choices vs defaults (departures highlighted), checks, verdicts, source rows; approve or send back with a comment
7. **Send and log:** email text plus Excel; log who asked, built and approved, the data dates and the version
8. **Follow-up:** reopen, change one choice (often already computed). One change within defaults with all checks passing → fast-track review, where Sarah sees only what changed

## Decisions
1. Askers stay on email; only the analyst and Sarah use the tool: **yes**
2. Question input: **AI interprets, the analyst confirms**; a form is the fallback. AI never touches a number
3. Fast-track review for one-change follow-ups: **yes** (to confirm with Sarah)
4. Output: **email text plus Excel**, as today: **yes**
5. Prototype scope: **steps 1–6 plus 8** on the practice data, with a small made-up loan book to show the join, exclusions and staleness check; step 0 simulated; step 7 as a log only: **yes**

## Open items
- Confirm the scenario mapping: central = `ssp245`, severe = `ssp585` (inferred)
- Confirm with Sarah that she'd accept fast-track review for follow-ups
