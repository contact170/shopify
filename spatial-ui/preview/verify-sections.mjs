import { chromium } from 'playwright';

const shots = '/tmp/spatial-hero-shots';
await import('node:fs/promises').then((fs) => fs.mkdir(shots, { recursive: true }));

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const logs = [];
page.on('pageerror', (err) => logs.push(`[pageerror] ${err.message}`));

try {
  await page.goto('http://127.0.0.1:8934/spatial-ui/preview/preview-sections.html', { waitUntil: 'networkidle' });

  // Before scroll: cards/nodes should still be at opacity 0 (not yet revealed).
  const beforeOpacity = await page.locator('.wd-card').first().evaluate((el) => getComputedStyle(el).opacity);
  logs.push(`[check] why-daewoo card opacity before scroll = ${beforeOpacity}`);

  await page.screenshot({ path: `${shots}/06-why-daewoo-before-scroll.png` });

  await page.locator('#why-daewoo').scrollIntoViewIfNeeded();
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${shots}/07-why-daewoo-revealed.png` });
  const afterOpacity = await page.locator('.wd-card').first().evaluate((el) => getComputedStyle(el).opacity);
  logs.push(`[check] why-daewoo card opacity after scroll = ${afterOpacity}`);

  await page.locator('#how-it-works').scrollIntoViewIfNeeded();
  await page.waitForTimeout(1200);
  await page.screenshot({ path: `${shots}/08-how-it-works-revealed.png` });
  const nodeOpacity = await page.locator('.hiw-node').first().evaluate((el) => getComputedStyle(el).opacity);
  logs.push(`[check] how-it-works node opacity after scroll = ${nodeOpacity}`);
} catch (err) {
  logs.push(`[error] ${err.message}`);
} finally {
  console.log(logs.join('\n'));
  await browser.close();
}
