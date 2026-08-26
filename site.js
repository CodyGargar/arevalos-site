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

// ---------------------------------------------------------------------------
// Call + lead tracking.
//
// The shop's conversion is a phone call, not a page view. Every tel: link on
// the site is recorded here, tagged with WHERE it was tapped (sticky bar,
// header, ticket panel, footer...) and WHICH language the page was in — so you
// can see whether the Spanish pages or the English ones are producing calls,
// and which button is doing the work.
//
// SETUP: paste your GA4 Measurement ID between the quotes below. It looks like
// G-XXXXXXXXXX and comes from Google Analytics -> Admin -> Data streams.
// Leave it empty and this whole block does nothing at all: no script loads, no
// network requests, no cookies, no errors. Nothing breaks either way.
//
// Once it's live, import "call_click" and "generate_lead" as conversions in
// Google Ads (Tools -> Conversions -> Import from GA4). Without that step the
// ads spend cannot be tied to calls.
// ---------------------------------------------------------------------------
var ANALYTICS_ID = '';

(function () {
  if (!ANALYTICS_ID) return;

  // Load GA4.
  var g = document.createElement('script');
  g.async = true;
  g.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ANALYTICS_ID);
  document.head.appendChild(g);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', ANALYTICS_ID);

  var lang = document.documentElement.lang || 'en';

  // Name the region of the page a link sits in, so "which button gets tapped"
  // is answerable. Falls back to 'page' for one-off inline links.
  var REGIONS = [
    ['.callbar',   'sticky_call_bar'],
    ['.masthead',  'header'],
    ['.foot',      'footer'],
    ['.ticket',    'ticket_panel'],
    ['.hero',      'hero'],
    ['.btn-row',   'button_row'],
    ['.infolist',  'contact_details'],
    ['.form',      'form']
  ];
  function regionOf(el) {
    for (var i = 0; i < REGIONS.length; i++) {
      if (el.closest && el.closest(REGIONS[i][0])) return REGIONS[i][1];
    }
    return 'page';
  }

  function send(name, params) {
    params.page_language = lang;
    params.page_path = location.pathname;
    gtag('event', name, params);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';

    if (href.indexOf('tel:') === 0) {
      send('call_click', {
        link_location: regionOf(a),
        phone_number: href.slice(4)
      });
    } else if (href.indexOf('mailto:') === 0) {
      send('email_click', { link_location: regionOf(a) });
    } else if (href.indexOf('google.com/maps') > -1) {
      send('directions_click', { link_location: regionOf(a) });
    }
  }, true);

  // Quote / wholesale forms. Fires on submit, before the page hands off to
  // Formspree. generate_lead is GA4's standard name for this.
  Array.prototype.forEach.call(document.querySelectorAll('form.form'), function (form) {
    form.addEventListener('submit', function () {
      var isFleet = !!form.querySelector('#w-note');
      send('generate_lead', { form_name: isFleet ? 'fleet_wholesale' : 'quote_request' });
    });
  });
})();
