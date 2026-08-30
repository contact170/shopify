(function () {
  function pret(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  pret(function () {
    /* --- chronologie : revelation au defilement --- */
    document.querySelectorAll('.accp-chrono').forEach(function (c) {
      if (!('IntersectionObserver' in window) ||
          window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        c.classList.add('est-actif');
        return;
      }
      new IntersectionObserver(function (entrees, obs) {
        entrees.forEach(function (e) {
          if (e.isIntersecting) { c.classList.add('est-actif'); obs.unobserve(e.target); }
        });
      }, { threshold: 0.4 }).observe(c);
    });

    /* --- galerie --- */
    document.querySelectorAll('[data-accp-galerie]').forEach(function (g) {
      var scene = g.querySelector('[data-accp-scene]');
      if (!scene) return;
      g.querySelectorAll('[data-accp-vignette]').forEach(function (v) {
        v.addEventListener('click', function () {
          scene.src = v.dataset.src;
          scene.srcset = v.dataset.srcset || '';
          scene.alt = v.dataset.alt || '';
          g.querySelectorAll('[data-accp-vignette]').forEach(function (o) { o.removeAttribute('aria-current'); });
          v.setAttribute('aria-current', 'true');
        });
      });
    });

    /* --- quantite --- */
    var zone = document.querySelector('[data-accp-prix-unite]');
    if (!zone) return;
    var prix = parseFloat(zone.dataset.accpPrixUnite) || 0;   // en centimes
    var suffixe = zone.dataset.accpDevise || ' €';
    var max = parseInt(zone.dataset.accpMax || '20', 10);
    var q = 1;

    function formate(centimes) {
      return (centimes / 100).toFixed(2).replace('.', ',') + suffixe;
    }
    function peindre() {
      document.querySelectorAll('[data-accp-valeur]').forEach(function (o) { o.textContent = q; });
      document.querySelectorAll('[data-accp-champ]').forEach(function (i) { i.value = q; });
      document.querySelectorAll('[data-accp-moins]').forEach(function (b) { b.disabled = q <= 1; });
      document.querySelectorAll('[data-accp-plus]').forEach(function (b) { b.disabled = q >= max; });
      var t = q > 1 ? ('Total : ' + q + ' × ' + formate(prix) + ' = ' + formate(q * prix)) : '';
      document.querySelectorAll('[data-accp-total]').forEach(function (p) { p.textContent = t; });
    }
    document.querySelectorAll('[data-accp-qte]').forEach(function (g) {
      var moins = g.querySelector('[data-accp-moins]');
      var plus = g.querySelector('[data-accp-plus]');
      if (moins) moins.addEventListener('click', function () { if (q > 1) { q--; peindre(); } });
      if (plus) plus.addEventListener('click', function () { if (q < max) { q++; peindre(); } });
    });
    peindre();
  });
})();
