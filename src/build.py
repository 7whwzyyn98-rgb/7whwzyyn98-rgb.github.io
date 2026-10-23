#!/usr/bin/env python3
"""Static generator for usecontesta.com.

Run from the repo root:  python3 src/build.py
Writes /es/, /en/, /assets/, sitemap.xml, robots.txt, the root language redirect and /demo/ redirect.
Every indexable page exists in Spanish and English with reciprocal hreflang and a self-canonical URL.
"""
import datetime, hashlib, html, json, pathlib, shutil
from content import PAGES, NAV, FOOT, home, page_body  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
SITE = 'https://usecontesta.com'
TODAY = datetime.date.today().isoformat()
LOGO_SVG = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#173D30"/>'
            '<g transform="translate(6.2 6.2) scale(.82)"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z" fill="#D9EF8B"/></g></svg>')


def asset_versions():
    out = {}
    (ROOT / 'assets').mkdir(exist_ok=True)
    for name in ['site.css', 'site.js', 'app.js']:
        data = (SRC / name).read_bytes()
        (ROOT / 'assets' / name).write_bytes(data)
        out[name] = hashlib.sha1(data).hexdigest()[:8]
    return out


def url(key, lang):
    return PAGES[key][lang]['path']


def head(key, lang, p, v):
    other = 'en' if lang == 'es' else 'es'
    title = html.escape(p['title']); desc = html.escape(p['desc'])
    canon = SITE + p['path']
    alts = ''
    if not p.get('noindex'):
        alts = (f'<link rel="alternate" hreflang="{lang}" href="{canon}">\n'
                f'<link rel="alternate" hreflang="{other}" href="{SITE + url(key, other)}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{SITE + url(key, "es")}">\n')
    robots = '<meta name="robots" content="noindex">\n' if p.get('noindex') else ''
    ld = ''
    for block in p.get('ld', []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + '</script>\n'
    og_img = f'{SITE}/assets/og-{lang}.png'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canon}">
{alts}<meta name="theme-color" content="#173D30">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Contesta">
<meta property="og:locale" content="{'es_US' if lang == 'es' else 'en_US'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gabarito:wght@700;800&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={v['site.css']}">
{ld}</head>'''


def header(key, lang):
    n = NAV[lang]
    other = 'en' if lang == 'es' else 'es'
    cur = ' aria-current="page"'
    links = ''.join(
        f'<a href="{url(k, lang)}"{cur if k == key else ""}>{html.escape(label)}</a>' for k, label in n['links'])
    sw = (f'<a class="lang-link" href="{url(key, other)}" hreflang="{other}" lang="{other}" data-lang-switch="{other}">'
          f'{"EN" if other == "en" else "ES"}<span class="hp"> {html.escape(n["switch"])}</span></a>')
    return f'''<a class="skip" href="#main">{html.escape(n['skip'])}</a>
<header class="top"><div class="wrap nav">
<a class="brand" href="{url('home', lang)}" aria-label="Contesta">{LOGO_SVG}<span>Contesta</span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">{html.escape(n['menu'])}</button>
<nav class="nav-links" id="nav-links" aria-label="{html.escape(n['aria'])}">{links}{sw}
<a class="btn small" href="{url('signup', lang)}">{html.escape(n['cta'])}</a></nav>
</div></header>'''


def footer(key, lang):
    f = FOOT[lang]
    other = 'en' if lang == 'es' else 'es'
    cols = ''
    for title, items in f['cols']:
        lis = ''.join(f'<li><a href="{url(k, lang)}">{html.escape(t)}</a></li>' for k, t in items)
        cols += f'<div><h3>{html.escape(title)}</h3><ul>{lis}</ul></div>'
    return f'''<footer><div class="wrap">
<div class="foot-grid"><div class="stack"><p class="foot-brand">Contesta</p><p>{html.escape(f['tag'])}</p>
<p><a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a><br>{html.escape(f['demo'])} <a href="tel:+18137221120">(813) 722-1120</a></p></div>{cols}</div>
<div class="foot-legal"><span>© 2026 Contesta LLC · Tampa, Florida</span><span>{html.escape(f['legal'])}</span>
<a href="{url('privacy', lang)}">{html.escape(PAGES['privacy'][lang]['crumb'])}</a><a href="{url('terms', lang)}">{html.escape(PAGES['terms'][lang]['crumb'])}</a>
<a href="{url(key, other)}" hreflang="{other}" lang="{other}" data-lang-switch="{other}">{html.escape(f['switch'])}</a></div>
</div></footer>'''


def crumbs(key, lang, p):
    if key == 'home' or p.get('noindex'):
        return '', None
    trail = [('home', PAGES['home'][lang]['crumb'])]
    if p.get('parent'):
        trail.append((p['parent'], PAGES[p['parent']][lang]['crumb']))
    trail.append((key, p['crumb']))
    items = ''.join(f'<li><a href="{url(k, lang)}">{html.escape(t)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{html.escape(t)}</li>'
                    for i, (k, t) in enumerate(trail))
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': t, 'item': SITE + url(k, lang)} for i, (k, t) in enumerate(trail)]}
    label = 'Ruta' if lang == 'es' else 'Breadcrumb'
    return f'<nav class="crumbs" aria-label="{label}"><ol>{items}</ol></nav>', ld


def render(key, lang, v):
    p = dict(PAGES[key][lang])
    body = home(lang) if key == 'home' else page_body(key, lang)
    cr, cr_ld = crumbs(key, lang, p)
    if cr_ld:
        p['ld'] = list(p.get('ld', [])) + [cr_ld]
    scripts = f'<script src="/assets/site.js?v={v["site.js"]}" defer></script>'
    if p.get('app'):
        scripts += f'\n<script src="/assets/app.js?v={v["app.js"]}" defer></script>'
    if cr:
        body = body.replace('<!--CRUMBS-->', cr, 1)
    doc = (head(key, lang, p, v) + '\n<body>\n' + header(key, lang) + '\n<main id="main">\n' + body + '\n</main>\n' +
           footer(key, lang) + '\n' + scripts + '\n</body>\n</html>\n')
    out = ROOT / p['path'].lstrip('/') / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    return p


def redirects():
    (ROOT / 'index.html').write_text('''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contesta · Recepcionista con IA en español e inglés</title>
