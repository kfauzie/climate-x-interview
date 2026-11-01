"""Question → structured choices (the interpretation step). Never produces a number.

This prototype uses a rule-based interpreter so it runs offline and deterministically. The design's
AI interpreter plugs in behind the same function: it must return the same structure, validated against
ALLOWED, and the analyst confirms every choice before anything is computed. The tests in
tests/test_interpret.py are the golden set for checking that interpreter.
"""
from __future__ import annotations
import re
from .engine import Choices, defaults_for, RATINGS

ALLOWED = {'measure': ['count', 'loss', 'rise', 'share'], 'loan_type': [None, 'Residential mortgage', 'Commercial real estate'],
           'scenarios': ['central', 'severe', 'low'], 'unit': ['loans', 'properties']}
OUT_OF_SCOPE = r'loss to the bank|credit loss|\blgd\b|provision|capital (impact|charge)|expected credit'


def interpret(question: str, audience: str, hazards: list, years_available: list) -> dict:
    q = question.strip(); ql = q.lower()
    c = Choices(); src = {}; flags = []
    d = defaults_for(audience)

    if q.count('?') > 1:
        flags.append({'kind': 'split', 'text': f'This looks like {q.count("?")} questions. Split them into separate requests?'})
    if re.search(OUT_OF_SCOPE, ql):
        flags.append({'kind': 'out_of_scope', 'text': 'Loss to the bank needs default-loss and insurance data that isn\'t loaded. Showing damage to properties instead?'})

    # measure
    if re.search(r'how many', ql): c.measure = 'count'
    elif re.search(r'how much of (our|the)?.*lending|share of|% of|percent', ql): c.measure = 'share'
    elif re.search(r'\brise|increase|grow|go up|from (19|20)\d\d to (19|20)\d\d', ql): c.measure = 'rise'
    elif re.search(r'total|expected .*loss|loss|damage|driving|which hazard|which region', ql): c.measure = 'loss'
    src['measure'] = 'question'
    if re.search(r'which hazard|by hazard|driving', ql): c.group_by.append('hazard')
    if re.search(r'which region|by region|where', ql): c.group_by.append('region')
    if c.measure == 'loss' and not c.group_by: c.group_by = ['hazard', 'region']

    # loans
    if re.search(r'\bcre\b|commercial', ql): c.loan_type = 'Commercial real estate'; src['loan_type'] = 'question'
    elif re.search(r'mortgage|residential|homes?\b', ql): c.loan_type = 'Residential mortgage'; src['loan_type'] = 'question'
    else: src['loan_type'] = 'question'
    m = re.findall(r'\b(20\d\d)\b(?=[^?]*lending)', q)
    if re.search(r'lending', ql) and m:
        c.originated = sorted({int(y) for y in m}); src['originated'] = 'question'

    if c.loan_type == 'Commercial real estate' and c.measure == 'count':
        flags.append({'kind': 'suggestion', 'field': 'exclusions', 'text': 'Your CRE write-up also excluded loans maturing before 2030. Apply that here?'})

    # hazards and rating band
    hz = [h for h in hazards if h in ql]
    c.hazards = hz; src['hazards'] = 'question' if hz else 'default'
    if 'flood' in hz:
        flags.append({'kind': 'ambiguous', 'field': 'hazards', 'text': "'Flood': this file has one flood measure. Your write-ups combine river and coastal. Confirm that's the same."})
    m = re.search(r'\b([A-G]) or worse', q) or re.search(r'rat(?:ed|ing) (?:of )?([A-G])\b', q)
    m2 = re.search(r'\b([A-G]) to ([A-G])\b', q)
    if m2: c.rating_min, c.rating_max = m2.group(1), m2.group(2); src['rating'] = 'question'
    elif m: c.rating_min = m.group(1); src['rating'] = 'question'
    elif re.search(r'\bhigh\b', ql) and c.measure in ('count', 'share'):
        c.rating_min, c.rating_max = 'E', 'G'; src['rating'] = 'default'
        flags.append({'kind': 'unstated', 'field': 'rating', 'text': "'High' taken as rated E to G, as in your write-ups."})

    # years
    qy = re.findall(r'\b(20[3-9]\d)\b', q)
    years_q = [y for y in qy if y in years_available]
    if re.search(r'present[- ]day|today|current rating', ql):
        flags.append({'kind': 'not_in_data', 'field': 'years', 'text': f"Present-day ratings aren't in this export ({' and '.join(years_available)} only)."})
    if c.measure == 'rise' and len(years_q) >= 2:
        c.years = years_q[:2]; src['years'] = 'question'
    elif years_q:
        c.years = sorted(set(years_q)); src['years'] = 'question'
    else:
        c.years = d['years']; src['years'] = 'default'
        flags.append({'kind': 'unstated', 'field': 'years', 'text': f"The asker didn't say which year. Using {', '.join(c.years)} ({audience} default)."})
    unknown = [y for y in qy if y not in years_available]
    if unknown:
        flags.append({'kind': 'not_in_data', 'field': 'years', 'text': f"{', '.join(unknown)} isn't in this export ({' and '.join(years_available)} only)."})

    # scenario
    sc = []
    if re.search(r'severe|stress|worst|ssp585|high[- ]emission', ql): sc.append('severe')
    if re.search(r'central|base|ssp245|middle', ql): sc.append('central')
    if re.search(r'low[- ]emission|ssp126|net zero', ql): sc.append('low')
    if sc:
        c.scenarios = sc; src['scenarios'] = 'question'
    else:
        c.scenarios = d['scenarios']; src['scenarios'] = 'default'
        flags.append({'kind': 'unstated', 'field': 'scenarios', 'text': f"The asker didn't say which scenario. Using {' and '.join(c.scenarios)} ({audience} default)."})

    for f in ('exclusions', 'unit', 'origination_source'):
        src[f] = 'default'
    understood = bool(hz or c.measure != 'count' or re.search(r'how many', ql))
    return {'choices': c.__dict__, 'sources': src, 'flags': flags, 'question_years': qy, 'understood': understood}
