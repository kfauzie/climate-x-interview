# Climate X: discovery-to-build workspace

How I prepare for and run customer discovery on Climate X data, with Claude Code.

## Tour

### General PM skills (reusable for any customer)
| Skill | Purpose |
|---|---|
| [`pm-data-discovery`](.claude/skills/pm-data-discovery/) | Analyse a dataset: what it is, what to trust, which choices change the answer (Profile, Test, Answer) |
| [`pm-discovery-interview`](.claude/skills/pm-discovery-interview/) | Discovery interviews: principles, a 15-minute plan, follow-up triggers, base template |
| [`pm-problem-to-solution`](.claude/skills/pm-problem-to-solution/) | Problem statement and what's worth building: options, pick, narrowest slice, riskiest assumption |
| [`pm-design`](.claude/skills/pm-design/) | Design for AI products non-technical users trust: principles, flow → screens → prototype as spec, checklist |
| [`pm-prototype-review`](.claude/skills/pm-prototype-review/) | Review the prototype with the customer: script on their example, questions, what to measure |

### Climate X context
| Skill | Purpose |
|---|---|
| [`climate-x-company`](.claude/skills/climate-x-company/) | Company, method, regulation (PRA SS5/25), customers, partners, competitors, brand, sources |
| [`climate-x-products`](.claude/skills/climate-x-products/) | Spectra, Adapt, Carta, Infrastructure Screener: what each does, buyers, gaps, opportunities, questions |
| [`climate-x-role`](.claude/skills/climate-x-role/) | The role, round-1 learnings, my evidence, positioning, the live session |

### Everything else
| What | Where | Purpose |
|---|---|---|
| Toolkit | [`tools/cxlens.py`](tools/cxlens.py) | Fast, deterministic analysis for wide climate-risk exports: trust checks, one-at-a-time swings, verdicts computed from the numbers |
| Runs | [`runs/`](runs/) | One folder per run: dataset, interview notes, analysis, solution and `RUN.md`. Run 1 is a practice run on synthetic Spectra-style data |
| Context for Claude | [`CLAUDE.md`](CLAUDE.md) | Active run, run-isolation rules, workflow |

## Workflow (each run)
1. Open Claude Code on this repo
2. Upload the data and the customer and problem context → a new run folder, and a **Profile** of the data: what it is, what to trust, which judgment calls change the answer
3. Generate discovery questions, customised to this customer and data, in a **new Notion page**
4. Interview the customer, with notes taken in the same Notion page
5. Pull the notes back → **Test** what the customer said against the data → problem statement
6. **Problem to solution:** options with evidence-based trade-offs, one pick, its narrowest version → design and prototype (a reviewable PR). Deterministic code computes the numbers; AI interprets and explains
7. **Prototype review** with the customer and their gatekeepers, using a script built on their own example; feedback goes into the next design round

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
