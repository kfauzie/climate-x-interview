"""Test set from runs/run-1 (see solution-design.md), plus the review flow.  Run:  python3 -m pytest prototype/tests -q"""
import os
import pytest
from fastapi.testclient import TestClient

os.environ.setdefault('RUN_DIR', os.path.join(os.path.dirname(__file__), '..', '..', 'runs', 'run-1'))
from prototype.app import app, book  # noqa: E402
from prototype.engine import Choices, compute  # noqa: E402
from prototype.interpret import interpret  # noqa: E402

client = TestClient(app)
CRE_Q = 'How many CRE loans have a flood rating of E or worse by 2050?'


def ask(q, audience='committee'):
    r = client.post('/api/interpret', json={'question': q, 'audience': audience, 'asker': 'test'}); assert r.status_code == 200, r.text
    return r.json()


def run(q, audience='committee', edit=None, reasons=None, parent=None):
    r = ask(q, audience)
    if edit: edit(r)
    body = {'question': q, 'audience': audience, 'asker': 'test', 'choices': r['choices'], 'sources': r['sources'],
            'question_years': r['question_years'], 'reasons': reasons or {}, 'parent_id': parent}
    x = client.post('/api/compute', json=body); return x


# ---- interpretation (golden set for any future AI interpreter) ----
@pytest.mark.parametrize('q,expect', [
    (CRE_Q, {'measure': 'count', 'loan_type': 'Commercial real estate', 'hazards': ['flood'], 'rating_min': 'E', 'years': ['2050'], 'scenarios': ['central']}),
    ("What's our total expected climate loss by 2050?", {'measure': 'loss', 'years': ['2050'], 'scenarios': ['central']}),
    ('How much of our 2024 and 2025 lending went into high subsidence areas?', {'measure': 'share', 'hazards': ['subsidence'], 'originated': [2024, 2025], 'rating_min': 'E', 'rating_max': 'G'}),
    ('How much do expected losses rise from 2030 to 2050 under the severe scenario?', {'measure': 'rise', 'years': ['2030', '2050'], 'scenarios': ['severe']}),
])
def test_interpret_golden(q, expect):
    r = interpret(q, 'committee', book.hazards, book.d.years)
    for k, v in expect.items():
        assert r['choices'][k] == v, (k, r['choices'][k])


def test_unstated_scenario_is_flagged_and_defaulted():
    r = ask(CRE_Q)
    assert r['sources']['scenarios'] == 'default'
    assert any(f['kind'] == 'unstated' and f['field'] == 'scenarios' for f in r['flags'])


def test_pra_defaults():
    r = ask('How many CRE loans have a flood rating of E or worse?', 'pra')
    assert r['choices']['scenarios'] == ['central', 'severe'] and r['choices']['years'] == ['2030', '2050']


def test_out_of_scope_and_not_in_data_flags():
    assert any(f['kind'] == 'out_of_scope' for f in ask('What is the loss to the bank from flood by 2050?')['flags'])
    assert any(f['kind'] == 'not_in_data' for f in ask('How many CRE loans have a present-day flood rating of E or worse?')['flags'])


# ---- computed answers ----
def test_cre_flood_answer_and_verdict():
    rec = run(CRE_Q).json(); r = rec['result']
    d = r['grid'][0]['detail']
    assert (d['n'], d['of_n'], round(d['balance'] / 1e5) / 10) == (3, 144, 5.4)   # default exclusions incl. maturing before 2030
    assert all(c['ok'] for c in r['checks'])
    sev = next(v for v in r['versions'] if 'severe' in v['change']); assert sev['value'] == 5
    assert [x['loan_id'] for x in r['rows']] == ['L101880', 'L101854', 'L100322']
    assert 'same answer' in r['verdicts']['scenario']           # central and low give the same count
    assert any('Spectra export as at 2026-06-30' in l for l in r['method_note'])


def test_cre_flood_without_exclusions_matches_practice_profile():
    def no_ex(r): r['choices']['exclusions'] = {}; r['sources']['exclusions'] = 'analyst'
    rec = run(CRE_Q, edit=no_ex, reasons={'exclusions': 'compare with the raw export'}).json()
    d = rec['result']['grid'][0]['detail']
    assert (d['n'], round(d['balance'])) == (4, 7148900)        # matches the run 1 Profile (no loan book)


