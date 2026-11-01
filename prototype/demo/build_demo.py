"""Build a static, clickable demo of the prototype: every answer is precomputed by engine.py and replayed in the page.

    python3 prototype/demo/build_demo.py <out.html>

The page can't calculate new answers; it covers the preset questions and the choices you can toggle on the Confirm screen.
"""
import itertools, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from prototype.engine import Book, Choices, compute, defaults_for  # noqa: E402
from prototype.interpret import interpret  # noqa: E402

bk = Book(os.path.join(ROOT, 'runs', 'run-1'))
PRESETS = [
    ('cre', 'How many CRE loans have a flood rating of E or worse by 2050?', 'Credit committee'),
    ('cro', "What's our total expected climate loss by 2050?", 'CRO'),
    ('pricing', 'How much of our 2024 and 2025 lending went into high subsidence areas?', 'Mortgage pricing'),
    ('treasury', 'How much do expected losses rise from 2030 to 2050 under the severe scenario?', 'Treasury'),
]
SCENS = ['central', 'severe', 'low']
EXS = [dict(in_default=a, redeemed=b, maturing_before=(2030 if m else None)) for a, b, m in itertools.product([True, False], repeat=3)]


def key(pid, c):
    ex = c['exclusions'] or {}
    return '|'.join([pid, ','.join(sorted(c['scenarios'])), ','.join(sorted(c['years'])), c.get('unit', 'loans'),
                     ''.join('1' if ex.get(k) else '0' for k in ('in_default', 'redeemed', 'maturing_before'))])


def slim(res):
    return {k: res[k] for k in ('headline', 'versions', 'method_note', 'checks', 'counts', 'drivers')} | {
        'grid': [{'text': g['text']} for g in res['grid']], 'verdicts': res.get('verdicts') or {'scenario': res.get('versions_verdict')}}


out = {'meta': {'export_as_at': bk.export_as_at, 'book_as_at': bk.book_as_at, 'hazards': bk.hazards, 'years': bk.d.years},
       'presets': {}, 'answers': {}}
for pid, q, asker in PRESETS:
    out['presets'][pid] = {'question': q, 'asker': asker, 'by_audience': {}}
    for aud in ('committee', 'pra'):
        r = interpret(q, aud, bk.hazards, bk.d.years)
        out['presets'][pid]['by_audience'][aud] = {'choices': r['choices'], 'sources': r['sources'], 'flags': r['flags'],
                                                   'question_years': r['question_years'], 'defaults': defaults_for(aud)}
    base = interpret(q, 'committee', bk.hazards, bk.d.years)
    yopts = [['2030', '2050']] if base['choices']['measure'] == 'rise' else [['2030'], ['2050'], ['2030', '2050']]
    units = ['loans', 'properties'] if base['choices']['measure'] == 'count' else ['loans']
    for n in range(1, 4):
        for sc in itertools.combinations(SCENS, n):
            for ys in yopts:
                for u in units:
                    for ex in EXS:
                        c = dict(base['choices'], scenarios=list(sc), years=list(ys), unit=u, exclusions=ex)
                        out['answers'][key(pid, c)] = slim(compute(bk, Choices.from_dict(c), base['question_years'], q))
# the sent-back draft: wrong horizon, stale export, no scenario
r = interpret(PRESETS[0][1], 'committee', bk.hazards, bk.d.years)
draft = dict(r['choices'], years=['2030'], scenarios=[], exclusions={'in_default': True, 'redeemed': False, 'maturing_before': None})
out['draft'] = {'choices': draft, 'result': slim(compute(bk, Choices.from_dict(draft), r['question_years'], PRESETS[0][1]))}

tpl = open(os.path.join(os.path.dirname(__file__), 'demo_template.html')).read()
html = tpl.replace('/*__DATA__*/null', json.dumps(out, separators=(',', ':')))
open(sys.argv[1], 'w').write(html)
print(f"{len(out['answers'])} precomputed answers; {len(html)/1e6:.2f} MB")
