#!/usr/bin/env python3
"""Deterministic, offline static SEO build pass. No GitHub or deployment calls.

Run after navigation/listing-retirement preparation, before sitemap validation:
  python3 scripts/seo_audit.py --root . --apply
  python3 scripts/seo_audit.py --root . --check
Bulk HTML and sitemap outputs are generated at build time, not a second dataset.
"""
from __future__ import annotations
import argparse
import html
import json
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ORIGIN = 'https://praia.digital'
IMAGE = ORIGIN + '/assets/social/praia-digital-institucional-v1.png'
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
SKIP_DIRS = {'.git', '.github', '.audit', '.hermes-tmp-idempotency', '.venv',
             'node_modules', 'backup', 'backups', 'dist', 'build', '__pycache__'}
INTERNAL_DIRS = {'admin', 'api', 'backend', 'automation', 'dashboard', 'dashboards',
                 'lead', 'leads', 'outreach', 'scripts', 'tests', 'partials', 'templates', 'uploads'}
INTERNAL_FILES = {'404.html', 'acoes-hoje.html', 'acompanhamento-prospeccao.html',
                  'central-comando-praia-digital.html', 'top5-leads-hoje.html', 'form-tracker.html'}
META_KEYS = {'description', 'robots', 'googlebot', 'og:type', 'og:title', 'og:description',
             'og:url', 'og:image', 'og:image:alt', 'og:image:type', 'og:image:width',
             'og:image:height', 'og:site_name', 'og:locale', 'twitter:card',
             'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt'}
HEAD_RE = re.compile(r'(<head\b[^>]*>)(.*?)(</head\s*>)', re.I | re.S)
LD_RE = re.compile(r'<script\b(?=[^>]*\btype\s*=\s*[\"\']application/ld\+json[\"\'])[^>]*>(.*?)</script\s*>', re.I | re.S)


def is_internal(rel):
    path = Path(rel).as_posix().lstrip('/')
    parts = path.split('/')
    return (any(p in INTERNAL_DIRS or p.startswith('.') for p in parts[:-1])
            or parts[-1] in INTERNAL_FILES
            or parts[-1].startswith(('obrigado-', 'dashboard-', 'proposta-piloto-'))
            or path.startswith(('docs/sales/', 'docs/product/', 'docs/seo/')))


def public_url(rel):
    path = Path(rel).as_posix().lstrip('/')
    if path == 'index.html':
        path = ''
    elif path.endswith('/index.html'):
        path = path[:-10]
    return ORIGIN + '/' + quote(path, safe='/-._~')


def local_file(url, root):
    parts = urlsplit(url)
    if parts.scheme != 'https' or parts.netloc != 'praia.digital' or parts.query or parts.fragment:
        return None
    decoded = unquote(parts.path)
    if '..' in decoded.split('/') or '\\' in decoded:
        return None
    root = Path(root).resolve()
    target = root / decoded.lstrip('/')
    if decoded.endswith('/') or target.is_dir():
        target = target / 'index.html'
    try:
        target = target.resolve()
        target.relative_to(root)
    except (ValueError, OSError):
        return None
    return target if target.is_file() and target.suffix.lower() in {'.html', '.htm'} else None


class HeadInfo(HTMLParser):
    """Record editable tag spans without reserializing the page body."""
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.lines = [0] + [m.end() for m in re.finditer('\n', source)]
        self.metas, self.canonicals, self.edits = {}, [], []
        self.title, self.in_title, self.refresh = '', False, False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = {k.lower(): (v or '') for k, v in attrs}
        row, col = self.getpos()
        span = (self.lines[row - 1] + col, len(self.get_starttag_text()))
        if tag == 'title':
            self.in_title = True
        if tag == 'meta':
            key = (attrs.get('property') or attrs.get('name') or '').lower()
            self.metas.setdefault(key, []).append(attrs.get('content', ''))
            if key in META_KEYS:
                self.edits.append(span)
            if attrs.get('http-equiv', '').lower() == 'refresh':
                self.refresh = True
        if tag == 'link':
            if 'canonical' in attrs.get('rel', '').lower().split():
                self.canonicals.append(attrs.get('href', ''))
                self.edits.append(span)
            elif '/css/seo-responsive.css' in attrs.get('href', ''):
                self.edits.append(span)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

    def first(self, key, default=''):
        return next((v for v in self.metas.get(key, []) if v.strip()), default)

    @property
    def noindex(self):
        tokens = ' '.join(self.metas.get('robots', []) + self.metas.get('googlebot', [])).lower()
        return bool({'noindex', 'none'} & set(re.split(r'[\s,]+', tokens)))


