/* ══════════════════════════════════════════════════════════════════════════
   assets/pv-accessoires.js — Daewoo Security, 19/09/2026
   Compteurs, total et mise au panier du bloc snippets/pv-accessoires.liquid.

   Deux différences avec le bloc équivalent des pages Élite, qui expliquent
   presque tout le code ci-dessous :

   1. Les pages Vigilia ont un sélecteur de connectivité (Wi-Fi / Wi-Fi+GSM).
      Le prix du pack n'est donc pas figé au rendu : il est relu dans le
      JSON #PVData-… à partir de la variante actuellement sélectionnée, et
      le total est recalculé après chaque clic sur le sélecteur.

   2. Le tableau comparatif Wi-Fi / Wi-Fi+GSM affiche lui aussi des prix,
      avec les mêmes classes .pv-price-amount / .pv-price-compare. Ce sont
      les prix des deux versions, pas le total en cours : ils sont exclus
      des éléments réécrits, sans quoi choisir une version réécrirait le
      prix affiché sur l'autre.

   Le script est chargé en defer : il s'exécute après le script inline de
   la section, donc après que celle-ci a posé ses propres écouteurs.
   ══════════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  var QTE_MAX = 10;

  function formatEuros(cents) {
    return (cents / 100).toLocaleString('fr-FR', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }) + ' €';
  }

  /* Les prix du tableau comparatif décrivent les deux versions de la
     centrale, pas la configuration en cours. */
  function affichagesDuTotal(portee, selecteur) {
    return Array.prototype.filter.call(
      portee.querySelectorAll(selecteur),
      function (el) { return !el.closest('.pv-compare__price'); }
    );
  }

  function demarrer(racine) {
    var portee = racine.closest('.pv') || document;

    var formId = racine.getAttribute('data-pva-form');
    var form = formId ? document.getElementById(formId) : null;
    var erreurEl = form ? form.querySelector('.product-form__error-message') : null;

    /* ---- prix du pack : relu à chaque calcul, car il change avec la
       connectivité choisie ---- */
    var donnees = {};
    var dataEl = portee.querySelector('script[id^="PVData-"]');
    if (dataEl) {
      try { donnees = JSON.parse(dataEl.textContent); } catch (e) { donnees = {}; }
    }
    var champVariante = portee.querySelector('input[id^="PVVariantId-"]');

    function varianteCourante() {
      return (champVariante && donnees[champVariante.value]) || null;
    }
    function prixPack() {
      var v = varianteCourante();
      if (v && typeof v.priceCents === 'number') return v.priceCents;
      return parseInt(racine.getAttribute('data-pva-base'), 10) || 0;
    }
    function packABarre() {
      var v = varianteCourante();
      if (v) return !!v.hasCompare;
      return racine.getAttribute('data-pva-compare') === '1';
    }

    var detailEl = racine.querySelector('[data-pva-detail]');
    var detailInitial = detailEl ? detailEl.textContent : '';

    var choix = {};

    function recalculer() {
      var supplement = 0;
      var nombre = 0;
      Object.keys(choix).forEach(function (id) {
        supplement += choix[id].qte * choix[id].prix;
        nombre += choix[id].qte;
      });

      var base = prixPack();
      var total = base + supplement;

      affichagesDuTotal(portee, '.pv-price-amount').forEach(function (el) {
        el.textContent = formatEuros(total);
      });

      /* Un prix barré à côté d'un total configuré comparerait deux choses
         différentes : il ne reste visible que sur le pack seul. */
      affichagesDuTotal(portee, '.pv-price-compare').forEach(function (el) {
        el.classList.toggle('is-visible', packABarre() && nombre === 0);
      });

      if (detailEl) {
        detailEl.textContent = nombre === 0
          ? detailInitial
          : racine.getAttribute('data-pva-pack') + ' ' + formatEuros(base)
            + ' + ' + nombre + (nombre > 1 ? ' accessoires ' : ' accessoire ')
            + formatEuros(supplement);
      }
    }

    /* ---- compteurs ---- */
    var cartes = Array.prototype.slice.call(racine.querySelectorAll('[data-pva-item]'));

    cartes.forEach(function (carte) {
      var id = carte.getAttribute('data-pva-id');
      var prix = parseInt(carte.getAttribute('data-pva-price'), 10);
      if (!id || isNaN(prix)) return;

      choix[id] = { qte: 0, prix: prix };

      var qteEl = carte.querySelector('[data-pva-qty]');
      var moins = carte.querySelector('[data-pva-minus]');
      var plus = carte.querySelector('[data-pva-plus]');

      function poser(n) {
        var q = Math.max(0, Math.min(QTE_MAX, n));
        choix[id].qte = q;
        if (qteEl) qteEl.textContent = q;
        if (moins) moins.disabled = q === 0;
        if (plus) plus.disabled = q === QTE_MAX;
        carte.classList.toggle('is-picked', q > 0);
        recalculer();
      }

      carte._pvaReset = function () { poser(0); };
      if (moins) moins.addEventListener('click', function () { poser(choix[id].qte - 1); });
      if (plus) plus.addEventListener('click', function () { poser(choix[id].qte + 1); });
    });

    /* ---- resynchronisation après un changement de connectivité ----
       La section réécrit tous les prix avec celui de la variante seule.
       Le setTimeout laisse son écouteur finir avant de réappliquer le
       total accessoires compris. */
    portee.querySelectorAll('[data-pv-connectivity]').forEach(function (el) {
      el.addEventListener('click', function () { setTimeout(recalculer, 0); });
    });

    /* ---- mise au panier ----
       Les accessoires partent d'abord par /cart/add.js, puis le formulaire
       produit de la page est soumis pour le pack lui-même : le tiroir
       panier s'ouvre une seule fois, avec toutes les lignes dedans. Sans
       accessoire sélectionné, rien n'est intercepté et le thème garde son
       parcours normal. */
    if (!form) return;

    var boutons = Array.prototype.slice.call(
      portee.querySelectorAll('button[form="' + formId + '"]')
    );
    var enCours = false;

    function lignesChoisies() {
      var items = [];
      Object.keys(choix).forEach(function (id) {
        if (choix[id].qte > 0) items.push({ id: Number(id), quantity: choix[id].qte });
      });
      return items;
    }

    boutons.forEach(function (btn) {
      btn.addEventListener('click', function (evt) {
        if (enCours) return;
        var items = lignesChoisies();
        if (!items.length) return;

        evt.preventDefault();
        enCours = true;
        var aReactiver = boutons.filter(function (b) { return !b.disabled; });
        aReactiver.forEach(function (b) { b.disabled = true; });

        fetch('/cart/add.js', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ items: items })
        })
          .then(function (reponse) {
            if (!reponse.ok) throw new Error('cart/add');
            return reponse.json();
          })
          .then(function () {
            cartes.forEach(function (carte) {
              if (typeof carte._pvaReset === 'function') carte._pvaReset();
            });
          })
          .catch(function () {
            if (erreurEl) {
              erreurEl.textContent = "Les accessoires n'ont pas pu être ajoutés. Seul le pack a été mis au panier.";
              erreurEl.hidden = false;
            }
          })
          .then(function () {
            aReactiver.forEach(function (b) { b.disabled = false; });
            enCours = false;
            if (typeof form.requestSubmit === 'function') {
              form.requestSubmit();
            } else {
              form.submit();
            }
          });
      });
    });

    recalculer();
  }

  function lancer() {
    document.querySelectorAll('[data-pva-root]').forEach(demarrer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', lancer);
  } else {
    lancer();
  }
})();
