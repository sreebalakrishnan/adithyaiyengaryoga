"""Build the recovered site using only the Python standard library."""
from pathlib import Path
import json, os, re, shutil
from html import escape, unescape
ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
# The site's permanent address, e.g. 'https://example.org'. Until it is set, the site is built for the staging
# address: links and share images point there so they work, and every page asks search engines not to index it.
FINAL_URL = None
SITE_URL = (os.environ.get('SITE_URL') or FINAL_URL or 'https://adithyaiyengaryoga.sreeb.dev').rstrip('/')
if not SITE_URL.startswith(('https://', 'http://')):
    raise ValueError('SITE_URL must be an absolute HTTP(S) URL')
INDEXABLE = FINAL_URL is not None and SITE_URL == FINAL_URL.rstrip('/')
SITE = json.loads((ROOT / 'src' / 'site.json').read_text())  # facts about the institute, used for structured data and llms.txt
PAGE_TYPES = {'narayan-sir': 'ProfilePage', 'practice': 'FAQPage', 'visit': 'ContactPage'}  # schema.org type; others are WebPage


def text(fragment):
    """Visible text of an HTML fragment, on one line."""
    words = re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', fragment)))
    return re.sub(r' ([.,;:?!])', r'\1', words).strip()


def meta(html, attr, name):
    found = re.search(r'<meta\s+content="([^"]*)"\s+%s="%s"' % (attr, name), html)
    return unescape(found.group(1)) if found else None


def structured_data(stem, url, html):
    """JSON-LD for one page: the institute, its teacher, the website, and the page itself."""
    institute, teacher, website = SITE_URL + '/#institute', SITE_URL + '/narayan-sir/#teacher', SITE_URL + '/#website'
    page = {'@type': PAGE_TYPES.get(stem, 'WebPage'), '@id': url + '#page', 'url': url, 'name': text(re.search(r'<title>(.*?)</title>', html, re.S).group(1)),
            'description': meta(html, 'name', 'description'), 'inLanguage': 'en-IN', 'isPartOf': {'@id': website}, 'about': {'@id': institute},
            'primaryImageOfPage': meta(html, 'property', 'og:image')}
    if stem != 'home':
        page['breadcrumb'] = {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE_URL + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': text(re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S).group(1)), 'item': url}]}
    if stem == 'narayan-sir':
        page['mainEntity'] = {'@id': teacher}
    elif stem == 'visit':
        page['mainEntity'] = {'@id': institute}
    elif stem == 'practice':  # the Questions section
        page['mainEntity'] = [{'@type': 'Question', 'name': text(question), 'acceptedAnswer': {'@type': 'Answer', 'text': text(answer)}}
                              for question, answer in re.findall(r'<summary[^>]*>(.*?)</summary>(.*?)</details>', html, re.S)]
    elif stem == 'glossary':
        page['mainEntity'] = {'@type': 'DefinedTermSet', 'name': 'Glossary of yoga terms', 'hasDefinedTerm': [
            {'@type': 'DefinedTerm', 'name': text(term), 'description': text(meaning)}
            for term, meaning in re.findall(r'<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>', html, re.S)]}
    graph = [
        {'@type': 'WebSite', '@id': website, 'url': SITE_URL + '/', 'name': SITE['name'], 'inLanguage': 'en-IN', 'publisher': {'@id': institute}},
        {'@type': 'SportsActivityLocation', '@id': institute, 'name': SITE['name'], 'alternateName': SITE['alternateName'], 'description': SITE['description'],
         'url': SITE_URL + '/', 'logo': SITE_URL + '/logo.png', 'image': SITE_URL + '/og/hall.jpg', 'telephone': SITE['telephone'], 'email': SITE['email'],
         'foundingDate': SITE['foundingDate'], 'address': {'@type': 'PostalAddress', **SITE['address']}, 'geo': {'@type': 'GeoCoordinates', **SITE['geo']},
         'hasMap': SITE['map'], 'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': SITE['days'], **hours} for hours in SITE['hours']],
         'founder': {'@id': teacher}, 'knowsAbout': ['Iyengar yoga', 'Yoga Sutras of Patanjali', 'Pranayama']},
        {'@type': 'Person', '@id': teacher, 'name': SITE['teacher']['name'], 'jobTitle': 'Iyengar yoga teacher', 'description': SITE['teacher']['description'],
         'image': SITE_URL + SITE['teacher']['image'], 'url': SITE_URL + '/narayan-sir/', 'knowsLanguage': SITE['teacher']['knowsLanguage'],
         'worksFor': {'@id': institute}, 'knows': {'@type': 'Person', 'name': 'B.K.S. Iyengar', 'sameAs': 'https://en.wikipedia.org/wiki/B._K._S._Iyengar'}},
        page]
    data = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1).replace('</', '<\\/')
    return '<script type="application/ld+json">\n' + data + '\n    </script>'


