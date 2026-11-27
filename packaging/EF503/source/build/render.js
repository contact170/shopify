// node render.js <html> <outPrefix> [pdf] [scale]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [,, inp, out, doPdf, scale] = process.argv;
  const b = await chromium.launch();
  const mm = 96 / 25.4;
  const W = 802, H = 397;
  const p = await b.newPage({ viewport: { width: Math.ceil(W * mm), height: Math.ceil(H * mm) }, deviceScaleFactor: +(scale || 1) });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  await p.screenshot({ path: out + '.png', clip: { x: 0, y: 0, width: W * mm, height: H * mm } });
  if (doPdf === 'pdf') await p.pdf({ path: out + '.pdf', width: W + 'mm', height: H + 'mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
