"""Build a static, clickable demo of the prototype from the real UI (prototype/static/index.html).

Every answer is precomputed by engine.py; a small in-page mock stands in for the API.
    python3 prototype/demo/build_demo.py <out.html>
"""
import itertools, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from prototype.engine import Book, Choices, compute, defaults_for  # noqa: E402
from prototype.interpret import interpret  # noqa: E402

bk = Book(os.path.join(ROOT, 'runs', 'run-1'))
DIMS = {'region': sorted(bk.df.region.dropna().unique().tolist()), 'property_type': sorted(bk.df.property_type.dropna().unique().tolist())}
PRESETS = [
    'How many CRE loans have a flood rating of E or worse by 2050?',
    "What's our total expected climate loss by 2050?",
    'How much of our 2024 and 2025 lending went into high subsidence areas?',
    'How much do expected losses rise from 2030 to 2050 under the severe scenario?',
]
SCENS = ['central', 'severe', 'low']
EXS = [dict(in_default=a, redeemed=b, maturing_before=(2030 if m else None)) for a, b, m in itertools.product([True, False], repeat=3)]


def key(pid, c):
    ex = c['exclusions'] or {}
    f = ';'.join(f"{k}={','.join(sorted(v))}" for k, v in sorted((c.get('filters') or {}).items()) if v)
    return '|'.join([str(pid), ','.join(sorted(c['scenarios'])), ','.join(sorted(c['years'])), c.get('unit', 'loans'),
                     ''.join('1' if ex.get(k) else '0' for k in ('in_default', 'redeemed', 'maturing_before')), f])


def slim(res):
    keep = {k: res[k] for k in ('headline', 'versions', 'method_note', 'checks', 'counts', 'drivers')}
    keep['grid'] = [{'text': g['text']} for g in res['grid']]
    keep['verdicts'] = res.get('verdicts') or {}
    if res.get('versions_verdict'): keep['versions_verdict'] = res['versions_verdict']
    return keep


data = {'meta': {'export_as_at': bk.export_as_at, 'book_as_at': bk.book_as_at, 'hazards': bk.hazards, 'years': bk.d.years,
                 'scenarios': bk.scen_map, 'loan_types': sorted(bk.d.df.loan_type.unique().tolist()), 'dims': DIMS,
                 'audiences': {'committee': {'scenarios': ['central'], 'years': ['2050']}, 'pra': {'scenarios': ['central', 'severe'], 'years': ['2030', '2050']}, 'other': {'scenarios': ['central'], 'years': ['2050']}}},
        'presets': [], 'answers': {}, 'defaults': {a: defaults_for(a) for a in ('committee', 'pra', 'other')}}
n = 0
for pid, q in enumerate(PRESETS):
    data['presets'].append({'question': q, 'by_audience': {a: interpret(q, a, bk.hazards, bk.d.years, DIMS) for a in ('committee', 'pra', 'other')}})
    base = data['presets'][pid]['by_audience']['committee']
    yopts = [['2030', '2050']] if base['choices']['measure'] == 'rise' else [['2030'], ['2050'], ['2030', '2050']]
    units = ['loans', 'properties'] if base['choices']['measure'] == 'count' else ['loans']
    def add(c):
        k = key(pid, c)
        if k not in data['answers']:
            data['answers'][k] = slim(compute(bk, Choices.from_dict(c), base['question_years'], q))
    for r in range(1, 4):
        for sc in itertools.combinations(SCENS, r):
            for ys in yopts:
                for u in units:
                    for ex in EXS:
                        add(dict(base['choices'], scenarios=list(sc), years=list(ys), unit=u, exclusions=ex))
    # one added choice (a single region or property type), with each audience's default settings, and for follow-ups
    for d, vals in DIMS.items():
        for v in vals:
            for sc, ys in [(['central'], ['2050']), (['central', 'severe'], ['2030', '2050']), (['severe'], ['2050']), (['central'], ['2030'])]:
                if base['choices']['measure'] == 'rise': ys = ['2030', '2050']
                add(dict(base['choices'], scenarios=sc, years=ys, filters={d: [v]}))

ui = open(os.path.join(ROOT, 'prototype', 'static', 'index.html')).read()
title = re.search(r'<title>.*?</title>', ui, re.S).group(0)
style = re.search(r'<style>.*?</style>', ui, re.S).group(0)
body = re.search(r'<body>(.*)</body>', ui, re.S).group(1)
body = body.replace('<script>', '<script>' + open(os.path.join(os.path.dirname(__file__), 'mock_api.js')).read().replace('/*__DATA__*/null', json.dumps(data, separators=(',', ':'))) + '\n', 1)
page = f'{title}\n<meta name="claude:viewport-fit-sides" content="cover">\n{style}\n{body}'
open(sys.argv[1], 'w').write(page)
print(f"{len(data['answers'])} precomputed answers; {len(page)/1e6:.2f} MB")
