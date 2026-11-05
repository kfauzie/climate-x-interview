// Saves each step of the prototype as a design image in ../design/. Run: node capture_screens.js [scale]
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..'), scale = +(process.argv[2] || 2);
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': f.endsWith('.json') ? 'application/json' : 'text/html' }); r.end(b); }); });
(async () => {
  await new Promise(ok => srv.listen(0, ok)); const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: scale });
  await p.goto(`http://localhost:${srv.address().port}/build/mvp.html`); await p.waitForSelector('body[data-ready="1"]');
  const names = ['1-setup', '2-brief', '3-site', '4-send', '5-answers'];
  for (let i = 1; i <= 5; i++) {
    await p.evaluate(n => { if (n === 5) st.policyShown = true; go(n); }, i); await p.waitForTimeout(450);
    await p.screenshot({ path: path.join(root, 'design', names[i - 1] + '.png'), fullPage: true });
  }
  console.log('saved', names.length, 'screens'); await b.close(); srv.close();
})();
