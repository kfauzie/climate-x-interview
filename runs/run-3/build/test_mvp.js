// Test cases from the solution concept, run against the calculations in mvp.html. Run: node runs/run-3/build/test_mvp.js
const fs = require('fs'), path = require('path'), assert = require('assert');
const calc = fs.readFileSync(path.join(__dirname, 'mvp.html'), 'utf8').match(/<script id="calc">([\s\S]*?)<\/script>/)[1];
const m = {exports: {}}; new Function('module', calc)(m); const C = m.exports;
const sites = C.parseCsv(fs.readFileSync(path.join(__dirname, '..', 'data', 'northwind_renewables_spectra_infra_2026-09.csv'), 'utf8'));
const R = C.DEFAULT_RULE, byId = id => sites.find(s => s.site_id === id);
let n = 0; const test = (name, f) => { f(); n++; console.log('ok  ', name); };
const close = (a, b, t = 0.5) => assert(Math.abs(a - b) <= t, `${a} != ${b}`);

test('Default rule (E or worse, severe, 2050): 24 sites need a plan, 38 do not', () => {
  const {need, clear} = C.screen(sites, R); assert.deepStrictEqual([need.length, clear.length], [24, 38]); });
test("Under today's policies, 8 sites need a plan, all river flood, 7 of them UK battery sites", () => {
  const need = C.screen(sites, {...R, scenario: 'central'}).need; assert.strictEqual(need.length, 8);
  assert(need.every(s => C.flagged(s, {...R, scenario: 'central'}).join() === 'flood_river'));
  assert.strictEqual(need.filter(s => s.asset_type === 'battery' && s.country === 'UK').length, 7); });
test("The 8 under today's policies are all inside the 24 under severe", () => {
  const sev = new Set(C.screen(sites, R).need.map(s => s.site_id)); assert(C.screen(sites, {...R, scenario: 'central'}).need.every(s => sev.has(s.site_id))); });
test('4 of the 24 are scored at a single point: S014, S017, S027, S038', () => {
  assert.deepStrictEqual(C.screen(sites, R).need.filter(s => s.location_type === 'point').map(s => s.site_id).sort(), ['S014', 'S017', 'S027', 'S038']); });
test('A blank wildfire score is not counted as a rating, and counts as £0 in loss', () => {
  const s = byId('S001'); assert(!C.flagged(s, R).includes('wildfire')); close(C.totalLoss(s, 'central', '2030'), 154700 + 30200 + 7000 + 5400); });
test('S010 expected loss a year: £415,200 river flood by 2030 under severe (from Spectra)', () => {
  close(+byId('S010').flood_river_ssp585_2030_loss_gbp, 415200); });
test('Payback = cost ÷ loss avoided a year, for every measure', () => {
  for (const s of C.screen(sites, R).need) for (const x of C.measures(s, R)) close(x.payback, x.cost / x.avoided, 1e-9); });
test('Recommendation: biggest saving that pays back within 5 years, else the quickest', () => {
  for (const s of C.screen(sites, R).need) { const ms = C.measures(s, R), r = C.recommend(ms); if (!ms.length) continue;
    const ok = ms.filter(x => x.payback <= 5); if (ok.length) assert.strictEqual(r.avoided, Math.max(...ok.map(x => x.avoided)));
    else assert.strictEqual(r.payback, Math.min(...ms.map(x => x.payback))); } });
test('Every site that needs a plan has at least one measure to choose from', () => {
  for (const s of C.screen(sites, R).need) assert(C.measures(s, R).length > 0, s.site_id); });
test('Bank totals add up: before = sum of each site, after = before minus loss avoided', () => {
  const need = C.screen(sites, R).need, pick = s => C.recommend(C.measures(s, R)), t = C.bankTotals(need, R, pick);
  close(t.before, need.reduce((a, s) => a + C.totalLoss(s, 'severe', '2050'), 0));
  close(t.after, t.before - need.reduce((a, s) => a + pick(s).avoided2050, 0)); assert(t.after < t.before); });
test('A consultant quote is never used as a source: costs come from the synthetic Adapt table', () => {
  const s = byId('S010'), x = C.measures(s, R)[0]; const share = C.ADAPT_MEASURES_SYNTHETIC.find(a => a.name === x.name && a.hazard === x.hazard).costShare;
  close(x.cost, Math.round(+s.asset_value_gbp * share / 1e4) * 1e4); });
console.log(`\n${n} passed`);
