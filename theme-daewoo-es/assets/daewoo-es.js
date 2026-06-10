/* =========================================
   DAEWOO SECURITY ESPAÑA — JS vanilla
   ========================================= */

(function () {
  'use strict';

  /* --- Scroll Reveal --- */
  function initScrollReveal() {
    const targets = document.querySelectorAll('[data-ds-reveal]');
    if (!targets.length) return;
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('ds-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (el) { observer.observe(el); });
  }

  /* --- Accordion FAQ --- */
  function initAccordion() {
    document.querySelectorAll('.ds-accordion-trigger').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        const body = btn.nextElementSibling;
        // Close all siblings
        const parent = btn.closest('.ds-accordion-list') || btn.closest('.ds-faq__list') || btn.parentNode.parentNode;
        parent.querySelectorAll('.ds-accordion-trigger').forEach(function (other) {
          if (other !== btn) {
            other.setAttribute('aria-expanded', 'false');
            const otherBody = other.nextElementSibling;
            if (otherBody) otherBody.style.maxHeight = '0';
          }
        });
        if (!expanded) {
          btn.setAttribute('aria-expanded', 'true');
          if (body) body.style.maxHeight = body.scrollHeight + 'px';
        } else {
          btn.setAttribute('aria-expanded', 'false');
          if (body) body.style.maxHeight = '0';
        }
      });
    });
  }

  /* --- Gallery Thumbnails --- */
  function initGallery() {
    document.querySelectorAll('.ds-gallery').forEach(function (gallery) {
      const main = gallery.querySelector('.ds-gallery__main img');
      const thumbs = gallery.querySelectorAll('.ds-gallery__thumb');
      thumbs.forEach(function (thumb) {
        thumb.addEventListener('click', function () {
          const newSrc = thumb.getAttribute('data-full') || thumb.src;
          if (main) { main.src = newSrc; }
          thumbs.forEach(function (t) { t.classList.remove('ds-gallery__thumb--active'); });
          thumb.classList.add('ds-gallery__thumb--active');
        });
      });
    });
  }

  /* --- Counter Animation --- */
  function animateCounter(el) {
    const target = parseFloat(el.getAttribute('data-ds-counter'));
    const duration = parseInt(el.getAttribute('data-ds-counter-duration') || '1800', 10);
    const suffix = el.getAttribute('data-ds-counter-suffix') || '';
    const prefix = el.getAttribute('data-ds-counter-prefix') || '';
    const isFloat = String(target).includes('.');
    const decimals = isFloat ? String(target).split('.')[1].length : 0;
    const start = performance.now();
    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = target * eased;
      el.textContent = prefix + (isFloat ? current.toFixed(decimals) : Math.floor(current)) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  function initCounters() {
    const counters = document.querySelectorAll('[data-ds-counter]');
    if (!counters.length) return;
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { observer.observe(el); });
  }

  /* --- Product Tabs --- */
  function initProductTabs() {
    document.querySelectorAll('.ds-product__tabs').forEach(function (tabsEl) {
      const btns = tabsEl.querySelectorAll('.ds-product__tab-btn');
      const panels = tabsEl.querySelectorAll('.ds-product__tab-panel');
      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          const target = btn.getAttribute('data-tab');
          btns.forEach(function (b) { b.classList.remove('ds-product__tab-btn--active'); b.setAttribute('aria-selected', 'false'); });
          panels.forEach(function (p) { p.hidden = true; });
          btn.classList.add('ds-product__tab-btn--active');
          btn.setAttribute('aria-selected', 'true');
          const panel = tabsEl.querySelector('[data-tab-panel="' + target + '"]');
          if (panel) panel.hidden = false;
        });
      });
    });
  }

  /* --- Init --- */
  function init() {
    initScrollReveal();
    initAccordion();
    initGallery();
    initCounters();
    initProductTabs();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* --- Re-init on Shopify section load (design mode) --- */
  document.addEventListener('shopify:section:load', function () {
    initScrollReveal();
    initAccordion();
    initGallery();
    initCounters();
    initProductTabs();
  });

})();