def test_rise_severe():
    r = run('How much do expected losses rise from 2030 to 2050 under the severe scenario?').json()['result']
    assert 2.6 < r['grid'][0]['value'] < 2.9


def test_share_flags_spectra_origination():
    def spectra(r): r['choices']['origination_source'] = 'spectra'; r['sources']['origination_source'] = 'analyst'
    rec = run('How much of our 2024 and 2025 lending went into high subsidence areas?', edit=spectra,
              reasons={'origination_source': 'loan system down'}).json()
    chk = next(c for c in rec['result']['checks'] if c['name'] == 'Origination date source'); assert not chk['ok']


def test_sent_back_draft_fails_three_checks():
    """Present-day/wrong horizon, stale export (redeemed loans included), no scenario stated."""
    r = interpret(CRE_Q, 'committee', book.hazards, book.d.years)
    c = Choices.from_dict(r['choices']); c.years = ['2030']; c.exclusions = {'in_default': True}; c.scenarios = []
    failed = {x['name'] for x in compute(book, c, r['question_years'])['checks'] if not x['ok']}
    assert failed == {'Horizon matches the question', 'Data is fresh', 'Scenario stated'}


def test_departure_needs_reason():
    def sev(r): r['choices']['scenarios'] = ['severe']; r['sources']['scenarios'] = 'analyst'
    assert run(CRE_Q, edit=sev).status_code == 400
    assert run(CRE_Q, edit=sev, reasons={'scenarios': 'asked on the phone'}).status_code == 200


def test_same_inputs_same_number():
    a, b = run(CRE_Q).json(), run(CRE_Q).json()
    assert a['result']['headline'] == b['result']['headline']


# ---- review flow and fast-track ----
def test_review_and_fast_track_followup():
    rec = run(CRE_Q).json(); rid = rec['id']
    assert client.post(f'/api/answers/{rid}/review', json={'decision': 'approve'}).status_code == 400   # not submitted yet
    client.post(f'/api/answers/{rid}/submit', json={'comment': ''})
    assert client.post(f'/api/answers/{rid}/review', json={'decision': 'approve'}).json()['status'] == 'approved'
    fu = client.post(f'/api/answers/{rid}/followup', json={'question': 'What about the severe scenario?'}).json()
    assert fu['choices']['scenarios'] == ['severe'] and fu['sources']['scenarios'] == 'question'
    x = client.post('/api/compute', json={'question': fu['question'], 'audience': 'committee', 'asker': 'test', 'choices': fu['choices'],
                                          'sources': fu['sources'], 'question_years': fu['question_years'], 'reasons': {}, 'parent_id': rid}).json()
    assert x['fast_track'] and x['diff'] == [{'field': 'scenarios', 'from': ['central'], 'to': ['severe']}]


def test_failed_checks_need_comment_and_send_back_needs_reason():
    def stale(r): r['choices']['exclusions'] = {'in_default': True}; r['sources']['exclusions'] = 'analyst'
    rec = run(CRE_Q, edit=stale, reasons={'exclusions': 'testing'}).json()
    assert client.post(f"/api/answers/{rec['id']}/submit", json={'comment': ''}).status_code == 400
    assert client.post(f"/api/answers/{rec['id']}/submit", json={'comment': 'known stale'}).status_code == 200
    assert client.post(f"/api/answers/{rec['id']}/review", json={'decision': 'send_back'}).status_code == 400


def test_excel_export():
    rec = run(CRE_Q).json()
    x = client.get(f"/api/answers/{rec['id']}/export.xlsx")
    assert x.status_code == 200 and x.content[:2] == b'PK'


# ---- feedback round 1: free text, added choices, follow-ups keep approved changes ----
def test_free_text_audience_uses_other_defaults():
    r = client.post('/api/interpret', json={'question': CRE_Q, 'audience': 'Board ESG committee', 'asker': 'x'}).json()
    assert r['audience_key'] == 'other' and r['choices']['scenarios'] == ['central']


def test_region_in_question_becomes_a_choice():
    r = ask('How many CRE loans in the South East have a flood rating of E or worse by 2050?')
    assert r['choices']['filters'] == {'region': ['South East']} and r['sources']['filter:region'] == 'question'


