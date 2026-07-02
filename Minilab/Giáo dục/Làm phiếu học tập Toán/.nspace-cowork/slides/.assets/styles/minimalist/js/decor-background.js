/* minimalist · decor-background.js
   The Minimalist signature is near-absence: this injects a single full-width
   hairline above the baseline of every .slide and nothing else. No fills,
   no color. Intentionally the quietest decoration of the five styles. */
(function () {
  document.querySelectorAll('.slide').forEach(function (slide) {
    var line = document.createElement('div');
    line.style.cssText =
      'position:absolute;left:0;right:0;bottom:96px;height:0;' +
      'border-top:1px solid var(--hairline,#e6e6e6);pointer-events:none;';
    slide.insertBefore(line, slide.firstChild);
  });
})();
