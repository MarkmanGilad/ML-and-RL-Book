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
  const result = `<!doctype html>\n<html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escape(title)}</title><style>body{margin:0;background:#fff;color:#183b50;font-family:Arial,sans-serif}img{max-width:100%;height:auto}pre{overflow-x:auto}pre,pre code{direction:ltr;text-align:left;unicode-bidi:isolate}table{border-collapse:collapse}th,td{padding:8px;border:1px solid #d4e3e9}</style></head><body>${html}</body></html>`;
  const dest = path.join(out, page.replace(/\.md$/, '.html'));
  await fs.mkdir(path.dirname(dest), { recursive: true });
  await fs.writeFile(dest, result);
}
await fs.writeFile(path.join(out, '.nojekyll'), '');
console.log(`Built ${pages.length} pages; ${localOnly} local source links shown as text. All chapter links and local images checked.`);