def read_head(text):
    match = HEAD_RE.search(text)
    return HeadInfo(match.group(2)) if match else None


def catalog_items(root):
    source = (Path(root) / 'js/main.js').read_text(encoding='utf-8')
    match = re.search(r'\bconst\s+properties\s*=\s*(\[)', source)
    if not match:
        raise ValueError('Active properties array missing; refusing to invent catalog data')
    properties, _ = json.JSONDecoder().raw_decode(source[match.start(1):])
    properties = [p for p in properties if p.get('active', True) is not False]
    properties.sort(key=lambda p: -float(p.get('score') or 0))
    items, seen = [], set()
    for p in properties:
        slug = p['slug']
        if not re.fullmatch(r'(?:\.\./)?[\w-]+', slug):
            raise ValueError('Unsafe catalog slug: ' + slug)
        rel = slug[3:] + '.html' if slug.startswith('../') else 'imoveis/' + slug + '.html'
        url = public_url(rel)
        if url in seen:
            raise ValueError('Duplicate active catalog URL: ' + url)
        seen.add(url)
        items.append({'@type': 'ListItem', 'position': len(items) + 1, 'url': url, 'name': p['title']})
    return items


def catalog_schema(items):
    return {'@context': 'https://schema.org', '@type': 'ItemList',
            '@id': ORIGIN + '/imoveis.html#catalog-itemlist', 'name': 'Imóveis no litoral de SP',
            'numberOfItems': len(items), 'itemListElement': items}


def sync_catalog(text, items):
    def remove_old(match):
        value = json.loads(match.group(1))
        if isinstance(value, dict) and value.get('@type') == 'ItemList':
            return ''
        if isinstance(value, dict) and isinstance(value.get('@graph'), list):
            value['@graph'] = [v for v in value['@graph'] if v.get('@type') != 'ItemList']
            return '<script type="application/ld+json">' + json.dumps(value, ensure_ascii=False, sort_keys=True) + '</script>'
        return match.group(0)
    # Remove owned trailing whitespace with the old block, not just its tag.
    text = re.sub(LD_RE.pattern + r'[ \t\r\n]*', remove_old, text, flags=LD_RE.flags)
    payload = json.dumps(catalog_schema(items), ensure_ascii=False, sort_keys=True).replace('<', '\\u003c')
    # Replace both managed scripts as one stable head suffix. Removing just the
    # ItemList moved it past the runtime script on pass two and retained a new
    # blank line on every pass. Do not change unrelated scripts or page bodies.
    runtime = re.compile(
        r'<script\b(?=[^>]*\bsrc\s*=\s*["\'](?:https://praia\.digital)?'
        r'/js/catalog-seo\.js(?:\?[^"\']*)?["\'])[^>]*>\s*</script\s*>[ \t\r\n]*', re.I)
    text = runtime.sub('', text)
    block = '<script id="catalog-itemlist" type="application/ld+json">' + payload + '</script>\n'
    block += '<script defer src="/js/catalog-seo.js"></script>\n'
    text = HEAD_RE.sub(lambda m: m.group(1) + m.group(2).rstrip() + '\n' + block + m.group(3),
                       text, count=1)
    cards = '\n'.join('<article class="property-card"><h3 class="property-title"><a href="' +
                      html.escape(urlsplit(p['url']).path, quote=True) + '">' +
                      html.escape(p['name']) + '</a></h3><a class="btn-secondary" href="' +
                      html.escape(urlsplit(p['url']).path, quote=True) + '">Ver detalhes</a></article>'
                      for p in items)
    content = '<!-- SEO_CATALOG_START -->\n' + cards + '\n<!-- SEO_CATALOG_END -->'
    if '<!-- SEO_CATALOG_START -->' in text:
        text = re.sub(r'<!-- SEO_CATALOG_START -->.*?<!-- SEO_CATALOG_END -->',
                      lambda m: content, text, count=1, flags=re.S)
    else:
        pattern = r'(<div\b[^>]*\bid=[\"\']lista-imoveis[\"\'][^>]*>)\s*<!-- Carregado via JS -->\s*(</div>)'
        text, count = re.subn(pattern, lambda m: m.group(1) + content + m.group(2), text, count=1, flags=re.I)
        if not count:
            raise ValueError('Catalog container changed; refusing to overwrite unknown body content')
    return text


