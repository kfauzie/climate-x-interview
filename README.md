# Climate X: discovery-to-build workspace

How I go from a customer's data and a short interview to a prototype they'd trust, with Claude Code.

## Skills
**General PM, any customer**
| Skill | |
|---|---|
| [`pm-data-discovery`](.claude/commands/pm-data-discovery.md) | What the data is, what to trust, which choices change the answer |
| [`pm-discovery-interview`](.claude/commands/pm-discovery-interview.md) | Finding the problem behind the ask, in 15 minutes |
| [`pm-problem-to-solution`](.claude/commands/pm-problem-to-solution.md) | Solution concept: what's worth building, and the narrowest slice |
| [`pm-design`](.claude/commands/pm-design.md) | Solution detail (each screen, inputs, checks), visual design, clickable prototype |
| [`pm-prototype-review`](.claude/commands/pm-prototype-review.md) | Testing the prototype with the people who'd use and approve it |

**Climate X context**
| Skill | |
|---|---|
| [`climate-x-company`](.claude/commands/climate-x-company.md) | Company, method, regulation, customers, competitors, brand |
| [`climate-x-products`](.claude/commands/climate-x-products.md) | Spectra, Adapt, Carta, Infrastructure Screener |
| [`climate-x-role`](.claude/commands/climate-x-role.md) | The role and the live session |

## How a run works
data → profile → discovery questions → interview → problem → solution concept → solution detail → visual design → clickable prototype (PR) → review

Each run lives in [`runs/`](runs/); run 1 is practice on synthetic Spectra-style data. [`tools/cxlens.py`](tools/cxlens.py) does the number crunching; every figure comes from code. Run 1's prototype is in [`prototype/`](prototype/). Rules and workflow for Claude: [`CLAUDE.md`](CLAUDE.md).

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
