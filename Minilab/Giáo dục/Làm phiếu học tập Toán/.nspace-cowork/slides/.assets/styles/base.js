/* base.js — optional shared runtime for previewing HTML slides as a deck.

   Style-agnostic and decoupled from the per-style scripts. Unlike base.css
   (which every slide links), this is meant for a VIEWER document: include it
   once when you open a slide or a combined multi-slide file in a browser.

   What it provides:
     1. window.Slides — { reducedMotion, ready(fn), WIDTH, HEIGHT }, a tiny
        shared surface other scripts may read.
     2. Fit-to-viewport: scales the fixed 1280x720 canvas to fill the window.
     3. Deck navigation: arrow / page / space / home / end keys move between
        slides when there is more than one (or when <body data-deck> is set).

   Render-safe: at a native 1280x720 viewport the fit scale is ~1, so it does
   nothing and never interferes with headless rendering to image / PPTX.

   Note: the fit step uses the non-standard `zoom` property, which the app's
   Chromium-based webview supports and which (unlike `transform: scale`) keeps
   layout and centering correct with no manual size compensation. */
(function () {
  var SW = 1280, SH = 720;
  var reduced = !!(window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches);

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  window.Slides = { reducedMotion: reduced, ready: ready, WIDTH: SW, HEIGHT: SH };

  ready(function () {
    var slides = [].slice.call(document.querySelectorAll('.slide'));
    if (!slides.length) return;

    // 1. Fit the fixed canvas to the window. No-op at native size.
    function fit() {
      var scale = Math.min(window.innerWidth / SW, window.innerHeight / SH);
      document.documentElement.style.zoom = Math.abs(scale - 1) < 0.01 ? '' : String(scale);
    }
    fit();
    window.addEventListener('resize', fit);

    // 2. Keyboard navigation, only in deck mode.
    if (slides.length < 2 && !document.body.hasAttribute('data-deck')) return;
    var i = 0;
    function show(n) {
      i = Math.max(0, Math.min(slides.length - 1, n));
      slides[i].scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); show(i + 1); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(i - 1); }
      else if (e.key === 'Home') { e.preventDefault(); show(0); }
      else if (e.key === 'End') { e.preventDefault(); show(slides.length - 1); }
    });
  });
})();
