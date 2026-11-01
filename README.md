# Climate X: discovery-to-build workspace

How I prepare for and run customer discovery on Climate X data, with Claude Code.

## Tour
| What | Where | Purpose |
|---|---|---|
| Product skill | [`.claude/skills/climate-x-products/`](.claude/skills/climate-x-products/) | Spectra, Adapt and Carta: customers, value proposition, strengths, weaknesses, opportunities, discovery questions |
| Company research | [`docs/climate-x-brief.md`](docs/climate-x-brief.md) | Products, methodology, banking use cases, competitors, with sources |
| Data profile | [`notebooks/spectra_profile.ipynb`](notebooks/spectra_profile.ipynb) | Profile of a practice portfolio export: trust checks, judgment calls, discovery questions. Every number is computed in code |
| Practice data | [`data/`](data/) | Synthetic Spectra-style loan portfolio (not real Climate X data) |
| Context for Claude | [`CLAUDE.md`](CLAUDE.md) | Data notes and default analysis choices |

## Workflow
1. **Profile** the data before discovery: what it is, what to trust, which judgment calls change the answer
2. **Discover:** ask non-leading questions drawn from the data and the product skill
3. **Test** what the customer said against the data, then write the problem statement
4. **Build** the narrowest useful version to a reviewable PR. Deterministic code computes the numbers; AI interprets and explains

## Setup
```bash
pip install -q -r requirements.txt && python3 -m ipykernel install --user
```
