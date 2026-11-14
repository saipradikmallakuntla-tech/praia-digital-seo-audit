"""Offline regression tests. Optional real Chromium geometry: SEO_BROWSER_TESTS=1.
Run: python3 -m unittest discover -s tests -p 'test_seo_audit.py' -v
"""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('seo_audit', ROOT / 'scripts/seo_audit.py')
seo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seo)


def page(head='', body='<h1>Imóveis no litoral</h1>'):
    return '<!doctype html><html lang="pt-BR"><head><title>Teste | Praia Digital</title>' + head + '</head><body><main>' + body + '</main></body></html>'


class SeoAuditTests(unittest.TestCase):
    def test_production_self_canonical(self):
        info = seo.read_head(seo.normalize_html(page(), 'cidades/bertioga.html'))
        self.assertEqual(info.canonicals, ['https://praia.digital/cidades/bertioga.html'])

    def test_directory_and_home_canonicals(self):
        self.assertEqual(seo.public_url('index.html'), 'https://praia.digital/')
        self.assertEqual(seo.public_url('blog/index.html'), 'https://praia.digital/blog/')
        self.assertIn('%C3%A1', seo.public_url('blog/guarujá.html'))

    def test_social_tags_match_canonical_title_and_description(self):
        result = seo.normalize_html(page('<meta name="description" content="Descrição útil.">'), 'sobre.html')
        info = seo.read_head(result)
        self.assertEqual(info.first('og:url'), info.canonicals[0])
        self.assertEqual(info.first('og:title'), info.title)
        self.assertEqual(info.first('twitter:title'), info.title)
        self.assertEqual(info.first('twitter:description'), 'Descrição útil.')
        self.assertEqual(info.first('twitter:card'), 'summary_large_image')
        self.assertEqual(info.first('og:image'), info.first('twitter:image'))
        self.assertEqual(info.first('og:image:width'), '1200')

    def test_duplicate_metadata_collapses(self):
        result = seo.normalize_html(page('<meta name="description" content="A"><meta name="description" content="B"><link rel="canonical" href="https://wrong.example/">'), 'sobre.html')
        info = seo.read_head(result)
        self.assertEqual(info.metas['description'], ['A'])
        self.assertEqual(info.canonicals, ['https://praia.digital/sobre.html'])

    def test_operational_pages_are_noindex(self):
        for rel in ['acoes-hoje.html', 'acompanhamento-prospeccao.html', 'obrigado-contato.html', 'docs/sales/dashboard.html']:
            with self.subTest(rel=rel):
                info = seo.read_head(seo.normalize_html(page(), rel))
                self.assertTrue(info.noindex)
                self.assertIn('follow', info.first('robots'))

    def test_public_docs_are_not_blanket_noindexed(self):
        self.assertFalse(seo.read_head(seo.normalize_html(page(), 'docs/inteligencia/boletim.html')).noindex)

    def test_existing_noindex_and_nofollow_survive(self):
        result = seo.normalize_html(page('<meta name="robots" content="noindex,nofollow">'), 'guia.html')
        self.assertEqual(seo.read_head(result).first('robots'), 'noindex, nofollow')

    def test_refresh_not_indexable(self):
        self.assertTrue(seo.read_head(seo.normalize_html(page('<meta http-equiv="refresh" content="0; url=/">'), 'antigo.html')).noindex)

    def test_html_body_is_preserved(self):
        source = page(body='<h1>Correto</h1><form><input name="nome"></form><!-- editorial -->')
        self.assertEqual(source.split('</head>')[1], seo.normalize_html(source, 'sobre.html').split('</head>')[1])

    def test_head_normalization_is_idempotent(self):
        one = seo.normalize_html(page(), 'sobre.html')
        self.assertEqual(one, seo.normalize_html(one, 'sobre.html'))

    def test_robots_does_not_block_noindex_or_assets(self):
        robots = seo.robots_text(['sitemap.xml'])
        self.assertNotIn('Disallow: /docs/', robots)
        self.assertNotIn('Disallow: /acoes-hoje.html', robots)
        self.assertIn('Allow: /css/', robots)
        self.assertIn('Sitemap: https://praia.digital/sitemap.xml', robots)

    def test_encoded_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertIsNone(seo.local_file('https://praia.digital/%2e%2e/secret.html', directory))
            self.assertIsNone(seo.local_file('https://other.example/a.html', directory))

    def test_alias_is_preserved_but_not_indexable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'index.html').write_text(page(), encoding='utf-8')
            source = page('<link rel="canonical" href="https://praia.digital/">')
            (root / 'home-classica.html').write_text(source, encoding='utf-8')
            info = seo.read_head(seo.normalize_html(source, 'home-classica.html', root))
            self.assertEqual(info.canonicals, ['https://praia.digital/'])
            self.assertTrue(info.noindex)

    def fixture(self, root):
        (root / 'js').mkdir()
        data = [{'slug': 'apartamento-real', 'title': 'Apartamento real', 'score': 1},
                {'slug': '../casa-real', 'title': 'Casa real', 'score': 2}]
        (root / 'js/main.js').write_text('const properties = ' + json.dumps(data) + ';', encoding='utf-8')
        (root / 'imoveis').mkdir()
        for rel in ['index.html', 'casa-real.html', 'imoveis/apartamento-real.html', 'acoes-hoje.html', 'noindex.html', 'antigo.html']:
            head = '<meta name="robots" content="noindex,follow">' if rel == 'noindex.html' else ''
            if rel == 'antigo.html':
                head = '<meta http-equiv="refresh" content="0; url=/">'
            (root / rel).write_text(page(head), encoding='utf-8')
        old = '<script type="application/ld+json">{"@type":"ItemList","itemListElement":[]}</script>'
        (root / 'imoveis.html').write_text(page(old, '<div id="lista-imoveis"><!-- Carregado via JS --></div>'), encoding='utf-8')
        urls = ['index.html', 'imoveis.html', 'casa-real.html', 'imoveis/apartamento-real.html', 'acoes-hoje.html', 'noindex.html', 'antigo.html', 'missing.html']
        (root / 'sitemap.xml').write_text('<urlset xmlns="' + seo.NS + '">' + ''.join('<url><loc>' + seo.ORIGIN + '/' + u + '</loc></url>' for u in urls) + '</urlset>', encoding='utf-8')

    def test_catalog_uses_actual_dataset_not_a_second_list(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            items = seo.catalog_items(root)
            self.assertEqual([p['name'] for p in items], ['Casa real', 'Apartamento real'])
            result = seo.sync_catalog((root / 'imoveis.html').read_text(), items)
            blocks = [json.loads(m.group(1)) for m in seo.LD_RE.finditer(result)]
            self.assertEqual(len(blocks), 1)
            self.assertEqual(blocks[0]['itemListElement'], items)
            self.assertEqual(blocks[0]['numberOfItems'], 2)
            self.assertIn('/casa-real.html', result)
            self.assertIn('/js/catalog-seo.js', result)
            self.assertEqual(result, seo.sync_catalog(result, items))

    def test_sitemap_contains_only_canonical_indexable_existing_html(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            report = seo.apply_site(root, write=True)
            urls = [n.text for n in ET.parse(root / 'sitemap.xml').findall('.//{' + seo.NS + '}loc')]
            self.assertEqual(len(urls), 4)
            self.assertIn('https://praia.digital/', urls)
            self.assertFalse(any(t in u for u in urls for t in ['acoes-hoje', 'noindex', 'antigo', 'missing']))
            self.assertEqual(report['active_catalog_items'], 2)

    def test_build_is_idempotent_and_check_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.fixture(root)
            before = (root / 'sitemap.xml').read_bytes()
            self.assertGreater(seo.apply_site(root)['changed_files'], 0)
            self.assertEqual(before, (root / 'sitemap.xml').read_bytes())
            seo.apply_site(root, write=True)
            self.assertEqual(seo.apply_site(root)['changed_files'], 0)

    def test_responsive_css_does_not_hide_overflow(self):
        css = (ROOT / 'css/seo-responsive.css').read_text()
        self.assertIn('max-width: 100%', css)
        self.assertIn('height: auto', css)
        self.assertNotIn('overflow-x: hidden', css)


@unittest.skipUnless(os.environ.get('SEO_BROWSER_TESTS') == '1', 'Set SEO_BROWSER_TESTS=1; requires Playwright Chromium')
class ResponsiveBrowserTests(unittest.TestCase):
    def test_800px_hero_regression(self):
        from playwright.sync_api import sync_playwright
        css = (ROOT / 'css/seo-responsive.css').read_text()
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
            for width in [360, 390, 1440]:
                with self.subTest(width=width):
                    tab = browser.new_page(viewport={'width': width, 'height': 844})
                    tab.set_content('<style>body{margin:0}main{box-sizing:border-box;width:100%;padding:16px}</style><main><picture><img width="800" height="600" src="data:image/svg+xml,%3Csvg xmlns=\"http://www.w3.org/2000/svg\" width=\"1024\" height=\"576\"/%3E"></picture></main>')
                    if width < 800:
                        self.assertGreater(tab.evaluate('document.documentElement.scrollWidth'), width)
                    tab.add_style_tag(content=css)
                    self.assertLessEqual(tab.evaluate('document.documentElement.scrollWidth'), width)
                    tab.close()
            browser.close()


if __name__ == '__main__':
    unittest.main()
