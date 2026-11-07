const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const body = fs.readFileSync(require('path').join(__dirname, '..', 'out', 'narrow-path.html'), 'utf8');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(`<!doctype html><html><head><meta charset="utf-8"></head><body>${body}</body></html>`, { waitUntil: 'load' });
  await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  const text = await page.evaluate(() => document.querySelector('.page').innerText);
  fs.writeFileSync(require('path').join(__dirname, '..', 'out', 'reading-copy.txt'), text);
  console.log('chars', text.length);
  await browser.close();
})();
