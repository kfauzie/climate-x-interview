# Climate X: discovery-to-build workspace

Used over several **runs**. Each run brings its own data, customer and interview notes.

## Active run
**run-1** (`runs/run-1/`). Change this line when a new run starts.

## Rules
- Company, role and product facts come from the skills (`climate-x-company`, `climate-x-products`, `climate-x-role`), not memory
- Work only in the active run's folder; read its `RUN.md` first. Never open or cite another run
- Nothing carries over between runs: numbers, findings, defaults, customer context. New data is profiled from scratch
- Skills hold general knowledge only. Run-specific findings go in the run's `RUN.md` or `notes/`
- Unsure which run something belongs to → ask
- Setup at the start of every session: `pip install -q -r requirements.txt && python3 -m ipykernel install --user`

## Run folder
```
runs/run-N/
  RUN.md                  status, customer, the ask, data notes, defaults, links
  data/  notes/  notebooks/
  discovery-questions.md  solution-concept.md  solution-detail.md
  visual-design.md  clickable-prototype.md  prototype-review.md
```

## Workflow
| Step | Who | Skill | Output |
|---|---|---|---|
| 1. Data and context arrive | Claude | `pm-1-data-discovery` (Profile; start with `python3 tools/cxlens.py profile <csv>`) | new `runs/run-N/`, `RUN.md` with the profile and the ask word for word, notebook |
| 2. Discovery questions | Claude | `pm-2-discovery-interview` | `discovery-questions.md` + new Notion page |
| 3. Interview | me | | notes in that Notion page |
| 4. Summarise the problem | Claude | `pm-1-data-discovery` (Test) | `notes/interview.md` (one fetch of the meeting notes with transcript, saved as is), problem statement in `RUN.md` |
| 5. Solution concept | Claude | `pm-3-problem-to-solution-concept` | `solution-concept.md` |
| 6. Solution detail | Claude | `pm-4-solution-detail` | `solution-detail.md`: each screen, its inputs (mandatory or not), checks, edge cases |
| 7. Visual design | Claude | `pm-5-visual-design` | `visual-design.md` + static images of the key screens, one shown first; agreed with me |
| 8. Clickable prototype | Claude | `pm-5-visual-design` | `clickable-prototype.md`, the prototype on a branch + PR |
| 9. Prototype review | me + Claude | `pm-6-prototype-review` | `prototype-review.md` + new Notion page; feedback back into the files above |

Keep each step quick: about 15 minutes of the session is interview; the rest is synthesis, design and the build. Show results in chat first, commit once per step.

## Other files
- `tools/cxlens.py`: fast analysis for wide climate-risk exports (general code, no run data); self-test `tools/test_cxlens.py`
- `README.md`: tour for people
