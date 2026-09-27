#!/usr/bin/env node
/** Optional smoke evidence, not a fidelity/accessibility/interaction certification. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const args = {};
const allowed = new Set(['url', 'expect', 'project', 'out', 'playwright', 'executable', 'allow-remote']);
for (let i = 2; i < process.argv.length; i++) {
  const key = process.argv[i].replace(/^--/, '');
  if (!process.argv[i].startsWith('--') || !allowed.has(key)) throw new Error('Unknown argument');
  if (key === 'allow-remote') { args[key] = true; continue; }
  if (!process.argv[i + 1] || process.argv[i + 1].startsWith('--')) throw new Error(`Missing value for --${key}`);
  args[key] = process.argv[++i];
}
for (const key of ['url', 'expect', 'project', 'out']) {
  if (!args[key]?.trim()) throw new Error(`Required --${key}`);
}
const url = new URL(args.url);
if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) throw new Error('Use HTTP(S) without URL credentials');
if (!args['allow-remote'] && !['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname)) throw new Error('External preview requires --allow-remote');
const project = path.resolve(args.project);
if (!(await fs.stat(project)).isDirectory()) throw new Error('--project must be a directory');
const out = path.resolve(args.out);
await fs.mkdir(out, { recursive: true });
const requireFromProject = createRequire(path.join(project, 'package.json'));
let modulePath = args.playwright;
if (modulePath && !path.isAbsolute(modulePath)) throw new Error('--playwright must be an absolute installed module path');
if (!modulePath) {
  for (const name of ['playwright', '@playwright/test', 'playwright-core']) {
    try { modulePath = requireFromProject.resolve(name); break; } catch {}
  }
}
if (!modulePath) throw new Error('Installed Playwright unavailable; use an existing browser tool or mark browser checks not verified');
const pw = await import(pathToFileURL(modulePath).href);
const chromium = pw.chromium ?? pw.default?.chromium;
if (!chromium) throw new Error('Module does not export Playwright chromium');
const report = {
  check: 'smoke-only',
  limitations: ['No interaction, accessibility, theme or reference-fidelity certification.', 'Chromium only. No external reachability check.'],
  viewports: []
};
let browser;
try {
  browser = await chromium.launch({ headless: true, ...(args.executable ? { executablePath: args.executable } : {}) });
  for (const viewport of [{ width: 1440, height: 1000 }, { width: 390, height: 844 }]) {
    const context = await browser.newContext({ viewport, reducedMotion: 'reduce' });
    const page = await context.newPage();
    const result = { viewport, findings: [], screenshot: `${viewport.width}.png` };
    page.on('pageerror', () => result.findings.push({ kind: 'uncaught-page-error' }));
    page.on('console', message => {
      if (message.type() === 'error') result.findings.push({ kind: 'console-error' });
    });
    page.on('requestfailed', request => result.findings.push({ kind: 'request-failed', resourceType: request.resourceType() }));
    page.on('response', response => {
      if (response.status() >= 400) result.findings.push({ kind: 'http-error', status: response.status(), resourceType: response.request().resourceType() });
    });
    try {
      const response = await page.goto(url.href, { waitUntil: 'domcontentloaded', timeout: 30000 });
      result.mainStatus = response?.status() ?? null;
      await page.waitForFunction(marker => document.body?.innerText.includes(marker), args.expect, { timeout: 12000 });
      // Wait for both fonts and eager/lazy images after scrolling, with a hard bound.
      await page.evaluate(async () => {
        const start = window.scrollY;
        const height = Math.min(document.documentElement.scrollHeight, 20000);
        for (let y = 0; y < height; y += window.innerHeight) {
          window.scrollTo(0, y);
          await new Promise(resolve => requestAnimationFrame(resolve));
        }
        window.scrollTo(0, start);
        await Promise.race([
          Promise.all([document.fonts.ready, ...Array.from(document.images, img => img.complete ? Promise.resolve() : new Promise(resolve => {
            img.addEventListener('load', resolve, { once: true });
            img.addEventListener('error', resolve, { once: true });
          }))]),
          new Promise(resolve => setTimeout(resolve, 5000))
        ]);
      });
      const layout = await page.evaluate(() => ({
        documentOverflow: document.documentElement.scrollWidth > window.innerWidth + 1,
        brokenImages: Array.from(document.images).filter(img => img.currentSrc && img.complete && img.naturalWidth === 0).length,
        pendingImages: Array.from(document.images).filter(img => img.currentSrc && !img.complete).length,
        fontsPending: document.fonts.status !== 'loaded'
      }));
      result.layout = layout;
      if (layout.documentOverflow) result.findings.push({ kind: 'document-horizontal-overflow' });
      if (layout.brokenImages) result.findings.push({ kind: 'broken-images', count: layout.brokenImages });
      if (layout.pendingImages || layout.fontsPending) result.findings.push({ kind: 'assets-not-ready', pendingImages: layout.pendingImages, fontsPending: layout.fontsPending });
      result.redirected = page.url() !== url.href;
    } catch {
      result.findings.push({ kind: 'navigation-marker-or-readiness-failed' });
    }
    try { await page.screenshot({ path: path.join(out, result.screenshot), fullPage: true, timeout: 15000 }); }
    catch { result.findings.push({ kind: 'screenshot-failed' }); }
    result.passed = result.findings.length === 0;
    report.viewports.push(result);
    await context.close();
  }
} catch {
  report.runtimeFailure = 'Browser unavailable or check interrupted; not verified. Inspect installed browser/runtime locally.';
} finally {
  if (browser) await browser.close();
  report.passed = !report.runtimeFailure && report.viewports.length === 2 && report.viewports.every(v => v.passed);
  await fs.writeFile(path.join(out, 'smoke-report.json'), JSON.stringify(report, null, 2));
}
console.log(JSON.stringify(report, null, 2));
process.exitCode = report.passed ? 0 : 1;
