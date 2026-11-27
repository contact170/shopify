// usage: node shot.js in.html out.png width height [scale]
const { chromium } = require('playwright');
(async () => {
  const [,, inp, out, w, h, s] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +(s||1) });
  await p.goto('file://' + require('path').resolve(inp));
  await p.waitForTimeout(300);
  await p.screenshot({ path: out, fullPage: false });
  await b.close();
})();
