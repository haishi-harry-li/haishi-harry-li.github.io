"""One-time migration; reads captured Google HTML and asset manifest in .migration/.
Do not rerun after hand-editing the website: generated pages will be replaced.
"""
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from html import escape
import json, re

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ('index.html', 'Home', 'haishi-original.html'),
    ('research.html', 'Research', 'haishi-research.html'),
    ('policy-discussions.html', 'Policy Discussions', 'haishi-policy-discussions.html'),
    ('international-economics-joint-conference.html', 'International Economics Joint Conference', 'haishi-international-economics-joint-conference.html'),
]
ASSET_MANIFEST = ROOT / '.migration/assets.json'
ASSETS = json.loads(ASSET_MANIFEST.read_text()) if ASSET_MANIFEST.exists() else []
REPLACEMENTS = {a['source']: a['local'] for a in ASSETS if a['status'] == 'downloaded'}
# Verified replacement on ETSG's current website (includes the 2021 prize).
REPLACEMENTS['https://www.etsg.org/award-winners.html'] = 'https://etsg.org/award-winners/review-of-world-economics-rowe-prize/'
BASE = 'https://haishi-harry-li.github.io/'

def clean(node):
    if isinstance(node, NavigableString):
        return escape(str(node))
    if node.get('aria-hidden') == 'true' or node.name in ('svg', 'script', 'style') or 'PPhIP' in node.get('class', []):
        return ''
    if node.name == 'br':
        return '<br>'
    content = ''.join(clean(c) for c in node.children)
    if node.name == 'a':
        href = node.get('href', '')
        if href.startswith('#'):
            return ''  # Google heading-copy widget
        href = REPLACEMENTS.get(href, href)
        if href.startswith('https://scholar.google.com/citations'):
            href = 'https://scholar.google.com/citations?user=2NppHJkAAAAJ&hl=en'
        if href.startswith('/view/haishi-harry-li/'):
            slug = href.rstrip('/').split('/')[-1]
            href = 'index.html' if slug == 'home' else slug + '.html'
        return f'<a href="{escape(href, quote=True)}">{content}</a>'
    style = node.get('style', '')
    if re.search(r'font-style:\s*italic', style) or node.name in ('i', 'em'):
        content = f'<em>{content}</em>'
    if re.search(r'font-weight:\s*(700|bold)', style) or node.name in ('b', 'strong'):
        content = f'<strong>{content}</strong>'
    return content

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def header(current):
    links = '\n'.join(f'        <a href="{file}"' + (' aria-current="page"' if current == file else '') + f'>{label}</a>' for file, label, _ in PAGES)
    return f'''<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <a class="site-name" href="index.html">Haishi Li</a>
  <nav aria-label="Main navigation">
{links}
  </nav>
</header>'''

def document(file, title, body):
    description = {
        'Home': 'Haishi "Harry" Li, Assistant Professor in Economics at the University of Hong Kong. Research in international trade and international macroeconomics.',
        'Research': 'Working papers, abstracts, and published research by Haishi "Harry" Li on international trade, multinational production, technology, and climate change.',
        'Policy Discussions': 'Policy discussions, research summaries, and public talks by Haishi "Harry" Li.',
        'International Economics Joint Conference': 'International Economics Joint Conference in the Greater Bay Area: conference programs and calls for papers.',
    }.get(title, 'Haishi "Harry" Li — academic website.')
    canonical = BASE if file == 'index.html' else BASE + file
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape('Haishi “Harry” Li' if title == 'Home' else title + ' | Haishi “Harry” Li')}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{escape(title + ' | Haishi Harry Li', quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}assets/images/haishi-harry-li.jpg">
  <link rel="icon" href="assets/favicon.svg?v=2" type="image/svg+xml">
  <link rel="stylesheet" href="assets/fonts/fonts.css">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{header(file)}
<main id="main" tabindex="-1">
{body}
</main>
</body>
</html>
'''

def main():
    if not ASSET_MANIFEST.exists():
        raise SystemExit('Original migration snapshots are missing; edit the HTML pages directly instead.')
    for file, title, source in PAGES:
        soup = BeautifulSoup((ROOT / '.migration' / source).read_text(), 'html.parser')
        sections = []
        for index, section in enumerate(soup.select('section')):
            elements = section.select('h1.zfr3Q, h2.zfr3Q, h3.zfr3Q, p.zfr3Q')
            if not elements:
                continue
            blocks = []
            intro = file == 'index.html' and index == 0
            for element in elements:
                content = clean(element)
                if not BeautifulSoup(content, 'html.parser').get_text().strip():
                    continue
                if element.name.startswith('h'):
                    text = BeautifulSoup(content, 'html.parser').get_text()
                    tag = 'h1' if (intro and element.name == 'h2') or (file == 'international-economics-joint-conference.html' and not blocks) else 'h2'
                    if intro and element.name == 'h3':
                        blocks.append(f'    <p class="profile-highlight">{content}</p>')
                    else:
                        blocks.append(f'    <{tag} id="{slugify(text)}">{content}</{tag}>')
                else:
                    is_abstract = BeautifulSoup(content, 'html.parser').get_text().lstrip().startswith('Abstract:')
                    cls = ' class="abstract"' if is_abstract else ''
                    blocks.append(f'    <p{cls}>{content}</p>')
            block = '\n'.join(blocks)
            if intro:
                block = f'''  <section class="profile" aria-label="Biography">
    <img class="portrait" src="assets/images/haishi-harry-li.jpg" alt="Haishi Harry Li speaking at an academic event" width="365" height="428" fetchpriority="high">
    <div class="biography">
{block}
    </div>
  </section>'''
            else:
                block = f'  <section class="content-section">\n{block}\n  </section>'
            sections.append(block)
        if file in ('research.html', 'policy-discussions.html'):
            sections.insert(0, f'  <h1 class="visually-hidden">{title}</h1>')
        (ROOT / file).write_text(document(file, title, '\n'.join(sections)))
    (ROOT / '404.html').write_text(document('404.html', 'Page not found', '<section class="content-section"><h1>Page not found</h1><p>This address does not point to a page on this website.</p><p><a href="/">Return to the homepage</a></p></section>').replace('href="assets/', 'href="/assets/').replace('href="index.html"', 'href="/index.html"').replace('href="research.html"', 'href="/research.html"').replace('href="policy-discussions.html"', 'href="/policy-discussions.html"').replace('href="international-economics-joint-conference.html"', 'href="/international-economics-joint-conference.html"'))
    urls = [BASE if file == 'index.html' else BASE + file for file, _, _ in PAGES]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls) + '</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
    (ROOT / '.nojekyll').touch()

if __name__ == '__main__':
    main()
