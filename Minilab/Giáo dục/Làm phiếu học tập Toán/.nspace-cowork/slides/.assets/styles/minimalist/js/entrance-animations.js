/* minimalist · entrance-animations.js
   Restrained entrance: a soft fade plus an 8px rise on every [data-animate],
   lightly staggered. No bounce, no scale — calm and deliberate.
   Usage: add the `data-animate` attribute to any element. */
(function () {
  var els = document.querySelectorAll('[data-animate]');
  els.forEach(function (el, i) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(8px)';
    el.style.transition = 'opacity .5s ease, transform .5s ease';
    el.style.transitionDelay = (i * 90) + 'ms';
  });
  requestAnimationFrame(function () {
    requestAnimationFrame(function () {
      els.forEach(function (el) { el.style.opacity = '1'; el.style.transform = 'none'; });
    });
  });
})();
