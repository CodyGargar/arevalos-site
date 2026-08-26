// Mobile nav toggle
(function () {
  var btn = document.querySelector('.navtoggle');
  var nav = document.getElementById('nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? 'CLOSE' : 'MENU';
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
      btn.textContent = 'MENU';
    }
  });
})();

// Photo gallery: probe each photo and hide the ones that aren't there yet.
// Hides the whole section if none are present. This lets you add
// shop-1.jpg ... shop-6.jpg one at a time without ever showing a broken
// image on the live site. A separate probe is used instead of the <img>
// load event because lazy-loaded images off-screen never fire one.
(function () {
  var section = document.querySelector('.gallery-section');
  if (!section) return;
  var imgs = Array.prototype.slice.call(section.querySelectorAll('.gallery img'));
  if (!imgs.length) { section.classList.add('is-empty'); return; }
  var pending = imgs.length, found = 0;
  function settle(img, ok) {
    if (ok) { found++; } else { img.classList.add('is-missing'); }
    if (--pending === 0 && found === 0) section.classList.add('is-empty');
  }
  imgs.forEach(function (img) {
    var probe = new Image();
    probe.onload = function () { settle(img, true); };
    probe.onerror = function () { settle(img, false); };
    probe.src = img.getAttribute('src');
  });
})();
