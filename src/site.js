/* Contesta site: first-party measurement (no third-party trackers) and small UI helpers.
   Events go to the Contesta Apps Script backend and land in the "Eventos" sheet.
   Never send names, emails, phone numbers, calendar contents or transcripts here. */
(function () {
  'use strict';
  var API = 'https://script.google.com/macros/s/AKfycbyXR-yNxKBagHakXhU7jxM6dKD9QKz2AFt11QPZmwIUacn4RIWdTG_4vjSbg21EiqA/exec';
  var lang = document.documentElement.lang === 'en' ? 'en' : 'es';
  function store(kind) { try { var s = window[kind]; s.setItem('__t', '1'); s.removeItem('__t'); return s; } catch (e) { return null; } }
  var ls = store('localStorage'), ss = store('sessionStorage');
  function get(s, k) { try { return s ? s.getItem(k) : null; } catch (e) { return null; } }
  function set(s, k, v) { try { if (s) s.setItem(k, v); } catch (e) {} }

  var qs = new URLSearchParams(location.search);
  if (qs.get('interno') === '1') set(ls, 'ct-int', '1');
  if (qs.get('interno') === '0') { try { ls && ls.removeItem('ct-int'); } catch (e) {} }
  var interno = get(ls, 'ct-int') === '1';

  var sid = get(ss, 'ct-sid');
  if (!sid) { sid = Math.random().toString(36).slice(2) + Date.now().toString(36); set(ss, 'ct-sid', sid); }

  // Source classification. Keeps Google organic, other search engines, social/video, referral, email and direct apart.
  function classify() {
    var src = (qs.get('utm_source') || '').toLowerCase(), med = (qs.get('utm_medium') || '').toLowerCase(), camp = qs.get('utm_campaign') || '';
    if (src || med) return { s: src || 'desconocido', m: med || 'desconocido', c: camp };
    var ref = '';
    try { ref = document.referrer ? new URL(document.referrer).hostname.replace(/^www\./, '') : ''; } catch (e) {}
    if (!ref) return { s: 'direct', m: 'none', c: '' };
    if (ref === location.hostname.replace(/^www\./, '')) return null; // internal navigation: keep first touch
    if (/(^|\.)google\./.test(ref)) return { s: 'google', m: 'organic', c: '' };
    if (/(^|\.)(bing\.com|duckduckgo\.com|yahoo\.com|search\.brave\.com|ecosia\.org|yandex\.|baidu\.com)/.test(ref)) return { s: ref, m: 'organic', c: '' };
    if (/(facebook|instagram|tiktok|youtube|youtu\.be|linkedin|twitter|x\.com|t\.co|whatsapp|reddit|threads\.net|nextdoor)/.test(ref)) return { s: ref, m: 'social', c: '' };
    if (/(mail\.|outlook\.|gmail)/.test(ref)) return { s: ref, m: 'email', c: '' };
    return { s: ref, m: 'referral', c: '' };
  }
  var now = classify(), at = null;
  try { at = JSON.parse(get(ls, 'ct-at') || 'null'); } catch (e) {}
  if (!at && now) { at = { s: now.s, m: now.m, c: now.c, lp: location.pathname }; set(ls, 'ct-at', JSON.stringify(at)); }
  var visita = now || at || { s: 'direct', m: 'none', c: '' };

  function send(e, extra) {
    var o = { e: e, p: location.pathname, l: lang, s: visita.s, m: visita.m, c: visita.c, sid: sid, int: interno ? 1 : 0 };
    if (extra) for (var k in extra) o[k] = extra[k];
    var body = JSON.stringify(o);
    try {
      if (navigator.sendBeacon && navigator.sendBeacon(API + '?fn=evento', new Blob([body], { type: 'text/plain;charset=utf-8' }))) return;
    } catch (err) {}
    try { fetch(API + '?fn=evento', { method: 'POST', body: body, keepalive: true, headers: { 'Content-Type': 'text/plain;charset=utf-8' } }); } catch (err) {}
  }
  window.ctEvent = send;
  window.ctAttribution = function () { return at || visita; };
  window.ctInterno = function () { return interno; };

  if (!document.body.hasAttribute('data-noview')) send('page_view');

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('a, button');
    if (!a) return;
    if (a.matches('a[href^="tel:+18137221120"]')) send('phone_demo_clicked');
    var plan = a.getAttribute('data-plan');
    if (plan) send('plan_selected', { pl: plan });
    if (a.hasAttribute('data-lang-switch')) set(ls, 'contesta-lang', a.getAttribute('data-lang-switch'));
  });
  document.querySelectorAll('audio[data-demo], video[data-demo]').forEach(function (m) {
    m.addEventListener('play', function once() { send('demo_started', { st: m.tagName.toLowerCase() }); m.removeEventListener('play', once); });
  });

  var btn = document.querySelector('.menu-btn'), links = document.getElementById('nav-links');
  if (btn && links) btn.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
