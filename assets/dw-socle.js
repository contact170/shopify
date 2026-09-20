/* ══════════════════════════════════════════════════════════════════════
   SOCLE DAEWOO — comportements partagés des pages gamme
   ──────────────────────────────────────────────────────────────────────
   Version asset du script né dans les sections Vigilia. La différence
   tient en une ligne : le script d'origine interpolait {{ section.id }}
   dans ses sélecteurs, ce qui l'obligeait à vivre dans la section et
   interdisait toute mise en cache. Ici tout passe par des attributs
   data-, si bien que le fichier est statique, servi une fois et réutilisé
   sur toutes les pages de la gamme.

   Chaque page est un conteneur [data-dw-page]. Plusieurs conteneurs
   peuvent cohabiter sur une même page sans se marcher dessus.

   Attributs lus :
     [data-dw-page]              conteneur d'une page gamme
     .pv-reveal                  apparaît au défilement
     [data-dw-sticky]            barre d'achat collante
     [data-dw-sticky-anchor]     élément dont la sortie de l'écran l'affiche
     [data-dw-hero]              conteneur de la photo principale
     [data-dw-thumb]             vignette (data-full, data-full-srcset)
     [data-dw-variant-data]      <script type="application/json"> des variantes
     [data-dw-variant="clé"]     bouton ou carte qui sélectionne une variante
     [data-dw-variant-id]        champ caché envoyé au panier
     [data-dw-swap="champ"]      texte réécrit au changement de variante
     [data-dw-swap-href="champ"] lien réécrit au changement de variante
     [data-dw-swap-img="champ"]  image (ou conteneur d'image) réécrite
     [data-dw-modal="nom"]       <dialog>
     [data-dw-modal-open="nom"]  ouvre ce dialog
     [data-dw-modal-close]       ferme le dialog parent
     [data-dw-alma]              bloc de simulation de paiement en plusieurs fois
     [data-dw-reviews-json]      <script type="application/json"> des avis
     [data-dw-reviews-list]      conteneur où ils sont rendus, à l'ouverture
   ══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  function tousLes(racine, sel) {
    return Array.prototype.slice.call(racine.querySelectorAll(sel));
  }

  function euros(centimes) {
    return (centimes / 100).toLocaleString('fr-FR', {
      minimumFractionDigits: 2, maximumFractionDigits: 2
    }) + ' €';
  }

  function lireJson(el) {
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch (e) { return null; }
  }

  /* ---- apparition au défilement ------------------------------------ */
  function apparitions(racine) {
    var els = tousLes(racine, '.pv-reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      });
    }, { threshold: 0.15 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---- barre d'achat collante -------------------------------------- */
  function barreCollante(racine) {
    var barre = racine.querySelector('[data-dw-sticky]');
    var ancre = racine.querySelector('[data-dw-sticky-anchor]');
    if (!barre || !ancre || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (e) {
        barre.classList.toggle('is-shown', !e.isIntersecting);
      });
    }, { threshold: 0, rootMargin: '-64px 0px 0px 0px' });
    io.observe(ancre);
  }

  /* ---- vignettes de la photo principale ---------------------------- */
  function vignettes(racine) {
    /* Le filtre image_tag ne documente pas le passage d'attributs à
       tirets : la photo est donc repérée par son conteneur, pas par un
       attribut posé sur la balise elle-même. */
    var photo = racine.querySelector('[data-dw-hero] img')
             || racine.querySelector('[data-dw-hero-img]');
    var items = tousLes(racine, '[data-dw-thumb]');
    if (!photo || !items.length) return;
    items.forEach(function (v) {
      v.addEventListener('click', function () {
        var src = v.getAttribute('data-full');
        if (src) photo.src = src;
        photo.srcset = v.getAttribute('data-full-srcset') || '';
        items.forEach(function (autre) { autre.classList.remove('is-active'); });
        v.classList.add('is-active');
      });
    });
  }

  /* ---- sélection de variante ---------------------------------------
     Une même page peut afficher les prix de PLUSIEURS versions côte à
     côte dans un comparatif. Réécrire ces prix-là ferait qu'en
     choisissant une version on écraserait le prix affiché sur l'autre :
     les affichages situés dans .pv-compare__price sont donc exclus. */
  function horsComparatif(el) { return !el.closest('.pv-compare__price'); }

  function variantes(racine) {
    var donnees = lireJson(racine.querySelector('[data-dw-variant-data]'));
    if (!donnees) return null;

    var parCle = {};
    Object.keys(donnees).forEach(function (id) { parCle[donnees[id].key] = id; });

    var boutons = tousLes(racine, '[data-dw-variant]');
    var champId = racine.querySelector('[data-dw-variant-id]');
    var prix     = tousLes(racine, '.pv-price-amount').filter(horsComparatif);
    var barres   = tousLes(racine, '.pv-price-compare').filter(horsComparatif);
    var refs     = tousLes(racine, '.pv-ref');
    var textes   = tousLes(racine, '[data-dw-swap]');
    var liens    = tousLes(racine, '[data-dw-swap-href]');
    var images   = tousLes(racine, '[data-dw-swap-img]');

    function choisir(cle) {
      var id = parCle[cle];
      if (!id) return;
      var d = donnees[id];

      boutons.forEach(function (el) {
        var actif = el.getAttribute('data-dw-variant') === cle;
        el.classList.toggle('is-selected', actif);
        el.setAttribute('aria-pressed', actif ? 'true' : 'false');
      });
      if (champId) champId.value = id;

      prix.forEach(function (el) { el.textContent = d.price; });
      barres.forEach(function (el) {
        el.textContent = d.compare || '';
        el.classList.toggle('is-visible', !!d.hasCompare);
      });
      refs.forEach(function (el) { if (d.sku) el.textContent = d.sku; });

      textes.forEach(function (el) {
        var champ = el.getAttribute('data-dw-swap');
        if (d[champ] != null) el.textContent = d[champ];
      });
      liens.forEach(function (el) {
        var champ = el.getAttribute('data-dw-swap-href');
        if (d[champ]) el.setAttribute('href', d[champ]);
      });
      images.forEach(function (el) {
        var champ = el.getAttribute('data-dw-swap-img');
        if (!d[champ]) return;
        /* Le marqueur est posé sur le conteneur quand l'image vient du
           filtre image_tag, qui ne documente pas les attributs à tirets. */
        var img = el.tagName === 'IMG' ? el : el.querySelector('img');
        if (!img) return;
        img.removeAttribute('srcset');
        img.removeAttribute('sizes');
        img.src = d[champ];
        var alt = d[champ + 'Alt'];
        if (alt != null) img.alt = alt;
      });

      racine.dispatchEvent(new CustomEvent('dw:variante', { detail: d, bubbles: true }));
    }

    boutons.forEach(function (el) {
      el.addEventListener('click', function () {
        choisir(el.getAttribute('data-dw-variant'));
      });
    });

    return {
      centimes: function () {
        var id = champId && champId.value;
        return (id && donnees[id]) ? donnees[id].priceCents : null;
      }
    };
  }

  /* ---- fenêtres modales --------------------------------------------
     De vrais <dialog> : la touche Échap, le clic sur le fond et le
     piégeage du focus sont assurés par le navigateur. La classe
     .is-open est posée une image après showModal() pour que la
     transition CSS se joue réellement. */
  function ouvrir(dlg) {
    if (!dlg || typeof dlg.showModal !== 'function') return;
    dlg.showModal();
    requestAnimationFrame(function () { dlg.classList.add('is-open'); });
  }
  function fermer(dlg) {
    if (!dlg) return;
    dlg.classList.remove('is-open');
    dlg.close();
  }

  function modales(racine) {
    tousLes(racine, '[data-dw-modal]').forEach(function (dlg) {
      tousLes(dlg, '[data-dw-modal-close]').forEach(function (btn) {
        btn.addEventListener('click', function () { fermer(dlg); });
      });
      dlg.addEventListener('click', function (e) {
        if (e.target === dlg) fermer(dlg);
      });
      dlg.addEventListener('close', function () { dlg.classList.remove('is-open'); });
    });
  }

  function trouverModale(racine, nom) {
    return racine.querySelector('[data-dw-modal="' + nom + '"]');
  }

  /* ---- paiement en plusieurs fois -----------------------------------
     3x et 4x sont sans frais. Le 10x ne s'applique qu'à partir de 200 €
     et porte des frais réels de 7,34 % : en dessous de ce seuil il n'est
     pas affiché plutôt que d'être affiché grisé. */
  function alma(racine, varApi, centimesParDefaut) {
    var bloc = racine.querySelector('[data-dw-alma]');
    var dlg = trouverModale(racine, 'alma');
    var ouvreur = racine.querySelector('[data-dw-modal-open="alma"]');
    if (!bloc || !dlg || !ouvreur) return;

    function majMontants() {
      var c = (varApi && varApi.centimes()) || centimesParDefaut;
      if (c == null) return;
      var t  = bloc.querySelector('[data-dw-alma-total]');
      var e3 = bloc.querySelector('[data-dw-alma-3x]');
      var e4 = bloc.querySelector('[data-dw-alma-4x]');
      var w10 = bloc.querySelector('[data-dw-alma-10x-wrap]');
      var e10 = bloc.querySelector('[data-dw-alma-10x]');
      if (t)  t.textContent  = euros(c);
      if (e3) e3.textContent = '3 x ' + euros(Math.round(c / 3));
      if (e4) e4.textContent = '4 x ' + euros(Math.round(c / 4));
      var dixPossible = c >= 20000;
      if (w10) w10.hidden = !dixPossible;
      if (dixPossible && e10) {
        e10.textContent = '10 x ' + euros(Math.round(Math.round(c * 1.0734) / 10));
      }
    }

    ouvreur.addEventListener('click', function () { majMontants(); ouvrir(dlg); });
    racine.addEventListener('dw:variante', majMontants);
  }

  /* ---- liste complète des avis --------------------------------------
     Rendue au premier clic seulement : elle n'a d'intérêt que si un
     visiteur demande à tout lire, et la construire au chargement
     alourdirait la page pour tout le monde. */
  function avis(racine) {
    var dlg = trouverModale(racine, 'avis');
    var ouvreur = racine.querySelector('[data-dw-modal-open="avis"]');
    var liste = dlg ? dlg.querySelector('[data-dw-reviews-list]') : null;
    if (!dlg || !ouvreur) return;
    var rendu = false;

    function rendre() {
      if (rendu || !liste) return;
      rendu = true;
      var items = lireJson(racine.querySelector('[data-dw-reviews-json]')) || [];
      var frag = document.createDocumentFragment();
      items.forEach(function (a) {
        var bloc = document.createElement('div');
        bloc.className = 'pv-all-review';

        var etoiles = document.createElement('div');
        etoiles.className = 'pv-all-review__stars';
        etoiles.setAttribute('aria-hidden', 'true');
        var n = Math.max(0, Math.min(5, a.r || 0));
        etoiles.textContent = '★★★★★'.slice(0, n) + '☆☆☆☆☆'.slice(0, 5 - n);
        bloc.appendChild(etoiles);

        var texte = document.createElement('p');
        texte.className = 'pv-all-review__text';
        texte.textContent = a.t || '';
        bloc.appendChild(texte);

        var meta = document.createElement('p');
        meta.className = 'pv-all-review__meta';
        var nom = document.createElement('strong');
        nom.textContent = a.n || '';
        meta.appendChild(nom);
        var reste = [a.c, a.d].filter(Boolean).join(' · ');
        if (reste) meta.appendChild(document.createTextNode(' · ' + reste));
        bloc.appendChild(meta);

        frag.appendChild(bloc);
      });
      liste.innerHTML = '';
      liste.appendChild(frag);
    }

    ouvreur.addEventListener('click', function () { rendre(); ouvrir(dlg); });
  }

  /* ---- démarrage ---------------------------------------------------- */
  function demarrer(racine) {
    if (racine.dataset.dwPret === '1') return;
    racine.dataset.dwPret = '1';
    apparitions(racine);
    barreCollante(racine);
    vignettes(racine);
    modales(racine);
    var varApi = variantes(racine);
    var parDefaut = parseInt(racine.getAttribute('data-dw-prix-centimes'), 10);
    alma(racine, varApi, isNaN(parDefaut) ? null : parDefaut);
    avis(racine);
  }

  function tout() {
    tousLes(document, '[data-dw-page]').forEach(demarrer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tout);
  } else {
    tout();
  }

  /* L'éditeur de thème recharge une section sans recharger la page. */
  document.addEventListener('shopify:section:load', function (e) {
    tousLes(e.target, '[data-dw-page]').forEach(demarrer);
  });
})();
