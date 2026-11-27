// Outils Playwright du moteur de boîtes.
//   node outils.js pdf  <page.html> <sortie> <largeur_mm> <hauteur_mm> [échelle_png]   → sortie.pdf + sortie.png + sortie.controle.json
//   node outils.js shot <page.html> <sortie.png> <largeur_px> <hauteur_px> [échelle]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [, , mode, inp, out, a, b, sc] = process.argv;
  const browser = await chromium.launch();
  if (mode === 'shot') {
    const p = await browser.newPage({ viewport: { width: +a, height: +b }, deviceScaleFactor: +(sc || 1) });
    await p.goto('file://' + path.resolve(inp));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: out });
  } else {
    const mm = 96 / 25.4, W = +a, H = +b;
    const p = await browser.newPage({ viewport: { width: Math.ceil(W * mm), height: Math.ceil(H * mm) }, deviceScaleFactor: +(sc || 1) });
    await p.goto('file://' + path.resolve(inp));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(400);
    // contrôles automatiques : débordements, chevauchements, zones réservées
    const rapport = await p.evaluate(() => {
      const mm = 96 / 25.4, res = [];
      const R = (e) => { const r = e.getBoundingClientRect(); return { x: r.left / mm, y: r.top / mm, w: r.width / mm, h: r.height / mm }; };
      const inter = (a, b) => Math.max(0, Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x)) * Math.max(0, Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y));
      for (const f of document.querySelectorAll('.face')) {
        const role = f.dataset.role, fr = R(f), marge = 2.5;
        const zones = JSON.parse(f.dataset.zones || '[]');
        const els = [...f.querySelectorAll('.chk')].map(e => ({ e, r: R(e), nom: e.dataset.nom || e.textContent.trim().slice(0, 40) || e.tagName }));
        for (const o of els) {
          const r = o.r;
          if (r.w === 0 || r.h === 0) continue;
          if (r.x < fr.x + marge - 0.05 || r.y < fr.y + marge - 0.05 || r.x + r.w > fr.x + fr.w - marge + 0.05 || r.y + r.h > fr.y + fr.h - marge + 0.05)
            res.push({ face: role, type: 'hors zone de sécurité (2,5 mm)', element: o.nom });
          for (const z of zones) if (!o.e.classList.contains('img') && inter(r, z) > 0.3) res.push({ face: role, type: 'empiète sur une zone réservée (' + z.nom + ')', element: o.nom });
        }
        for (let i = 0; i < els.length; i++) for (let j = i + 1; j < els.length; j++) {
          if (els[i].e.contains(els[j].e) || els[j].e.contains(els[i].e)) continue;
          if (inter(els[i].r, els[j].r) > 0.5) res.push({ face: role, type: 'chevauchement', element: els[i].nom + ' ↔ ' + els[j].nom });
        }
      }
      return res;
    });
    fs.writeFileSync(out + '.controle.json', JSON.stringify(rapport, null, 1));
    await p.screenshot({ path: out + '.png', clip: { x: 0, y: 0, width: W * mm, height: H * mm } });
    await p.pdf({ path: out + '.pdf', width: W + 'mm', height: H + 'mm', printBackground: true, preferCSSPageSize: true });
  }
  await browser.close();
})();
