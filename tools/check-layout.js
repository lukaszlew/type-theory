const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const body = fs.readFileSync(require('path').join(__dirname, '..', 'out', 'narrow-path.html'), 'utf8');
  const html = (t) => `<!doctype html><html data-theme="${t}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;font:14px system-ui}</style></head><body>${body}</body></html>`;
  const browser = await chromium.launch();
  const check = async (page) => page.evaluate(() => {
    const W = document.documentElement.clientWidth;
    const wide = [...document.querySelectorAll('.page *')].filter(e => e.getBoundingClientRect().right > W + 1 && !e.closest('.tw') && !e.closest('.eq')).map(e => e.tagName + '.' + e.className + ':' + (e.textContent || '').slice(0, 50));
    const ids = [...document.querySelectorAll('[id]')].map(e => e.id); const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
    const dead = [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => !document.getElementById(h.slice(1)));
    return { h: document.body.scrollHeight, wide: wide.slice(0, 12), dup, dead: [...new Set(dead)], xr: document.querySelectorAll('a.xr').length, secs: document.querySelectorAll('h2').length, st: document.querySelectorAll('.tag .st').length };
  });
  const go = async (page, text, file, off = 60) => {
    const ok = await page.evaluate(([t, o]) => { const w = document.createTreeWalker(document.querySelector('.page'), NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) { if (n.textContent.includes(t)) { scrollTo(0, n.parentElement.getBoundingClientRect().top + scrollY - o); return true; } } return false; }, [text, off]);
    if (!ok) console.log('MISSING', text); else await page.screenshot({ path: file });
  };
  let page = await browser.newPage({ viewport: { width: 1000, height: 1300 }, deviceScaleFactor: 1 });
  await page.setContent(html('light'), { waitUntil: 'load' });
  console.log('desktop', JSON.stringify(await check(page)));
  await go(page, 'How the sections depend on each other', require('path').join(__dirname, '..', 'out') + '/o-graph.png', 20);
  await go(page, 'Lemma · The inductive part, for monotone F', require('path').join(__dirname, '..', 'out') + '/o-induct.png', 200);
  await go(page, 'Lemma · The main line runs on pairs', require('path').join(__dirname, '..', 'out') + '/o-pairs.png', 200);
  await go(page, 'Status of the claims', require('path').join(__dirname, '..', 'out') + '/o-status.png', 20);
  await page.close();
  page = await browser.newPage({ viewport: { width: 390, height: 1200 }, deviceScaleFactor: 1 });
  await page.setContent(html('dark'), { waitUntil: 'load' });
  console.log('phone', JSON.stringify(await check(page)));
  await go(page, 'Addition lemma · One lemma per addition', require('path').join(__dirname, '..', 'out') + '/o-pprice.png', 100);
  await go(page, 'Characterization theorem', require('path').join(__dirname, '..', 'out') + '/o-pchar.png', 100);
  await page.close();
  await browser.close();
})();
