# Run 1: design for option A, "answer with its method"

From `solution.md`, `notes/interview.md` and `notes/sarah-followup.md`. Status: **user flow agreed; screens drafted** (to review).

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

## Screens (prototype scope: steps 1–6 + 8)
Practice-data values below were computed with `tools/cxlens.py` (central = `ssp245`, severe = `ssp585`, inferred). Sarah's own figures are made up, so only the *shape* of her questions is used.
Common to every screen: plain risk language (no "model", "LLM", "eval"); the data dates (Spectra export and loan book) shown in the header; a step indicator (Ask → Confirm → Answer → Review).

### Screen 1 · Ask (step 1)
- **Input:** the question as written (free text); audience (Committee / PRA-stress / Other); who asked (free text, e.g. "Credit committee")
- **Output:** a request, passed to Confirm
- **Happy path:** analyst pastes "How many CRE loans have a flood rating of E or worse by 2050?", picks Committee, asker "Credit committee" → Confirm
- **Edge cases:**
  - Empty or one-word question → "Add the question as the asker wrote it"
  - Audience not picked → can't continue; one line on why it matters ("it sets the default scenario and years")
  - Several questions in one message → "This looks like 2 questions. Split them?", making two requests
- **Acceptance criteria:**
  - Audience is required, and its defaults are shown before continuing (Committee: central 2050; PRA-stress: central and severe, 2030 and 2050)
  - The original wording is kept unchanged on every later screen and in the log

### Screen 2 · Confirm the choices (steps 2–3)
- **Input:** the request; Sarah's defaults for the audience
- **Output:** a confirmed set of choices, each tagged *from the question*, *default* or *changed by analyst*
- **Layout:** one row per choice: what to measure · which loans · hazard and threshold · per loan or per property · scenario · years · exclusions · data dates. Flags sit next to their row
- **Happy path (credit committee question):** measure = count of loans plus their balance, out of all CRE; loans = CRE; hazard = flood, rated E or worse; years = 2050 *(from the question)*; scenario = central *(default: the asker didn't say)*; exclusions = in default, maturing before 2030 *(default)* → analyst accepts
- **Flags:**
  - **Unstated:** "The asker didn't say which scenario. Using central (committee default)"
  - **Ambiguous:** "'Flood': this file has one flood measure. Your write-ups combine river and coastal. Confirm that's the same"
  - **Out of scope, refused with the reason:** "Loss to the bank needs default-loss and insurance data that isn't loaded. Showing damage to properties instead?"
  - **Not in the data:** "Present-day ratings aren't in this export (2030 and 2050 only)" (catches the sent-back slip)
- **Edge cases:**
  - Analyst changes a choice outside the methodology (e.g. severe for a committee question) → row marked **"Needs Sarah's approval"**, with a required reason
  - The AI can't read the question → falls back to the same rows as a form, all empty, and says which parts it couldn't read
  - A choice the data can't support (e.g. a hazard not in the file) → blocked, with what's available
- **Acceptance criteria:**
  - Nothing is computed until the analyst confirms
  - Every choice shows where it came from (question / default / analyst)
  - Every departure from the defaults needs a reason and is carried to Sarah's review
  - The AI only fills in choices. It never shows or estimates a number on this screen

### Screen 3 · Answer (step 4, then submit = step 5)
- **Input:** the confirmed choices
- **Output:**
  1. **Answer in her shape**, e.g. on practice data: "**4 of 243 CRE loans, £7.1m of £594.2m balance**, rated flood E or worse at 2050 (central)"
  2. **One-change versions** with the computed verdict, e.g. "Severe: 8 loans, £17.0m (2.0× central)"; "2030: same answer". For PRA-stress, central and severe at 2030 and 2050 are shown as a grid by default
  3. **Method note** in her write-up fields: scenario and horizon; hazard definition; aggregation rule; exclusions; data dates; join result ("N loans didn't match, listed separately"); balance basis. Written in full sentences she could paste
  4. **Checks**, each pass or fail with the reason: horizon matches the question · export is not older than the loan book · scenario stated · unmatched loans listed · unscored loans listed · counting basis stated
  5. **Source rows:** download as Excel (the loans counted, plus the unmatched and excluded loans on separate tabs)
- **Happy paths for her other two questions (practice data):**
  - CRO total by 2050: "**£3.31m central, £6.10m severe**" annual expected damage to properties; drivers: subsidence 53.6%, South East 37.5% of central. Verdict: "Same top hazard and region under both scenarios"
  - Mortgage pricing, 2024–25 lending in high subsidence (E to G, central, 2050): "**£52.3m, 24.3% of new lending, vs 8.6% of the older book**". Check flags: "Origination date taken from the Spectra export; your method uses the loan system". 2 new loans unscored, listed
- **Edge cases:**
  - Any check fails → **Submit is still possible, but the failed check goes first on Sarah's screen** and needs an analyst comment
  - Zero results → shown as 0 with the choices, not as an error
  - The answer depends on unscored loans → "N loans have no score for this hazard and year: excluded, listed on tab 3"
- **Acceptance criteria:**
  - Every number on the screen is produced by code from the loaded files; the same inputs always give the same number
  - The method note never omits the scenario, the years or the data dates
  - The sent-back draft (present-day ratings, a stale export, no scenario) produces 3 failed checks

### Screen 4 · Sarah's review (step 6) and fast-track (step 8)
- **Input:** a submitted answer
- **Output:** approve, or send back with a comment; an entry in the log (who asked, built and approved; data dates; version)
- **Layout, most important first:**
  1. Failed checks and departures from her defaults (with the analyst's reasons)
  2. The answer, and the one-change versions with verdicts ("Severe doubles it" / "2030: same answer"), so she can see which choices actually matter
  3. The method note as it will be sent
  4. Source rows, one click away
- **Happy path:** no failed checks, no departures → she reads the answer and the note, approves; the analyst gets email text plus the Excel file to send
- **Fast-track (follow-up, step 8):** "What about severe?" → the analyst reopens the approved answer and changes one choice. If that's the only change, it's within her defaults and all checks pass, Sarah sees **only the difference** ("Scenario: central → severe. 4 → 8 loans") and approves in one click. Otherwise, the full review
- **Edge cases:**
  - Send back → her comment goes to the analyst, and the answer reopens at Confirm with her comment shown
  - A new Spectra export arrives while an answer is waiting → "Data has changed since this was built. Rebuild?"
- **Acceptance criteria:**
  - Nothing can be sent without her approval
  - Every approved answer can be rebuilt later from its log entry and give the same number
  - Fast-track appears only when exactly one choice changed, within the defaults, with all checks passing

## Test set for the prototype
| Case | Expected (practice data) |
|---|---|
| Credit committee: CRE flood E or worse, 2050, central | 4 of 243 loans; £7,148,900 of £594,232,500; severe 8 loans, £16,981,600 |
| CRO: total by 2050, then hazard and region | £3,313,709 central; £6,099,020 severe; subsidence and South East top under both |
| Mortgage pricing: 2024–25 lending, subsidence E–G, central 2050 | £52,312,700, 24.26% of new lending vs 8.58% older; origination-source check flagged |
| Treasury: rise 2030 → 2050, severe | 2.74× (vs 1.57× central) |
| Sent-back draft: present-day ratings, stale export, no scenario | 3 failed checks; can't be approved without a comment |
| Out of scope: "loss to the bank" | Refused with the reason; offers damage to properties |

## Open items
- Confirm the scenario mapping: central = `ssp245`, severe = `ssp585` (inferred)
- Confirm with Sarah that she'd accept fast-track review for follow-ups
