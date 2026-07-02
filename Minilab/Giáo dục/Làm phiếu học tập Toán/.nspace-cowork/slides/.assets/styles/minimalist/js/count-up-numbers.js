/* minimalist · count-up-numbers.js
   Animates every [data-countup] from 0 to its target with a gentle ease-out.
   Optional data-prefix / data-suffix wrap the value (e.g. "%", "$").
   Usage: <span class="stat-number" data-countup="98" data-suffix="%">0%</span> */
(function () {
  function ease(t) { return 1 - Math.pow(1 - t, 2); } // calm ease-out
  document.querySelectorAll('[data-countup]').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-countup')) || 0;
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1200, start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      el.textContent = prefix + Math.round(target * ease(p)) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
})();
