#!/usr/bin/env node
// Mesure de pages de daewoo-security.fr pour l'agent « optimisation-site ».
//
// Usage : node scripts/audit-site.js --out <dossier> <url1> [<url2> ...]
//
// Pour chaque page :
//   - mobile (390 x 844, écran x2) en 4G lente simulée (1,6 Mbit/s, 150 ms) :
//     poids par type et par domaine (hors préchargements en basse priorité,
//     comptés à part), requêtes, LCP, CLS, images trop lourdes,
//     surdimensionnées, cassées ou sans texte alternatif, débordement
//     horizontal, 3 captures (haut, milieu, bas) ;
//   - ordinateur (1366 x 900) : 1 capture du haut de page, débordement.
// Puis vérifie les liens internes trouvés (150 au maximum).
//
// Écrit le détail dans <dossier>/audit.json et les captures PNG dans
// <dossier>, et affiche un résumé JSON sur la sortie standard.
// Lecture seule : le script ne fait que charger des pages publiques.

const { chromium } = require('playwright');
const { execFile } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');

const SITE_HOST = 'daewoo-security.fr';
const MAX_LINKS = 150;
const MOBILE = {
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  userAgent:
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
};
const DESKTOP = { viewport: { width: 1366, height: 900 } };
const SLOW_4G = { offline: false, latency: 150, downloadThroughput: 1.6e6 / 8, uploadThroughput: 750e3 / 8 };

const kb = (b) => Math.round(b / 1024);
const short = (u, n = 110) => (u.length > n ? u.slice(0, n) + '…' : u);
const slug = (u) =>
  new URL(u).pathname.replace(/\/+$/, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').slice(0, 60) || 'accueil';

function parseArgs() {
  const args = process.argv.slice(2);
  let out = path.join(os.tmpdir(), 'audit-site');
  const urls = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--out') out = args[++i];
    else urls.push(args[i]);
  }
  if (!urls.length) {
    console.error('Usage : node scripts/audit-site.js --out <dossier> <url1> [<url2> ...]');
    process.exit(1);
  }
  for (const u of urls) {
    if (new URL(u).hostname !== SITE_HOST) {
      console.error(`Adresse refusée (hors ${SITE_HOST}) : ${u}`);
      process.exit(1);
    }
  }
  fs.mkdirSync(out, { recursive: true });
  return { out, urls };
}

async function scrollThrough(page) {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h; y += 500) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 200));
    }
  });
}

