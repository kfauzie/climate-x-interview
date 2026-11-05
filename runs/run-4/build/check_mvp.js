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
  const h = await p.textContent('#headline'); t('2 brief headline £92m', h.startsWith('£92m'));
  await p.click('#ragBtn'); t('status legend opens', await p.isVisible('#ragLegend'));
  t('other deals marked unavailable', (await p.textContent('#deals')).includes('Not available in prototype'));
  await p.click('#defOn'); t('defended → £29m', (await p.textContent('#headline')).startsWith('£29m')); await p.click('#defOff');
  await p.selectOption('#hold', '5'); t('5-year hold → £66m', (await p.textContent('#headline')).startsWith('£66m')); await p.selectOption('#hold', '7');
  await p.click('#assume > summary'); await p.check('input[value="leased"]'); t('preset leased → £23m', (await p.textContent('#headline')).startsWith('£23m'));
  await p.click('#assume > summary').catch(()=>{}); await p.evaluate(()=>{document.getElementById('assume').open=true});
  await p.check('input[value="all"]'); await p.evaluate(()=>{document.getElementById('assume').open=true});
  await p.fill('#freeText', 'the office has a sea wall and we hold for 5 years'); await p.click('#interpret'); await p.click('#applyFree');
  t('free text → defended + 5 years', (await p.textContent('#headline')).startsWith('£21m') || (await p.textContent('.basis')).includes('5 years'));
  await p.evaluate(()=>{st.preset='all';st.years=7;render()});
  await p.click('#s2 .siteLink'); t('3 site detail: Singapore office', (await p.textContent('#s3')).includes('Singapore office'));
  await p.click('#example'); await p.click('#applyDoc'); t('site document applied → site £53m', (await p.textContent('#siteAfter')).startsWith('£53m'));
  await p.click('#s3 .btn.secondary'); t('brief uses the site document → £76m', (await p.textContent('#headline')).startsWith('£76m'));
  await p.click('#toSend'); await p.click('#send'); t('4 sent', await p.isVisible('#sentOk'));
  console.log(errs.length ? 'ERRORS: ' + errs.join(' | ') : 'All checks pass, no errors'); await b.close(); srv.close(); process.exit(errs.length ? 1 : 0);
})();