def normalize_html(text, rel, root=None):
    match = HEAD_RE.search(text)
    if not match:
        return text
    info = HeadInfo(match.group(2))
    canonical = public_url(rel)
    alias = False
    if root and len(info.canonicals) == 1:
        target = local_file(urljoin(ORIGIN + '/', info.canonicals[0]), root)
        own = (Path(root) / rel).resolve()
        if target is not None and target != own:
            canonical, alias = urljoin(ORIGIN + '/', info.canonicals[0]), True
    noindex = info.noindex or info.refresh or is_internal(rel) or alias
    tokens = set(re.split(r'[\s,]+', ' '.join(info.metas.get('robots', []) + info.metas.get('googlebot', [])).lower()))
    if 'none' in tokens:
        tokens.add('nofollow')
    tokens -= {'', 'none', 'index', 'noindex'}
    if 'nofollow' not in tokens:
        tokens.add('follow')
    else:
        tokens.discard('follow')
    robots = ', '.join(['noindex' if noindex else 'index'] + sorted(tokens))
    title = ' '.join(info.title.split()) or Path(rel).stem.replace('-', ' ') + ' | Praia Digital'
    description = info.first('description')
    if not description or description in {'Voltar para a Praia Digital', 'Conteúdo sobre imóveis no litoral paulista.'}:
        description = title.split(' | ')[0] + ': informações e atendimento da Praia Digital para imóveis no litoral paulista.'
    image = urljoin(ORIGIN + '/', info.first('og:image') or info.first('twitter:image') or IMAGE)
    if urlsplit(image).scheme not in {'http', 'https'}:
        image = IMAGE
    image_alt = info.first('og:image:alt') or info.first('twitter:image:alt') or title
    values = [('name', 'description', description), ('name', 'robots', robots),
              ('property', 'og:type', info.first('og:type', 'website')),
              ('property', 'og:title', title), ('property', 'og:description', description),
              ('property', 'og:url', canonical), ('property', 'og:site_name', 'Praia Digital'),
              ('property', 'og:locale', 'pt_BR'), ('property', 'og:image', image),
              ('property', 'og:image:alt', image_alt), ('name', 'twitter:card', 'summary_large_image'),
              ('name', 'twitter:title', title), ('name', 'twitter:description', description),
              ('name', 'twitter:image', image), ('name', 'twitter:image:alt', image_alt)]
    if image == IMAGE:
        values += [('property', 'og:image:type', 'image/png'), ('property', 'og:image:width', '1200'),
                   ('property', 'og:image:height', '630')]
    tags = ['<link rel="canonical" href="' + html.escape(canonical, quote=True) + '">']
    tags += ['<meta ' + kind + '="' + key + '" content="' + html.escape(value, quote=True) + '">'
             for kind, key, value in values]
    tags += ['<link rel="stylesheet" href="/css/seo-responsive.css">']
    head = match.group(2)
    for start, length in sorted(info.edits, reverse=True):
        # Consume each managed tag's formatting whitespace as well. Otherwise
        # catalog insertion can strand old metadata newlines before its script.
        end = start + length
        while end < len(head) and head[end] in ' \t\r\n':
            end += 1
        head = head[:start] + head[end:]
    # Whitespace at the end is normalized so repeated builds are byte-stable.
    head = head.rstrip() + '\n' + '\n'.join(tags) + '\n'
    result = text[:match.start(2)] + head + text[match.end(2):]
    return result.replace(ORIGIN + '/litoral-prime-imoveis/img/logo.png', ORIGIN + '/img/logo.png')


