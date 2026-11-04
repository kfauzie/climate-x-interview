// Quick check after each change: loads, nothing covers it, the main flow clicks through, no page errors. No screenshots.
const http = require('http'), fs = require('fs'), path = require('path'), {chromium} = require('playwright');
const root = path.join(__dirname, '..'), types = {'.html': 'text/html', '.csv': 'text/csv'};
const server = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, {'Content-Type': types[path.extname(f)] || 'text/plain'}); r.end(b); }); });
(async () => {
  const t0 = Date.now(); await new Promise(r => server.listen(0, r));
  const b = await chromium.launch(), p = await b.newPage(), errors = []; p.on('pageerror', e => errors.push(e.message));
  const step = async (name, f) => { try { await f(); console.log('ok  ', name); } catch (e) { console.log('FAIL', name, '-', e.message.split('\n')[0]); process.exitCode = 1; } };
  await p.goto(`http://localhost:${server.address().port}/build/mvp.html`);
  await step('Screen sites loads: 24 need a plan, 38 don\'t; nothing covering it', async () => {
    await p.waitForFunction(() => document.querySelector('#headline')?.textContent.includes('24 need a plan · 38'), null, {timeout: 5000});
    if (await p.isVisible('#ov')) throw new Error('overlay showing'); });
  await step("Changing the rule recalculates (today's policies → 8), then back", async () => {
    await p.selectOption('[data-rule="scenario"]', 'central'); await p.waitForFunction(() => document.querySelector('#headline').textContent.startsWith('8 need'));
    await p.selectOption('[data-rule="scenario"]', 'severe'); await p.waitForFunction(() => document.querySelector('#headline').textContent.startsWith('24 need')); });
  await step('Check locations: 4 single-point sites, all confirmed', async () => {
    await p.click('#go-loc'); await p.waitForSelector('#s-locations');
    for (let k = 0; k < 4; k++) await p.click('[data-loc$="|right"] >> nth=0');
    if (await p.locator('[data-loc]').count()) throw new Error('unconfirmed left'); });
  await step('Plan each site: a recommendation shows; walk through all 24', async () => {
    await p.click('#go-plan'); await p.waitForSelector('#rec');
    for (let k = 0; k < 24; k++) await p.click('#use');
    await p.waitForSelector('#s-doc'); });
  await step('Bank document: headline before → after, send works', async () => {
    const h = await p.textContent('#doc-headline'); if (!/→/.test(h) || /NaN|nan/.test(h)) throw new Error(h);
    await p.click('#send'); await p.waitForFunction(() => document.querySelector('#send')?.textContent.includes('Sent'), null, {timeout: 4000}); });
  await step('No errors on the page', async () => { if (errors.length) throw new Error(errors.join('; ')); });
  await b.close(); server.close(); console.log(`\nchecked in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
})();
