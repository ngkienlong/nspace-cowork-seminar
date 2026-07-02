/* toan-hoc · entrance-animations.js
   Clean fade-up entrance on every [data-animate] element, staggered.
   Smooth and professional — no bounce. */
(function () {
  var els = document.querySelectorAll('[data-animate]');
  els.forEach(function (el, i) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(12px)';
    el.style.transition = 'opacity .45s ease, transform .45s ease';
    el.style.transitionDelay = (i * 80) + 'ms';
  });
  requestAnimationFrame(function () {
    requestAnimationFrame(function () {
      els.forEach(function (el) { el.style.opacity = '1'; el.style.transform = 'none'; });
    });
  });
})();
