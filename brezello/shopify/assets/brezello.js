/* Brezello : interactions de la fiche produit (choix des variantes, couleurs du parfum, galerie). */
(function () {
  'use strict';

  function lower(value) {
    return String(value == null ? '' : value).trim().toLowerCase();
  }

  function readJSON(root, selector) {
    var el = root.querySelector(selector);
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch (e) { return null; }
  }

  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function initProduct(root) {
    if (!root || root.getAttribute('data-bz-ready') === 'true') return;
    root.setAttribute('data-bz-ready', 'true');

    var variants = readJSON(root, '[data-bz-variants]') || [];
    var parfums = readJSON(root, '[data-bz-parfums]') || [];
    var parfumPos = parseInt(root.getAttribute('data-parfum-pos') || '0', 10);
    var fieldsets = Array.prototype.slice.call(root.querySelectorAll('[data-bz-fieldset]'));
    var idInput = root.querySelector('[data-bz-id]');
    var addButton = root.querySelector('[data-bz-add]');
    var addLabel = root.querySelector('[data-bz-add-label]');
    var planInput = root.querySelector('[data-bz-plan-input]');
    var labels = {
      add: root.getAttribute('data-label-add') || 'Ajouter au panier',
      soldout: root.getAttribute('data-label-soldout') || 'Épuisé',
      unavailable: root.getAttribute('data-label-unavailable') || 'Indisponible',
      pick: root.getAttribute('data-label-pick') || 'Choisir',
      selected: root.getAttribute('data-label-selected') || 'Sélectionné'
    };

    function selectedOptions() {
      return fieldsets.map(function (fieldset) {
        var checked = fieldset.querySelector('input[type="radio"]:checked');
        return checked ? checked.value : null;
      });
    }

    function findVariant(options) {
      for (var i = 0; i < variants.length; i++) {
        var match = true;
        for (var j = 0; j < options.length; j++) {
          if (variants[i].options[j] !== options[j]) { match = false; break; }
        }
        if (match) return variants[i];
      }
      return null;
    }

    function setText(field, value) {
      root.querySelectorAll('[data-bz-field="' + field + '"]').forEach(function (el) {
        el.textContent = value || '';
      });
    }

    function findParfum(name) {
      for (var i = 0; i < parfums.length; i++) {
        if (lower(parfums[i].name) === lower(name)) return parfums[i];
      }
      return null;
    }

    function applyParfum(name) {
      var parfum = findParfum(name);
      var shownName = parfum ? parfum.name : name;
      setText('name', shownName);
      root.querySelectorAll('[data-bz-live]').forEach(function (svg) {
        if (svg.getAttribute('role') === 'img') svg.setAttribute('aria-label', 'Inhaler Brezello ' + shownName);
        var printed = svg.querySelector('[data-bz-label]');
        if (printed) printed.textContent = String(shownName || '').toUpperCase();
      });
      if (!parfum) return;
      ['tint', 'deep', 'body'].forEach(function (key) {
        if (parfum[key]) root.style.setProperty('--bz-' + key, parfum[key]);
      });
      setText('mood', parfum.mood);
      setText('notes', parfum.notes);
      setText('line', parfum.line);
      setText('inci', parfum.inci);
      root.querySelectorAll('[data-bz-mood]').forEach(function (card) {
        var cardName = card.getAttribute('data-bz-mood');
        var isCurrent = lower(cardName) === lower(parfum.name);
        card.classList.toggle('is-current', isCurrent);
        var button = card.querySelector('[data-bz-pick]');
        if (button) {
          button.setAttribute('aria-pressed', isCurrent ? 'true' : 'false');
          button.textContent = isCurrent ? labels.selected : labels.pick + ' ' + cardName;
        }
      });
    }

    function showMedia(mediaId) {
      if (!mediaId) return;
      var target = root.querySelector('[data-media-id="' + mediaId + '"]');
      if (!target) return;
      root.querySelectorAll('[data-media-id]').forEach(function (media) {
        media.hidden = media !== target;
      });
      root.querySelectorAll('[data-bz-thumb]').forEach(function (thumb) {
        if (thumb.getAttribute('data-bz-thumb') === String(mediaId)) thumb.setAttribute('aria-current', 'true');
        else thumb.removeAttribute('aria-current');
      });
    }

    function markAvailability(options) {
      fieldsets.forEach(function (fieldset, index) {
        fieldset.querySelectorAll('input[type="radio"]').forEach(function (input) {
          var test = options.slice();
          test[index] = input.value;
          var variant = findVariant(test);
          var label = fieldset.querySelector('label[for="' + input.id + '"]');
          if (label) label.classList.toggle('is-unavailable', !variant || !variant.available);
        });
      });
    }

    function update(fromUser) {
      var options = selectedOptions();
      var variant = findVariant(options);
      if (parfumPos > 0) applyParfum(options[parfumPos - 1]);
      markAvailability(options);

      if (!variant) {
        if (addButton) addButton.disabled = true;
        if (addLabel) addLabel.textContent = labels.unavailable;
        return;
      }

      if (idInput) idInput.value = variant.id;
      if (addButton) addButton.disabled = !variant.available;
      if (addLabel) addLabel.textContent = variant.available ? labels.add : labels.soldout;
      root.querySelectorAll('[data-bz-price]').forEach(function (el) { el.textContent = variant.price; });
      root.querySelectorAll('[data-bz-compare]').forEach(function (el) {
        el.textContent = variant.compare || '';
        el.hidden = !variant.hasCompare;
      });
      if (variant.media) showMedia(variant.media);

      var designMode = window.Shopify && window.Shopify.designMode;
      if (fromUser && !designMode && window.history && window.history.replaceState) {
        var url = new URL(window.location.href);
        url.searchParams.set('variant', variant.id);
        window.history.replaceState({}, '', url.toString());
      }
      root.dispatchEvent(new CustomEvent('bz:variant-change', { bubbles: true, detail: { variant: variant } }));
    }

    fieldsets.forEach(function (fieldset) {
      fieldset.addEventListener('change', function () { update(true); });
    });

    root.querySelectorAll('[data-bz-thumb]').forEach(function (thumb) {
      thumb.addEventListener('click', function () { showMedia(thumb.getAttribute('data-bz-thumb')); });
    });

    root.querySelectorAll('[data-bz-plan]').forEach(function (radio) {
      radio.addEventListener('change', function () {
        if (!planInput) return;
        planInput.value = radio.value;
        planInput.disabled = radio.value === '';
      });
    });

    root.querySelectorAll('[data-bz-pick]').forEach(function (button) {
      button.addEventListener('click', function () {
        if (parfumPos < 1 || !fieldsets[parfumPos - 1]) return;
        var name = button.closest('[data-bz-mood]').getAttribute('data-bz-mood');
        var radios = fieldsets[parfumPos - 1].querySelectorAll('input[type="radio"]');
        var target = null;
        radios.forEach(function (radio) { if (lower(radio.value) === lower(name)) target = radio; });
        if (!target) return;
        target.checked = true;
        update(true);
        var hero = root.querySelector('.bz-hero');
        if (hero) hero.scrollIntoView({ behavior: prefersReducedMotion() ? 'auto' : 'smooth', block: 'start' });
      });
    });

    update(false);
  }

  function initAll(scope) {
    (scope || document).querySelectorAll('[data-bz-product]').forEach(initProduct);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initAll(); });
  } else {
    initAll();
  }
  document.addEventListener('shopify:section:load', function (event) { initAll(event.target); });
})();
