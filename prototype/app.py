"""Web app for "answer with its method" (prototype).

    python3 -m uvicorn prototype.app:app --port 8000      # RUN_DIR defaults to runs/run-1
"""
from __future__ import annotations
import copy, io, json, os, time, uuid
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

from .engine import Book, Choices, compute, defaults_for, departures, source_rows, AUDIENCE_DEFAULTS
from .interpret import interpret

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_DIR = os.environ.get('RUN_DIR', os.path.join(ROOT, 'runs', 'run-1'))
book = Book(RUN_DIR)
STORE: dict[str, dict] = {}
LOG: list[dict] = []
app = FastAPI(title='Answer with its method (prototype)')


class AskIn(BaseModel):
    question: str
    audience: str
    asker: str = ''


class ComputeIn(BaseModel):
    question: str
    audience: str
    asker: str = ''
    choices: dict
    sources: dict
    question_years: list = []
    reasons: dict = {}
    parent_id: str | None = None


class SubmitIn(BaseModel):
    comment: str = ''


class ReviewIn(BaseModel):
    decision: str            # approve | send_back
    comment: str = ''


class FollowIn(BaseModel):
    question: str


def _log(event, rec, **kw):
    LOG.append({'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'event': event, 'id': rec['id'], 'question': rec['question'],
                'asker': rec['asker'], 'status': rec['status'], 'export_as_at': book.export_as_at, 'book_as_at': book.book_as_at, **kw})


@app.get('/api/meta')
def meta():
    return {'export_as_at': book.export_as_at, 'book_as_at': book.book_as_at, 'hazards': book.hazards, 'years': book.d.years,
            'scenarios': book.scen_map, 'audiences': {k: v for k, v in AUDIENCE_DEFAULTS.items()},
            'loan_types': sorted(book.d.df.loan_type.unique().tolist()), 'run_dir': os.path.relpath(RUN_DIR, ROOT)}


@app.post('/api/interpret')
def api_interpret(a: AskIn):
    if len(a.question.split()) < 3:
        raise HTTPException(400, 'Add the question as the asker wrote it')
    if a.audience not in AUDIENCE_DEFAULTS:
        raise HTTPException(400, 'Pick an audience: it sets the default scenario and years')
    r = interpret(a.question, a.audience, book.hazards, book.d.years)
    r['defaults'] = defaults_for(a.audience)
    return r


def _validate(c: Choices):
    bad = [h for h in c.hazards if h not in book.hazards]
    if bad: raise HTTPException(400, f"Hazard not in the data: {', '.join(bad)}. Available: {', '.join(book.hazards)}")
    badf = [y for y in c.years if y not in book.d.years]
    if badf: raise HTTPException(400, f"Year not in the data: {', '.join(badf)}. Available: {', '.join(book.d.years)}")
    bads = [s for s in c.scenarios if s not in book.scen_map]
    if bads: raise HTTPException(400, f"Unknown scenario: {', '.join(bads)}")


@app.post('/api/compute')
def api_compute(x: ComputeIn):
    c = Choices.from_dict(x.choices); _validate(c)
    deps = departures(c, x.sources, x.audience)
    missing = [d['field'] for d in deps if not x.reasons.get(d['field'])]
    if missing:
        raise HTTPException(400, f"Give a reason for each change from Sarah's defaults: {', '.join(missing)}")
    res = compute(book, c, x.question_years, x.question)
    rid = uuid.uuid4().hex[:8]
    rec = {'id': rid, 'question': x.question, 'audience': x.audience, 'asker': x.asker, 'choices': c.__dict__, 'sources': x.sources,
           'question_years': x.question_years, 'reasons': x.reasons, 'departures': deps, 'result': res, 'status': 'draft',
           'parent_id': x.parent_id, 'comments': [], 'fast_track': False, 'diff': []}
    if x.parent_id and x.parent_id in STORE:
        p = STORE[x.parent_id]
        rec['diff'] = [{'field': k, 'from': p['choices'][k], 'to': v} for k, v in c.__dict__.items() if p['choices'].get(k) != v]
        rec['fast_track'] = (p['status'] == 'approved' and len(rec['diff']) == 1 and x.sources.get(rec['diff'][0]['field']) == 'question'
                             and not deps and all(ch['ok'] for ch in res['checks']))
        rec['parent_headline'] = p['result']['headline']
    STORE[rid] = rec; _log('computed', rec)
    return rec


