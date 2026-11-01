# Climate X: customer discovery workspace

A workspace for discovery and building on Climate X data. It is used over several **runs**. Each run brings its own dataset and its own interview notes (from Notion).

## Active run
**run-1** (`runs/run-1/`). Change this line when a new run starts.

## Always use the skills for company, role and product information
The skills are the single source of truth and are kept up to date. Do not answer from memory or from older notes in this file.
- `climate-x-company`: funding, stage, methodology, partners, competitors, with sources
- `climate-x-role`: the Principal PM role, positioning, round-1 learnings. Its `live-session.md` covers the live build session
- `climate-x-products`: Spectra, Adapt and Carta (one file each): customers, value proposition, strengths, weaknesses, opportunities, discovery questions
- `discovery-interview`: principles for interview questions and the base template. Customise it per run into `runs/run-N/discovery-questions.md`
- `pm-data-lens`: the analysis method. `/pm-data-lens` = Profile, `/pm-data-lens <notes>` = Test, `/pm-data-lens <question>` = Answer

## Runs: keep them isolated
Each run lives in `runs/run-N/`:
```
runs/run-N/
  RUN.md        # status, customer context, data notes and analysis defaults for THIS run
  data/         # this run's dataset(s)
  notes/        # this run's interview notes, saved from Notion
  discovery-questions.md  # template customised for this run's data and customer
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
The process is always the same five steps. Keep each step quick: about 15 minutes of the session is interview time, and the rest is synthesis, design and the prototype.

1. **Set up** (session start): run the session setup above
2. **Data and context arrive** (uploaded data, plus the customer profile and any problem or ask):
   - Create `runs/run-N/` (next number) and set **Active run** above. If unsure whether this is a new run, ask
   - Save the dataset to `data/`. Write the customer profile and the problem or ask, word for word, into `RUN.md`
   - Run `/pm-data-lens` (Profile) on the data, saving the notebook to `notebooks/`
3. **Generate discovery questions in a new Notion page:**
   - Customise the `discovery-interview` template for this run's customer, ask and Profile findings (15-minute budget, 7 live questions), saved as `discovery-questions.md`
   - Create a **new** Notion page for this run under 2nd round prep, titled `Run N: discovery questions (<customer>)`, with an empty `## Notes` section at the end. Record its link in `RUN.md`
4. **Interview** (done by me, not Claude): I interview the customer, and the Notion note-taking assistant writes notes into that same page
5. **Summarise the problem:**
   - Fetch the run's Notion page, and save the notes to `notes/interview.md` with the page link
   - Run `/pm-data-lens <notes>` (Test): contradictions first, then the problem statement (narrow and broad), updated product implications and the top 3 follow-up questions
   - Record the problem statement in `RUN.md`, then move on to design and the prototype (a reviewable PR)

## Files
- `.claude/skills/`: `pm-data-lens` (method; this repo copy is the one to edit), `discovery-interview` (question principles and template), `climate-x-company`, `climate-x-role`, `climate-x-products`
- `runs/`: one folder per run
- `README.md`: tour of the repo
- `requirements.txt`: Python packages for the notebooks
