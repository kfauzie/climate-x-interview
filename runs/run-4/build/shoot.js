// Usage: node shoot.js <runs/run-N/build/page.html> <outdir> [scale]   (serves runs/run-N over http)
// Screenshots each element with [data-screen="name"] (or the whole page if none) to <outdir>/<name>.png.
// Elements with class "no-export" (ribbon, step bar, buttons) are hidden in exports.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const [page_, out = '../design', scale = '2'] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: +scale });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  // serve the run folder over http (like tools/open_run.sh) so fetch('../data/sites.json') works
  const http = require('http'); const root = path.resolve(path.dirname(path.resolve(page_)), '..');
  const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png' };
  const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
    fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' }); r.end(b); }); });
  await new Promise(ok => srv.listen(0, ok));
  await p.goto(`http://localhost:${srv.address().port}/${path.relative(root, path.resolve(page_))}`); await p.waitForLoadState('networkidle');
  await p.addStyleTag({ content: '.no-export{display:none!important}' });
  const names = await p.$$eval('[data-screen]', els => els.map(e => e.dataset.screen));
  if (!names.length) await p.screenshot({ path: `${out}/page.png`, fullPage: true });
  for (const n of names) {
    await p.evaluate(n => window.showScreen ? window.showScreen(n) : null, n); await p.waitForTimeout(200);
    const el = await p.$(`[data-screen="${n}"]`); await el.screenshot({ path: `${out}/${n}.png` });
  }
  console.log('shots:', names.length || 1, 'errors:', errs.length ? errs : 'none'); await b.close(); srv.close();
})();
