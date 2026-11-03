# Climate X: discovery-to-build workspace

How I go from a customer's data and a short interview to a prototype they'd trust, with Claude Code.

## Skills
**General PM, any customer**
| Skill | |
|---|---|
| [`pm-data-discovery`](.claude/skills/pm-data-discovery/SKILL.md) | What the data is, what to trust, which choices change the answer |
| [`pm-discovery-interview`](.claude/skills/pm-discovery-interview/SKILL.md) | Finding the problem behind the ask, in 15 minutes |
| [`pm-problem-to-solution`](.claude/skills/pm-problem-to-solution/SKILL.md) | Solution concept: what's worth building, and the narrowest slice |
| [`pm-design`](.claude/skills/pm-design/SKILL.md) | Solution detail (each screen, inputs, checks), visual design, clickable prototype |
| [`pm-prototype-review`](.claude/skills/pm-prototype-review/SKILL.md) | Testing the prototype with the people who'd use and approve it |

**Climate X context**
| Skill | |
|---|---|
| [`climate-x-company`](.claude/skills/climate-x-company/SKILL.md) | Company, method, regulation, customers, competitors, brand |
| [`climate-x-products`](.claude/skills/climate-x-products/SKILL.md) | Spectra, Adapt, Carta, Infrastructure Screener |
| [`climate-x-role`](.claude/skills/climate-x-role/SKILL.md) | The role and the live session |

## How a run works
data → profile → discovery questions → interview → problem → solution concept → solution detail → visual design → clickable prototype (PR) → review

Each run lives in [`runs/`](runs/); run 1 is practice on synthetic Spectra-style data. [`tools/cxlens.py`](tools/cxlens.py) does the number crunching; every figure comes from code. Run 1's prototype is in [`prototype/`](prototype/). Rules and workflow for Claude: [`CLAUDE.md`](CLAUDE.md).

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
