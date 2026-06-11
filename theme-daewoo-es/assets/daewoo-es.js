/* ==========================================================================
   Daewoo Security España — JS vanilla
   ========================================================================== */
(function () {
  'use strict';

  /* ---- 1. Scroll Reveal ---- */
  function initScrollReveal() {
    var els = document.querySelectorAll('[data-ds-reveal]');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('ds-visible'); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('ds-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { observer.observe(el); });
  }

  /* ---- 2. Accordion ---- */
  function initAccordion() {
    var triggers = document.querySelectorAll('.ds-accordion-trigger');
    triggers.forEach(function (trigger) {
      trigger.addEventListener('click', function () {
        var item = trigger.closest('.ds-accordion-item');
        var body = item.querySelector('.ds-accordion-body');
        var isOpen = item.classList.contains('ds-open');

        // Close all in same container
        var container = item.closest('.ds-accordion-dark, .ds-accordion');
        if (container) {
          container.querySelectorAll('.ds-accordion-item.ds-open').forEach(function (openItem) {
            openItem.classList.remove('ds-open');
            openItem.querySelector('.ds-accordion-body').classList.remove('ds-open');
            openItem.querySelector('.ds-accordion-trigger').setAttribute('aria-expanded', 'false');
          });
        }

        if (!isOpen) {
          item.classList.add('ds-open');
          body.classList.add('ds-open');
          trigger.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  /* ---- 3. Gallery Thumbnails ---- */
  function initGallery() {
    var galleries = document.querySelectorAll('[data-ds-gallery]');
    galleries.forEach(function (gallery) {
      var mainImg = gallery.querySelector('[data-ds-gallery-main]');
      var thumbs  = gallery.querySelectorAll('[data-ds-gallery-thumb]');
      if (!mainImg || !thumbs.length) return;
      thumbs.forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          thumbs.forEach(function (t) { t.classList.remove('ds-active'); });
          thumb.classList.add('ds-active');
          var src = thumb.getAttribute('data-src') || thumb.querySelector('img').src;
          mainImg.src = src;
        });
      });
    });
  }

  /* ---- 4. Counter Animation ---- */
  function animateCounter(el) {
    var target  = parseFloat(el.getAttribute('data-ds-counter'));
    var suffix  = el.getAttribute('data-ds-counter-suffix') || '';
    var prefix  = el.getAttribute('data-ds-counter-prefix') || '';
    var duration = 1800;
    var start    = null;
    var isFloat  = target % 1 !== 0;

    function step(timestamp) {
      if (!start) start = timestamp;
      var progress = Math.min((timestamp - start) / duration, 1);
      var eased    = 1 - Math.pow(1 - progress, 3);
      var current  = target * eased;
      el.textContent = prefix + (isFloat ? current.toFixed(1) : Math.floor(current).toLocaleString('es-ES')) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function initCounters() {
    var els = document.querySelectorAll('[data-ds-counter]');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { animateCounter(el); });
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { observer.observe(el); });
  }

  /* ---- 5. Product Tabs ---- */
  function initProductTabs() {
    var tabBtns = document.querySelectorAll('.ds-product__tab-btn');
    tabBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var panel = btn.getAttribute('data-tab');
        var container = btn.closest('[data-ds-tabs]');
        if (!container) return;

        container.querySelectorAll('.ds-product__tab-btn').forEach(function (b) {
          b.classList.remove('ds-active');
          b.setAttribute('aria-selected', 'false');
        });
        container.querySelectorAll('[data-tab-panel]').forEach(function (p) {
          p.hidden = true;
        });

        btn.classList.add('ds-active');
        btn.setAttribute('aria-selected', 'true');
        var target = container.querySelector('[data-tab-panel="' + panel + '"]');
        if (target) target.hidden = false;
      });
    });
  }

  /* ---- 6. Init all ---- */
  function initAll() {
    initScrollReveal();
    initAccordion();
    initGallery();
    initCounters();
    initProductTabs();
  }

  /* ---- 7. Run ---- */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  /* ---- 8. Re-init on Shopify section load (theme editor) ---- */
  document.addEventListener('shopify:section:load', function () {
    initAll();
  });

})();
