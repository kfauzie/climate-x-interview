// Test cases from the solution concept, run against the calculations in mvp.html.
// Expected numbers come from the Python engine (prototype/engine.py), calculated separately.
// Run: node runs/run-1/build/test_mvp.js
const fs = require('fs'), path = require('path'), assert = require('assert');
const html = fs.readFileSync(path.join(__dirname, 'mvp.html'), 'utf8');
const calc = html.match(/<script id="calc">([\s\S]*?)<\/script>/)[1];
const m = {exports: {}}; new Function('module', calc)(m); const C = m.exports;
const data = f => C.parseCsv(fs.readFileSync(path.join(__dirname, '..', 'data', f), 'utf8'));
const SP = data('spectra_portfolio_export.csv'), BK = data('loan_book_synthetic.csv');
const base = (o = {}) => ({scenario: 'severe', loans: 'all', from: '2030', to: '2050', exclusions: [...C.DEFAULT_EXCLUSIONS], ...o});
const close = (a, b, tol = 0.001) => assert(Math.abs(a - b) < tol, `${a} != ${b}`);
const draft = (q, choices = {}, sources = {}) => { const r = C.interpret(q); return {reading: r, choices: base({scenario: r.scenario || 'central', loans: r.loans || 'all', ...choices}),
  sources: {scenario: r.scenario ? 'question' : 'default', loans: r.loans ? 'question' : 'default', ...sources}}; };
let n = 0; const test = (name, f) => { f(); n++; console.log('ok  ', name); };

test("Treasury: severe rise 2030 to 2050 is 2.81x, £1.7m to £4.7m", () => {
  const r = C.interpret('How much do expected losses rise from 2030 to 2050 under the severe scenario?');
  assert.deepStrictEqual([r.scenario, r.years, r.loans, r.notes.length], ['severe', [2030, 2050], null, 0]);
  const R = C.rise(SP, BK, base());
  close(R.rise, 2.8128); close(R.from, 1671288, 1); close(R.to, 4700998, 1);
  assert.strictEqual(`${C.money(R.from)} → ${C.money(R.to)}`, '£1.7m → £4.7m');
});
test('Other scenarios shown next to it: central 1.58x, low 1.19x', () => {
  close(C.rise(SP, BK, base(), 'central').rise, 1.5791); close(C.rise(SP, BK, base(), 'low').rise, 1.1854);
});
test('Follow-up in one click: mortgages 2.70x, CRE 2.88x (severe)', () => {
  close(C.rise(SP, BK, base({loans: 'Residential mortgage'})).rise, 2.6951); close(C.rise(SP, BK, base({loans: 'Commercial real estate'})).rise, 2.8754);
});
test('Every loan accounted for: 2,000 = 1,832 counted + 148 left out + 20 not in the loan book', () => {
  const R = C.rise(SP, BK, base());
  assert.deepStrictEqual([R.total, R.counted, R.excluded, R.notInBook.length, R.missing.length], [2000, 1832, 148, 20, 40]);
  for (const l of ['Residential mortgage', 'Commercial real estate']) { const x = C.rise(SP, BK, base({loans: l})); assert.strictEqual(x.counted + x.excluded + x.notInBook.length, x.total); }
});
test('Rise by hazard: subsidence leads (4.00x)', () => {
  const R = C.rise(SP, BK, base()); assert.strictEqual(R.byHazard[0].hazard, 'subsidence'); close(R.byHazard[0].rise, 3.9976);
});
test('Treasury answer as drafted: nothing needs the approver\'s attention', () => {
  assert.deepStrictEqual(C.attention(draft('How much do expected losses rise from 2030 to 2050 under the severe scenario?')), []);
});
test('Follow-up "What about commercial property?": CRE, central by default, 1.59x', () => {
  const d = draft('What about commercial property?');
  assert.deepStrictEqual([d.choices.loans, d.choices.scenario, d.reading.notes.length], ['Commercial real estate', 'central', 0]);
  close(C.rise(SP, BK, d.choices).rise, 1.5874);
});
test('Sent-back case: counting redeemed loans is flagged for the approver', () => {
  const d = draft('How much do expected losses rise from 2030 to 2050 under the severe scenario?', {exclusions: ['default', 'mat2030']});
  assert.deepStrictEqual(C.attention(d), ['Counts loans your standard leaves out: redeemed since the export.']);
});
test('Scenario changed from the question is flagged', () => {
  const d = draft('How much do expected losses rise from 2030 to 2050 under the severe scenario?', {scenario: 'central'}, {scenario: 'analyst'});
  assert.deepStrictEqual(C.attention(d), ['Scenario: the question asks for severe; the answer uses central.']);
});
test('CRO "total expected climate loss by 2050": central by default, no warning', () => {
  const d = draft("What's our total expected climate loss by 2050?");
  assert.deepStrictEqual([d.choices.scenario, d.reading.years, d.reading.notes.length], ['central', [2030, 2050], 0]);
});
test('Out of scope: credit committee count question gets the closest answer, with a note', () => {
  const r = C.interpret('How many CRE loans have a flood rating of E or worse by 2050?');
  assert.strictEqual(r.loans, 'Commercial real estate'); assert.strictEqual(r.notes.length, 1);
});
test('A year the data does not have (2040) says so', () => {
  assert.match(C.interpret('How much do losses rise from 2030 to 2040?').notes[0], /2030 and 2050 only/);
});
test('Reply to Treasury is written from the numbers', () => {
  const c = base(), R = C.rise(SP, BK, c), per = {low: C.rise(SP, BK, c, 'low').rise, central: C.rise(SP, BK, c, 'central').rise, severe: R.rise};
  const t = C.emailText(c, R, per, {full: 'Sarah Okafor', role: 'Head of Climate Risk'});
  assert.strictEqual(t[1], 'Under the severe scenario, our expected climate losses rise **2.81×** from 2030 to 2050: from £1.7m a year to £4.7m a year.');
  assert.strictEqual(t[2], "For comparison: 1.58× under the central scenario (today's policies) and 1.19× with emissions cut fast. Most of the rise comes from subsidence.");
});
console.log(`\n${n} passed`);