async function auditMobile(browser, url, out) {
  const name = slug(url);
  const ctx = await browser.newContext(MOBILE);
  const page = await ctx.newPage();
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('Network.enable');
  await cdp.send('Network.emulateNetworkConditions', SLOW_4G);
  await page.addInitScript(() => {
    window.__cls = 0;
    window.__lcp = null;
    new PerformanceObserver((l) => {
      for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value;
    }).observe({ type: 'layout-shift', buffered: true });
    new PerformanceObserver((l) => {
      const e = l.getEntries().pop();
      if (e) window.__lcp = { ms: Math.round(e.startTime), tag: e.element ? e.element.tagName : null, url: e.url || null };
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  });

  const reqs = [];
  const failed = [];
  page.on('requestfinished', async (r) => {
    try {
      const s = await r.sizes();
      // Préchargements en basse priorité (paiement Shopify, pages suivantes) :
      // comptés à part car ils ne retardent pas l'affichage.
      const purpose = (await r.headerValue('sec-purpose')) || (await r.headerValue('purpose')) || '';
      reqs.push({
        url: r.url(),
        type: r.resourceType(),
        bytes: s.responseBodySize + s.responseHeadersSize,
        prefetch: /prefetch|prerender/i.test(purpose),
      });
    } catch {}
  });
  page.on('requestfailed', (r) => {
    const err = (r.failure() || {}).errorText || '';
    if (!/ERR_ABORTED/.test(err)) failed.push({ url: short(r.url()), error: err });
  });

  const t0 = Date.now();
  const resp = await page.goto(url, { waitUntil: 'load', timeout: 120000 });
  const loadMs = Date.now() - t0;
  await page.waitForTimeout(3000);
  const lcp = await page.evaluate(() => window.__lcp);
  const clsAtLoad = await page.evaluate(() => window.__cls);
  const shots = [];
  const shot = async (suffix) => {
    const p = path.join(out, `${name}-mobile-${suffix}.png`);
    await page.screenshot({ path: p });
    shots.push(p);
  };
  await shot('1-haut');

  await scrollThrough(page);
  await page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {});
  const height = await page.evaluate(() => document.documentElement.scrollHeight);
  await page.evaluate((y) => window.scrollTo(0, y), Math.round(height / 2));
  await page.waitForTimeout(800);
  await shot('2-milieu');
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(800);
  await shot('3-bas');

  const dom = await page.evaluate((host) => {
    const imgs = [...document.images].map((img) => {
      const r = img.getBoundingClientRect();
      return {
        src: img.currentSrc || img.src || '',
        alt: img.getAttribute('alt'),
        naturalW: img.naturalWidth,
        renderW: Math.round(r.width),
        renderH: Math.round(r.height),
        complete: img.complete,
        lazy: img.getAttribute('loading') === 'lazy',
        hasDims: img.hasAttribute('width') && img.hasAttribute('height'),
        responsive: img.hasAttribute('srcset') || !!img.closest('picture'),
        visible: r.width > 1 && r.height > 1,
      };
    });
    const links = [...document.querySelectorAll('a[href]')]
      .map((a) => {
        try {
          const u = new URL(a.getAttribute('href'), location.href);
          u.hash = '';
          return u;
        } catch {
          return null;
        }
      })
      .filter((u) => u && u.hostname === host && /^https?:$/.test(u.protocol))
      .filter((u) => !/^\/(cart|account|checkout|search)/.test(u.pathname))
      .map((u) => u.href);
    return {
      title: document.title,
      h1: [...document.querySelectorAll('h1')].map((h) => h.innerText.replace(/\s+/g, ' ').trim()).slice(0, 3),
      overflowX: document.documentElement.scrollWidth > window.innerWidth + 2,
      imgs,
      links: [...new Set(links)],
      cls: window.__cls,
    };
  }, SITE_HOST);
  await ctx.close();

  const bytesByUrl = new Map(reqs.map((r) => [r.url, r.bytes]));
  const byType = {};
  const byHost = {};
  let total = 0;
  let prefetch = 0;
  let prefetchCount = 0;
  for (const r of reqs) {
    if (r.prefetch) {
      prefetch += r.bytes;
      prefetchCount++;
      continue;
    }
    total += r.bytes;
    byType[r.type] = (byType[r.type] || 0) + r.bytes;
    const h = new URL(r.url).hostname;
    byHost[h] = (byHost[h] || 0) + r.bytes;
  }
  const images = dom.imgs.filter((i) => i.src && !i.src.startsWith('data:'));
  const withBytes = images.map((i) => ({ ...i, kb: kb(bytesByUrl.get(i.src) || 0) }));
  const lcpImg = lcp && lcp.url ? withBytes.find((i) => i.src === lcp.url) : null;

  return {
    url,
    status: resp ? resp.status() : null,
    title: dom.title,
    h1: dom.h1,
    mobile: {
      loadMs,
      lcpMs: lcp ? lcp.ms : null,
      lcpElement: lcp ? `${lcp.tag || ''} ${lcp.url ? short(lcp.url, 90) : ''}`.trim() : null,
      lcpImageLazy: lcpImg ? lcpImg.lazy : null,
      clsAtLoad: Number(clsAtLoad.toFixed(3)),
      clsTotal: Number(dom.cls.toFixed(3)),
      requests: reqs.length - prefetchCount,
      totalKB: kb(total),
      prefetchKB: kb(prefetch),
      prefetchRequests: prefetchCount,
      byTypeKB: Object.fromEntries(Object.entries(byType).map(([k, v]) => [k, kb(v)])),
      topHostsKB: Object.fromEntries(
        Object.entries(byHost)
          .sort((a, b) => b[1] - a[1])
          .slice(0, 6)
          .map(([k, v]) => [k, kb(v)])
      ),
      heaviest: reqs
        .filter((r) => !r.prefetch)
        .sort((a, b) => b.bytes - a.bytes)
        .slice(0, 8)
        .map((r) => ({ kb: kb(r.bytes), type: r.type, url: short(r.url) })),
      failedRequests: failed.slice(0, 10),
      overflowX: dom.overflowX,
    },
    images: {
      count: images.length,
      totalKB: withBytes.reduce((s, i) => s + i.kb, 0),
      heavy: withBytes.filter((i) => i.kb > 200).slice(0, 10).map((i) => ({ kb: i.kb, src: short(i.src) })),
      oversized: withBytes
        .filter((i) => i.visible && i.renderW > 0 && i.naturalW > i.renderW * 3 && i.kb > 30)
        .slice(0, 10)
        .map((i) => ({ naturalW: i.naturalW, renderW: i.renderW, kb: i.kb, src: short(i.src) })),
      broken: withBytes.filter((i) => i.complete && i.naturalW === 0).slice(0, 10).map((i) => short(i.src)),
      missingAlt: withBytes.filter((i) => i.alt === null).slice(0, 15).map((i) => short(i.src)),
      emptyAltLarge: withBytes
        .filter((i) => i.alt === '' && i.visible && i.renderW >= 150)
        .slice(0, 10)
        .map((i) => short(i.src)),
      notResponsive: withBytes.filter((i) => i.visible && !i.responsive && i.kb > 30).length,
      withoutDimensions: withBytes.filter((i) => i.visible && !i.hasDims).length,
    },
    links: dom.links,
    screenshots: shots,
  };
}

async function auditDesktop(browser, url, out) {
  const ctx = await browser.newContext(DESKTOP);
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  await page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {});
  await page.waitForTimeout(1500);
  const p = path.join(out, `${slug(url)}-ordinateur.png`);
  await page.screenshot({ path: p });
  const overflowX = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 2);
  await ctx.close();
  return { overflowX, screenshot: p };
}

