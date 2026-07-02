/* toan-hoc · decor-background.js
   Injects a clean blue geometric accent: a subtle gradient bar at the top
   and small dot-grid pattern in the bottom-right corner of every .slide.
   Light and airy — matches the white-blue, tidy aesthetic. */
(function () {
  document.querySelectorAll('.slide').forEach(function (slide) {
    var bar = document.createElement('div');
    bar.style.cssText =
      'position:absolute;top:0;left:0;right:0;height:4px;' +
      'background:linear-gradient(90deg,var(--accent,#2563eb),#60a5fa);' +
      'pointer-events:none;';
    slide.insertBefore(bar, slide.firstChild);

    var dots = document.createElement('div');
    dots.style.cssText =
      'position:absolute;bottom:24px;right:24px;width:64px;height:64px;' +
      'background-image:radial-gradient(circle,var(--hairline,#d4e4f4) 1.5px,transparent 1.5px);' +
      'background-size:12px 12px;pointer-events:none;opacity:.6;';
    slide.insertBefore(dots, slide.firstChild);
  });
})();
