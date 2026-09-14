import { publicationHead, sitemap, siteUrl } from './publication.mjs';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

// MARKED_MODULE supports an already installed local runtime for offline previews.
const { marked } = await import(process.env.MARKED_MODULE
  ? pathToFileURL(process.env.MARKED_MODULE).href : 'marked');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, '_site');
const pages = ['index.md'];
for (const entry of await fs.readdir(root, { withFileTypes: true })) {
  if (entry.isDirectory() && /^\d{2}-/.test(entry.name)) {
    for (const name of await fs.readdir(path.join(root, entry.name))) {
      if (name.endsWith('.md')) pages.push(`${entry.name}/${name}`);
    }
  }
}
await fs.mkdir(out, { recursive: true });
// Remove stale build products only from this script's fixed output directory.
for (const entry of await fs.readdir(out)) {
  await fs.rm(path.join(out, entry), { recursive: true, force: true });
}
await fs.cp(path.join(root, 'assets'), path.join(out, 'assets'), { recursive: true });
const escape = s => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');

// The sidebar is derived from the table of contents in index.md: part headings
// ("### חלק ...") and the chapter links listed under each of them.
const indexSource = await fs.readFile(path.join(root, 'index.md'), 'utf8');
const tocSource = indexSource.slice(indexSource.indexOf('# תוכן העניינים'));
const parts = [];
for (const line of tocSource.split('\n')) {
  const part = line.match(/^### (חלק .+)$/);
  if (part) { parts.push({ title: part[1].trim(), chapters: [] }); continue; }
  const chapter = line.match(/^- \[(.+)\]\(([^)\s]+\.md)\)\s*$/);
  if (chapter && parts.length) {
    const target = decodeURIComponent(chapter[2]).split(/[?#]/)[0];
    if (!pages.includes(target)) throw Error(`Sidebar: missing page in index.md: ${chapter[2]}`);
    parts[parts.length - 1].chapters.push({ title: chapter[1], target, href: chapter[2] });
  }
}
if (!parts.length) throw Error('Sidebar: no parts found in index.md');

const sidebarScript = `<script>
(function () {
  var KEY = 'book-sidebar-width', root = document.documentElement;
  try { var saved = localStorage.getItem(KEY); if (saved) root.style.setProperty('--sidebar-w', saved + 'px'); } catch (e) {}
  var handle = document.querySelector('.sidebar-handle'), side = document.querySelector('.sidebar');
  if (!handle || !side) return;
  var width = null;
  function move(e) {
    width = Math.round(Math.min(450, Math.max(200, side.getBoundingClientRect().right - e.clientX)));
    root.style.setProperty('--sidebar-w', width + 'px');
  }
  function stop() {
    document.removeEventListener('pointermove', move); document.removeEventListener('pointerup', stop);
    handle.classList.remove('dragging'); document.body.classList.remove('resizing');
    try { if (width) localStorage.setItem(KEY, width); } catch (e) {}
  }
  handle.addEventListener('pointerdown', function (e) {
    e.preventDefault(); handle.classList.add('dragging'); document.body.classList.add('resizing');
    document.addEventListener('pointermove', move); document.addEventListener('pointerup', stop);
  });
  handle.addEventListener('dblclick', function () {
    width = null; root.style.removeProperty('--sidebar-w');
    try { localStorage.removeItem(KEY); } catch (e) {}
  });
  handle.title = 'גררו לשינוי רוחב התפריט; לחיצה כפולה מחזירה לברירת המחדל';
})();
</script>`;

const sidebarStyles = `<style>
.toc-toggle { display: none; }
.toc-button { display: none; position: fixed; bottom: 18px; right: 18px; z-index: 30; padding: 10px 16px; border-radius: 999px; background: #174e49; color: #fff; font-weight: bold; box-shadow: 0 2px 8px rgba(0,0,0,.25); cursor: pointer; }
.layout { display: flex; flex-direction: row; align-items: flex-start; }
.sidebar { box-sizing: border-box; flex: 0 0 var(--sidebar-w, 270px); width: var(--sidebar-w, 270px); position: sticky; top: 0; height: 100vh; overflow-y: auto; padding: 18px 14px 40px; background: #f4f8fb; border-left: 1px solid #d4e3e9; direction: rtl; text-align: right; font-size: 14px; line-height: 1.6; }
.sidebar .sidebar-home { display: block; margin: 0 0 14px; padding: 10px 14px; border-radius: 8px; background: #174e49; color: #fff !important; font-weight: bold; text-decoration: none; }
.sidebar details { margin: 6px 0; }
.sidebar summary { cursor: pointer; padding: 8px 10px; border-radius: 6px; background: #eef5fc; color: #153b56; font-weight: bold; border-right: 4px solid #299c91; list-style: none; }
.sidebar summary::-webkit-details-marker { display: none; }
.sidebar summary::before { content: "\\25B8"; display: inline-block; margin-left: 6px; color: #299c91; transition: transform .15s; }
.sidebar details[open] > summary::before { transform: rotate(90deg); }
.sidebar ul { list-style: none; margin: 4px 0 8px; padding: 0 8px 0 0; }
.sidebar li a { display: block; padding: 4px 10px; border-radius: 6px; color: #183e63; text-decoration: none; border-right: 3px solid transparent; }
.sidebar li a:hover { background: #d4eee8; }
.sidebar li.current a { background: #e3f3f0; border-right-color: #299c91; font-weight: bold; color: #174e49; }
.content { flex: 1 1 auto; min-width: 0; }
.sidebar-handle { flex: 0 0 8px; width: 8px; position: sticky; top: 0; height: 100vh; cursor: col-resize; background: transparent; touch-action: none; user-select: none; }
.sidebar-handle:hover, .sidebar-handle.dragging { background: #299c91; opacity: .5; }
body.resizing { cursor: col-resize; user-select: none; }
@media screen and (max-width: 960px) {
  .toc-button { display: block; }
  .sidebar-handle { display: none; }
  .sidebar { position: fixed; top: 0; right: 0; bottom: 0; height: auto; z-index: 20; transform: translateX(100%); transition: transform .2s; box-shadow: -2px 0 10px rgba(0,0,0,.2); }
  .toc-toggle:checked ~ .layout .sidebar { transform: none; }
}
@media print { .sidebar, .toc-button { display: none !important; } }
</style>`;

function sidebarFor(page) {
  const prefix = page.includes('/') ? '../'.repeat(page.split('/').length - 1) : '';
  const toHtml = href => prefix + href.replace(/\.md(?=[?#]|$)/, '.html');
  const isIndex = page === 'index.md';
  const items = parts.map(part => {
    const open = isIndex || part.chapters.some(c => c.target === page) ? ' open' : '';
    const list = part.chapters.map(c =>
      `<li${c.target === page ? ' class="current"' : ''}><a href="${toHtml(c.href)}">${c.title}</a></li>`).join('');
    return `<details${open}><summary>${part.title}</summary><ul>${list}</ul></details>`;
  }).join('');
  return `<aside class="sidebar" aria-label="פרקי הספר"><a class="sidebar-home" href="${prefix}index.html">תוכן העניינים</a>${items}</aside>`;
}

// Shared mobile gutters override individual chapters without affecting print or desktop.
const mobileStyles = `<style>@media screen and (max-width: 960px) {
  body .book { box-sizing: border-box; padding-inline: 20px; }
}</style>`;
let localOnly = 0;
for (const page of pages) {
  const source = await fs.readFile(path.join(root, page), 'utf8');
  let html = marked.parse(source.replace(/<!--[^]*?-->/g, ''), { gfm: true });
  const rewrite = (url, image = false) => {
    const decoded = decodeURIComponent(url.replaceAll('&amp;', '&'));
    if (/^(https?:|mailto:|tel:|data:)/i.test(decoded) || decoded.startsWith('#')) return url;
    if (/^[a-z][a-z\d+.-]*:/i.test(decoded)) return null;
    const [pathname] = decoded.split(/[?#]/);
    const target = path.resolve(root, path.dirname(page), pathname);
    const relative = path.relative(root, target);
    if (relative.startsWith('..') || path.isAbsolute(relative)) return null;
    if (!image && pathname.endsWith('.md')) {
      if (!pages.includes(relative.split(path.sep).join('/'))) throw Error(`Missing page: ${page}: ${url}`);
      return url.replace(/\.md(?=[?#]|$)/, '.html');
    }
    return url;
  };
  html = html.replace(/<a\b([^]*?)href="([^"]*)"([^]*?)>([^]*?)<\/a>/g,
    (_, before, url, after, label) => {
      const href = rewrite(url);
      if (href === null) { localOnly++; return `<span title="זמין בעותק המקומי בלבד">${label} (עותק מקומי)</span>`; }
      return `<a${before}href="${href}"${after}>${label}</a>`;
    });
  const images = [...html.matchAll(/<img\b[^>]*src="([^"]+)"/g)];
  for (const [, url] of images) {
    if (rewrite(url, true) === null) throw Error(`Image outside book: ${page}: ${url}`);
    if (!/^(https?:|data:)/i.test(url)) await fs.access(path.resolve(root, path.dirname(page), decodeURIComponent(url)));
  }
  const title = html.match(/<h1[^>]*>([^]*?)<\/h1>/)?.[1].replace(/<[^>]*>/g, ' ') || path.basename(page, '.md');
  const body = `<input type="checkbox" id="toc-toggle" class="toc-toggle"><label for="toc-toggle" class="toc-button">&#9776; פרקים</label><div class="layout">${sidebarFor(page)}<div class="sidebar-handle" role="separator" aria-orientation="vertical" aria-label="רוחב התפריט"></div><main class="content">${html}</main></div>${sidebarScript}`;
  const result = `<!doctype html>\n<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">${publicationHead(page, title)}<style>body{margin:0;background:#fff;color:#183b50;font-family:Arial,sans-serif}img{max-width:100%;height:auto}pre{overflow-x:auto}pre,pre code{direction:ltr;text-align:left;unicode-bidi:isolate}table{border-collapse:collapse}th,td{padding:8px;border:1px solid #d4e3e9}</style>${sidebarStyles}${mobileStyles}</head><body>${body}</body></html>`;
  const dest = path.join(out, page.replace(/\.md$/, '.html'));
  await fs.mkdir(path.dirname(dest), { recursive: true });
  await fs.writeFile(dest, result);
}
await fs.writeFile(path.join(out, '.nojekyll'), '');
await fs.writeFile(path.join(out, 'sitemap.xml'), sitemap(pages));
await fs.writeFile(path.join(out, 'robots.txt'), 'User-agent: *\nAllow: /\nSitemap: ' + siteUrl + 'sitemap.xml\n');
console.log(`Built ${pages.length} pages with a ${parts.length}-part sidebar; ${localOnly} local source links shown as text. All chapter links and local images checked.`);
