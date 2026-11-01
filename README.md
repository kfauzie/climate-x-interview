# Climate X: discovery-to-build workspace

How I prepare for and run customer discovery on Climate X data, with Claude Code.

## Tour
| What | Where | Purpose |
|---|---|---|
| Method skill | [`.claude/skills/pm-data-lens/`](.claude/skills/pm-data-lens/) | How I analyse a dataset for discovery: Profile, Test and Answer modes, trust checks, judgment calls, product implications |
| Discovery skill | [`.claude/skills/discovery-interview/`](.claude/skills/discovery-interview/) | Principles for discovery questions and a base template, customised per run |
| Solution skill | [`.claude/skills/problem-to-solution/`](.claude/skills/problem-to-solution/) | Turns interview notes and data into a problem summary, options with trade-offs, and a recommended solution |
| Company skill | [`.claude/skills/climate-x-company/`](.claude/skills/climate-x-company/) | Funding, stage, methodology, banking use cases, partners, competitors, with sources |
| Role skill | [`.claude/skills/climate-x-role/`](.claude/skills/climate-x-role/) | The Principal PM role, positioning, and the live build session |
| Product skill | [`.claude/skills/climate-x-products/`](.claude/skills/climate-x-products/) | Spectra, Adapt and Carta: customers, value proposition, strengths, weaknesses, opportunities, discovery questions |
| Toolkit | [`tools/cxlens.py`](tools/cxlens.py) | Fast, deterministic analysis for wide climate-risk exports: trust checks, one-at-a-time swings, verdicts computed from the numbers |
| Runs | [`runs/`](runs/) | One folder per run: dataset, interview notes, analysis and `RUN.md`. Run 1 is a practice run on synthetic Spectra-style data |
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