@app.post('/api/answers/{rid}/submit')
def api_submit(rid: str, s: SubmitIn):
    rec = STORE.get(rid) or _404()
    failed = [c['name'] for c in rec['result']['checks'] if not c['ok']]
    if failed and not s.comment.strip():
        raise HTTPException(400, f"Add a comment for the failed checks: {', '.join(failed)}")
    rec['status'] = 'submitted'; rec['comments'].append({'by': 'analyst', 'text': s.comment}); _log('submitted', rec)
    return rec


@app.post('/api/answers/{rid}/review')
def api_review(rid: str, r: ReviewIn):
    rec = STORE.get(rid) or _404()
    if rec['status'] != 'submitted':
        raise HTTPException(400, 'Only submitted answers can be reviewed')
    if r.decision == 'send_back' and not r.comment.strip():
        raise HTTPException(400, 'Say what needs changing')
    rec['status'] = 'approved' if r.decision == 'approve' else 'sent_back'
    rec['comments'].append({'by': 'Sarah', 'text': r.comment}); _log(rec['status'], rec, approved_by='Sarah' if r.decision == 'approve' else None)
    return rec


@app.post('/api/answers/{rid}/followup')
def api_followup(rid: str, f: FollowIn):
    """Interpret a follow-up against an approved answer: only what the follow-up states changes."""
    p = STORE.get(rid) or _404()
    r = interpret(f.question, p['audience'], book.hazards, book.d.years)
    ch = copy.deepcopy(p['choices']); src = dict(p['sources'])
    for k, v in r['choices'].items():
        if r['sources'].get(k) == 'question' and k not in ('measure', 'loan_type') and v not in (None, [], {}):
            if v != ch.get(k): ch[k] = v; src[k] = 'question'
    if r['sources'].get('rating') == 'question':
        ch['rating_min'], ch['rating_max'] = r['choices']['rating_min'], r['choices']['rating_max']
    return {'choices': ch, 'sources': src, 'flags': [x for x in r['flags'] if x['kind'] not in ('unstated', 'suggestion')],
            'question_years': p['question_years'], 'parent_id': rid, 'question': f'{p["question"]} → follow-up: {f.question}'}


@app.get('/api/answers')
def api_list():
    return list(STORE.values())


@app.get('/api/answers/{rid}')
def api_get(rid: str):
    return STORE.get(rid) or _404()


@app.get('/api/log')
def api_log():
    return LOG


@app.get('/api/answers/{rid}/export.xlsx')
def api_export(rid: str):
    rec = STORE.get(rid) or _404()
    res = rec['result']; buf = io.BytesIO()
    summary = pd.DataFrame({'Item': ['Question', 'Asked by', 'Answer'] + [f'Method {i+1}' for i in range(len(res['method_note']))]
                                     + [f"Check: {c['name']}" for c in res['checks']] + ['Status'],
                            'Value': [rec['question'], rec['asker'], res['headline']] + res['method_note']
                                     + [('PASS: ' if c['ok'] else 'FAIL: ') + c['detail'] for c in res['checks']] + [rec['status']]})
    with pd.ExcelWriter(buf, engine='openpyxl') as w:
        summary.to_excel(w, sheet_name='Answer', index=False)
        for name, df in source_rows(book, Choices.from_dict(rec['choices'])).items():
            df.to_excel(w, sheet_name=name[:31], index=False)
    buf.seek(0)
    return StreamingResponse(buf, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                             headers={'Content-Disposition': f'attachment; filename="answer-{rid}.xlsx"'})


@app.get('/')
def index():
    return FileResponse(os.path.join(os.path.dirname(__file__), 'static', 'index.html'))


def _404():
    raise HTTPException(404, 'Not found')
