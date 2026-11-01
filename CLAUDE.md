# Climate X: customer discovery workspace

A workspace for discovery and building on Climate X data. It is used over several **runs**. Each run brings its own dataset and its own interview notes (from Notion).

## Active run
**run-1** (`runs/run-1/`). Change this line when a new run starts.

## Always use the skills for company, role and product information
The skills are the single source of truth and are kept up to date. Do not answer from memory or from older notes in this file.
- `climate-x-company`: funding, stage, methodology, partners, competitors, with sources
- `climate-x-role`: the Principal PM role, positioning, round-1 learnings. Its `live-session.md` covers the live build session
- `climate-x-products`: Spectra, Adapt and Carta (one file each): customers, value proposition, strengths, weaknesses, opportunities, discovery questions
- `pm-data-lens`: the analysis method. `/pm-data-lens` = Profile, `/pm-data-lens <notes>` = Test, `/pm-data-lens <question>` = Answer

## Runs: keep them isolated
Each run lives in `runs/run-N/`:
```
runs/run-N/
  RUN.md        # status, customer context, data notes and analysis defaults for THIS run
  data/         # this run's dataset(s)
  notes/        # this run's interview notes, saved from Notion
  notebooks/    # this run's analysis
```
Rules:
1. **Work only in the active run's folder.** Read its `RUN.md` first. Do not open, read or cite other runs' data, notes, notebooks or `RUN.md`
2. **Nothing carries over between runs:** no numbers, findings, data notes, column meanings, defaults, customer context or interview answers. A new dataset is profiled from scratch, even if it looks like an earlier one
3. **Skills hold only general knowledge** (company, role, products, method). Never write run-specific findings, numbers or interview answers into a skill or into this file. They go in that run's `RUN.md` or `notes/`
4. **Starting a new run:** create `runs/run-N/` with the structure above, update **Active run** here, save the dataset to `data/` and the Notion notes to `notes/` (as markdown, with the source page link), then run `/pm-data-lens` Profile
5. **If it is unclear which run a dataset or note belongs to, ask** before using it

## Session setup
At the start of every session, before any analysis, run `pip install -q -r requirements.txt && python3 -m ipykernel install --user`

## Workflow for each run
1. When the dataset arrives: `/pm-data-lens` (Profile) for a fast decode, trust checks and judgment calls → discovery questions for the customer
2. Save the customer's answers (Notion notes) to `notes/`, then `/pm-data-lens <notes>` (Test) → contradictions first, problem statement
3. Turn product implications into requirements for the feature, then build it to a reviewable PR
4. Record the run's data notes and analysis defaults in its `RUN.md`

## Files
- `.claude/skills/`: `climate-x-company`, `climate-x-role`, `climate-x-products`
- `runs/`: one folder per run
- `README.md`: tour of the repo
- `requirements.txt`: Python packages for the notebooks
