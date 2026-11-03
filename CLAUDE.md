# Climate X: customer discovery workspace

A workspace for discovery and building on Climate X data. It is used over several **runs**. Each run brings its own dataset and its own interview notes (from Notion).

## Active run
**run-1** (`runs/run-1/`). Change this line when a new run starts.

## Always use the skills for company, role and product information
The skills are the single source of truth and are kept up to date. Do not answer from memory or from older notes in this file.
- `climate-x-company`: mission and values, funding, advisers, methodology, regulation (PRA SS5/25), use cases, partners, thought leadership, brand, competitors, with sources
- `climate-x-role`: the Principal PM role, positioning, round-1 learnings. Its `live-session.md` covers the live build session
- `climate-x-products`: Spectra, Adapt (with Adaptation Finance), Carta and the Infrastructure Screener (one file each): what each does, customers, value proposition, strengths, weaknesses, opportunities, discovery questions
- `pm-discovery-interview`: principles for interview questions and the base template. Customise it per run into `runs/run-N/discovery-questions.md`
- `pm-problem-to-solution`: turns the run's notes and Test results into a problem summary and a recommended solution, saved as `runs/run-N/solution.md`
- `pm-design`: design philosophy and process (what's worth building, success first, trust and ease of use for non-technical users, flow before screens, design brief, review checklist, prototype as spec). Output: `runs/run-N/design.md`
- `pm-prototype-review`: script and questions for reviewing the prototype with the customer and their gatekeepers, saved as `runs/run-N/prototype-review.md` and published to Notion
- `pm-data-discovery`: the analysis method. `/pm-data-discovery` = Profile, `/pm-data-discovery <notes>` = Test, `/pm-data-discovery <question>` = Answer

## Runs: keep them isolated
Each run lives in `runs/run-N/`:
```
runs/run-N/
  RUN.md        # status, customer context, data notes and analysis defaults for THIS run
  data/         # this run's dataset(s)
  notes/        # this run's interview notes, saved from Notion
  discovery-questions.md  # template customised for this run's data and customer
  solution.md   # problem summary and recommended solution
  design.md     # user flow, screens, test set, feedback rounds
  prototype-review.md  # review script and questions (also in Notion)
  notebooks/    # this run's analysis
```
Rules:
1. **Work only in the active run's folder.** Read its `RUN.md` first. Do not open, read or cite other runs' data, notes, notebooks or `RUN.md`
2. **Nothing carries over between runs:** no numbers, findings, data notes, column meanings, defaults, customer context or interview answers. A new dataset is profiled from scratch, even if it looks like an earlier one
3. **Skills hold only general knowledge** (company, role, products, method). Never write run-specific findings, numbers or interview answers into a skill or into this file. They go in that run's `RUN.md` or `notes/`
4. **Starting a new run:** follow steps 2–3 of the workflow below
5. **If it is unclear which run a dataset or note belongs to, ask** before using it

## Session setup
At the start of every session, before any analysis, run `pip install -q -r requirements.txt && python3 -m ipykernel install --user`

## Workflow for each run
The process is always the same seven steps. Keep each step quick: about 15 minutes of the session is interview time, and the rest is synthesis, design and the prototype.

1. **Set up** (session start): run the session setup above
2. **Data and context arrive** (uploaded data, plus the customer profile and any problem or ask):
   - Create `runs/run-N/` (next number) and set **Active run** above. If unsure whether this is a new run, ask
   - Save the dataset to `data/`. Write the customer profile and the problem or ask, word for word, into `RUN.md`
   - Run `/pm-data-discovery` (Profile), starting with `python3 tools/cxlens.py profile runs/run-N/data/<file>.csv`. Show the result in chat, then save the notebook to `notebooks/`
3. **Generate discovery questions in a new Notion page:**
   - Customise the `pm-discovery-interview` template for this run's customer, ask and Profile findings (15-minute budget, 7 live questions), saved as `discovery-questions.md`
   - Create a **new** Notion page for this run under 2nd round prep, titled `Run N: discovery questions (<customer>)`, with an empty `## Notes` section at the end. Record its link in `RUN.md`
4. **Interview** (done by me, not Claude): I interview the customer, and the Notion note-taking assistant writes notes into that same page
5. **Summarise the problem:**
   - **One fetch:** fetch the meeting-notes block inside the run's Notion page directly, with `include_transcript: true` (it already contains the summary). Save the summary and transcript as they are, without rewriting, to `notes/interview.md` with the page link
   - Run `/pm-data-discovery <notes>` (Test): contradictions first, then the problem statement (narrow and broad), updated product implications and the top 3 follow-up questions
   - Use `cx` functions for every test, with verdicts from `cx.swing` / `cx.verdict`. Show the result in chat first
   - Record the problem statement in `RUN.md` and commit once
6. **Problem to solution:** run the `pm-problem-to-solution` skill (options with evidence-based trade-offs, one pick, narrowest version, success criteria, riskiest assumption), saved as `solution.md`. Then design with `pm-design` (flow first, then screens) and the prototype (a reviewable PR)
7. **Prototype review:** run `pm-prototype-review` to write the script and questions (`prototype-review.md`), publish it to a new Notion page under 2nd round prep, and record the link in `RUN.md`. After the review, save the notes, add a feedback round to `design.md` and update the riskiest assumption in `solution.md`

## Files
- `.claude/skills/`: `pm-data-discovery` (method; this repo copy is the one to edit), `pm-discovery-interview` (question principles and template), `pm-problem-to-solution` (problem and recommended solution), `pm-design` (flow, screens, prototype principles), `pm-prototype-review` (review script and questions), `climate-x-company`, `climate-x-role`, `climate-x-products`
- `tools/cxlens.py`: fast analysis toolkit for wide climate-risk exports (general code, no run data); self-test `tools/test_cxlens.py`
- `runs/`: one folder per run
- `README.md`: tour of the repo
- `requirements.txt`: Python packages for the notebooks