def robots_text(names):
    return ('# Private material requires access control; robots.txt is not security.\n'
            '# Do not disallow public noindex pages: crawlers must read their directives.\n'
            'User-agent: *\nDisallow: /.git/\nDisallow: /.github/\n'
            'Disallow: /node_modules/\nDisallow: /backup/\nDisallow: /backups/\n'
            'Disallow: /scripts/\nAllow: /css/\nAllow: /js/\nAllow: /assets/\n\n' +
            ''.join('Sitemap: ' + ORIGIN + '/' + name + '\n' for name in sorted(names)))


def apply_site(root, write=False):
    root = Path(root).resolve()
    groups = {}
    for path in sorted(root.glob('sitemap*.xml')):
        tree = ET.parse(path).getroot()
        if tree.tag != '{' + NS + '}urlset':
            raise ValueError('Expected URL set, not a silently flattened sitemap index: ' + path.name)
        groups[path.name] = [n.text or '' for n in tree.findall('.//{' + NS + '}loc')]
    groups.setdefault('sitemap.xml', [])
    items = catalog_items(root) if (root / 'imoveis.html').is_file() else []
    groups['sitemap.xml'] = list(dict.fromkeys([u for urls in groups.values() for u in urls] +
                                             [p['url'] for p in items]))
    outputs, infos = {}, {}
    changed_html = 0
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith('.'))
        for filename in sorted(files):
            if not filename.endswith(('.html', '.htm')):
                continue
            path = Path(directory) / filename
            rel = path.relative_to(root).as_posix()
            source = path.read_text(encoding='utf-8', errors='surrogateescape')
            text = sync_catalog(source, items) if rel == 'imoveis.html' else source
            text = normalize_html(text, rel, root)
            infos[path.resolve()] = read_head(text)
            if text != source:
                outputs[path] = text
                changed_html += 1
    counts, excluded = {}, {}
    for name, urls in sorted(groups.items()):
        included = set()
        for url in urls:
            path = local_file(url, root)
            info = infos.get(path)
            if path is None or info is None:
                excluded['missing_or_non_html'] = excluded.get('missing_or_non_html', 0) + 1
                continue
            rel = path.relative_to(root).as_posix()
            if info.noindex or info.refresh or is_internal(rel) or len(info.canonicals) != 1:
                excluded['non_indexable'] = excluded.get('non_indexable', 0) + 1
                continue
            canonical = info.canonicals[0]
            if local_file(canonical, root) != path or canonical != public_url(rel):
                excluded['canonical_alias'] = excluded.get('canonical_alias', 0) + 1
                continue
            included.add(canonical)
        body = '\n'.join('  <url><loc>' + html.escape(url, quote=False) + '</loc></url>' for url in sorted(included))
        output = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="' + NS + '">\n' + body + '\n</urlset>\n'
        path = root / name
        if not path.exists() or path.read_text(encoding='utf-8') != output:
            outputs[path] = output
        counts[name] = len(included)
    robots = robots_text(groups)
    if not (root / 'robots.txt').exists() or (root / 'robots.txt').read_text(encoding='utf-8') != robots:
        outputs[root / 'robots.txt'] = robots
    # Calculate everything before modifying files. No HTML pages are deleted.
    if write:
        for path, text in outputs.items():
            path.write_text(text, encoding='utf-8', errors='surrogateescape')
    return {'changed_files': len(outputs), 'changed_html': changed_html, 'sitemap_urls': counts,
            'excluded_url_entries': excluded, 'active_catalog_items': len(items),
            'mode': 'apply' if write else 'check'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--apply', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    report = apply_site(args.root, write=args.apply)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return 1 if args.check and report['changed_files'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
