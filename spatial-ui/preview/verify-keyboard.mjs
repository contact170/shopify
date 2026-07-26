import { chromium } from 'playwright';

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const logs = [];
page.on('pageerror', (err) => logs.push(`[pageerror] ${err.message}`));

try {
  await page.goto('http://127.0.0.1:8934/spatial-ui/preview/preview.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);

  // Tab through the page until a .spatial-hotspot button is focused.
  let focused = '';
  for (let i = 0; i < 30 && focused !== 'spatial-hotspot'; i++) {
    await page.keyboard.press('Tab');
    focused = await page.evaluate(() => document.activeElement?.className || '');
  }
  logs.push(`[check] focused element class after tabbing = "${focused}"`);
  const label = await page.evaluate(() => document.activeElement?.getAttribute('aria-label'));
  logs.push(`[check] focused hotspot aria-label = "${label}"`);

  await page.waitForTimeout(600);
  const cardOpacity = await page.locator('.spatial-card').first().evaluate((el) => getComputedStyle(el).opacity);
  logs.push(`[check] card opacity after keyboard focus (no mouse) = ${cardOpacity}`);

  await page.keyboard.press('Enter');
  await page.waitForTimeout(2200);
  const active = await page.locator('#spatial-hero').getAttribute('data-active-zone');
  logs.push(`[check] data-active-zone after Enter = ${active}`);

  await page.keyboard.press('Escape');
  await page.waitForTimeout(1200);
  const activeAfterEscape = await page.locator('#spatial-hero').getAttribute('data-active-zone');
  logs.push(`[check] data-active-zone after Escape = ${activeAfterEscape}`);
} catch (err) {
  logs.push(`[error] ${err.message}`);
} finally {
  console.log(logs.join('\n'));
  await browser.close();
}
