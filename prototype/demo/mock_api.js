// In-page stand-in for prototype/app.py, replaying answers precomputed by engine.py (demo only).
(() => {
const D = /*__DATA__*/null;
const STORE = {}; let seq = 1;
const cl = o => JSON.parse(JSON.stringify(o));
const norm = s => s.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/\s+/g, ' ').trim();
const DEFAULTED = ['scenarios','years','exclusions','unit','origination_source'];
const err = m => { throw new Error(m); };
function key(pid, c) {
  const ex = c.exclusions || {};
  const f = Object.entries(c.filters || {}).filter(([,v]) => v && v.length).sort(([a],[b]) => a < b ? -1 : 1).map(([k,v]) => `${k}=${[...v].sort().join(',')}`).join(';');
  return [pid, [...c.scenarios].sort().join(','), [...c.years].sort().join(','), c.unit || 'loans', ['in_default','redeemed','maturing_before'].map(k => ex[k] ? '1' : '0').join(''), f].join('|');
}
const audKey = a => ['committee','pra'].includes(a) ? a : 'other';
function departures(c, src, aud) { const d = D.defaults[audKey(aud)];
  return DEFAULTED.filter(f => src[f] === 'analyst' && JSON.stringify(c[f]) !== JSON.stringify(d[f])).map(f => ({field:f, default:d[f], chosen:c[f]})); }
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
function presetOf(q) { const n = norm(q); const i = D.presets.findIndex(p => norm(p.question) === n); return i; }
window.demoNote = 'Clickable demo: answers were calculated in advance by the prototype’s code on practice data and a made-up loan book. Use the example questions (any wording that matches them), change any setting, add one region or property type, and try the follow-ups. New questions need the full app.';
window.mockApi = async (path, body) => {
  if (path === '/api/meta') return D.meta;
  if (path === '/api/answers') return Object.values(STORE);
  let m;
  if ((m = path.match(/^\/api\/answers\/(\w+)$/))) return STORE[m[1]];
  if (path === '/api/interpret') {
    if (body.question.trim().split(/\s+/).length < 3) err('Add the question as the asker wrote it');
    const i = presetOf(body.question); if (i < 0) err('This demo only has answers for the example questions. Pick one under “Try an example”.');
    const r = cl(D.presets[i].by_audience[audKey(body.audience)]); r.defaults = D.defaults[audKey(body.audience)]; r.audience_key = audKey(body.audience); r.pid = i; return r;
  }
  if (path === '/api/compute') {
    const c = body.choices; const pid = presetOf(body.question.split(' → follow-up:')[0]);
    const deps = departures(c, body.sources, body.audience); const p = body.parent_id && STORE[body.parent_id];
    const reasons = {...body.reasons};
    if (p) deps.forEach(d => { if (p.departures.some(x => same(x, d)) && !reasons[d.field]) reasons[d.field] = p.reasons[d.field]; });
    const missing = deps.filter(d => !(reasons[d.field] || '').trim()).map(d => d.field);
    if (missing.length) err(`Give a reason for each change from Sarah's defaults: ${missing.join(', ')}`);
    const fixed = D.presets[pid].by_audience.committee.choices;
    for (const f of ['measure','loan_type','hazards','rating_min','rating_max','originated','origination_source'])
      if (!same(c[f], fixed[f])) err('That change needs the full app: this demo can change scenario, years, counting, exclusions and one added region or property type.');
    const result = D.answers[key(pid, c)]; if (!result) err('That combination wasn’t calculated for this demo. Try one region or property type at a time.');
    const id = 'd' + seq++;
    const rec = {id, question:body.question, audience:body.audience, asker:body.asker, choices:cl(c), sources:cl(body.sources), question_years:body.question_years, reasons, departures:deps,
      result, status:'draft', parent_id:body.parent_id, comments:[], fast_track:false, diff:[], defaults:D.defaults[audKey(body.audience)]};
    if (p) {
      rec.diff = Object.keys(c).filter(k => !same(p.choices[k], c[k])).map(k => ({field:k, from:p.choices[k], to:c[k]}));
      const f0 = rec.diff[0]?.field;
      const fromQ = f0 === 'filters' ? Object.keys(c.filters || {}).every(k => same((p.choices.filters || {})[k], c.filters[k]) || body.sources['filter:' + k] === 'question') : body.sources[f0] === 'question';
      rec.fast_track = p.status === 'approved' && rec.diff.length === 1 && fromQ && deps.every(d => p.departures.some(x => same(x, d))) && result.checks.every(x => x.ok);
      rec.parent_headline = p.result.headline;
    }
    STORE[id] = rec; return rec;
  }
  if ((m = path.match(/^\/api\/answers\/(\w+)\/submit$/))) { const r = STORE[m[1]]; const f = r.result.checks.filter(x => !x.ok).map(x => x.name);
    if (f.length && !body.comment.trim()) err(`Add a comment for the failed checks: ${f.join(', ')}`); r.status = 'submitted'; r.comments.push({by:'analyst', text:body.comment}); return r; }
  if ((m = path.match(/^\/api\/answers\/(\w+)\/review$/))) { const r = STORE[m[1]];
    if (body.decision === 'send_back' && !body.comment.trim()) err('Say what needs changing');
    r.status = body.decision === 'approve' ? 'approved' : 'sent_back'; r.comments.push({by:'Sarah', text:body.comment}); return r; }
  if ((m = path.match(/^\/api\/answers\/(\w+)\/followup$/))) {
    const p = STORE[m[1]]; const q = body.question.toLowerCase(); const c = cl(p.choices), s = cl(p.sources); let qy = [];
    const sc = []; if (/severe|stress|worst/.test(q)) sc.push('severe'); if (/central|base/.test(q)) sc.push('central'); if (/low[- ]emission/.test(q)) sc.push('low');
    if (sc.length) { c.scenarios = sc; s.scenarios = 'question'; }
    const ys = (body.question.match(/\b20[3-9]\d\b/g) || []).filter(y => D.meta.years.includes(y)); if (ys.length) { c.years = [...new Set(ys)].sort(); s.years = 'question'; qy = ys; }
    for (const [d, vals] of Object.entries(D.meta.dims)) { const hit = vals.filter(v => q.includes(v.toLowerCase())); if (hit.length) { c.filters = {...(c.filters || {}), [d]: hit}; s['filter:' + d] = 'question'; } }
    if (!sc.length && !ys.length && !Object.keys(c.filters || {}).some(d => !same(c.filters[d], (p.choices.filters || {})[d]))) err('In this demo, follow-ups can change the scenario, the year or the region. Try one of the examples.');
    return {choices:c, sources:s, flags:[], question_years:qy.length ? qy : p.question_years, parent_id:p.id, question:`${p.question} → follow-up: ${body.question}`};
  }
  err('Not available in this demo');
};
})();
