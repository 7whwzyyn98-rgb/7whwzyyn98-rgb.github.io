/* Contesta signup + guided setup. Every state shown here comes from the backend; nothing is simulated. */
(function () {
  'use strict';
  var API = 'https://script.google.com/macros/s/AKfycbyXR-yNxKBagHakXhU7jxM6dKD9QKz2AFt11QPZmwIUacn4RIWdTG_4vjSbg21EiqA/exec';
  var root = document.getElementById('app');
  if (!root) return;
  var L = document.documentElement.lang === 'en' ? 'en' : 'es';
  var PAGE = root.getAttribute('data-page');
  var ACCOUNT_URL = L === 'en' ? '/en/account/' : '/es/cuenta/';

  var T = {
    es: {
      plans: { inicial: ['Inicial', '$197/mes', '150 minutos al mes'], pro: ['Pro', '$297/mes', '400 minutos + transferencias'], maximo: ['Máximo', '$597/mes', '1,000 minutos + varias líneas'] },
      email: 'Correo electrónico', emailHint: 'Aquí le llega el enlace de su cuenta y los resúmenes de llamadas.',
      business: 'Nombre del negocio', plan: 'Plan', create: 'Crear mi cuenta', creating: 'Creando su cuenta…',
      errs: {
        email: 'Escriba un correo válido.', negocio: 'Escriba el nombre del negocio.', plan: 'Elija un plan.', limite: 'Demasiados intentos. Espere una hora o escríbanos a hola@usecontesta.com.',
        red: 'No pudimos conectar. Revise su conexión e intente otra vez. Lo que escribió sigue aquí.', servidor: 'Algo falló de nuestro lado. Intente otra vez en un minuto.',
        nombre: 'Escriba el nombre del negocio.', tipo: 'Elija el tipo de negocio.', ciudad: 'Escriba la ciudad.', visita: 'Elija dónde atiende a sus clientes.',
        direccion: 'Escriba la dirección completa con código postal.', zona: 'Escriba las ciudades o códigos postales donde trabaja.', lista: 'Escriba al menos un servicio.',
        lista_formato: 'Cada línea necesita precio y duración. Ejemplo: Cambio de aceite — $45 — 30 min', agenda: 'Elija si Sofía agenda citas.',
        dias: 'Revise el horario: cada día abierto necesita hora de apertura y de cierre.', dueno: 'Escriba su nombre.', celular: 'Su celular con código de área (10 dígitos).',
        telefono: 'El teléfono del negocio con código de área (10 dígitos).', plan_transfer: 'Las transferencias están en los planes Pro y Máximo.', numero: 'El número para transferir (10 dígitos).',
        correo: 'Escriba el correo de su Google Calendar.'
      },
      existente: 'Ya existe una cuenta con ese correo y ese negocio. Le enviamos un enlace nuevo para entrar; revise su correo (y la carpeta de spam).',
      linkTitle: 'Entre a su cuenta', linkText: 'Escriba el correo con el que se registró y le enviamos un enlace para entrar.', sendLink: 'Enviarme el enlace',
      linkSent: 'Si ese correo tiene una cuenta, el enlace ya va en camino. Revise su bandeja (y spam).', expired: 'Su enlace venció o ya no es válido. Pida uno nuevo aquí.',
      loading: 'Cargando su cuenta…', save: 'Guardar', saving: 'Guardando…', saved: 'Guardado', savedPending: 'Guardado, pero falta información:', updatedAgent: 'Sofía ya usa estos cambios.',
      states: { registrada: 'Configuración en curso', configurando: 'Configuración en curso', lista_espera: 'Lista: esperando activación', esperando_pago: 'Lista: esperando activación', construyendo: 'Construyendo', revision: 'Revisión pendiente', prueba_pendiente: 'Lista para probar', activa: 'Activa', cancelada: 'Cancelada' },
      stateReady: 'Lista para empezar la prueba',
      partB: 'Configure su negocio', partBHint: 'Siete pasos cortos. Cada uno se guarda por separado; puede volver cuando quiera.',
      partC: 'Conecte y verifique', partD: 'Prueba, número y activación',
      steps: { negocio: 'Su negocio', servicios: 'Servicios y citas', horario: 'Horario', saludo: 'Saludo', respuestas: 'Respuestas aprobadas', contacto: 'Contacto', escalamiento: 'Transferencias' },
      done: 'Listo', missing: 'Falta',
      check: { config: 'Datos del negocio completos', cal: 'Google Calendar conectado', pago: 'Prueba de 14 días iniciada (tarjeta registrada)', numero: 'Recepcionista construida', prueba: 'Llamada de prueba aprobada', reserva: 'Cita de prueba en su calendario', desvio: 'Desvío de llamadas activado (lo confirma usted)', activa: 'Activación completa' },
      whenOpen: ' — cuando la activación esté disponible',
      opt: '(opcional)'
    },
    en: {
      plans: { inicial: ['Starter', '$197/mo', '150 minutes a month'], pro: ['Pro', '$297/mo', '400 minutes + transfers'], maximo: ['Max', '$597/mo', '1,000 minutes + multiple lines'] },
      email: 'Email', emailHint: 'Your account link and call summaries go here.',
      business: 'Business name', plan: 'Plan', create: 'Create my account', creating: 'Creating your account…',
      errs: {
        email: 'Enter a valid email.', negocio: 'Enter the business name.', plan: 'Choose a plan.', limite: 'Too many attempts. Wait an hour or email hola@usecontesta.com.',
        red: 'We couldn\'t connect. Check your connection and try again. What you typed is still here.', servidor: 'Something failed on our side. Try again in a minute.',
        nombre: 'Enter the business name.', tipo: 'Choose the business type.', ciudad: 'Enter the city.', visita: 'Choose where you serve customers.',
        direccion: 'Enter the full address with ZIP code.', zona: 'Enter the cities or ZIP codes you serve.', lista: 'Add at least one service.',
        lista_formato: 'Each line needs a price and a length. Example: Oil change — $45 — 30 min', agenda: 'Choose whether Sofía books appointments.',
        dias: 'Check the hours: every open day needs an opening and a closing time.', dueno: 'Enter your name.', celular: 'Your cell with area code (10 digits).',
        telefono: 'The business phone with area code (10 digits).', plan_transfer: 'Transfers are included in Pro and Max.', numero: 'The number to transfer to (10 digits).',
        correo: 'Enter your Google Calendar email.'
      },
      existente: 'An account with that email and business already exists. We sent you a new sign-in link; check your inbox (and spam).',
      linkTitle: 'Sign in to your account', linkText: 'Enter the email you signed up with and we\'ll send you a sign-in link.', sendLink: 'Email me the link',
      linkSent: 'If that email has an account, the link is on its way. Check your inbox (and spam).', expired: 'Your link expired or is no longer valid. Request a new one here.',
      loading: 'Loading your account…', save: 'Save', saving: 'Saving…', saved: 'Saved', savedPending: 'Saved, but something is missing:', updatedAgent: 'Sofía is already using these changes.',
      states: { registrada: 'Setup in progress', configurando: 'Setup in progress', lista_espera: 'Ready—awaiting activation', esperando_pago: 'Ready—awaiting activation', construyendo: 'Building', revision: 'Review pending', prueba_pendiente: 'Ready to test', activa: 'Live', cancelada: 'Cancelled' },
      stateReady: 'Ready to start your trial',
      partB: 'Set up your business', partBHint: 'Seven short steps. Each one saves on its own; come back any time.',
      partC: 'Connect and verify', partD: 'Trial, number and activation',
      steps: { negocio: 'Your business', servicios: 'Services and booking', horario: 'Hours', saludo: 'Greeting', respuestas: 'Approved answers', contacto: 'Contact', escalamiento: 'Transfers' },
      done: 'Done', missing: 'Missing',
      check: { config: 'Business details complete', cal: 'Google Calendar connected', pago: '14-day trial started (card on file)', numero: 'Receptionist built', prueba: 'Test call passed', reserva: 'Test booking in your calendar', desvio: 'Call forwarding on (you confirm it)', activa: 'Activation complete' },
      whenOpen: ' — once activation is available',
      opt: '(optional)'
    }
  }[L];

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === 'text') n.textContent = attrs[k];
      else if (k === 'html') n.innerHTML = attrs[k];
      else if (k.slice(0, 2) === 'on') n.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] !== false && attrs[k] != null) n.setAttribute(k, attrs[k] === true ? '' : attrs[k]);
    }
    (kids || []).forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function pretty(n) { var d = String(n || '').replace(/\D/g, '').slice(-10); return d.length === 10 ? '(' + d.slice(0, 3) + ') ' + d.slice(3, 6) + '-' + d.slice(6) : n; }
  function fecha(iso) { try { return new Date(iso).toLocaleDateString(L === 'en' ? 'en-US' : 'es-US', { dateStyle: 'long', timeZone: 'America/New_York' }); } catch (e) { return iso; } }
  function when(iso) { if (!iso) return ''; try { return new Date(iso).toLocaleString(L === 'en' ? 'en-US' : 'es-US', { dateStyle: 'medium', timeStyle: 'short', timeZone: 'America/New_York' }); } catch (e) { return iso; } }
  function ev(name, extra) { if (window.ctEvent) window.ctEvent(name, extra); }

  function api(fn, body) {
    return fetch(API + '?fn=' + fn, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(body) })
      .then(function (r) { if (!r.ok) throw new Error('http'); return r.json(); })
      .catch(function (e) { if (e && e.message === 'http') return { ok: false, error: 'servidor' }; return { ok: false, error: 'red' }; });
  }
  function tokenStore(v) {
    try { if (v === undefined) return sessionStorage.getItem('ct-t'); if (v === null) sessionStorage.removeItem('ct-t'); else sessionStorage.setItem('ct-t', v); } catch (e) { if (v !== undefined) tokenStore.mem = v; return tokenStore.mem; }
  }
  function status(box, kind, msg) { box.className = 'status ' + kind; box.textContent = msg; box.hidden = !msg; }

  // ---------- signup ----------
  function signup() {
    var params = new URLSearchParams(location.search), pre = params.get('plan');
    var box = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var started = false;
    function start() { if (!started) { started = true; ev('signup_started'); } }
    var planWrap = el('div', { 'class': 'plan-pick', role: 'radiogroup', 'aria-labelledby': 'plan-l' });
    ['inicial', 'pro', 'maximo'].forEach(function (p) {
      var inp = el('input', { type: 'radio', name: 'plan', value: p, checked: p === (pre || 'pro') });
      planWrap.appendChild(el('label', { 'class': 'choice' }, [inp, el('b', { text: T.plans[p][0] + ' · ' + T.plans[p][1] }), el('span', { 'class': 'small muted', text: T.plans[p][2] })]));
    });
    var email = el('input', { type: 'email', id: 'f-email', name: 'email', autocomplete: 'email', required: true, onfocus: start });
    var neg = el('input', { type: 'text', id: 'f-neg', name: 'negocio', autocomplete: 'organization', required: true, maxlength: 120, onfocus: start });
    var hp = el('div', { 'class': 'hp', 'aria-hidden': 'true' }, [el('label', { 'for': 'f-web', text: 'Web' }), el('input', { type: 'text', id: 'f-web', name: 'web', tabindex: '-1', autocomplete: 'off' })]);
    var btn = el('button', { type: 'submit', 'class': 'btn' , text: T.create });
    var fEmail = el('div', { 'class': 'field' }, [el('label', { 'for': 'f-email', text: T.email }), email, el('span', { 'class': 'hint', text: T.emailHint })]);
    var fNeg = el('div', { 'class': 'field' }, [el('label', { 'for': 'f-neg', text: T.business }), neg]);
    var fPlan = el('div', { 'class': 'field' }, [el('span', { 'class': 'legend', id: 'plan-l', text: T.plan }), planWrap]);
    var form = el('form', { 'class': 'form', novalidate: true }, [fPlan, fEmail, fNeg, hp, box, btn]);
    function fieldErr(f, msg) {
      var old = f.querySelector('.field-error'); if (old) old.remove();
      f.classList.toggle('has-error', !!msg);
      if (msg) f.appendChild(el('span', { 'class': 'field-error', text: msg }));
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault(); start();
      [fEmail, fNeg, fPlan].forEach(function (f) { fieldErr(f, ''); });
      var plan = (form.querySelector('input[name=plan]:checked') || {}).value || '';
      var body = { email: email.value.trim(), negocio: neg.value.trim(), plan: plan, idioma: L, web: form.querySelector('#f-web').value, at: window.ctAttribution ? window.ctAttribution() : {}, p: location.pathname, int: window.ctInterno && window.ctInterno() ? 1 : 0 };
      btn.disabled = true; btn.textContent = T.creating; status(box, 'info', '');
      api('registro', body).then(function (r) {
        btn.disabled = false; btn.textContent = T.create;
        if (r.ok && r.t) { tokenStore(r.t); location.href = ACCOUNT_URL + '#t=' + r.t; return; }
        if (r.ok && r.existente) { status(box, 'info', T.existente); return; }
        if (r.error === 'validacion') {
          (r.campos || []).forEach(function (c) { var f = { email: fEmail, negocio: fNeg, plan: fPlan }[c]; if (f) fieldErr(f, T.errs[c]); });
          ev('form_error', { er: 'signup_validacion' });
          var first = form.querySelector('.has-error input'); if (first) first.focus();
          return;
        }
        ev('form_error', { er: 'signup_' + (r.error || 'x') });
        status(box, 'err', T.errs[r.error] || T.errs.servidor);
      });
    });
    root.innerHTML = ''; root.appendChild(form);
  }

  // ---------- account ----------
  var acc = null;
  function requestLink(msg) {
    var box = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var email = el('input', { type: 'email', id: 'l-email', autocomplete: 'email', required: true });
    var btn = el('button', { type: 'submit', 'class': 'btn', text: T.sendLink });
    var form = el('form', { 'class': 'form card', novalidate: true }, [el('h2', { text: T.linkTitle }), msg ? el('div', { 'class': 'status warn', text: msg }) : null, el('p', { 'class': 'muted', text: T.linkText }),
      el('div', { 'class': 'field' }, [el('label', { 'for': 'l-email', text: T.email }), email]), box, btn]);
    form.addEventListener('submit', function (e) {
      e.preventDefault(); btn.disabled = true;
      api('enlace', { email: email.value.trim() }).then(function (r) {
        btn.disabled = false;
        if (r.ok) status(box, 'ok', T.linkSent);
        else status(box, 'err', r.error === 'validacion' ? T.errs.email : (T.errs[r.error] || T.errs.servidor));
      });
    });
    root.innerHTML = ''; root.appendChild(form);
  }

  // Return from Stripe: ?pago=cs_... (verified server-side against Stripe's API) or ?pago=cancelado.
  var notice = null;
  function payMsg(err) {
    var es = L === 'es';
    return ({ pago_incompleto: es ? 'Stripe todavía no muestra el registro de la tarjeta como completo. Si lo terminó, toque "Actualizar estado" en un minuto. No se cobró nada.' : 'Stripe doesn\'t show the card step as complete yet. If you finished it, tap "Refresh status" in a minute. Nothing was charged.',
      activacion_pendiente: es ? 'La activación todavía no está disponible. No se cobró nada.' : 'Activation isn\'t available yet. Nothing was charged.',
      red: T.errs.red })[err] || (es ? 'No pudimos confirmar el pago con Stripe. No se cobró nada que no aparezca en Stripe; escríbanos a hola@usecontesta.com.' : 'We couldn\'t confirm the payment with Stripe. Email hola@usecontesta.com and we\'ll check it.');
  }
  function load() {
    var es = L === 'es', m = location.hash.match(/t=([A-Za-z0-9]+)/), q = new URLSearchParams(location.search), pago = q.get('pago');
    if (m) tokenStore(m[1]);
    if (m || pago) history.replaceState(null, '', location.pathname);
    var t = tokenStore();
    if (pago === 'cancelado') notice = { k: 'info', m: es ? 'No terminó el registro de la tarjeta. No se cobró nada y su configuración sigue guardada.' : 'You didn\'t finish adding your card. Nothing was charged and your setup is still saved.' };
    if (pago && /^cs_(test|live)_[A-Za-z0-9]+$/.test(pago)) {
      root.innerHTML = ''; root.appendChild(el('p', { 'class': 'status info', role: 'status', text: es ? 'Confirmando su tarjeta con Stripe y preparando su número de Contesta. Puede tardar un minuto…' : 'Confirming your card with Stripe and preparing your Contesta number. This can take a minute…' }));
      api('pago', { cs: pago, t: t || '' }).then(function (r) {
        notice = r.ok ? { k: 'ok', m: es ? 'Stripe confirmó su tarjeta: su prueba de 14 días empezó. Le enviamos los detalles por correo.' : 'Stripe confirmed your card: your 14-day trial has started. We emailed you the details.' } : { k: 'warn', m: payMsg(r.error) };
        if (!t) { requestLink(notice.m); return; }
        if (r.cuenta) { acc = r.cuenta; render(); return; }
        load();
      });
      return;
    }
    if (!t) { requestLink(notice ? notice.m : ''); return; }
    root.innerHTML = ''; root.appendChild(el('p', { 'class': 'status info', text: T.loading }));
    api('cuenta', { t: t }).then(function (r) {
      if (r.ok) { acc = r.cuenta; ev('setup_viewed'); render(); return; }
      if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
      root.innerHTML = '';
      var retry = el('button', { 'class': 'btn', type: 'button', text: L === 'en' ? 'Try again' : 'Intentar otra vez', onclick: load });
      root.appendChild(el('div', { 'class': 'stack' }, [el('p', { 'class': 'status err', text: T.errs[r.error] || T.errs.servidor }), retry]));
    });
  }

  // field builders
  function field(id, label, input, opts) {
    opts = opts || {};
    return el('div', { 'class': 'field', 'data-f': opts.key || id }, [el('label', { 'for': 'a-' + id }, [label, opts.optional ? el('span', { 'class': 'opt', text: ' ' + T.opt }) : null]), input, opts.hint ? el('span', { 'class': 'hint', text: opts.hint }) : null]);
  }
  function txt(id, val, attrs) { var a = { type: 'text', id: 'a-' + id, name: id, value: val == null ? '' : val }; for (var k in attrs || {}) a[k] = attrs[k]; return el('input', a); }
  function area(id, val, ph) { var n = el('textarea', { id: 'a-' + id, name: id, placeholder: ph || '' }); n.value = val || ''; return n; }
  function radios(name, opts, val, key) {
    return el('div', { 'class': 'field', 'data-f': key || name }, [el('span', { 'class': 'legend', text: opts.label }), el('div', { 'class': 'choices', role: 'radiogroup' }, opts.items.map(function (it) {
      return el('label', { 'class': 'choice' }, [el('input', { type: 'radio', name: name, value: it[0], checked: val === it[0], disabled: it[2] || false }), el('span', { text: it[1] })]);
    }))]);
  }
  function val(form, name) { var n = form.querySelector('[name="' + name + '"]'); if (!n) return ''; if (n.type === 'radio') { var c = form.querySelector('[name="' + name + '"]:checked'); return c ? c.value : ''; } return n.value; }

  var EX = {
    es: {
      taller: 'Cambio de aceite — $45 — 30 min\nDiagnóstico — $80 — 60 min\nAlineación — desde $90 — 60 min', detailing: 'Lavado completo — $60 — 60 min\nDetailing interior — desde $120 — 2 h',
      limpieza: 'Limpieza estándar (1-2 cuartos) — $120 — 2 h\nLimpieza profunda — desde $220 — 4 h\nEstimado en casa — gratis — 30 min', otro: 'Servicio — $precio — duración',
      preg: { taller: 'Año, marca y modelo del carro', detailing: 'Tipo de vehículo (carro, SUV, camioneta)', limpieza: '¿Cuántos cuartos y baños tiene la casa? ¿Tiene mascotas?' },
      faq: '¿Hacen estimados gratis? — Sí, en el taller, sin cita.\n¿Dónde se estaciona? — En la parte de atrás.', never: 'No prometer fechas de entrega de piezas.'
    },
    en: {
      taller: 'Oil change — $45 — 30 min\nDiagnostics — $80 — 60 min\nAlignment — from $90 — 60 min', detailing: 'Full wash — $60 — 60 min\nInterior detail — from $120 — 2 h',
      limpieza: 'Standard clean (1-2 bedrooms) — $120 — 2 h\nDeep clean — from $220 — 4 h\nIn-home estimate — free — 30 min', otro: 'Service — $price — length',
      preg: { taller: 'Year, make and model of the car', detailing: 'Vehicle type (car, SUV, truck)', limpieza: 'How many bedrooms and bathrooms? Any pets?' },
      faq: 'Free estimates? — Yes, at the shop, no appointment needed.\nWhere do I park? — Around the back.', never: 'Never promise part delivery dates.'
    }
  }[L];

  function stepForm(paso) {
    var c = (acc.config || {})[paso] || {}, kids = [], es = L === 'es';
    if (paso === 'negocio') {
      var tipo = el('select', { id: 'a-tipo', name: 'tipo' }, [['', es ? 'Elija…' : 'Choose…'], ['taller', es ? 'Taller mecánico' : 'Auto repair shop'], ['detailing', 'Detailing'], ['limpieza', es ? 'Limpieza' : 'Cleaning'], ['barberia', es ? 'Barbería' : 'Barbershop'], ['salon', es ? 'Salón de belleza' : 'Beauty salon'], ['otro', es ? 'Otro' : 'Other']].map(function (o) { return el('option', { value: o[0], selected: (c.tipo || '') === o[0] }, [o[1]]); }));
      var otro = field('tipoOtro', es ? '¿Qué tipo de negocio?' : 'What kind of business?', txt('tipoOtro', c.tipoOtro, { maxlength: 60 }), { key: 'tipo' });
      var visita = radios('visita', { label: es ? '¿Dónde atiende a sus clientes?' : 'Where do you serve customers?', items: [['local', es ? 'Vienen a mi local' : 'They come to my location'], ['domicilio', es ? 'Voy a donde el cliente' : 'I go to the customer'], ['ambos', es ? 'Las dos cosas' : 'Both']] }, c.visita);
      var dir = field('direccion', es ? 'Dirección del local' : 'Business address', txt('direccion', c.direccion, { autocomplete: 'street-address', maxlength: 200 }), { hint: es ? 'Calle, ciudad y código postal. Sofía la da cuando le preguntan cómo llegar.' : 'Street, city and ZIP. Sofía gives it when callers ask for directions.' });
      var zona = field('zona', es ? 'Zona de servicio' : 'Service area', txt('zona', c.zona, { maxlength: 200, placeholder: es ? 'Ej.: Tampa, Brandon y Riverview' : 'E.g. Tampa, Brandon and Riverview' }), { hint: es ? 'Si alguien llama desde fuera de esta zona, Sofía toma el mensaje en vez de agendar.' : 'If a caller is outside this area, Sofía takes a message instead of booking.' });
      kids = [field('nombre', es ? 'Nombre del negocio' : 'Business name', txt('nombre', c.nombre || acc.negocio, { maxlength: 120 })), field('tipo', es ? 'Tipo de negocio' : 'Business type', tipo), otro,
        field('ciudad', es ? 'Ciudad' : 'City', txt('ciudad', c.ciudad, { maxlength: 60, placeholder: 'Tampa' }), { hint: es ? 'Por ahora atendemos negocios en Florida (hora del Este).' : 'For now we serve businesses in Florida (Eastern time).' }), visita, dir, zona,
        field('comoLlegar', es ? 'Cómo encontrarlos' : 'How to find you', txt('comoLlegar', c.comoLlegar, { maxlength: 200 }), { optional: true }), field('sitio', es ? 'Sitio web o Instagram' : 'Website or Instagram', txt('sitio', c.sitio, { maxlength: 200 }), { optional: true })];
      var sync = function () {
        var f = tipo.value;
        otro.hidden = f !== 'otro';
        var vis = (visita.querySelector('input:checked') || {}).value;
        dir.hidden = !(vis === 'local' || vis === 'ambos'); zona.hidden = !(vis === 'domicilio' || vis === 'ambos');
      };
      tipo.addEventListener('change', sync); visita.addEventListener('change', sync); setTimeout(sync);
    } else if (paso === 'servicios') {
      var tp = ((acc.config.negocio || {}).tipo) || 'otro';
      kids = [field('lista', es ? 'Servicios: uno por línea, con precio y duración' : 'Services: one per line, with price and length', area('lista', c.lista, EX[tp] || EX.otro), { hint: es ? 'Use "desde $X" si el precio varía. Sofía solo da los precios que están aquí.' : 'Use "from $X" if the price varies. Sofía only quotes prices listed here.' }),
        radios('agenda', { label: es ? '¿Sofía agenda citas en su Google Calendar?' : 'Should Sofía book appointments in your Google Calendar?', items: [['si', es ? 'Sí, que agende' : 'Yes, book them'], ['no', es ? 'No, solo que tome mensajes' : 'No, just take messages']] }, c.agenda),
        field('anticipacion', es ? 'Anticipación mínima (horas)' : 'Minimum notice (hours)', txt('anticipacion', c.anticipacion != null ? c.anticipacion : 2, { type: 'number', min: 0, max: 72, inputmode: 'numeric' }), { hint: es ? 'Ej.: 2 = no agenda nada que empiece en menos de 2 horas.' : 'E.g. 2 = never books anything starting within 2 hours.' }),
        field('buffer', es ? 'Minutos libres entre citas' : 'Minutes between appointments', txt('buffer', c.buffer != null ? c.buffer : 0, { type: 'number', min: 0, max: 120, inputmode: 'numeric' })),
        field('preguntas', es ? 'Preguntas al agendar' : 'Questions to ask when booking', txt('preguntas', c.preguntas, { maxlength: 500, placeholder: (EX.preg || {})[tp] || '' }), { optional: true, hint: es ? 'Las respuestas quedan en la cita del calendario.' : 'Answers are saved in the calendar event.' }),
        radios('sinCita', { label: (es ? '¿Atiende sin cita?' : 'Do you take walk-ins?'), items: [['si', es ? 'Sí' : 'Yes'], ['no', 'No']] }, c.sinCita)];
    } else if (paso === 'horario') {
      var dias = c.dias || {}, names = es ? ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'] : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
      var rows = ['lun', 'mar', 'mie', 'jue', 'vie', 'sab', 'dom'].map(function (k, i) {
        var d = dias[k] || (k === 'dom' ? { cerrado: true } : { abre: '09:00', cierra: k === 'sab' ? '14:00' : '18:00' });
        var cb = el('input', { type: 'checkbox', name: 'c-' + k, checked: !!d.cerrado });
        var a = el('input', { type: 'time', name: 'a-' + k, value: d.abre || '', 'aria-label': names[i] + (es ? ' abre' : ' opens') });
        var z = el('input', { type: 'time', name: 'z-' + k, value: d.cierra || '', 'aria-label': names[i] + (es ? ' cierra' : ' closes') });
        var sync2 = function () { a.disabled = z.disabled = cb.checked; }; cb.addEventListener('change', sync2); sync2();
        return el('div', { 'class': 'day' }, [el('span', { 'class': 'dname', text: names[i] }), el('label', { 'class': 'closed' }, [cb, es ? 'Cerrado' : 'Closed']), a, z]);
      });
      kids = [el('div', { 'class': 'field', 'data-f': 'dias' }, [el('span', { 'class': 'legend', text: es ? 'Horario (hora del Este, Florida)' : 'Hours (Eastern time, Florida)' }), el('div', { 'class': 'days' }, rows)]),
        radios('fuera', { label: es ? 'Cuando llaman fuera de horario' : 'When people call after hours', items: [['mensaje', es ? 'Tomar mensaje' : 'Take a message'], ['agenda', es ? 'Agendar en la próxima hora libre' : 'Book the next open time']] }, c.fuera || 'mensaje'),
        field('feriados', es ? 'Días feriados cerrados' : 'Holidays closed', txt('feriados', c.feriados, { maxlength: 300 }), { optional: true })];
    } else if (paso === 'saludo') {
      kids = [field('asistente', es ? 'Nombre de la asistente' : 'Assistant name', txt('asistente', c.asistente || 'Sofía', { maxlength: 20 })),
        radios('idioma', { label: es ? 'Idioma en que contesta primero' : 'Language she answers in first', items: [['es', es ? 'Español (cambia a inglés si el cliente quiere)' : 'Spanish (switches to English on request)'], ['en', es ? 'Inglés (cambia a español si el cliente quiere)' : 'English (switches to Spanish on request)']] }, c.idioma || 'es'),
        el('div', { 'class': 'field' }, [el('span', { 'class': 'legend', text: es ? 'Así va a contestar' : 'How she will answer' }), el('p', { 'class': 'preview', 'data-preview': '1' })])];
      setTimeout(function () { greetPreview(kids[0].closest('form')); });
    } else if (paso === 'respuestas') {
      kids = [field('faq', es ? 'Preguntas frecuentes y sus respuestas' : 'Frequent questions and answers', area('faq', c.faq, EX.faq), { optional: true, hint: es ? 'Pregunta — respuesta, una por línea. Si algo no está aquí, Sofía no lo inventa: toma el mensaje.' : 'Question — answer, one per line. If something isn\'t here, Sofía doesn\'t make it up: she takes a message.' }),
        field('pagos', es ? 'Formas de pago' : 'Payment methods', txt('pagos', c.pagos, { maxlength: 300, placeholder: es ? 'Efectivo, tarjeta, Zelle' : 'Cash, card, Zelle' }), { optional: true }),
        field('cancelacion', es ? 'Política de cancelación o depósito' : 'Cancellation or deposit policy', txt('cancelacion', c.cancelacion, { maxlength: 500 }), { optional: true }),
        field('nuncaDecir', es ? 'Cosas que Sofía nunca debe decir' : 'Things Sofía must never say', area('nuncaDecir', c.nuncaDecir, EX.never), { optional: true })];
    } else if (paso === 'contacto') {
      kids = [field('dueno', es ? 'Su nombre' : 'Your name', txt('dueno', c.dueno, { autocomplete: 'name', maxlength: 80 })),
        field('celular', es ? 'Su celular' : 'Your cell', txt('celular', c.celular, { type: 'tel', autocomplete: 'tel', inputmode: 'tel' }), { hint: es ? 'Con este número reconocemos su llamada de prueba. Los resúmenes llegan por correo.' : 'We use it to recognize your test call. Summaries arrive by email.' }),
        field('telefono', es ? 'Teléfono del negocio (el que sus clientes ya conocen)' : 'Business phone (the one customers already call)', txt('telefono', c.telefono, { type: 'tel', inputmode: 'tel' })),
        field('devolucion', es ? '¿Cuándo devuelve las llamadas?' : 'When do you return calls?', txt('devolucion', c.devolucion, { maxlength: 120, placeholder: es ? 'El mismo día antes de las 6pm' : 'Same day before 6pm' }), { optional: true })];
    } else if (paso === 'escalamiento') {
      var puede = acc.plan === 'pro' || acc.plan === 'maximo';
      var num = field('numero', es ? 'Número al que transfiere' : 'Number to transfer to', txt('numero', c.numero, { type: 'tel', inputmode: 'tel' }));
      var rad = radios('transferir', { label: es ? '¿Transferir llamadas urgentes?' : 'Transfer urgent calls?', items: [['no', es ? 'No, siempre tomar mensaje' : 'No, always take a message'], ['si', es ? 'Sí, en horario, para urgencias, quejas o si piden hablar con usted' : 'Yes, during business hours, for urgent calls, complaints or callers asking for you', !puede]] }, c.transferir || 'no');
      kids = [rad, puede ? null : el('p', { 'class': 'small muted', text: es ? 'Las transferencias están en los planes Pro y Máximo. Puede cambiar de plan arriba, en el resumen de su cuenta, antes de empezar la prueba.' : 'Transfers are included in Pro and Max. You can change plans above, in your account summary, before starting the trial.' }), num];
      var sync3 = function () { num.hidden = val(rad.closest('form') || rad, 'transferir') !== 'si'; };
      rad.addEventListener('change', sync3); setTimeout(sync3);
    }
    var box = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var btn = el('button', { type: 'submit', 'class': 'btn small', text: T.save });
    var form = el('form', { 'class': 'form', novalidate: true, 'data-paso': paso }, kids.concat([box, btn]));
    form.addEventListener('submit', function (e) { e.preventDefault(); saveStep(form, paso, btn, box); });
    if (paso === 'saludo') form.addEventListener('input', function () { greetPreview(form); });
    return form;
  }

  function greetPreview(form) {
    if (!form) return;
    var p = form.querySelector('[data-preview]'); if (!p) return;
    var asis = val(form, 'asistente') || 'Sofía', biz = ((acc.config.negocio || {}).nombre) || acc.negocio, en = val(form, 'idioma') === 'en';
    p.textContent = en ? 'Thanks for calling ' + biz + '. This is ' + asis + ', the virtual assistant. This call may be recorded. How can I help you? Para español, diga español.'
      : 'Gracias por llamar a ' + biz + '. Le habla ' + asis + ', la asistente virtual. Esta llamada puede ser grabada. ¿En qué le puedo ayudar? For English, just say English.';
  }

  function collect(form, paso) {
    if (paso === 'horario') {
      var d = {};
      ['lun', 'mar', 'mie', 'jue', 'vie', 'sab', 'dom'].forEach(function (k) {
        var c = form.querySelector('[name="c-' + k + '"]').checked;
        d[k] = c ? { cerrado: true } : { abre: form.querySelector('[name="a-' + k + '"]').value, cierra: form.querySelector('[name="z-' + k + '"]').value };
      });
      return { dias: d, fuera: val(form, 'fuera'), feriados: val(form, 'feriados') };
    }
    var o = {};
    form.querySelectorAll('input[name], select[name], textarea[name]').forEach(function (n) { if (n.name) o[n.name] = val(form, n.name); });
    return o;
  }

  function markErrors(form, campos) {
    form.querySelectorAll('.field-error').forEach(function (n) { n.remove(); });
    form.querySelectorAll('.has-error').forEach(function (n) { n.classList.remove('has-error'); });
    (campos || []).forEach(function (c) {
      var f = form.querySelector('[data-f="' + (c === 'lista_formato' ? 'lista' : c === 'plan_transfer' ? 'transferir' : c) + '"]');
      if (f) { f.hidden = false; f.classList.add('has-error'); f.appendChild(el('span', { 'class': 'field-error', text: T.errs[c] || c })); }
    });
  }

  function saveStep(form, paso, btn, box) {
    btn.disabled = true; btn.textContent = T.saving; status(box, 'info', '');
    api('guardar', { t: tokenStore(), paso: paso, datos: collect(form, paso) }).then(function (r) {
      btn.disabled = false; btn.textContent = T.save;
      if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
      if (r.cuenta) acc = r.cuenta;
      markErrors(form, r.campos);
      if (r.ok) { status(box, 'ok', T.saved + ' · ' + when(new Date().toISOString()) + (r.actualizado ? ' · ' + T.updatedAgent : '')); refreshChrome(); return; }
      if (r.guardado) { status(box, 'warn', T.savedPending + ' ' + (r.campos || []).map(function (c) { return T.errs[c] || c; }).join(' ')); ev('form_error', { st: paso, er: 'validacion' }); refreshChrome(); return; }
      ev('form_error', { st: paso, er: r.error || 'x' });
      status(box, 'err', T.errs[r.error] || T.errs.servidor);
    });
  }

  var chrome = {};
  var lastCal = null;

  function planChanger() {
    if (acc.pago || acc.numero) return null;
    var es = L === 'es';
    var st = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var opts = el('div', { 'class': 'plan-pick', role: 'radiogroup', 'aria-label': 'Plan' });
    ['inicial', 'pro', 'maximo'].forEach(function (p) {
      opts.appendChild(el('label', { 'class': 'choice' }, [el('input', { type: 'radio', name: 'cambio-plan', value: p, checked: p === acc.plan }), el('b', { text: T.plans[p][0] + ' · ' + T.plans[p][1] }), el('span', { 'class': 'small muted', text: T.plans[p][2] })]));
    });
    var btn = el('button', { type: 'submit', 'class': 'btn small ghost', text: es ? 'Guardar plan' : 'Save plan' });
    var form = el('form', { 'class': 'form', novalidate: true }, [el('p', { 'class': 'small muted', text: es ? 'Puede cambiarlo hasta que empiece su prueba. Sus pasos guardados no cambian.' : 'You can change it until your trial starts. Your saved steps stay as they are.' }), opts, st, btn]);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var p = (form.querySelector('input[name=cambio-plan]:checked') || {}).value;
      if (!p || p === acc.plan) { status(st, 'info', es ? 'Ese ya es su plan.' : 'That is already your plan.'); return; }
      btn.disabled = true;
      api('guardar', { t: tokenStore(), paso: 'plan', datos: { plan: p } }).then(function (r) {
        btn.disabled = false;
        if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
        if (r.cuenta) acc = r.cuenta;
        if (r.ok) { notice = { k: 'ok', m: (es ? 'Plan cambiado a ' : 'Plan changed to ') + T.plans[p][0] + '.' }; render(); return; }
        status(st, 'err', r.error === 'plan_bloqueado' ? (es ? 'Su prueba ya empezó: para cambiar de plan, escríbanos a hola@usecontesta.com.' : 'Your trial has started: to change plans, email hola@usecontesta.com.') : (T.errs[r.error] || T.errs.servidor));
      });
    });
    return el('details', { 'class': 'acc-step' }, [el('summary', {}, [el('span', { text: es ? 'Cambiar de plan' : 'Change plan' })]), el('div', { 'class': 'body' }, [form])]);
  }

  // Status shown to the owner. Setup states are derived from what the server verified (steps complete, activation open);
  // "Live" only appears once the backend has recorded activation, and trial wording only once Stripe reports a trial.
  function stateLabel() {
    var e = acc.estado, act = acc.activacion || {};
    if (e === 'registrada' || e === 'configurando' || e === 'lista_espera' || e === 'esperando_pago') {
      if (!acc.listo) return { t: T.states.configurando, k: '' };
      return act.disponible ? { t: T.stateReady, k: '' } : { t: T.states.lista_espera, k: '' };
    }
    return { t: T.states[e] || e, k: e === 'activa' ? 'ok' : (e === 'revision' || e === 'cancelada' ? 'warn' : '') };
  }
  function render() {
    root.innerHTML = '';
    var es = L === 'es';
    chrome.badge = el('span', { 'class': 'badge' });
    chrome.check = el('ul', { 'class': 'checklist' });
    var head = el('div', { 'class': 'card stack' }, [
      el('div', { 'class': 'call-head' }, [el('h2', { text: acc.negocio }), chrome.badge]),
      el('p', { 'class': 'muted' }, [(T.plans[acc.plan] || ['', ''])[0] + ' · ' + (T.plans[acc.plan] || ['', ''])[1] + ' · ' + acc.email]),
      planChanger(),
      chrome.check
    ]);
    if (notice) { root.appendChild(el('p', { 'class': 'status ' + notice.k, role: 'status', text: notice.m, style: 'margin-bottom:18px' })); notice = null; }
    var stepsWrap = el('div', { 'class': 'stack' });
    chrome.stepBadges = {};
    ['negocio', 'servicios', 'horario', 'saludo', 'respuestas', 'contacto', 'escalamiento'].forEach(function (p, i) {
      var b = el('span', { 'class': 'badge' }); chrome.stepBadges[p] = b;
      var d = el('details', { 'class': 'acc-step' }, [el('summary', {}, [el('span', { text: (i + 1) + '. ' + T.steps[p] }), b]), el('div', { 'class': 'body' }, [stepForm(p)])]);
      stepsWrap.appendChild(d);
    });
    var firstOpen = ['negocio', 'servicios', 'horario', 'saludo', 'respuestas', 'contacto', 'escalamiento'].filter(function (p) { return !acc.pasos[p]; })[0];
    if (firstOpen) stepsWrap.children[['negocio', 'servicios', 'horario', 'saludo', 'respuestas', 'contacto', 'escalamiento'].indexOf(firstOpen)].open = true;

    chrome.partC = el('div', { 'class': 'stack' });
    chrome.partD = el('div', { 'class': 'stack' });
    root.appendChild(el('div', { 'class': 'stack-lg' }, [head,
      el('section', { 'class': 'tight stack', 'aria-labelledby': 'h-b' }, [el('h2', { id: 'h-b', text: 'A. ' + T.partB }), el('p', { 'class': 'muted', text: T.partBHint }), stepsWrap]),
      el('section', { 'class': 'tight stack', 'aria-labelledby': 'h-c' }, [el('h2', { id: 'h-c', text: 'B. ' + T.partC }), chrome.partC]),
      el('section', { 'class': 'tight stack', 'aria-labelledby': 'h-d' }, [el('h2', { id: 'h-d', text: 'C. ' + T.partD }), chrome.partD]),
      el('p', { 'class': 'muted small', html: es ? '¿Necesita ayuda? Escríbanos a <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>. No hace falta una reunión.' : 'Need help? Email <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>. No meeting needed.' })
    ]));
    refreshChrome();
  }

  function subCard() {
    var es = L === 'es', s = acc.suscripcion || {}, inst = acc.instalacion || {}, plan = acc.planInfo || {};
    var st = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var linea = s.estado === 'trialing' && s.pruebaFin ? { k: 'ok', m: (es ? 'Prueba de 14 días activa. Termina el ' : '14-day trial active. It ends on ') + fecha(s.pruebaFin) + (es ? '. No se cobra nada antes de esa fecha.' : '. Nothing is charged before then.') }
      : s.estado === 'active' ? { k: 'ok', m: es ? 'Suscripción activa.' : 'Subscription active.' }
      : (s.estado === 'past_due' || s.estado === 'unpaid') ? { k: 'warn', m: es ? 'El último cobro no pasó. Actualice su tarjeta en "Administrar pago".' : 'The last charge didn\'t go through. Update your card under "Manage billing".' }
      : s.estado === 'canceled' ? { k: 'warn', m: es ? 'Suscripción cancelada.' : 'Subscription cancelled.' } : { k: 'info', m: s.estado };
    var pend = es ? 'Instalación: $297, pago único, se cobra con su primer pago mensual.' : 'Setup fee: $297 one-time, charged with your first monthly payment.';
    var instTxt = { exenta: es ? 'Instalación: sin costo (uno de los primeros cinco negocios).' : 'Setup fee: waived (one of the first five businesses).', pendiente: pend, agregada: pend,
      cobrada: es ? 'Instalación: pagada.' : 'Setup fee: paid.', anulada: es ? 'Instalación: no se cobra (canceló durante la prueba).' : 'Setup fee: not charged (cancelled during the trial).' }[inst.estado];
    var kids = [el('h3', { text: es ? 'Su plan y pago' : 'Your plan and billing' }),
      el('p', { text: (es ? 'Plan ' + plan.es + ': $' + plan.precio + ' al mes, ' : plan.en + ' plan: $' + plan.precio + '/month, ') + plan.minutos + (es ? ' minutos incluidos.' : ' minutes included.') }),
      el('p', { 'class': 'status ' + linea.k, text: linea.m })];
    if (s.cancelaEn && s.estado !== 'canceled') kids.push(el('p', { 'class': 'status warn', text: (es ? 'Se cancela el ' : 'Cancels on ') + fecha(s.cancelaEn) + (es ? '. No se cobra nada después de esa fecha.' : '. Nothing is charged after that date.') }));
    if (instTxt) kids.push(el('p', { 'class': 'small', text: instTxt }));
    if (s.portal) {
      var pb = el('button', { type: 'button', 'class': 'btn ghost small', text: es ? 'Administrar pago o cancelar' : 'Manage billing or cancel' });
      pb.addEventListener('click', function () {
        pb.disabled = true; status(st, 'info', es ? 'Abriendo Stripe…' : 'Opening Stripe…');
        api('portal', { t: tokenStore() }).then(function (r) {
          if (r.ok && r.url) { location.assign(r.url); return; }
          pb.disabled = false; status(st, 'err', T.errs[r.error] || T.errs.servidor);
        });
      });
      kids.push(st, el('div', { 'class': 'btn-row' }, [pb]));
    } else kids.push(el('p', { 'class': 'small muted', html: es ? 'Para cancelar o cambiar la tarjeta, escriba a <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.' : 'To cancel or change your card, email <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.' }));
    return el('div', { 'class': 'card stack' }, kids);
  }

  function refreshChrome() {
    var es = L === 'es';
    var sl = stateLabel();
    chrome.badge.textContent = sl.t;
    chrome.badge.className = 'badge ' + sl.k;
    Object.keys(chrome.stepBadges).forEach(function (p) { var ok = acc.pasos[p]; chrome.stepBadges[p].textContent = ok ? T.done : T.missing; chrome.stepBadges[p].className = 'badge ' + (ok ? 'ok' : 'warn'); });
    var allSteps = Object.keys(acc.pasos).every(function (p) { return acc.pasos[p]; });
    var items = [['config', allSteps], acc.agenda ? ['cal', !!acc.calendario.verificado] : null, ['pago', acc.pago], ['numero', !!acc.numero], ['prueba', !!acc.prueba], acc.agenda ? ['reserva', !!acc.reserva] : null, ['desvio', !!acc.desvio], ['activa', !!acc.activada]].filter(Boolean);
    chrome.check.innerHTML = '';
    var cerrada = !(acc.activacion || {}).disponible && !acc.pago;
    items.forEach(function (it) {
      var suf = it[1] ? '' : (cerrada && it[0] === 'pago' ? T.whenOpen : (es ? ' — pendiente' : ' — pending'));
      chrome.check.appendChild(el('li', { 'class': it[1] ? 'done' : 'pending' }, [el('span', { 'class': 'dot', 'aria-hidden': 'true', text: it[1] ? '✓' : '' }), el('span', { text: T.check[it[0]] + suf })]));
    });
    renderC(); renderD();
  }

  function summaryOf() {
    var es = L === 'es', c = acc.config || {}, s = c.servicios || {}, h = c.horario || {}, e = c.escalamiento || {}, n = c.negocio || {};
    var lines = [];
    lines.push((es ? 'Zona horaria: ' : 'Time zone: ') + (es ? 'hora del Este (America/New_York)' : 'Eastern time (America/New_York)'));
    if (h.texto) lines.push((es ? 'Horario: ' : 'Hours: ') + h.texto);
    if (s.lista) lines.push((es ? 'Servicios y duraciones:\n' : 'Services and lengths:\n') + s.lista);
    if (s.agenda === 'si') lines.push((es ? 'Agenda: sí. Anticipación mínima ' : 'Booking: yes. Minimum notice ') + (s.anticipacion || 0) + (es ? ' h; ' : ' h; ') + (s.buffer || 0) + (es ? ' min entre citas; una cita a la vez en su calendario.' : ' min between appointments; one appointment at a time on your calendar.'));
    else if (s.agenda === 'no') lines.push(es ? 'Agenda: no. Toma las solicitudes de cita como mensaje.' : 'Booking: no. Appointment requests are taken as messages.');
    lines.push((es ? 'Fuera de horario: ' : 'After hours: ') + (h.fuera === 'agenda' ? (es ? 'agenda en la próxima hora libre' : 'books the next open time') : (es ? 'toma mensaje' : 'takes a message')));
    if (n.visita === 'domicilio' || n.visita === 'ambos') lines.push((es ? 'Va a donde el cliente: pide la dirección del servicio' : 'Goes to the customer: asks for the service address') + (n.zona ? (es ? ' y revisa la zona (' : ' and checks the area (') + n.zona + ')' : '') + '.');
    lines.push((es ? 'Transferencias: ' : 'Transfers: ') + (e.transferir === 'si' ? (es ? 'en horario, urgencias, quejas o si piden por usted → ' : 'during hours, urgent calls, complaints or callers asking for you → ') + pretty(e.numero) : (es ? 'no; siempre toma mensaje' : 'no; always takes a message')));
    return lines.join('\n');
  }

  function renderC() {
    var es = L === 'es', box = chrome.partC; box.innerHTML = '';
    if (acc.agenda) {
      var st = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
      if (lastCal) status(st, lastCal.k, lastCal.m);
      var inp = el('input', { type: 'email', id: 'a-cal', value: acc.calendario.correo || acc.email });
      var btn = el('button', { type: 'submit', 'class': 'btn small', text: es ? 'Verificar conexión' : 'Check connection' });
      var form = el('form', { 'class': 'card form', novalidate: true }, [
        el('h3', { text: es ? 'Google Calendar' : 'Google Calendar' }),
        el('ol', {}, [el('li', { html: es ? 'En una computadora, abra <b>Google Calendar → Configuración</b> y elija su calendario.' : 'On a computer, open <b>Google Calendar → Settings</b> and pick your calendar.' }),
          el('li', { html: es ? 'En <b>Compartir con determinadas personas</b>, agregue <b>hola@usecontesta.com</b> con permiso <b>Hacer cambios en eventos</b>.' : 'Under <b>Share with specific people</b>, add <b>hola@usecontesta.com</b> with <b>Make changes to events</b>.' }),
          el('li', { text: es ? 'Escriba aquí el correo de ese calendario y toque Verificar.' : 'Enter that calendar\'s email here and tap Check.' })]),
        el('p', { 'class': 'small muted', text: es ? 'Con ese permiso, Contesta puede ver los eventos de ese calendario y crear citas. Sofía usa los horarios ocupados para no agendar encima. Puede quitar el permiso cuando quiera.' : 'With that permission, Contesta can see that calendar\'s events and create appointments. Sofía uses busy times to avoid double-booking. You can remove access any time.' }),
        el('div', { 'class': 'field', 'data-f': 'correo' }, [el('label', { 'for': 'a-cal', text: es ? 'Correo del calendario' : 'Calendar email' }), inp]),
        acc.calendario.verificado ? el('p', { 'class': 'status ok', text: (es ? 'Conectado y verificado: ' : 'Connected and verified: ') + when(acc.calendario.verificado) }) : null,
        st, btn]);
      form.addEventListener('submit', function (e) {
        e.preventDefault(); btn.disabled = true; status(st, 'info', es ? 'Probando lectura y escritura en su calendario…' : 'Testing read and write access to your calendar…');
        api('calendario', { t: tokenStore(), correo: inp.value.trim() }).then(function (r) {
          btn.disabled = false;
          if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
          if (r.cuenta) acc = r.cuenta;
          if (r.ok && r.escritura) {
            var tzw = r.zona && r.zona !== 'America/New_York' ? (es ? ' Ojo: su calendario está en ' + r.zona + '; Sofía agenda en hora del Este.' : ' Note: your calendar is set to ' + r.zona + '; Sofía books in Eastern time.') : '';
            lastCal = { k: 'ok', m: (es ? 'Conectado. Podemos leer y crear eventos. Eventos en los próximos 7 días: ' : 'Connected. We can read and create events. Events in the next 7 days: ') + r.ocupados7d + '.' + tzw };
            refreshChrome(); return;
          }
          var msg = { sin_acceso: es ? 'Todavía no vemos ese calendario. Revise que lo compartió con hola@usecontesta.com y que el correo es el correcto. A veces tarda un minuto.' : 'We can\'t see that calendar yet. Check that you shared it with hola@usecontesta.com and that the email is right. It can take a minute.',
            solo_lectura: es ? 'Vemos el calendario, pero sin permiso para crear citas. Cambie el permiso a "Hacer cambios en eventos".' : 'We can see the calendar but can\'t create events. Change the permission to "Make changes to events".',
            validacion: T.errs.correo, limite: T.errs.limite, red: T.errs.red }[r.error] || T.errs.servidor;
          lastCal = { k: r.error === 'red' || r.error === 'servidor' ? 'err' : 'warn', m: msg };
          status(st, lastCal.k, lastCal.m);
        });
      });
      box.appendChild(form);
    }
    box.appendChild(el('div', { 'class': 'card stack' }, [el('h3', { text: es ? 'Lo que Sofía va a usar' : 'What Sofía will use' }), el('p', { 'class': 'preview', text: summaryOf() }),
      el('p', { 'class': 'small muted', text: es ? 'Sale de lo que guardó arriba. Si algo no está bien, corríjalo en su paso y guarde.' : 'This comes from what you saved above. If something is off, fix it in its step and save.' })]));
  }

  function renderD() {
    var es = L === 'es', box = chrome.partD; box.innerHTML = '';
    var st = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    var refresh = el('button', { type: 'button', 'class': 'btn ghost small', text: es ? 'Actualizar estado' : 'Refresh status', onclick: function () {
      refresh.disabled = true;
      api('cuenta', { t: tokenStore() }).then(function (r) { refresh.disabled = false; if (r.ok) { acc = r.cuenta; refreshChrome(); } else if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); } else status(st, 'err', T.errs[r.error] || T.errs.servidor); });
    } });
    var act = acc.activacion || {}, plan = acc.planInfo || {}, inst = acc.instalacion || {};
    // Shown while activation is closed. The email promise only appears when this account is on the notice list.
    var espera = function () {
      return el('p', { 'class': 'status info', text: act.aviso
        ? (es ? 'Le avisaremos por correo a ' + acc.email + ' cuando la activación de la prueba esté disponible. Su prueba de 14 días no empieza mientras espera y no se cobra nada.' : 'We\'ll email ' + acc.email + ' when trial activation is available. Your 14-day trial won\'t begin while you\'re waiting, and nothing is charged.')
        : (es ? 'La activación de la prueba todavía no está disponible. Su prueba de 14 días no empieza mientras espera y no se cobra nada.' : 'Trial activation isn\'t available yet. Your 14-day trial won\'t begin while you\'re waiting, and nothing is charged.') });
    };
    var cuota = function () {
      if (inst.fundadorLibre === true) return es ? 'Instalación de $297: no se le cobra; todavía hay cupo entre los primeros cinco negocios que empiezan su prueba.' : '$297 setup fee: waived for you; there are still spots among the first five businesses to start a trial.';
      return es ? 'Instalación de $297, pago único: se cobra junto con su primer pago mensual, al terminar la prueba. Si cancela durante la prueba, no paga nada. Los primeros cinco negocios que empiezan su prueba no la pagan.' : 'One-time $297 setup fee: charged with your first monthly payment, when the trial ends. Cancel during the trial and you pay nothing. Waived for the first five businesses to start a trial.';
    };
    var reglas = function () {
      return el('ul', { 'class': 'small' }, [
        el('li', { text: es ? 'La prueba de 14 días empieza cuando registra su tarjeta en la página segura de pago de Stripe. No se cobra nada durante la prueba.' : 'The 14-day trial starts when you add your card on Stripe\'s secure payment page. Nothing is charged during the trial.' }),
        el('li', { text: es ? 'Al terminar la prueba empieza la mensualidad de $' + plan.precio + ' (plan ' + plan.es + '), salvo que cancele antes.' : 'When the trial ends, $' + plan.precio + '/month (' + plan.en + ' plan) starts unless you cancel before.' }),
        el('li', { text: cuota() })]);
    };
    if (!acc.numero) {
      var card = el('div', { 'class': 'card stack' });
      if (!acc.listo) {
        card.appendChild(el('h3', { text: es ? 'Cuando termine la configuración' : 'When setup is done' }));
        card.appendChild(el('p', { text: act.disponible ? (es ? 'Aquí empieza su prueba de 14 días y construimos su número de Contesta.' : 'This is where you start your 14-day trial and we build your Contesta number.') : (es ? 'Su cuenta queda lista para activar. Todo lo que guarda arriba se conserva.' : 'Your account will be ready to activate. Everything you save above is kept.') }));
        if (!act.disponible) card.appendChild(espera());
      } else if (acc.revision) {
        card.appendChild(el('h3', { text: T.states.revision }));
        card.appendChild(el('p', { 'class': 'status warn', text: acc.motivoRevision === 'industria' ? (es ? 'Su tipo de negocio necesita una revisión manual antes de activarse. No se cobró nada. Le escribimos a ' + acc.email + '.' : 'Your business type needs a manual review before activation. Nothing was charged. We\'ll email ' + acc.email + '.') : (es ? 'Algo falló al construir su recepcionista. Ya nos llegó el aviso y le escribimos a ' + acc.email + '.' : 'Building your receptionist failed. We were notified and will email ' + acc.email + '.') }));
        card.appendChild(el('div', { 'class': 'btn-row' }, [refresh]));
      } else if (acc.pago) {
        var rb = el('button', { type: 'button', 'class': 'btn', text: es ? 'Construir mi número' : 'Build my number' });
        card.appendChild(el('h3', { text: es ? 'Construyendo su recepcionista' : 'Building your receptionist' }));
        card.appendChild(el('p', { text: es ? 'Su prueba ya empezó. Si su número de Contesta no aparece en un par de minutos, toque Construir.' : 'Your trial has started. If your Contesta number doesn\'t appear within a couple of minutes, tap Build.' }));
        card.appendChild(st); card.appendChild(el('div', { 'class': 'btn-row' }, [rb, refresh]));
        rb.addEventListener('click', function () {
          rb.disabled = true; status(st, 'info', es ? 'Construyendo… puede tardar un minuto.' : 'Building… this can take a minute.');
          api('construir', { t: tokenStore() }).then(function (r) {
            rb.disabled = false;
            if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
            if (r.cuenta) acc = r.cuenta;
            if (r.ok || r.error === 'revision') { refreshChrome(); return; }
            status(st, 'err', T.errs[r.error] || T.errs.servidor);
          });
        });
      } else if (!act.disponible) {
        card.appendChild(el('h3', { text: T.states.lista_espera }));
        card.appendChild(el('p', { text: es ? 'Su configuración está completa y guardada. Cuando la activación esté disponible, solo le falta registrar su tarjeta para empezar la prueba; no tendrá que repetir nada.' : 'Your setup is complete and saved. Once activation is available, all that\'s left is adding your card to start the trial; you won\'t have to repeat anything.' }));
        card.appendChild(espera());
        card.appendChild(el('p', { 'class': 'small muted', text: es ? 'Cuando se active:' : 'When it opens:' }));
        card.appendChild(reglas());
        card.appendChild(el('div', { 'class': 'btn-row' }, [refresh]));
      } else {
        var go = el('button', { type: 'button', 'class': 'btn', text: es ? 'Empezar mi prueba de 14 días' : 'Start my 14-day trial' });
        card.appendChild(el('h3', { text: es ? 'Empiece su prueba de 14 días' : 'Start your 14-day trial' }));
        if (act.pruebaInterna) card.appendChild(el('p', { 'class': 'status warn', text: es ? 'Modo de prueba de Stripe: solo cuentas internas; use una tarjeta de prueba de Stripe.' : 'Stripe test mode: internal accounts only; use a Stripe test card.' }));
        card.appendChild(reglas());
        card.appendChild(st);
        card.appendChild(el('div', { 'class': 'btn-row' }, [go, refresh]));
        card.appendChild(el('p', { 'class': 'small muted', html: es ? 'Lo llevamos a la página de pago de Stripe. Al volver, construimos su número de Contesta. <a href="/es/terminos/">Términos</a> · <a href="/es/privacidad/">Privacidad</a>' : 'We take you to Stripe\'s payment page. When you come back, we build your Contesta number. <a href="/en/terms/">Terms</a> · <a href="/en/privacy/">Privacy</a>' }));
        go.addEventListener('click', function () {
          go.disabled = true; status(st, 'info', es ? 'Abriendo la página segura de pago…' : 'Opening the secure payment page…');
          api('checkout', { t: tokenStore() }).then(function (r) {
            if (r.ok && r.url) { location.assign(r.url); return; }
            go.disabled = false;
            if (r.error === 'sesion' || r.error === 'expirada') { tokenStore(null); requestLink(T.expired); return; }
            if (r.cuenta) acc = r.cuenta;
            var msg = { cupo: es ? 'Llegamos al cupo de números por ahora. No se cobró nada; ya nos avisaron y le escribimos a ' + acc.email + '.' : 'We\'ve reached our number capacity for now. Nothing was charged; we were notified and will email ' + acc.email + '.',
              ya_activa: es ? 'Su prueba ya está activa.' : 'Your trial is already active.', limite: T.errs.limite, red: T.errs.red }[r.error];
            if (r.error === 'revision' || r.error === 'activacion_pendiente' || r.error === 'incompleto' || r.error === 'ya_activa') { if (msg) notice = { k: 'info', m: msg }; render(); return; }
            status(st, 'err', msg || T.errs.servidor);
          });
        });
      }
      if (acc.pago && acc.suscripcion && acc.suscripcion.estado) box.appendChild(subCard());
      box.appendChild(card);
      return;
    }
    if (acc.suscripcion && acc.suscripcion.estado) box.appendChild(subCard());
    // built: test + forwarding
    var num = pretty(acc.numero), d = String(acc.numero).replace(/\D/g, '').slice(-10), cel = ((acc.config.contacto || {}).celular || '').slice(-4);
    box.appendChild(el('div', { 'class': 'card stack' }, [el('h3', { text: es ? '1. Pruebe antes de cambiar su línea' : '1. Test before changing your line' }),
      el('p', { html: (es ? 'Su número de Contesta es <b>' : 'Your Contesta number is <b>') + esc(num) + '</b>. ' + (es ? 'Llámelo desde su celular (el que termina en ' + esc(cel) + '). Sus clientes no notan nada todavía.' : 'Call it from your cell (ending in ' + esc(cel) + '). Your customers notice nothing yet.') }),
      acc.agenda ? el('p', { text: es ? 'En la llamada, pida una cita: así verificamos que agenda en su calendario.' : 'During the call, ask for an appointment so we can verify booking in your calendar.' }) : null,
      el('p', { 'class': acc.prueba ? 'status ok' : 'status info', text: acc.prueba ? (es ? 'Llamada de prueba aprobada: ' : 'Test call passed: ') + when(acc.prueba) : (es ? 'Esperando su llamada de prueba. Después de colgar, el resumen llega a su correo en unos minutos; luego toque Actualizar estado.' : 'Waiting for your test call. After you hang up, the summary reaches your email within a few minutes; then tap Refresh status.') }),
      acc.agenda ? el('p', { 'class': acc.reserva ? 'status ok' : 'status info', text: acc.reserva ? (es ? 'Cita de prueba creada en su calendario: ' : 'Test booking created in your calendar: ') + when(acc.reserva) : (es ? 'Todavía no hay cita de prueba.' : 'No test booking yet.') }) : null,
      el('div', { 'class': 'btn-row' }, [refresh]), st]));
    var carriers = el('div', { 'class': 'table-wrap' }, [el('table', {}, [el('thead', {}, [el('tr', {}, [el('th', { text: es ? 'Compañía' : 'Carrier' }), el('th', { text: es ? 'Activar (cuando no contesta)' : 'Turn on (when you don\'t answer)' }), el('th', { text: es ? 'Quitar' : 'Turn off' })])]),
      el('tbody', {}, [el('tr', {}, [el('td', { text: 'Verizon' }), el('td', { html: '<code>*71' + esc(d) + '</code>' }), el('td', { html: '<code>*73</code>' })]),
        el('tr', {}, [el('td', { text: 'T-Mobile' }), el('td', { html: '<code>**61*1' + esc(d) + '#</code>' + (es ? ' (y si quiere también ocupado: ' : ' (and for busy too: ') + '<code>**67*1' + esc(d) + '#</code>)' }), el('td', { html: '<code>##61#</code> · <code>##67#</code> · <code>##004#</code> ' + (es ? '(todo)' : '(all)') })]),
        el('tr', {}, [el('td', { text: 'AT&T' }), el('td', { html: es ? 'Ajustes del teléfono → Teléfono → Desvío de llamadas, o las <a href="https://www.att.com/support/article/wireless/KM1011513/">instrucciones de AT&amp;T</a>' : 'Phone settings → Phone → Call forwarding, or <a href="https://www.att.com/support/article/wireless/KM1011513/">AT&amp;T\'s instructions</a>' }), el('td', { text: es ? 'El mismo menú' : 'Same menu' })]),
        el('tr', {}, [el('td', { text: es ? 'Otra / línea fija' : 'Other / landline' }), el('td', { text: (es ? 'Pida a su compañía "desvío cuando no contesto" al ' : 'Ask your provider for "forward when no answer" to ') + num }), el('td', { text: es ? 'Pida quitarlo' : 'Ask them to remove it' })])])])]);
    var dv = el('input', { type: 'checkbox', id: 'a-desvio', checked: !!acc.desvio });
    var dst = el('div', { 'class': 'status', role: 'status', 'aria-live': 'polite', hidden: true });
    dv.addEventListener('change', function () {
      dv.disabled = true;
      api('guardar', { t: tokenStore(), paso: 'verificacion', datos: { desvio: dv.checked } }).then(function (r) {
        dv.disabled = false;
        if (r.cuenta) acc = r.cuenta;
        if (r.ok) { status(dst, 'ok', T.saved); refreshChrome(); } else { dv.checked = !dv.checked; status(dst, 'err', T.errs[r.error] || T.errs.servidor); }
      });
    });
    box.appendChild(el('div', { 'class': 'card stack' }, [el('h3', { text: es ? '2. Active el desvío de llamadas' : '2. Turn on call forwarding' }),
      el('p', { text: es ? 'Desde el teléfono del negocio, marque el código y llame. Las llamadas que usted no conteste pasan a Sofía; su número no cambia.' : 'From the business phone, dial the code and press call. Calls you don\'t answer go to Sofía; your number stays the same.' }),
      carriers, el('p', { 'class': 'small muted', html: es ? 'Códigos según <a href="https://www.verizon.com/support/call-forwarding-faqs/">Verizon</a> y <a href="https://www.t-mobile.com/support/plans-features/self-service-short-codes">T-Mobile</a>. Para pausar el servicio, quite el desvío: las llamadas vuelven a su teléfono.' : 'Codes per <a href="https://www.verizon.com/support/call-forwarding-faqs/">Verizon</a> and <a href="https://www.t-mobile.com/support/plans-features/self-service-short-codes">T-Mobile</a>. To pause the service, turn forwarding off: calls go back to your phone.' }),
      el('label', { 'class': 'choice' }, [dv, el('span', { text: es ? 'Ya activé el desvío' : 'I turned forwarding on' })]), dst]));
    box.appendChild(el('div', { 'class': 'card stack' }, [el('h3', { text: es ? '3. Activación final' : '3. Final activation' }),
      el('p', { 'class': acc.activada ? 'status ok' : 'status info', text: acc.activada ? (es ? 'Su recepcionista está activa desde ' : 'Your receptionist has been live since ') + when(acc.activada) : (es ? 'Se activa cuando pasa la llamada de prueba' + (acc.agenda ? ' y la cita de prueba.' : '.') : 'It goes live when the test call' + (acc.agenda ? ' and the test booking pass.' : ' passes.')) }),
      acc.primeraLlamada ? el('p', { 'class': 'status ok', text: (es ? 'Primera llamada de un cliente: ' : 'First customer call: ') + when(acc.primeraLlamada) }) : null]));
  }

  if (PAGE === 'signup') signup(); else { load(); window.addEventListener('hashchange', function () { if (/t=/.test(location.hash)) load(); }); }
})();
