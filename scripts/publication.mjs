export const siteUrl = 'https://book.markman.co.il/';
const bookTitle = 'למידת מכונה ולמידת חיזוק באמצעות בניית משחקים';
const description = 'ספר בעברית מאת גלעד מרקמן לתלמידי י״א–י״ב: פייתון, בניית משחקים עם Pygame, למידת מכונה עם PyTorch ולמידת חיזוק.';
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');

export function pageUrl(page) {
  return page === 'index.md' ? siteUrl
    : siteUrl + page.replace(/\.md$/, '.html').split('/').map(encodeURIComponent).join('/');
}

export function publicationHead(page, heading) {
  const title = page === 'index.md' ? `${bookTitle} | גלעד מרקמן`
    : `${heading.trim()} | למידת מכונה ולמידת חיזוק | גלעד מרקמן`;
  const summary = page === 'index.md' ? description : `${heading.trim()} — ${description}`;
  const url = pageUrl(page);
  const book = page === 'index.md' ? `<script type="application/ld+json">${JSON.stringify({
    '@context': 'https://schema.org', '@type': 'Book', name: bookTitle,
    author: { '@type': 'Person', name: 'גלעד מרקמן', alternateName: 'Gilad Markman' },
    inLanguage: 'he', url: siteUrl, description,
  }).replaceAll('<', '\\u003c')}</script>` : '';
  return `<title>${escape(title)}</title>
<meta name="description" content="${escape(summary)}">
<meta name="author" content="גלעד מרקמן">
<link rel="canonical" href="${url}">
<meta property="og:type" content="${page === 'index.md' ? 'book' : 'article'}">
<meta property="og:locale" content="he_IL">
<meta property="og:site_name" content="${escape(bookTitle)}">
<meta property="og:title" content="${escape(title)}">
<meta property="og:description" content="${escape(summary)}">
<meta property="og:url" content="${url}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${escape(title)}">
<meta name="twitter:description" content="${escape(summary)}">
${book}`;
}

export function sitemap(pages) {
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pages.map(page => `  <url><loc>${escape(pageUrl(page))}</loc></url>`).join('\n')}\n</urlset>\n`;
}
