# Climate X: discovery-to-build workspace

How I go from a customer's data and a short interview to a prototype they'd trust, with Claude Code.

## Skills
**General PM, any customer**
| Skill | |
|---|---|
| [`pm-1-data-discovery`](.claude/commands/pm-1-data-discovery.md) | What the data is, what to trust, which choices change the answer |
| [`pm-2-discovery-interview`](.claude/commands/pm-2-discovery-interview.md) | Finding the problem behind the ask, in 15 minutes |
| [`pm-3-problem-to-solution-concept`](.claude/commands/pm-3-problem-to-solution-concept.md) | Solution concept: what's worth building, and the narrowest slice |
| [`pm-4-solution-design`](.claude/commands/pm-4-solution-design.md) | Medium-fidelity screens with their inputs and checks, reviewed live. Design principles |
| [`pm-5-clickable-prototype`](.claude/commands/pm-5-clickable-prototype.md) | Polished working prototype on a branch, tested, checked in a browser, PR |
| [`pm-6-prototype-review`](.claude/commands/pm-6-prototype-review.md) | Testing the prototype with the people who'd use and approve it |

**Climate X context**
| Skill | |
|---|---|
| [`climate-x-company`](.claude/commands/climate-x-company.md) | Company, method, regulation, customers, competitors, brand |
| [`climate-x-products`](.claude/commands/climate-x-products.md) | Spectra, Adapt, Carta, Infrastructure Screener |
| [`climate-x-role`](.claude/commands/climate-x-role.md) | The role and the live session |

## How a run works
data → profile → discovery questions → interview → problem → solution concept → solution design (medium fidelity) → clickable prototype (PR) → review

Each run lives in [`runs/`](runs/); run 1 is practice on synthetic Spectra-style data. [`tools/cxlens.py`](tools/cxlens.py) does the number crunching; every figure comes from code. Rules and workflow for Claude: [`CLAUDE.md`](CLAUDE.md).

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
