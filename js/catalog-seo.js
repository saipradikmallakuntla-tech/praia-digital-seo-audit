/* Keep structured data equal to the visible, filtered catalog. Static HTML is built separately. */
(function () {
  'use strict';
  function boot() {
    var grid = document.getElementById('lista-imoveis');
    var schema = document.getElementById('catalog-itemlist');
    if (!grid || !schema) return;
    function sync() {
      var items = [];
      grid.querySelectorAll('.property-card').forEach(function (card) {
        var link = card.querySelector('a.btn-secondary') || card.querySelector('h3 a');
        if (!link) return;
        var target = new URL(link.getAttribute('href'), location.href);
        if (!target.pathname.endsWith('.html')) return;
        var meta = card.querySelector('meta[itemprop="name"]');
        var heading = card.querySelector('.property-title') || card.querySelector('h3');
        var name = meta ? meta.content : heading ? heading.textContent.replace(/\s+#\d+\s*$/, '').trim() : '';
        items.push({'@type': 'ListItem', position: items.length + 1,
          url: 'https://praia.digital' + target.pathname, name: name});
      });
      schema.textContent = JSON.stringify({'@context': 'https://schema.org', '@type': 'ItemList',
        '@id': 'https://praia.digital/imoveis.html#catalog-itemlist',
        name: 'Imóveis no litoral de SP', numberOfItems: items.length, itemListElement: items});
    }
    sync();
    new MutationObserver(sync).observe(grid, {childList: true, subtree: true});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
