// Headless check (~10s): page loads, main flow clicks through, no errors. Run: node check_mvp.js
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  const t = (label, ok) => { console.log((ok ? 'PASS ' : 'FAIL ') + label); if (!ok) errs.push(label); };
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html`); await p.waitForSelector('body[data-ready="1"]');
  t('1 setup shows 22 of 22 sites', (await p.textContent('#s1')).includes('22 of 22 sites'));
  await p.click('#s1 .btn.primary');
  const h = await p.textContent('#headline'); t('2 brief headline £92m: ' + h.slice(0, 6), h.startsWith('£92m'));
  await p.click('#defOn'); t('defended toggle → £29m', (await p.textContent('#headline')).startsWith('£29m'));
  await p.click('#defOff'); await p.selectOption('#hold', '5'); t('5-year hold → £66m', (await p.textContent('#headline')).startsWith('£66m'));
  await p.selectOption('#hold', '7');
  await p.click('#s2 a:has-text("Why this number")'); t('3 site screen: Singapore office', (await p.textContent('#s3')).includes('Singapore office'));
  await p.click('#s3 .btn.primary'); await p.click('#send'); t('4 sent', await p.isVisible('#sentOk'));
  await p.click('#s4 .btn.primary'); await p.click('#example'); t('5 policy read, after total shown', (await p.textContent('#afterTotal')).startsWith('£76m'));
  await p.click('#apply'); await p.click('#s5 .btn.primary'); t('brief uses policy → £76m', (await p.textContent('#headline')).startsWith('£76m'));
  console.log(errs.length ? 'ERRORS: ' + errs.join(' | ') : 'All checks pass, no errors'); await b.close(); srv.close(); process.exit(errs.length ? 1 : 0);
})();
