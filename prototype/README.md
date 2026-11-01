# Prototype: answer with its method

A web app where an analyst turns a plain-English question into confirmed choices, code computes the answer with its method note and checks, and the reviewer approves it, with fast-track review for one-change follow-ups. Design: `runs/run-1/design.md`.

## Run it
```bash
pip install -q -r requirements.txt
python3 -m uvicorn prototype.app:app --port 8000      # then open http://localhost:8000
```
Uses `runs/run-1` by default; set `RUN_DIR=runs/run-N` for another run. Data in run 1 is practice data, and the loan book is synthetic (`runs/run-1/data/make_loan_book.py`).

## Clickable demo (no install)
A static page that replays answers precomputed by `engine.py` (728 combinations of the preset questions and the choices you can toggle):
```bash
python3 prototype/demo/build_demo.py demo.html
```

## Test it
```bash
python3 -m pytest prototype/tests -q
```
The tests are the design's test set: her three example questions, the treasury rise, the sent-back draft (must fail 3 checks), an out-of-scope question, departures needing a reason, reproducibility, the review flow and fast-track.

## How it's built
| File | Role |
|---|---|
| `engine.py` | Every number: population and exclusions, loan-book join, counts, £ damage, rises, shares, one-change versions, verdicts (via `tools/cxlens.py`), checks, method note, source rows |
| `interpret.py` | Question → choices and flags. **Never produces a number** |
| `app.py` | API: interpret, compute, submit, review, follow-up, Excel export, log |
| `static/index.html` | The four screens: Ask, Confirm, Answer, Review (with an Analyst / Sarah switch) |

## Deterministic vs AI
- **Code computes everything** in `engine.py`; the same inputs always give the same number
- **Interpretation is rule-based in this prototype**, so it runs offline and deterministically. The design's AI interpreter replaces `interpret()` behind the same output, validated against `ALLOWED`, and the analyst still confirms every choice. `tests/test_answer.py::test_interpret_golden` is the starting golden set for it
- **Humans check twice:** the analyst confirms the choices; the reviewer approves the answer

## Not built yet
AI interpreter (needs an API key and a larger golden set), persistent storage (answers live in memory), sign-in and named roles, loss to the bank (needs LGD and insurance data), PowerPoint export.