def test_added_region_filters_the_answer_and_note():
    def add(r): r['choices']['filters'] = {'region': ['London']}; r['sources']['filter:region'] = 'added'
    rec = run(CRE_Q, edit=add).json()
    assert 'in London' in rec['result']['headline'] and any('region: London' in l for l in rec['result']['method_note'])
    def bad(r): r['choices']['filters'] = {'region': ['Atlantis']}
    assert run(CRE_Q, edit=bad).status_code == 400


def test_followup_keeps_an_approved_departure_and_fast_tracks():
    def sev(r): r['choices']['scenarios'] = ['central', 'severe']; r['sources']['scenarios'] = 'analyst'
    rec = run(CRE_Q, edit=sev, reasons={'scenarios': 'board wants stress view'}).json()
    client.post(f"/api/answers/{rec['id']}/submit", json={'comment': ''}); client.post(f"/api/answers/{rec['id']}/review", json={'decision': 'approve'})
    fu = client.post(f"/api/answers/{rec['id']}/followup", json={'question': 'And by 2030?'}).json()
    assert fu['question_years'] == ['2030']
    x = client.post('/api/compute', json={'question': fu['question'], 'audience': 'committee', 'asker': 't', 'choices': fu['choices'], 'sources': fu['sources'],
                                          'question_years': fu['question_years'], 'reasons': {}, 'parent_id': rec['id']}).json()
    assert x['reasons']['scenarios'] == 'board wants stress view' and x['fast_track']


def test_preview_skips_reasons_but_sending_needs_them():
    def sev(r): r['choices']['scenarios'] = ['severe']; r['sources']['scenarios'] = 'analyst'
    r = ask(CRE_Q); sev(r)
    body = {'question': CRE_Q, 'audience': 'committee', 'asker': 'test', 'choices': r['choices'], 'sources': r['sources'], 'question_years': r['question_years']}
    assert client.post('/api/compute', json={**body, 'preview': True}).status_code == 200
    assert client.post('/api/compute', json=body).status_code == 400


def test_draft_review_send():
    rec = run(CRE_Q).json()
    assert client.post(f"/api/answers/{rec['id']}/send").status_code == 400          # not approved yet
    client.post(f"/api/answers/{rec['id']}/submit", json={'comment': ''})
    client.post(f"/api/answers/{rec['id']}/review", json={'decision': 'approve', 'comment': ''})
    assert client.post(f"/api/answers/{rec['id']}/send").json()['status'] == 'sent'


STRESS_Q = 'For the stress test, how many CRE loans have a flood rating of E or worse?'


def test_stress_test_question_uses_pra_standard_and_one_answer_with_four_cells():
    r = ask(STRESS_Q, 'pra')
    assert r['choices']['scenarios'] == ['central', 'severe'] and r['choices']['years'] == ['2030', '2050']
    assert 'stress test' in r['matched'] and 'CRE loans' in r['matched']
    res = run(STRESS_Q, 'pra').json()['result']
    cells = {(g['scenario'], g['year']): g['value'] for g in res['grid']}
    assert cells == {('central', '2030'): 4, ('central', '2050'): 3, ('severe', '2030'): 4, ('severe', '2050'): 5}
    assert res['rows_cell'] == {'scenario': 'severe', 'year': '2050'} and res['rows_total'] == 5


def test_departure_shows_its_effect_on_the_answer():
    def incl_maturing(r): r['choices']['exclusions'] = {'in_default': True, 'redeemed': True, 'maturing_before': None}; r['sources']['exclusions'] = 'analyst'
    rec = run(STRESS_Q, 'pra', edit=incl_maturing, reasons={'exclusions': 'The stress test covers the whole book'}).json()
    eff = next(e for e in rec['effects'] if e['field'] == 'exclusions')
    sev = next(c for c in eff['cells'] if c['scenario'] == 'severe' and c['year'] == '2050')
    assert (sev['value'], sev['standard']) == (8, 5)


def test_typed_exclusions():
    assert client.post('/api/exclusion', json={'text': 'loans maturing before 2035'}).json() == {'key': 'maturing_before', 'value': 2035, 'label': 'Maturing before 2035'}
    r = client.post('/api/exclusion', json={'text': 'loans in arrears'})
    assert r.status_code == 400 and 'Closest: loans in default' in r.json()['detail']
