// Quick check after each change: the page loads, nothing blocks it, and the main flow can be clicked through.
// No screenshots. Run: node runs/run-1/build/check_mvp.js
const http = require('http'), fs = require('fs'), path = require('path'), {chromium} = require('playwright');
const root = path.join(__dirname, '..'), types = {'.html': 'text/html', '.csv': 'text/csv', '.json': 'application/json'};
const server = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, {'Content-Type': types[path.extname(f)] || 'text/plain'}); r.end(b); }); });
(async () => {
  const t0 = Date.now(); await new Promise(r => server.listen(0, r));
  const browser = await chromium.launch(), page = await browser.newPage(), errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.route(/cdnjs/, r => r.abort());            // no internet needed for the check
  const step = async (name, f) => { try { await f(); console.log('ok  ', name); } catch (e) { console.log('FAIL', name, '-', e.message.split('\n')[0]); process.exitCode = 1; } };
  const clickThrough = async sel => { await page.click(sel); await page.click('#ov', {timeout: 3000}).catch(() => {}); await page.waitForSelector('#ov.hidden', {state: 'attached'}); };
  await page.goto(`http://localhost:${server.address().port}/build/mvp.html`);
  await step('Draft loads with the answer (2.81×) and nothing covering it', async () => {
    await page.waitForFunction(() => document.querySelector('#answer').textContent.includes('2.81× higher by 2050'), null, {timeout: 5000});
    if (await page.isVisible('#ov')) throw new Error('overlay is showing');
  });
  await step('Draft controls recalculate (CRE, then back to all)', async () => {
    await page.click('[data-loans="Commercial real estate"]'); await page.waitForFunction(() => document.querySelector('#answer').textContent.includes('2.88×'));
    await page.click('[data-loans="all"]');
  });
  await step('Send for approval → Review, nothing needs attention', async () => {
    await clickThrough('#send'); await page.waitForSelector('#review:not(.hidden)');
    if (!(await page.textContent('#rvAttention')).includes('Nothing needs your attention')) throw new Error('attention box is wrong');
  });
  await step('Send back with comment → Draft shows the comment', async () => {
    await page.fill('#rvComment', 'Please check the exclusions'); await clickThrough('#rvBack');
    await page.waitForSelector('#draft:not(.hidden)'); if (!(await page.textContent('#returned')).includes('Please check')) throw new Error('comment missing');
  });
  await step('Change the scenario, send again → Review flags it', async () => {
    await page.click('[data-scen="central"]'); await clickThrough('#send'); await page.waitForSelector('#review:not(.hidden)');
    if (!(await page.textContent('#rvAttention')).includes('the answer uses central')) throw new Error('change not flagged');
  });
  await step('Approve → Send screen with the drafted email', async () => {
    await clickThrough('#rvApprove'); await page.waitForSelector('#send3:not(.hidden)');
    if (!(await page.textContent('#sdBody')).includes('1.58×')) throw new Error('email missing the number');
  });
  await step('Send to Treasury → done', async () => {
    await clickThrough('#sdSend'); await page.waitForFunction(() => document.querySelector('#sdSend').textContent.startsWith('✓ Sent to Treasury'));
  });
  await step('No errors on the page', async () => { if (errors.length) throw new Error(errors.join('; ')); });
  await browser.close(); server.close(); console.log(`\nchecked in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
})();
