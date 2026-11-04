# Climate X: discovery-to-build workspace

Used over several **runs**. Each run brings its own data, customer and interview notes.

## Active run
**run-1** (`runs/run-1/`). Change this line when a new run starts.

## Rules
- Company, role and product facts come from the skills (`climate-x-company`, `climate-x-products`, `climate-x-role`), not memory
- Work only in the active run's folder; read its `RUN.md` first. Never open or cite another run
- Nothing carries over between runs: numbers, findings, defaults, customer context. New data is profiled from scratch
- Skills hold general knowledge only. Run-specific findings go in the run's `RUN.md`
- Documents I read or annotate (questions, interview notes, solution concept, review) live in Notion only; the repo holds data, code, screen images and `RUN.md` with the links
- Unsure which run something belongs to → ask
- Everything I show gets screen-shared to someone following along: lead with the point, tables and short lines over paragraphs, no detail that doesn't change a decision
- Setup at the start of every session: `pip install -q -r requirements.txt && python3 -m ipykernel install --user`

## Run folder
```
runs/run-N/
  RUN.md                  status, customer, the ask, data notes, defaults, links
  data/  notes/  notebooks/
  design/                 screen images
```

## Workflow
| Step | Who | Skill | Output |
|---|---|---|---|
| 1. Data and context arrive | Claude | `pm-1-data-discovery` (Initial review; start with `python3 tools/cxlens.py profile <csv>`) | new `runs/run-N/`, `RUN.md` with the data summary, top questions and the ask word for word |
| 2. Discovery questions | Claude | `pm-2-discovery-interview` | new Notion page, linked in `RUN.md` |
| 3. Interview | me | | notes in that Notion page |
| 4. Summarise the problem | Claude | `pm-1-data-discovery` (Answer: test each claim) | claims from the Notion interview notes tested against the data, results in `RUN.md` |
| 5. Solution concept | Claude | `pm-3-problem-to-solution-concept` | new Notion page, linked in `RUN.md` |
| 6. Solution design | Claude | `pm-4-solution-design` | medium-fidelity screen images in `runs/run-N/design/`, one per workflow step, most important first; reviewed live and agreed with me |
| 7. Build | Claude | `pm-5-build` | the working first version (MVP): one HTML file, one screen at a time; branch and PR only if I ask |
| 8. MVP review | me + Claude | `pm-6-mvp-review` | new Notion page; feedback back into the screens and the build |

Keep each step quick: about 15 minutes of the session is interview; the rest is synthesis, design and the build. Show results in chat first, commit once per step.

## Other files
- `tools/cxlens.py`: fast analysis for wide climate-risk exports (general code, no run data); self-test `tools/test_cxlens.py`
- `README.md`: tour for people