function headStatus(url) {
  return new Promise((resolve) => {
    execFile(
      'curl',
      ['-s', '-o', '/dev/null', '-I', '-m', '20', '-w', '%{http_code} %{redirect_url}', url],
      (err, stdout) => {
        const [code, redirect] = (stdout || '').trim().split(' ');
        resolve({ status: Number(code) || 0, redirect: redirect || null });
      }
    );
  });
}

async function checkLinks(pages) {
  const foundOn = new Map();
  for (const p of pages) for (const l of p.links || []) if (!foundOn.has(l)) foundOn.set(l, p.url);
  const all = [...foundOn.keys()];
  const list = all.slice(0, MAX_LINKS);
  const results = [];
  for (let i = 0; i < list.length; i += 8) {
    const batch = list.slice(i, i + 8);
    const res = await Promise.all(batch.map((u) => headStatus(u).then((r) => ({ url: u, ...r }))));
    results.push(...res);
  }
  return {
    found: all.length,
    checked: list.length,
    errors: results
      .filter((r) => r.status >= 400 || r.status === 0)
      .map((r) => ({ url: r.url, status: r.status, foundOn: foundOn.get(r.url) })),
    redirects: results
      .filter((r) => r.status >= 300 && r.status < 400)
      .map((r) => ({ url: r.url, status: r.status, to: r.redirect, foundOn: foundOn.get(r.url) })),
  };
}

(async () => {
  const { out, urls } = parseArgs();
  const browser = await chromium.launch();
  const pages = [];
  for (const url of urls) {
    try {
      const m = await auditMobile(browser, url, out);
      try {
        m.desktop = await auditDesktop(browser, url, out);
      } catch (e) {
        m.desktop = { error: String(e.message || e).slice(0, 200) };
      }
      pages.push(m);
    } catch (e) {
      pages.push({ url, error: String(e.message || e).slice(0, 200) });
    }
  }
  await browser.close();
  const links = await checkLinks(pages);
  const report = {
    generatedAt: new Date().toISOString(),
    profile: {
      mobile: '390 x 844, écran x2, 4G lente simulée (1,6 Mbit/s, 150 ms)',
      desktop: '1366 x 900, sans limitation réseau',
    },
    pages: pages.map(({ links: _l, ...p }) => p),
    links,
    outDir: out,
  };
  fs.writeFileSync(path.join(out, 'audit.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report));
})();