<meta name="robots" content="noindex">
<link rel="alternate" hreflang="es" href="https://usecontesta.com/es/">
<link rel="alternate" hreflang="en" href="https://usecontesta.com/en/">
<link rel="alternate" hreflang="x-default" href="https://usecontesta.com/es/">
<script>
/* Root keeps old links working: #en (and a saved English choice) open /en/; anything else opens /es/ with its anchor. No IP or browser-language guessing. */
(function () {
  var h = location.hash, saved = null;
  try { saved = localStorage.getItem('contesta-lang'); } catch (e) {}
  var en = h === '#en' || (!h && saved === 'en');
  var dest = (en ? '/en/' : '/es/') + location.search + (h && h !== '#en' && h !== '#es' ? h : '');
  location.replace(dest);
})();
</script>
<noscript><meta http-equiv="refresh" content="0; url=/es/"></noscript>
<style>body{margin:0;font:17px/1.6 system-ui,sans-serif;background:#F7F5EE;color:#173D30;padding:32px 16px}a{color:#173D30}</style>
</head>
<body><p><a href="/es/">Español</a> · <a href="/en/">English</a></p></body>
</html>
''')
    # Short links used in outreach emails (/demo, /empezar). Tagged as email so those visits and signups aren't counted as
    # direct or organic.
    for slug, dest, en_dest, title, es_label, en_label in [
            ('demo', '/es/demo/', '/en/demo/', 'Contesta · Demo', 'Ver la demo', 'See the demo'),
            ('empezar', '/es/registro/', '/en/signup/', 'Contesta · Empezar', 'Crear mi cuenta', 'Create my account')]:
        d = ROOT / slug; d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://usecontesta.com{dest}">
<script>
/* /{slug} is a short link used in outreach emails. It is tagged as email so it is not counted as direct or organic. */
(function () {{
  var q = location.search;
  if (!/utm_/.test(q)) q = (q ? q + '&' : '?') + 'utm_source=outreach&utm_medium=email';
  location.replace('{dest}' + q + location.hash);
}})();
</script>
<noscript><meta http-equiv="refresh" content="0; url={dest}?utm_source=outreach&utm_medium=email"></noscript>
<style>body{{margin:0;font:17px/1.6 system-ui,sans-serif;background:#F7F5EE;color:#173D30;padding:32px 16px}}a{{color:#173D30}}</style>
</head>
<body><p><a href="{dest}">{es_label}</a> · <a href="{en_dest}">{en_label}</a></p></body>
</html>
''')


def not_found(v):
    (ROOT / '404.html').write_text(f'''<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página no encontrada · Contesta</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css?v={v['site.css']}"></head>
<body><main id="main"><section><div class="wrap narrow stack">
<a class="brand" href="/es/">{LOGO_SVG}<span>Contesta</span></a>
<h1>Esta página no existe.</h1><p class="lede">This page doesn't exist.</p>
<div class="btn-row"><a class="btn" href="/es/">Ir al inicio</a><a class="btn ghost" href="/en/" lang="en">Go to the English site</a></div>
</div></section></main></body></html>
''')


def sitemap(rendered):
    rows = []
    for key, langs in PAGES.items():
        if langs['es'].get('noindex'):
            continue
        for lang in ('es', 'en'):
            alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE + langs[l]["path"]}"/>' for l in ('es', 'en'))
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE + langs["es"]["path"]}"/>'
            rows.append(f'  <url>\n    <loc>{SITE + langs[lang]["path"]}</loc>\n    <lastmod>{TODAY}</lastmod>{alts}\n  </url>')
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                      'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://usecontesta.com/sitemap.xml\n')


def main():
    v = asset_versions()
    rendered = {}
    for key in PAGES:
        for lang in ('es', 'en'):
            rendered[(key, lang)] = render(key, lang, v)
    redirects(); not_found(v); sitemap(rendered)
    (ROOT / 'favicon.svg').write_text(LOGO_SVG.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"') + '\n')
    print('pages', len(rendered))


if __name__ == '__main__':
    main()
