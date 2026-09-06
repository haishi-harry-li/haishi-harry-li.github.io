"""Validate local links and migrated content. Run: python scripts/check_site.py."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import re
from bs4 import BeautifulSoup
from import_site import PAGES, BASE

ROOT = Path(__file__).resolve().parents[1]

def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()

checks = 0
for file, _, source in PAGES:
    page = BeautifulSoup((ROOT / file).read_text(), 'html.parser')
    assert len(page.select('h1')) == 1, file
    assert page.html['lang'] == 'en', file
    assert page.select_one('a[aria-current="page"]')['href'] == file, file
    canonical = BASE if file == 'index.html' else BASE + file
    assert page.select_one('link[rel="canonical"]')['href'] == canonical, file
    ids = [n['id'] for n in page.select('[id]')]
    assert len(ids) == len(set(ids)), f'Duplicate IDs: {file}'
    for el in page.select('[href], [src]'):
        url = el.get('href', el.get('src'))
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            if el.name != 'a' and not (el.name == 'link' and 'canonical' in el.get('rel', [])):
                raise AssertionError(f'External runtime dependency: {file} {url}')
            continue
        path = parsed.path.lstrip('/')
        target = ROOT / (unquote(path) or file)
        assert target.is_file(), f'Missing target: {file} -> {url}'
        if parsed.fragment and target.suffix == '.html':
            dest = BeautifulSoup(target.read_text(), 'html.parser')
            assert dest.find(id=parsed.fragment), f'Missing anchor: {file} -> {url}'
        checks += 1
    source_path = ROOT / '.migration' / source
    if source_path.exists():
        original = BeautifulSoup(source_path.read_text(), 'html.parser')
        source_blocks = original.select('section h1.zfr3Q, section h2.zfr3Q, section h3.zfr3Q, section p.zfr3Q')
        expected = [normalized(n.get_text()) for n in source_blocks if normalized(n.get_text())]
        actual = [normalized(n.get_text()) for n in page.select('main section h1, main section h2, main section p')]
        assert expected == actual, f'Content differs: {file}\nExpected: {expected}\nActual: {actual}'
        # Every source hyperlink must survive, except heading widgets, migrated assets and Scholar tracking parameters.
        from import_site import REPLACEMENTS
        def map_url(u):
            if u.startswith('https://scholar.google.com/citations'):
                return 'https://scholar.google.com/citations?user=2NppHJkAAAAJ&hl=en'
            return REPLACEMENTS.get(u, u)
        before = Counter(map_url(a['href']) for a in original.select('section a[href]') if not a['href'].startswith('#'))
        after = Counter(a['href'] for a in page.select('main a[href]'))
        assert before == after, f'Link inventory differs: {file}: {before-after}, {after-before}'
        print(f'{file}: {len(expected)} content blocks and {sum(before.values())} links match source')
for pdf in (ROOT / 'assets').rglob('*.pdf'):
    assert pdf.read_bytes().startswith(b'%PDF'), f'Not a PDF: {pdf}'
for css in (ROOT / 'assets').rglob('*.css'):
    for url in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text()):
        assert not url.startswith(('http:', 'https:', '//')), css
        assert (css.parent / url).is_file(), url
print(f'PASS: {checks} local references, PDF signatures, local fonts, metadata and content checks')
