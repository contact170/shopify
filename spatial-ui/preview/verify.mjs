import { chromium } from 'playwright';

const shots = process.argv[2] || '/tmp/spatial-hero-shots';
await import('node:fs/promises').then((fs) => fs.mkdir(shots, { recursive: true }));

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

const logs = [];
page.on('console', (msg) => logs.push(`[console:${msg.type()}] ${msg.text()}`));
page.on('pageerror', (err) => logs.push(`[pageerror] ${err.message}`));

try {

await page.goto('http://127.0.0.1:8934/spatial-ui/preview/preview.html', { waitUntil: 'networkidle' });
await page.waitForTimeout(800);
await page.screenshot({ path: `${shots}/01-idle.png` });

const hotspotCount = await page.locator('.spatial-hotspot').count();
logs.push(`[check] hotspot buttons found = ${hotspotCount}`);

// Hover the "entree" hotspot (keyboard-accessible button) to trigger the halo + floating card.
const entreeBtn = page.locator('.spatial-hotspot[aria-label*="Entrée"]');
await entreeBtn.waitFor({ state: 'attached', timeout: 5000 });
const box = await entreeBtn.boundingBox();
if (!box) throw new Error('entree hotspot has no bounding box (not positioned over the canvas)');
await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
await page.waitForTimeout(700);
await page.screenshot({ path: `${shots}/02-hover-entree.png` });

const cardVisible = await page.locator('.spatial-card').first().evaluate((el) => getComputedStyle(el).opacity);
logs.push(`[check] hover card opacity = ${cardVisible}`);

// Click to open the zone: camera dolly + wall fade + functional demo + docked card.
await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2);
await page.waitForTimeout(1400);
await page.screenshot({ path: `${shots}/03-open-entree-mid.png` });
await page.waitForTimeout(2200);
await page.screenshot({ path: `${shots}/04-open-entree-signal.png` });

const activeAttr = await page.locator('#spatial-hero').getAttribute('data-active-zone');
logs.push(`[check] data-active-zone after click = ${activeAttr}`);
const dockedText = await page.locator('.spatial-card').first().innerText().catch(() => '(none)');
logs.push(`[check] docked card text = ${dockedText.replace(/\n/g, ' | ')}`);

// Close via the "Retour" button.
await page.locator('.spatial-card-close').click();
await page.waitForTimeout(1400);
await page.screenshot({ path: `${shots}/05-closed.png` });
const activeAfterClose = await page.locator('#spatial-hero').getAttribute('data-active-zone');
logs.push(`[check] data-active-zone after close = ${activeAfterClose}`);

} catch (err) {
  logs.push(`[error] ${err.message}`);
  await page.screenshot({ path: `${shots}/99-failure.png` }).catch(() => {});
} finally {
  console.log(logs.join('\n'));
  console.log('Screenshots written to', shots);
  await browser.close();
}