shutil.copytree(ROOT / 'public', DIST, dirs_exist_ok=True)
# Browsers keep stylesheets and scripts for a week (the host's default), so a fix would not show for visitors who had
# already loaded the site. Adding the version to their addresses makes every release fetch fresh copies.
ASSET_VERSION = re.search(r'^\| (\d+\.\d+\.\d+) \|', (ROOT / 'CHANGELOG.md').read_text(), re.M).group(1)


def versioned(html):
    return re.sub(r'((?:href|src)=")(/assets/(?:css|js)/[^"?]+)"', lambda m: f'{m.group(1)}{m.group(2)}?v={ASSET_VERSION}"', html)


partials = {name.upper(): (ROOT / 'src' / 'partials' / f'{name}.html').read_text() for name in ('head', 'header', 'footer')}
pages = []  # (url, title, description) of every public page
for page in sorted((ROOT / 'src' / 'pages').glob('[!_]*.html'), key=lambda page: (page.stem != 'home', page.stem)):  # _draft.html pages are not built
    route = '' if page.stem == 'home' else page.stem + '/'
    html = page.read_text()
    for name, value in partials.items():
        html = html.replace('{{' + name + '}}', value)
    html = versioned(html)
    html = html.replace('{{SITE_URL}}', escape(SITE_URL, quote=True)).replace('    {{ROBOTS}}\n', '' if INDEXABLE else '    <meta content="noindex" name="robots" />\n')
    if page.stem == '404':  # served by .htaccess for any missing URL; not in the sitemap
        (DIST / '404.html').write_text(html)
        continue
    url = SITE_URL + '/' + route
    html = html.replace('{{STRUCTURED_DATA}}', structured_data(page.stem, url, html))
    target = DIST / route / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)
    pages.append((url, text(re.search(r'<title>(.*?)</title>', html, re.S).group(1)), meta(html, 'name', 'description')))
(DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('<url><loc>' + escape(url) + '</loc></url>\n' for url, _, _ in pages) + '</urlset>\n')
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\n' + ('Sitemap: ' + SITE_URL + '/sitemap.xml\n' if INDEXABLE else ''))  # crawlers must reach pages to see noindex
address = SITE['address']
(DIST / 'llms.txt').write_text('\n'.join([  # a plain summary for AI assistants and answer engines, see llmstxt.org
    f"# {SITE['name']}", '', f"> {SITE['description']}", '',
    f"- Teacher: {SITE['teacher']['name']}. {SITE['teacher']['description']}",
    f"- Classes: {SITE['days'][0]} to {SITE['days'][-1]}, " + ' and '.join(f"{hours['opens']}–{hours['closes']}" for hours in SITE['hours']) + ' (India time).',
    '- Before the first class, call or email to confirm the batch, the fees and what to bring.',
    f"- Address: {address['streetAddress']}, {address['addressLocality']} {address['postalCode']}, {address['addressRegion']}, India. Map: {SITE['map']}",
    f"- Phone: {SITE['telephone']}. Email: {SITE['email']}",
    f"- Also known as: {', '.join(SITE['alternateName'])}.",
    '', '## Pages', ''] + [f'- [{title}]({url}): {description}' for url, title, description in pages]) + '\n')
changelog = (ROOT / 'CHANGELOG.md').read_text()
version, released = re.search(r'^\| (\d+\.\d+\.\d+) \| (\S+) \|', changelog, re.M).groups()  # the newest row of the version table
notes = re.search(r'^## ' + re.escape(version) + r' .*?\n(.*?)(?=^## |\Z)', changelog, re.M | re.S)
(DIST / 'version.txt').write_text('\n'.join([  # what this build contains; no timestamp, so rebuilding unchanged sources changes nothing
    f"{SITE['name']}: website", f'Version {version}, released {released}',
    f'Built for {SITE_URL}' + ('' if INDEXABLE else ' (staging, not indexed by search engines)'), '',
    f'What changed in {version}:', '', notes.group(1).strip() if notes else '(no notes in CHANGELOG.md)', '',
    'Every version: https://github.com/sreebalakrishnan/adithyaiyengaryoga/blob/main/CHANGELOG.md']) + '\n')
print(f'Built {len(pages)} pages, version {version}, in {DIST} for {SITE_URL}' + ('' if INDEXABLE else ' (staging: not indexed)'))
