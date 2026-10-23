"""Build the recovered site using only the Python standard library."""
from pathlib import Path
import os, shutil
from html import escape
ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
SITE_URL = os.environ.get('SITE_URL', 'https://adithyaiyengaryoga-website.yogs313.workers.dev').rstrip('/')
if not SITE_URL.startswith(('https://', 'http://')):
    raise ValueError('SITE_URL must be an absolute HTTP(S) URL')
shutil.copytree(ROOT / 'public', DIST, dirs_exist_ok=True)
partials = {name.upper(): (ROOT / 'src' / 'partials' / f'{name}.html').read_text() for name in ('header', 'footer')}
routes = []
for page in sorted((ROOT / 'src' / 'pages').glob('[!_]*.html')):  # _draft.html pages are not built
    route = '' if page.stem == 'home' else page.stem + '/'
    html = page.read_text()
    for name, value in partials.items():
        html = html.replace('{{' + name + '}}', value)
    html = html.replace('{{SITE_URL}}', escape(SITE_URL, quote=True))
    target = DIST / route / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)
    routes.append(SITE_URL + '/' + route)
(DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('<url><loc>' + escape(url) + '</loc></url>\n' for url in routes) + '</urlset>\n')
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + SITE_URL + '/sitemap.xml\n')
print(f'Built {len(routes)} pages in {DIST}')
