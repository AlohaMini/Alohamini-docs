/* Preserve section links when switching between corresponding pages. */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.am-language-switcher').forEach(link => {
    const update = () => {
      const target = new URL(link.href);
      const anchors = JSON.parse(link.dataset.amAnchors || '{}');
      let fragment = window.location.hash.slice(1);
      try { fragment = decodeURIComponent(fragment); } catch { /* Keep malformed fragments unchanged. */ }
      target.hash = anchors[fragment] || fragment;
      target.search = window.location.search;
      link.href = target.href;
    };
    update();
    window.addEventListener('hashchange', update);
  });
});
