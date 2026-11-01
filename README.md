# Climate X: discovery-to-build workspace

How I prepare for and run customer discovery on Climate X data, with Claude Code.

## Tour

### General PM skills (reusable for any customer)
| Skill | Purpose |
|---|---|
| [`pm-data-discovery`](.claude/skills/pm-data-discovery/) | Analyse a dataset for discovery: Profile, Test and Answer modes, trust checks, judgment calls, product implications |
| [`pm-discovery-interview`](.claude/skills/pm-discovery-interview/) | Principles for discovery questions and a base template, customised per run |
| [`pm-problem-to-solution`](.claude/skills/pm-problem-to-solution/) | Turn interview notes and data into a problem summary, options with trade-offs, and a recommended solution |
| [`pm-design`](.claude/skills/pm-design/) | Flow first, then screens, test set and prototype; interaction and visual principles |

### Climate X context
| Skill | Purpose |
|---|---|
| [`climate-x-company`](.claude/skills/climate-x-company/) | Mission and values, funding, methodology, regulation (PRA SS5/25), banking use cases, partners, thought leadership, brand, competitors, with sources |
| [`climate-x-products`](.claude/skills/climate-x-products/) | Spectra, Adapt and Adaptation Finance, Carta, Infrastructure Screener: customers, value proposition, strengths, weaknesses, opportunities, discovery questions |
| [`climate-x-role`](.claude/skills/climate-x-role/) | The Principal PM role, positioning, and the live build session |

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

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
