# -*- coding: utf-8 -*-
"""Page registry and copy for usecontesta.com (Spanish and English).

Facts used here were verified on Oct 21, 2026:
- Demo recording: real call to the test business, scripted AI caller, real Sofía (Retell call c54e546dd1842db770454aea842).
- Owner summary: the email hola@ received at 1:16 AM ET for that call.
- Forwarding codes: Verizon support FAQ and T-Mobile self-service short codes pages (AT&T publishes no codes on its page).
- Offer: $197 / $297 / $597 per month with 150 / 400 / 1,000 minutes; 14-day trial; card required to start it (owner decision,
  Oct 21); $297 setup waived for the first five businesses; no contract.
- Setup fee timing (Oct 21): one-time, billed with the first monthly payment at trial end; never during setup, while waiting
  or during the trial; nothing if cancelled during the trial. "First five" = first five businesses to start a trial.
- Minutes = time Sofía is on calls (Retell start-to-end), summed per calendar month, Eastern time (same as the Minutos sheet).
  Over the limit: she keeps answering, the owner is emailed once that month (backend cadaHora), nothing extra is charged.
"""
import html

E = html.escape

# Stripe checkout waits on the EIN (owner, Oct 21). While False the primary CTA is "Set up your receptionist" with the
# waiting note beside it, and the availability notices show. Flip to True only after the LIVE Stripe flow is verified end
# to end and the backend Script Property ACTIVACION is 'abierta'; then rebuild. That switches every CTA to
# "Start your 14-day trial", removes the notices and adds Stripe to the privacy policy's processor list.
ACTIVATION_LIVE = True


def cta_text(lang):
    if ACTIVATION_LIVE:
        return 'Empiece su prueba de 14 días' if lang == 'es' else 'Start your 14-day trial'
    return 'Configure su recepcionista' if lang == 'es' else 'Set up your receptionist'


def cta_note(lang):
    """The explanation that sits beside the temporary CTA. The email it promises is sent by the backend (notificarActivacion_)."""
    if ACTIVATION_LIVE:
        return ''
    t = ('Cree su cuenta y prepare su recepcionista desde ahora. Le avisaremos por correo cuando la activación de la prueba esté disponible. '
         'Su prueba de 14 días no empieza mientras espera.' if lang == 'es' else
         'Create your account and prepare your receptionist now. We’ll email you when trial activation is available. '
         'Your 14-day trial won’t begin while you’re waiting.')
    return f'<p class="cta-note">{E(t)}</p>'
REC = 'https://dxc03zgurdly9.cloudfront.net/54df0e4fd8e65e8bf9245a439269943b31fe88508016b6ee988afa8f4ab883e2/recording.wav'
TEL = 'tel:+18137221120'
SITE = 'https://usecontesta.com'

ORG = {'@context': 'https://schema.org', '@type': 'Organization', '@id': SITE + '/#org', 'name': 'Contesta', 'url': SITE + '/',
       'logo': SITE + '/assets/logo-512.png', 'email': 'hola@usecontesta.com',
       'address': {'@type': 'PostalAddress', 'addressLocality': 'Tampa', 'addressRegion': 'FL', 'addressCountry': 'US'}}


def service_ld(lang):
    names = {'es': ['Inicial', 'Pro', 'Máximo'], 'en': ['Starter', 'Pro', 'Max']}[lang]
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': 'Contesta',
            'serviceType': 'Recepcionista virtual con IA' if lang == 'es' else 'AI virtual receptionist',
            'provider': {'@id': SITE + '/#org'}, 'areaServed': {'@type': 'State', 'name': 'Florida'}, 'availableLanguage': ['es', 'en'],
            'offers': [{'@type': 'Offer', 'name': n, 'price': str(p), 'priceCurrency': 'USD',
                        'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': str(p), 'priceCurrency': 'USD', 'unitText': 'MONTH'}}
                       for n, p in zip(names, [197, 297, 597])]}


def P(es_path, en_path, es, en, **kw):
    a = dict(es); a['path'] = es_path
    b = dict(en); b['path'] = en_path
    for k, v in kw.items():
        a[k] = v; b[k] = v
    return {'es': a, 'en': b}


PAGES = {
    'home': P('/es/', '/en/',
              {'title': 'Contesta · Recepcionista con IA en español e inglés para negocios en Florida',
               'desc': 'Sofía contesta las llamadas de su negocio las 24 horas, agenda citas en su Google Calendar y le envía un resumen por correo. Desde $197 al mes. Escuche una llamada real.',
               'crumb': 'Inicio', 'ld': [ORG, service_ld('es')]},
              {'title': 'Contesta · AI receptionist in English and Spanish for Florida businesses',
               'desc': 'Sofía answers your business calls 24/7, books appointments in your Google Calendar and emails you a summary. From $197 a month. Hear a real call.',
               'crumb': 'Home', 'ld': [ORG, service_ld('en')]}),
    'pricing': P('/es/precios/', '/en/pricing/',
                 {'title': 'Precios de Contesta: planes desde $197 al mes', 'desc': 'Planes de $197, $297 y $597 al mes con 150, 400 y 1,000 minutos. Prueba de 14 días sin cobro y sin contrato. Qué pasa si se pasa de minutos y cuándo se cobra la instalación.', 'crumb': 'Precios', 'ld': [service_ld('es')]},
                 {'title': 'Contesta pricing: plans from $197 a month', 'desc': 'Plans at $197, $297 and $597 a month with 150, 400 and 1,000 minutes. 14-day trial with no charge and no contract. What happens if you go over and when setup is billed.', 'crumb': 'Pricing', 'ld': [service_ld('en')]}),
    'how': P('/es/como-funciona/', '/en/how-it-works/',
             {'title': 'Cómo funciona · Contesta', 'desc': 'De la cuenta a la primera llamada: qué le pedimos, cómo conecta Google Calendar, cómo probar antes de tocar su línea y cómo activar o quitar el desvío.', 'crumb': 'Cómo funciona'},
             {'title': 'How it works · Contesta', 'desc': 'From account to first call: what we ask for, how Google Calendar connects, how to test before touching your line, and how to turn forwarding on or off.', 'crumb': 'How it works'}),
    'demo': P('/es/demo/', '/en/demo/',
              {'title': 'Escuche a Sofía: llamada real con transcripción · Contesta', 'desc': 'Una llamada real a nuestro negocio de prueba: Sofía revisa el calendario, agenda la cita y el dueño recibe el resumen por correo. Audio y transcripción completa.', 'crumb': 'Demo'},
              {'title': 'Hear Sofía: a real call with transcript · Contesta', 'desc': 'A real call to our test business: Sofía checks the calendar, books the appointment and the owner gets an email summary. Audio and full transcript.', 'crumb': 'Demo'}),
    'calendar': P('/es/google-calendar/', '/en/google-calendar/',
                  {'title': 'Citas en Google Calendar con Sofía · Contesta', 'desc': 'Cómo Sofía revisa sus horas ocupadas, respeta horario, anticipación y tiempo entre citas, y crea el evento en su Google Calendar. Permisos y límites.', 'crumb': 'Google Calendar'},
                  {'title': 'Google Calendar booking with Sofía · Contesta', 'desc': 'How Sofía checks your busy times, respects hours, notice and buffers, and creates the event in your Google Calendar. Permissions and limits.', 'crumb': 'Google Calendar'}),
    'auto': P('/es/talleres/', '/en/auto-repair/',
              {'title': 'Recepcionista para talleres mecánicos y detailing · Contesta', 'desc': 'Sofía contesta mientras usted trabaja en el carro: agenda servicios en Google Calendar, anota año, marca y modelo, y le manda el resumen. En español e inglés.', 'crumb': 'Talleres y detailing'},
              {'title': 'Receptionist for auto repair and detailing shops · Contesta', 'desc': 'Sofía answers while you work on the car: books services in Google Calendar, notes year, make and model, and emails you the summary. In English and Spanish.', 'crumb': 'Auto repair and detailing'}),
    'cleaning': P('/es/limpieza/', '/en/cleaning/',
                  {'title': 'Recepcionista para servicios de limpieza · Contesta', 'desc': 'Sofía pide la dirección, revisa que esté en su zona y agenda limpiezas o estimados en su Google Calendar. En español e inglés, las 24 horas.', 'crumb': 'Limpieza'},
                  {'title': 'Receptionist for cleaning services · Contesta', 'desc': 'Sofía asks for the address, checks it is in your area and books cleanings or estimates in your Google Calendar. In English and Spanish, 24/7.', 'crumb': 'Cleaning'}),
    'about': P('/es/nosotros/', '/en/about/',
               {'title': 'Nosotros y contacto · Contesta', 'desc': 'Contesta es una empresa de Tampa que hace una recepcionista con IA en español primero para negocios locales. Cómo trabajamos y cómo escribirnos.', 'crumb': 'Nosotros'},
               {'title': 'About and contact · Contesta', 'desc': 'Contesta is a Tampa company building a Spanish-first AI receptionist for local businesses. How we work and how to reach us.', 'crumb': 'About'}),
    'guides': P('/es/guias/', '/en/guides/',
                {'title': 'Guías · Contesta', 'desc': 'Guías prácticas: cómo desviar las llamadas de su negocio, qué puede y qué no puede hacer una recepcionista con IA bilingüe, y cómo se compara con el buzón de voz o un servicio de contestadora.', 'crumb': 'Guías'},
                {'title': 'Guides · Contesta', 'desc': 'Practical guides: how to forward your business calls, what a bilingual AI receptionist can and can\'t do, and how it compares with voicemail or an answering service.', 'crumb': 'Guides'}),
    'g_forward': P('/es/guias/desvio-de-llamadas/', '/en/guides/call-forwarding/',
                   {'title': 'Cómo desviar las llamadas de su negocio a una recepcionista · Contesta', 'desc': 'Códigos oficiales de Verizon y T-Mobile para desviar solo las llamadas que no contesta, cómo hacerlo en AT&T y líneas fijas, cómo probar y cómo quitarlo.', 'crumb': 'Desvío de llamadas', 'parent': 'guides'},
                   {'title': 'How to forward your business calls to a receptionist · Contesta', 'desc': 'Official Verizon and T-Mobile codes to forward only the calls you don\'t answer, how to do it on AT&T and landlines, how to test and how to turn it off.', 'crumb': 'Call forwarding', 'parent': 'guides'}),
    'g_can': P('/es/guias/que-puede-hacer/', '/en/guides/what-it-can-do/',
               {'title': 'Qué puede y qué no puede hacer una recepcionista con IA bilingüe · Contesta', 'desc': 'Lo que Sofía hace bien (contestar en el idioma del cliente, agendar, tomar mensajes) y lo que no hace todavía, con ejemplos de una llamada real.', 'crumb': 'Qué puede hacer', 'parent': 'guides'},
               {'title': 'What a bilingual AI receptionist can and can\'t do · Contesta', 'desc': 'What Sofía does well (answering in the caller\'s language, booking, taking messages) and what she doesn\'t do yet, with examples from a real call.', 'crumb': 'What it can do', 'parent': 'guides'}),
    'g_compare': P('/es/guias/ia-buzon-o-servicio/', '/en/guides/ai-vs-voicemail-vs-answering-service/',
                   {'title': 'Recepcionista con IA, buzón de voz o servicio de contestadora · Contesta', 'desc': 'Una comparación honesta: qué resuelve cada opción, qué cuesta Contesta, y cuándo conviene más un buzón o una persona.', 'crumb': 'IA, buzón o servicio', 'parent': 'guides'},
                   {'title': 'AI receptionist vs voicemail vs answering service · Contesta', 'desc': 'An honest comparison: what each option solves, what Contesta costs, and when voicemail or a person is the better fit.', 'crumb': 'AI vs voicemail vs service', 'parent': 'guides'}),
    'privacy': P('/es/privacidad/', '/en/privacy/',
                 {'title': 'Política de privacidad · Contesta', 'desc': 'Qué datos recoge Contesta, para qué los usa, con quién los procesa y cuánto tiempo los guarda.', 'crumb': 'Privacidad'},
                 {'title': 'Privacy policy · Contesta', 'desc': 'What data Contesta collects, how it is used, who processes it and how long it is kept.', 'crumb': 'Privacy'}),
    'terms': P('/es/terminos/', '/en/terms/',
               {'title': 'Términos del servicio · Contesta', 'desc': 'Planes, prueba de 14 días, minutos, cancelación y responsabilidades del servicio de recepcionista Contesta.', 'crumb': 'Términos'},
               {'title': 'Terms of service · Contesta', 'desc': 'Plans, 14-day trial, minutes, cancellation and responsibilities for the Contesta receptionist service.', 'crumb': 'Terms'}),
    'signup': P('/es/registro/', '/en/signup/',
                {'title': 'Cree su cuenta · Contesta', 'desc': 'Elija su plan y cree su cuenta de Contesta.', 'crumb': 'Registro'},
                {'title': 'Create your account · Contesta', 'desc': 'Choose your plan and create your Contesta account.', 'crumb': 'Sign up'}, noindex=True, app=True),
    'account': P('/es/cuenta/', '/en/account/',
                 {'title': 'Su cuenta · Contesta', 'desc': 'Configure y active su recepcionista.', 'crumb': 'Cuenta'},
                 {'title': 'Your account · Contesta', 'desc': 'Set up and activate your receptionist.', 'crumb': 'Account'}, noindex=True, app=True),
}

NAV = {
    'es': {'links': [('how', 'Cómo funciona'), ('pricing', 'Precios'), ('demo', 'Demo'), ('guides', 'Guías')], 'cta': cta_text('es'), 'menu': 'Menú',
           'aria': 'Principal', 'skip': 'Saltar al contenido', 'switch': 'English version'},
    'en': {'links': [('how', 'How it works'), ('pricing', 'Pricing'), ('demo', 'Demo'), ('guides', 'Guides')], 'cta': cta_text('en'), 'menu': 'Menu',
           'aria': 'Main', 'skip': 'Skip to content', 'switch': 'Versión en español'},
}

FOOT = {
    'es': {'tag': 'Usted trabaja. Contesta responde.', 'demo': 'Demo en vivo:', 'legal': 'Hecho en Tampa para negocios en Florida.', 'switch': 'English',
           'cols': [('Producto', [('how', 'Cómo funciona'), ('pricing', 'Precios'), ('demo', 'Escuche a Sofía'), ('calendar', 'Google Calendar')]),
                    ('Para quién', [('auto', 'Talleres y detailing'), ('cleaning', 'Limpieza')]),
                    ('Guías y cuenta', [('g_forward', 'Desvío de llamadas'), ('g_can', 'Qué puede hacer'), ('g_compare', 'IA, buzón o servicio'), ('about', 'Nosotros y contacto'), ('account', 'Entrar a mi cuenta')])]},
    'en': {'tag': 'You work. Contesta answers.', 'demo': 'Live demo:', 'legal': 'Made in Tampa for Florida businesses.', 'switch': 'Español',
           'cols': [('Product', [('how', 'How it works'), ('pricing', 'Pricing'), ('demo', 'Hear Sofía'), ('calendar', 'Google Calendar')]),
                    ('Who it\'s for', [('auto', 'Auto repair and detailing'), ('cleaning', 'Cleaning')]),
                    ('Guides and account', [('g_forward', 'Call forwarding'), ('g_can', 'What it can do'), ('g_compare', 'AI vs voicemail vs service'), ('about', 'About and contact'), ('account', 'Sign in')])]},
}


def u(key, lang):
    return PAGES[key][lang]['path']


# ---------- shared blocks ----------
CALL = {
    'es': [('s', 'Gracias por llamar a Barbería Prueba Contesta. Le habla Sofía, la asistente virtual. Esta llamada puede ser grabada. ¿En qué le puedo ayudar? For English, just say English.'),
           ('c', 'Hola, buenas. Quisiera un corte de caballero para mañana en la tarde.'),
           ('s', 'Permítame revisar la disponibilidad para mañana. Para el jueves 22, tengo a las tres o a las cuatro de la tarde. ¿Cuál prefiere?'),
           ('c', 'A las cuatro de la tarde, por favor.'),
           ('s', 'Perfecto. ¿Me da su nombre, por favor?'),
           ('c', 'Carlos Méndez.'),
           ('s', 'Gracias, Carlos Méndez. ¿Le llamamos a este mismo número que termina en uno, uno, dos, cero?'),
           ('c', 'Sí, por favor.'),
           ('s', 'Perfecto, estoy confirmando su cita para el jueves a las cuatro de la tarde. Su cita queda confirmada para el jueves 22 de octubre, a las cuatro de la tarde, para corte de caballero.'),
           ('c', 'Perfecto, muchas gracias. Hasta luego.')],
    'en': [('s', 'Thank you for calling Barbería Prueba Contesta. This is Sofía, the virtual assistant. This call may be recorded. How can I help you? For English, just say English.'),
           ('c', 'Hi there. I\'d like a men\'s haircut tomorrow afternoon.'),
           ('s', 'Let me check availability for tomorrow. For Thursday the 22nd, I have three or four in the afternoon. Which do you prefer?'),
           ('c', 'Four in the afternoon, please.'),
           ('s', 'Perfect. May I have your name, please?'),
           ('c', 'Carlos Méndez.'),
           ('s', 'Thank you, Carlos Méndez. Shall we call you back at this same number ending in one, one, two, zero?'),
           ('c', 'Yes, please.'),
           ('s', 'Perfect, I\'m confirming your appointment for Thursday at four in the afternoon. Your appointment is confirmed for Thursday, October 22nd, at four in the afternoon, for a men\'s haircut.'),
           ('c', 'Perfect, thank you very much. Goodbye.')],
}


def call_card(lang, short=True):
    es = lang == 'es'
    lines = CALL[lang] if not short else [CALL[lang][i] for i in (1, 2, 3, 8)]
    who = {'s': 'Sofía', 'c': 'Cliente (simulado)' if es else 'Caller (simulated)'}
    bub = ''.join(f'<div class="bubble {"sofia" if w == "s" else "caller"}"><small>{who[w]}</small>{E(t)}</div>' for w, t in lines)
    return f'''<div class="card call">
<div class="call-head"><span class="label-chip lime">{"Llamada real · 21 oct 2026" if es else "Real call · Oct 21, 2026"}</span><span class="label-chip">{"Cliente simulado por IA" if es else "AI-simulated caller"}</span></div>
{'' if es else '<p class="small muted">Recorded in Spanish. English translation below.</p>'}
<div class="bubbles">{bub}</div>
<div class="summary"><span class="eyebrow">{"Lo que recibió el dueño por correo" if es else "What the owner got by email"}</span>
<b>{"Carlos Méndez agendó un corte de caballero para el jueves 22 de octubre a las 4:00 p. m." if es else "Carlos Méndez booked a men's haircut for Thursday, October 22 at 4:00 p.m."}</b>
<span class="small muted">{"Y la cita quedó en el Google Calendar del negocio." if es else "And the appointment landed in the business's Google Calendar."}</span></div>
</div>'''


def audio(lang):
    es = lang == 'es'
    return f'''<figure class="stack" style="margin:0">
<audio controls preload="none" data-demo src="{REC}"></audio>
<figcaption class="small muted">{"Llamada completa, 53 segundos, en español. Grabada el 21 de octubre de 2026 en nuestro negocio de prueba." if es else "Full call, 53 seconds, in Spanish. Recorded October 21, 2026 at our test business."}</figcaption>
</figure>'''


def plans(lang, cta=True):
    es = lang == 'es'
    data = [('inicial', 'Inicial' if es else 'Starter', 197, '150', '75',
             'Para negocios de una o dos personas que pierden algunas llamadas al día.' if es else 'For one- or two-person businesses that miss a few calls a day.',
             ['Español e inglés' if es else 'Spanish and English', 'Citas en Google Calendar' if es else 'Google Calendar booking',
              'Resumen de cada llamada por correo' if es else 'Emailed summary of every call'], None),
            ('pro', 'Pro', 297, '400', '200',
             'Para negocios con más llamadas, o que quieren que les pasen las urgencias.' if es else 'For busier businesses, or owners who want urgent calls passed to them.',
             ['Todo lo del plan Inicial' if es else 'Everything in Starter',
              'Transferencias a su celular en horario: urgencias, quejas o cuando piden hablar con usted' if es else 'Transfers to your cell during business hours: urgent calls, complaints or callers asking for you'],
             'Con transferencias' if es else 'Includes transfers'),
            ('maximo', 'Máximo' if es else 'Max', 597, '1,000', '500',
             'Para negocios con mucho volumen de llamadas, o con varias líneas o sucursales.' if es else 'For high call volume, or several lines or locations.',
             ['Todo lo del plan Pro' if es else 'Everything in Pro',
              'Varias líneas o sucursales: escríbanos y lo configuramos con usted' if es else 'Multiple lines or locations: email us and we set it up with you',
              'Soporte prioritario' if es else 'Priority support'], None)]
    out = '<div class="plans">'
    for key, name, price, mins, calls, fit, feats, tag in data:
        lis = ''.join(f'<li>{E(f)}</li>' for f in feats)
        chip = f'<span class="label-chip lime">{E(tag)}</span>' if tag else ''
        featured = key == 'pro'
        btn = (f'<a class="btn{"" if featured else " ghost"}" href="{u("signup", lang)}?plan={key}" data-plan="{key}">{E(cta_text(lang))}</a>' if cta else '')
        out += f'''<div class="card plan{' featured' if featured else ''}"><div class="name"><span>{E(name)}</span>{chip}</div>
<div class="price">${price}<span>/{"mes" if es else "mo"}</span></div>
<p class="fit">{E(fit)}</p>
<p class="muted"><b>{mins} {"minutos al mes" if es else "minutes a month"}</b><br><span class="small">{"Por ejemplo, unas " + calls + " llamadas de 2 minutos." if es else "For example, about " + calls + " two-minute calls."}</span></p><ul>{lis}</ul>{btn}</div>'''
    return out + '</div>' + (cta_note(lang) if cta else '')


def terms(lang):
    if lang == 'es':
        items = ['Prueba de 14 días: empieza cuando registra su tarjeta y no se cobra nada durante la prueba. Al terminar empieza la mensualidad de su plan, salvo que cancele antes.',
                 'Minutos: el tiempo que Sofía pasa en llamadas, sumado por mes calendario. Si se pasa, Sofía sigue contestando: le avisamos por correo y le sugerimos otro plan, sin cobros extra sin su acuerdo.',
                 'Instalación: $297, pago único. No se cobra mientras configura, mientras espera la activación ni durante la prueba: se cobra junto con el primer pago mensual. Si cancela durante la prueba, no paga nada. Sin costo para los primeros cinco negocios que empiecen su prueba.',
                 'Sin contrato. Cancele cuando quiera.']
        links = f'Detalles en los <a href="{u("terms", lang)}">Términos del servicio</a> y la <a href="{u("privacy", lang)}">Política de privacidad</a>.'
    else:
        items = ['14-day trial: it starts when you add your card, and nothing is charged during the trial. When it ends, your monthly plan starts unless you cancel before.',
                 'Minutes: the time Sofía spends on calls, added up per calendar month. If you go over, Sofía keeps answering: we email you and suggest another plan, and nothing extra is charged unless you agree.',
                 'Setup: $297, one-time. It is never charged while you set up, while you wait for activation or during the trial: it is charged with your first monthly payment. Cancel during the trial and you pay nothing. Waived for the first five businesses to start a trial.',
                 'No contract. Cancel any time.']
        links = f'Details in the <a href="{u("terms", lang)}">Terms of service</a> and the <a href="{u("privacy", lang)}">Privacy policy</a>.'
    return '<ul class="terms">' + ''.join(f'<li>{E(i)}</li>' for i in items) + f'</ul><p class="small muted terms-links">{links}</p>'


def cta_band(lang, title=None):
    es = lang == 'es'
    t = title or ('Pruebe a Sofía con su propio negocio.' if es else 'Try Sofía with your own business.')
    return f'''<section><div class="wrap"><div class="cta-band">
<h2>{E(t)}</h2>
<p>{"Cree su cuenta en un minuto, configure su negocio a su ritmo y pruébela desde su celular antes de cambiar nada en su línea." if es else "Create your account in a minute, set up your business at your own pace and test it from your cell before changing anything on your line."}</p>
<div class="btn-row"><a class="btn" href="{u('signup', lang)}">{E(cta_text(lang))}</a>
<a href="{TEL}">{"O llame a la demo: (813) 722-1120" if es else "Or call the demo: (813) 722-1120"}</a></div>
{cta_note(lang)}</div></div></section>'''


def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{E(q)}</summary><div>{a}</div></details>' for q, a in items) + '</div>'


def page_head(lang, eyebrow, h1, lede):
    return f'''<section class="hero"><div class="wrap narrow stack"><!--CRUMBS-->
<p class="eyebrow">{E(eyebrow)}</p><h1>{E(h1)}</h1><p class="lede">{lede}</p></div></section>'''


FWD_TABLE = {
    'es': '''<div class="table-wrap"><table>
<thead><tr><th>Compañía</th><th>Solo las que no contesta</th><th>Todas las llamadas</th><th>Quitar el desvío</th></tr></thead>
<tbody>
<tr><td>Verizon</td><td><code>*71</code> + número de Contesta</td><td><code>*72</code> + número</td><td><code>*73</code></td></tr>
<tr><td>T-Mobile</td><td><code>**61*1</code> + número + <code>#</code><br><span class="small muted">Ocupado: <code>**67*1</code> + número + <code>#</code></span></td><td><code>**21*1</code> + número + <code>#</code></td><td><code>##61#</code>, <code>##67#</code> o <code>##21#</code>; todo: <code>##004#</code></td></tr>
<tr><td>AT&amp;T</td><td colspan="2">AT&amp;T no publica códigos en su página de ayuda: use Ajustes → Teléfono → Desvío de llamadas, o sus <a href="https://www.att.com/support/article/wireless/KM1011513/">instrucciones oficiales</a>.</td><td>El mismo menú</td></tr>
<tr><td>Línea fija o VoIP</td><td colspan="2">Pida a su compañía "desvío cuando no contesto" (o "cuando está ocupado").</td><td>Pídales quitarlo</td></tr>
</tbody></table></div>
<p class="small muted">Fuentes: <a href="https://www.verizon.com/support/call-forwarding-faqs/">Verizon, preguntas frecuentes de desvío</a> · <a href="https://www.t-mobile.com/support/plans-features/self-service-short-codes">T-Mobile, códigos de autoservicio</a> · <a href="https://www.att.com/support/article/wireless/KM1011513/">AT&amp;T, desvío de llamadas</a>. Revisado el 21 de octubre de 2026.</p>''',
    'en': '''<div class="table-wrap"><table>
<thead><tr><th>Carrier</th><th>Only calls you don't answer</th><th>All calls</th><th>Turn it off</th></tr></thead>
<tbody>
<tr><td>Verizon</td><td><code>*71</code> + Contesta number</td><td><code>*72</code> + number</td><td><code>*73</code></td></tr>
<tr><td>T-Mobile</td><td><code>**61*1</code> + number + <code>#</code><br><span class="small muted">Busy: <code>**67*1</code> + number + <code>#</code></span></td><td><code>**21*1</code> + number + <code>#</code></td><td><code>##61#</code>, <code>##67#</code> or <code>##21#</code>; everything: <code>##004#</code></td></tr>
<tr><td>AT&amp;T</td><td colspan="2">AT&amp;T doesn't publish codes on its help page: use Settings → Phone → Call forwarding, or its <a href="https://www.att.com/support/article/wireless/KM1011513/">official instructions</a>.</td><td>Same menu</td></tr>
<tr><td>Landline or VoIP</td><td colspan="2">Ask your provider for "forward when no answer" (or "when busy").</td><td>Ask them to remove it</td></tr>
</tbody></table></div>
<p class="small muted">Sources: <a href="https://www.verizon.com/support/call-forwarding-faqs/">Verizon call forwarding FAQs</a> · <a href="https://www.t-mobile.com/support/plans-features/self-service-short-codes">T-Mobile self-service short codes</a> · <a href="https://www.att.com/support/article/wireless/KM1011513/">AT&amp;T call forwarding</a>. Checked October 21, 2026.</p>''',
}


# ---------- home ----------
def home(lang):
    es = lang == 'es'
    facts = [('Desde $197/mes', '150 minutos incluidos'), ('Español e inglés', 'Contesta en el idioma de quien llama'), ('Su número no cambia', 'Con desvío de llamadas'),
             ('Google Calendar', 'Revisa horas ocupadas antes de agendar'), ('Resumen por correo', 'Después de cada llamada'), ('Florida', 'Negocios en hora del Este, por ahora')] if es else \
            [('From $197/mo', '150 minutes included'), ('English and Spanish', 'Answers in the caller\'s language'), ('Keep your number', 'Using call forwarding'),
             ('Google Calendar', 'Checks busy times before booking'), ('Email summary', 'After every call'), ('Florida', 'Eastern-time businesses, for now')]
    facts_html = ''.join(f'<div class="fact"><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in facts)
    if es:
        compat = [('¿Tengo que cambiar mi número?', 'No. Activa el desvío de llamadas en su teléfono y las llamadas que usted no contesta pasan a Sofía. En Verizon es <code>*71</code> más el número; en T-Mobile, <code>**61*1</code> más el número y <code>#</code>. <a href="' + u('g_forward', lang) + '">Guía completa, con AT&amp;T y líneas fijas</a>.'),
                  ('¿Qué calendario necesito?', 'Google Calendar. Lo comparte con hola@usecontesta.com con permiso para hacer cambios, y Sofía revisa sus horas ocupadas antes de ofrecer una cita. Por ahora no conectamos con otros sistemas de citas. <a href="' + u('calendar', lang) + '">Cómo funciona la agenda</a>.'),
                  ('¿Qué escuchan sus clientes?', 'Sofía contesta con el nombre de su negocio, dice que es la asistente virtual y que la llamada puede ser grabada, y sigue en el idioma de quien llama.'),
                  ('¿Qué pasa después de registrarme?', 'Configura su negocio en su cuenta (servicios, horario, respuestas), conecta el calendario y registra su tarjeta para empezar la prueba' + ('' if ACTIVATION_LIVE else ' (cuando la activación esté disponible; le avisamos por correo)') + '. Construimos su número de Contesta, lo prueba desde su celular y, cuando sale bien, activa el desvío. <a href="' + u('how', lang) + '">Paso a paso</a>.')]
        faqs = [('¿Sofía dice que es una inteligencia artificial?', '<p>Sí. Al contestar dice que es la asistente virtual. Si alguien pregunta si es un robot, lo confirma y ofrece tomar la cita o el mensaje.</p>'),
                ('¿Qué hace si le preguntan algo que no sabe?', '<p>No lo inventa. Toma nombre, teléfono y motivo, y le avisa a usted en el resumen, incluida la pregunta exacta que no pudo contestar.</p>'),
                ('¿Manda mensajes de texto?', '<p>Todavía no. Hoy los resúmenes le llegan por correo después de cada llamada.</p>'),
                ('¿Puede pasarme las llamadas urgentes?', '<p>Sí, en los planes Pro y Máximo: en horario de trabajo, para urgencias, quejas o cuando alguien pide hablar con usted.</p>'),
                ('¿Cómo pauso el servicio?', '<p>Quite el desvío desde su teléfono (en Verizon, <code>*73</code>; en T-Mobile, <code>##61#</code>) y las llamadas vuelven a sonar solo en su teléfono.</p>'),
                ('¿Funciona fuera de Florida?', '<p>Por ahora atendemos negocios en Florida, en hora del Este.</p>')]
        return f'''<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">Recepcionista con IA · Florida</p>
<h1>Su recepcionista con IA,<br> <span class="mark">en español e inglés.</span></h1>
<p class="lede">Sofía atiende llamadas, agenda citas en su Google Calendar y le envía un resumen mientras usted trabaja. Disponible las 24 horas.</p>
<div class="btn-row"><a class="btn" href="{u('signup', lang)}">{E(cta_text(lang))}</a><a class="btn ghost" href="#demo">Escuche a Sofía</a></div>
{cta_note(lang)}
<p class="demo-line">¿Prefiere llamar? Pruébela en vivo: <a href="{TEL}">(813) 722-1120</a></p>
<p class="brandline">Usted trabaja. Contesta responde.</p>
</div>
{call_card(lang)}
</div></section>
<section class="tight" aria-label="Datos del servicio"><div class="wrap"><div class="facts">{facts_html}</div></div></section>
<section id="demo"><div class="wrap grid-2" style="align-items:center">
<div class="stack"><p class="eyebrow">Demo real</p><h2>Escuche a Sofía: una llamada real, de principio a fin.</h2>
<p class="muted">Llamamos a nuestro negocio de prueba, Barbería Prueba Contesta. Quien llama es un cliente simulado por IA, para no publicar la voz de nadie. Sofía, la consulta al calendario, la cita y el correo al dueño son el producto real.</p>
{audio(lang)}<p><a href="{u('demo', lang)}">Leer la transcripción completa y el correo del dueño</a></p></div>
<div class="card stack"><span class="eyebrow">Correo recibido · 1:16 a. m.</span><h3>Llamada: Carlos Méndez (cita)</h3>
<p><b>Carlos Méndez agendó un corte de caballero para el jueves 22 de octubre a las 4:00 p. m.</b></p>
<ul class="small"><li>Llamó desde: +1 (813) 722-1120 <span class="muted">(nuestra línea de demo)</span></li><li>Cita: corte de caballero, jueves 22 de octubre de 2026, 4:00 p. m.</li><li>Incluye la conversación completa por escrito.</li></ul></div>
</div></section>
<section id="como" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Cómo funciona</p><h2>Listo sin reuniones y sin cambiar su número.</h2></div>
<div class="grid-3">
<div class="card step"><span class="step-n">1</span><h3>Cree su cuenta</h3><p class="muted">Elija su plan y escriba su correo y el nombre del negocio. Toma un minuto.</p></div>
<div class="card step"><span class="step-n">2</span><h3>Enséñele su negocio</h3><p class="muted">Servicios con precio y duración, horario, respuestas aprobadas y a quién avisar. Cada paso se guarda; puede volver cuando quiera.</p></div>
<div class="card step"><span class="step-n">3</span><h3>Pruebe y active</h3><p class="muted">Conecte Google Calendar, empiece su prueba con su tarjeta y llame a su nuevo número desde su celular. Si la prueba sale bien, active el desvío.{"" if ACTIVATION_LIVE else " La activación con tarjeta todavía no está disponible; le avisamos por correo."}</p></div>
</div><p style="margin-top:18px"><a href="{u('how', lang)}">Ver el paso a paso completo</a></p></div></section>
<section class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Para quién es</p><h2>Negocios que viven del teléfono y de las citas.</h2></div>
<div class="grid-2">
<a class="card stack" href="{u('auto', lang)}" style="text-decoration:none"><h3>Talleres y detailing</h3><p class="muted">Contesta mientras usted está debajo del carro: agenda cambios de aceite, diagnósticos o lavados, y anota año, marca y modelo.</p><span>Ver cómo funciona en un taller →</span></a>
<a class="card stack" href="{u('cleaning', lang)}" style="text-decoration:none"><h3>Limpieza a domicilio</h3><p class="muted">Pide la dirección, revisa que esté en su zona y agenda limpiezas o estimados en su calendario.</p><span>Ver cómo funciona en limpieza →</span></a>
</div>
<p class="small muted" style="margin-top:14px">¿Otro tipo de negocio con citas? Si trabaja con Google Calendar y una persona en el teléfono le resolvería el día, escríbanos a <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.</p>
</div></section>
<section id="precios" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Precios</p><h2>Desde $197 al mes. Sin contrato.</h2></div>
{plans(lang)}{terms(lang)}<p style="margin-top:14px"><a href="{u('pricing', lang)}">Detalles de precios y preguntas sobre el cobro</a></p></div></section>
<section id="compatibilidad" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Configuración y compatibilidad</p><h2>Lo que necesita saber antes de empezar.</h2></div>
<div class="grid-2">{''.join(f'<div class="card flat stack"><h3>{E(q)}</h3><p class="muted">{a}</p></div>' for q, a in compat)}</div></div></section>
<section id="faq" class="tight"><div class="wrap narrow">
<div class="sec-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Lo que todos preguntan.</h2></div>{faq(faqs)}</div></section>
{cta_band(lang)}'''
    compat = [('Do I have to change my number?', 'No. You turn on call forwarding on your phone, and calls you don\'t answer go to Sofía. On Verizon it\'s <code>*71</code> plus the number; on T-Mobile, <code>**61*1</code> plus the number and <code>#</code>. <a href="' + u('g_forward', lang) + '">Full guide, including AT&amp;T and landlines</a>.'),
              ('Which calendar do I need?', 'Google Calendar. You share it with hola@usecontesta.com with permission to make changes, and Sofía checks your busy times before offering an appointment. We don\'t connect to other booking systems yet. <a href="' + u('calendar', lang) + '">How booking works</a>.'),
              ('What do your callers hear?', 'Sofía answers with your business name, says she\'s the virtual assistant and that the call may be recorded, and continues in the caller\'s language.'),
              ('What happens after I sign up?', 'You set up your business in your account (services, hours, answers), connect your calendar and add your card to start the trial' + ('' if ACTIVATION_LIVE else ' (once activation is available; we’ll email you)') + '. We build your Contesta number, you test it from your cell and, once it works, you turn on forwarding. <a href="' + u('how', lang) + '">Step by step</a>.')]
    faqs = [('Does Sofía say she\'s an AI?', '<p>Yes. When she answers she says she\'s the virtual assistant. If someone asks whether she\'s a robot, she confirms it and offers to take the appointment or message.</p>'),
            ('What if someone asks something she doesn\'t know?', '<p>She doesn\'t make it up. She takes name, number and reason, and tells you in the summary, including the exact question she couldn\'t answer.</p>'),
            ('Does she send text messages?', '<p>Not yet. Today summaries reach you by email after every call.</p>'),
            ('Can she pass urgent calls to me?', '<p>Yes, on Pro and Max: during business hours, for urgent calls, complaints, or when a caller asks for you.</p>'),
            ('How do I pause the service?', '<p>Turn forwarding off from your phone (on Verizon, <code>*73</code>; on T-Mobile, <code>##61#</code>) and calls ring only on your phone again.</p>'),
            ('Does it work outside Florida?', '<p>For now we serve businesses in Florida, on Eastern time.</p>')]
    return f'''<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">AI receptionist · Florida</p>
<h1>Your AI receptionist,<br> <span class="mark">in English and Spanish.</span></h1>
<p class="lede">Sofía answers calls, books appointments in Google Calendar, and sends you a summary while you work. Available 24/7.</p>
<div class="btn-row"><a class="btn" href="{u('signup', lang)}">{E(cta_text(lang))}</a><a class="btn ghost" href="#demo">Hear Sofía</a></div>
{cta_note(lang)}
<p class="demo-line">Rather call? Try her live: <a href="{TEL}">(813) 722-1120</a></p>
<p class="brandline">You work. Contesta answers.</p>
</div>
{call_card(lang)}
</div></section>
<section class="tight" aria-label="Service facts"><div class="wrap"><div class="facts">{facts_html}</div></div></section>
<section id="demo"><div class="wrap grid-2" style="align-items:center">
<div class="stack"><p class="eyebrow">Real demo</p><h2>Hear Sofía: a real call, start to finish.</h2>
<p class="muted">We called our test business, Barbería Prueba Contesta. The caller is an AI-simulated customer so no one's real voice is published. Sofía, the calendar check, the booking and the owner's email are the real product. The call is in Spanish; Sofía also answers in English.</p>
{audio(lang)}<p><a href="{u('demo', lang)}">Read the full transcript (with English translation) and the owner's email</a></p></div>
<div class="card stack"><span class="eyebrow">Email received · 1:16 a.m.</span><h3>Llamada: Carlos Méndez (cita)</h3>
<p><b>Carlos Méndez booked a men's haircut for Thursday, October 22 at 4:00 p.m.</b></p>
<ul class="small"><li>Called from: +1 (813) 722-1120 <span class="muted">(our demo line)</span></li><li>Appointment: men's haircut, Thursday, October 22, 2026, 4:00 p.m.</li><li>Includes the full written conversation.</li></ul>
<p class="small muted">The email arrives in the owner's chosen language; this one is translated from Spanish.</p></div>
</div></section>
<section id="how" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">How it works</p><h2>Set up without meetings and without changing your number.</h2></div>
<div class="grid-3">
<div class="card step"><span class="step-n">1</span><h3>Create your account</h3><p class="muted">Pick a plan and enter your email and business name. It takes a minute.</p></div>
<div class="card step"><span class="step-n">2</span><h3>Teach her your business</h3><p class="muted">Services with price and length, hours, approved answers and who to notify. Each step saves; come back any time.</p></div>
<div class="card step"><span class="step-n">3</span><h3>Test and go live</h3><p class="muted">Connect Google Calendar, start your trial with your card and call your new number from your cell. If the test works, turn on forwarding.{"" if ACTIVATION_LIVE else " Card activation isn’t available yet; we’ll email you when it is."}</p></div>
</div><p style="margin-top:18px"><a href="{u('how', lang)}">See the full step by step</a></p></div></section>
<section class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Who it's for</p><h2>Businesses that live on the phone and on appointments.</h2></div>
<div class="grid-2">
<a class="card stack" href="{u('auto', lang)}" style="text-decoration:none"><h3>Auto repair and detailing</h3><p class="muted">Answers while you're under the car: books oil changes, diagnostics or washes, and notes year, make and model.</p><span>How it works for a shop →</span></a>
<a class="card stack" href="{u('cleaning', lang)}" style="text-decoration:none"><h3>Home cleaning</h3><p class="muted">Asks for the address, checks it's in your area and books cleanings or estimates in your calendar.</p><span>How it works for cleaning →</span></a>
</div>
<p class="small muted" style="margin-top:14px">Another appointment-based business? If you run on Google Calendar and a person on the phone would make your day, email <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.</p>
</div></section>
<section id="pricing" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Pricing</p><h2>From $197 a month. No contract.</h2></div>
{plans(lang)}{terms(lang)}<p style="margin-top:14px"><a href="{u('pricing', lang)}">Pricing details and billing questions</a></p></div></section>
<section id="compatibility" class="tight"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Setup and compatibility</p><h2>What to know before you start.</h2></div>
<div class="grid-2">{''.join(f'<div class="card flat stack"><h3>{E(q)}</h3><p class="muted">{a}</p></div>' for q, a in compat)}</div></div></section>
<section id="faq" class="tight"><div class="wrap narrow">
<div class="sec-head"><p class="eyebrow">FAQ</p><h2>What everyone asks.</h2></div>{faq(faqs)}</div></section>
{cta_band(lang)}'''


# ---------- other pages ----------
def page_body(key, lang):
    es = lang == 'es'
    if key == 'pricing':
        if es:
            q = [('¿Cuándo se cobra?', '<p>Nada mientras configura su cuenta ni durante los 14 días de prueba. La prueba empieza cuando registra su tarjeta; al terminar se cobra la mensualidad del plan que eligió (y la instalación, si le aplica), salvo que cancele antes.</p>')]
            if not ACTIVATION_LIVE:
                q.append(('¿Puedo empezar la prueba hoy?', '<p>Todavía no: la activación de la prueba con tarjeta aún no está disponible. Puede crear su cuenta y dejar su recepcionista configurada hoy; le avisaremos por correo cuando pueda activarla. Su prueba de 14 días no empieza mientras espera y no se cobra nada.</p>'))
            q += [('¿Cuándo se cobra la instalación de $297 y quién no la paga?', '<p>Es un pago único por construir su recepcionista y su número de Contesta. Se cobra junto con su primer pago mensual, al terminar la prueba. Nunca se cobra mientras configura, mientras espera la activación ni durante la prueba, y si cancela durante la prueba no paga nada.</p><p>Los primeros cinco negocios que empiecen su prueba no la pagan. Su cuenta y la página de pago le dicen si le aplica antes de registrar la tarjeta.</p>'),
                  ('¿Qué cuenta como minuto?', '<p>El tiempo que Sofía está en una llamada, desde que contesta hasta que cuelga, sumado por mes calendario (hora del Este). Las llamadas que usted contesta no cuentan. Con llamadas de unos 2 minutos, 150 minutos son unas 75 llamadas al mes.</p>'),
                  ('¿Qué pasa si me paso de los minutos?', '<p>Sofía sigue contestando: no le cortamos el servicio. Le avisamos por correo ese mismo mes y le sugerimos el plan que le queda mejor; no cobramos nada extra sin su acuerdo.</p>'),
                  ('¿Puedo cambiar de plan?', '<p>Sí. Antes de empezar la prueba lo cambia en su cuenta; después, escríbanos a hola@usecontesta.com.</p>'),
                  ('¿Cómo cancelo?', '<p>' + ('Desde su cuenta, en "Administrar pago o cancelar", o escribiéndonos a hola@usecontesta.com. ' if ACTIVATION_LIVE else 'Escríbanos a hola@usecontesta.com. ') + 'No hay contrato. Si cancela durante la prueba, no se cobra nada. Después, el servicio sigue hasta el final del mes pagado y no hay reembolsos por meses parciales. Para que las llamadas vuelvan a su teléfono de inmediato, quite el desvío desde su teléfono.</p>')]
        else:
            q = [('When am I charged?', '<p>Nothing while you set up your account or during the 14-day trial. The trial starts when you add your card; when it ends, the monthly price of the plan you chose is charged (plus setup, if it applies to you), unless you cancel first.</p>')]
            if not ACTIVATION_LIVE:
                q.append(('Can I start the trial today?', '<p>Not yet: card activation for the trial isn’t available yet. You can create your account and finish setting up your receptionist today; we’ll email you when you can activate it. Your 14-day trial won’t begin while you’re waiting, and nothing is charged.</p>'))
            q += [('When is the $297 setup fee charged, and who doesn’t pay it?', '<p>It’s a one-time fee for building your receptionist and your Contesta number. It’s charged with your first monthly payment, when the trial ends. It is never charged while you set up, while you wait for activation or during the trial, and if you cancel during the trial you pay nothing.</p><p>The first five businesses to start a trial don’t pay it. Your account and the payment page tell you whether it applies before you add your card.</p>'),
                  ('What counts as a minute?', '<p>The time Sofía is on a call, from when she answers until the call ends, added up per calendar month (Eastern time). Calls you answer yourself don’t count. With calls of about 2 minutes, 150 minutes is about 75 calls a month.</p>'),
                  ('What if I go over my minutes?', '<p>Sofía keeps answering: we don’t cut off your service. We email you that same month and suggest the plan that fits better; nothing extra is charged unless you agree.</p>'),
                  ('Can I change plans?', '<p>Yes. Before starting the trial you change it in your account; after that, email hola@usecontesta.com.</p>'),
                  ('How do I cancel?', '<p>' + ('From your account, under "Manage billing or cancel", or by emailing hola@usecontesta.com. ' if ACTIVATION_LIVE else 'Email hola@usecontesta.com. ') + 'There’s no contract. Cancel during the trial and nothing is charged. After that, service runs to the end of the paid month and partial months aren’t refunded. To send calls back to your phone right away, turn forwarding off from your phone.</p>')]
        inc = (['Español e inglés: contesta en el idioma de quien llama', 'Citas en su Google Calendar, sin agendar encima de horas ocupadas', 'Resumen de cada llamada por correo, con la conversación escrita',
                'Respuestas solo de la información que usted aprobó', 'Aviso de grabación y de asistente virtual en cada llamada'] if es else
               ['English and Spanish: answers in the caller\'s language', 'Appointments in your Google Calendar, never over busy times', 'Email summary of every call, with the written conversation',
                'Answers only from information you approved', 'Recording and virtual-assistant notice on every call'])
        return page_head(lang, 'Precios' if es else 'Pricing', 'Precios claros, sin contrato.' if es else 'Clear pricing, no contract.',
                         ('Tres planes según cuántos minutos de llamadas atiende Sofía al mes. Todos incluyen español e inglés, Google Calendar y el resumen por correo.' if es else
                          'Three plans based on how many call minutes Sofía handles a month. All include English and Spanish, Google Calendar and the email summary.')) + f'''
<section class="tight"><div class="wrap">{plans(lang)}{terms(lang)}</div></section>
<section class="tight"><div class="wrap grid-2">
<div class="card stack"><h2>{"Incluido en todos los planes" if es else "Included in every plan"}</h2><ul>{''.join(f'<li>{E(i)}</li>' for i in inc)}</ul></div>
<div class="card stack"><h2>{"Lo que todavía no incluye" if es else "Not included yet"}</h2><ul>
<li>{"Mensajes de texto: hoy los resúmenes llegan por correo." if es else "Text messages: summaries arrive by email today."}</li>
<li>{"Otros sistemas de citas que no sean Google Calendar." if es else "Booking systems other than Google Calendar."}</li>
<li>{"Negocios fuera de Florida." if es else "Businesses outside Florida."}</li></ul>
<p class="small muted">{"Preferimos decirlo antes de que se registre." if es else "We'd rather say so before you sign up."}</p></div>
</div></section>
<section class="tight"><div class="wrap narrow"><div class="sec-head"><h2>{"Preguntas sobre el cobro" if es else "Billing questions"}</h2></div>{faq(q)}</div></section>
{cta_band(lang)}'''

    if key == 'how':
        if es:
            steps = [('1. Cree su cuenta', 'Elija el plan y escriba su correo y el nombre del negocio. Le llega un enlace para volver a su cuenta cuando quiera; no hay contraseña que recordar.'),
                     ('2. Configure su negocio', 'Siete pasos cortos que se guardan por separado: su negocio (y si va a donde el cliente, su zona), servicios con precio y duración, horario, saludo, respuestas aprobadas, contacto y transferencias. Cada campo trae un ejemplo.'),
                     ('3. Conecte Google Calendar', 'Si quiere que Sofía agende, comparte su calendario con hola@usecontesta.com con permiso para hacer cambios. Al tocar Verificar probamos de verdad que podemos leer y crear eventos (creamos uno de prueba y lo borramos al instante).'),
                     ('4. Revise lo que Sofía va a usar', 'Su cuenta le muestra el resumen exacto: zona horaria, horario, servicios y duraciones, anticipación, tiempo entre citas, qué hace fuera de horario y cuándo transfiere.'),
                     ('5. Empiece su prueba', 'Registra su tarjeta en la página segura de pago para empezar la prueba de 14 días; no se cobra nada durante la prueba. La instalación, si le aplica, se cobra con el primer pago mensual.' + ('' if ACTIVATION_LIVE else ' Esta activación todavía no está disponible: su configuración queda guardada, su prueba no empieza mientras espera y le avisamos por correo cuando pueda activar.')),
                     ('6. Pruebe desde su celular', 'Construimos su número de Contesta. Llámelo desde su celular y pida una cita: sus clientes no notan nada todavía. Su cuenta marca la prueba como aprobada cuando llega la llamada y el resumen.'),
                     ('7. Active el desvío', 'Desde el teléfono del negocio marca el código de su compañía. Las llamadas que usted no contesta pasan a Sofía; su número no cambia. Para pausar, quita el desvío.')]
        else:
            steps = [('1. Create your account', 'Pick a plan and enter your email and business name. You get a link to come back to your account any time; there\'s no password to remember.'),
                     ('2. Set up your business', 'Seven short steps that save separately: your business (and your service area if you go to customers), services with price and length, hours, greeting, approved answers, contact and transfers. Every field has an example.'),
                     ('3. Connect Google Calendar', 'If you want Sofía to book, share your calendar with hola@usecontesta.com with permission to make changes. When you tap Check, we really test that we can read and create events (we create a test event and delete it right away).'),
                     ('4. Review what Sofía will use', 'Your account shows the exact summary: time zone, hours, services and lengths, notice, buffer between appointments, what happens after hours and when she transfers.'),
                     ('5. Start your trial', 'Add your card on the secure payment page to start the 14-day trial; nothing is charged during the trial. Setup, if it applies to you, is charged with the first monthly payment.' + ('' if ACTIVATION_LIVE else ' This activation isn’t available yet: your setup stays saved, your trial won’t begin while you’re waiting, and we’ll email you when you can activate.')),
                     ('6. Test from your cell', 'We build your Contesta number. Call it from your cell and ask for an appointment: your customers notice nothing yet. Your account marks the test as passed once the call and summary come through.'),
                     ('7. Turn on forwarding', 'From the business phone, dial your carrier\'s code. Calls you don\'t answer go to Sofía; your number stays the same. To pause, turn forwarding off.')]
        st = ''.join(f'<div class="card stack"><h3>{E(t)}</h3><p class="muted">{E(d)}</p></div>' for t, d in steps)
        return page_head(lang, 'Cómo funciona' if es else 'How it works', 'De la cuenta a la primera llamada.' if es else 'From account to first call.',
                         ('Lo hace usted, a su ritmo, sin reuniones. Si se traba, escríbanos y le ayudamos por correo.' if es else
                          'You do it yourself, at your own pace, no meetings. If you get stuck, email us and we\'ll help.')) + f'''
<section class="tight"><div class="wrap narrow stack">{st}</div></section>
<section class="tight"><div class="wrap narrow stack">
<h2>{"Qué cambia para quien llama" if es else "What changes for callers"}</h2>
<p class="muted">{"Si usted contesta, nada. Si no contesta, en vez del buzón oye a Sofía: el nombre de su negocio, el aviso de asistente virtual y de grabación, y una pregunta corta. Si llama en inglés, sigue en inglés." if es else "If you answer, nothing. If you don't, instead of voicemail they hear Sofía: your business name, the virtual-assistant and recording notice, and a short question. If they speak English, she continues in English."}</p>
<h2>{"Activar, probar y quitar el desvío" if es else "Turning forwarding on, testing and off"}</h2>
{FWD_TABLE[lang]}
<p><a href="{u('g_forward', lang)}">{"Guía completa de desvío de llamadas" if es else "Full call forwarding guide"}</a></p>
</div></section>
{cta_band(lang)}'''

    if key == 'demo':
        who = {'s': 'Sofía', 'c': 'Cliente (simulado)' if es else 'Caller (simulated)'}
        tr = ''.join(f'<p class="{w}"><b>{who[w]}:</b> {E(t)}</p>' for w, t in CALL['es'])
        tr_en = '' if es else '<h3>English translation</h3><div class="transcript">' + ''.join(f'<p class="{w}"><b>{who[w]}:</b> {E(t)}</p>' for w, t in CALL['en']) + '</div>'
        return page_head(lang, 'Demo', 'Escuche a Sofía.' if es else 'Hear Sofía.',
                         ('Una llamada real a nuestro negocio de prueba, grabada el 21 de octubre de 2026. Quien llama es un cliente simulado por IA; Sofía, la consulta al calendario, la cita y el correo al dueño son el producto real.' if es else
                          'A real call to our test business, recorded October 21, 2026. The caller is an AI-simulated customer; Sofía, the calendar check, the booking and the owner\'s email are the real product.')) + f'''
<section class="tight"><div class="wrap narrow stack-lg">
<div class="card stack">{audio(lang)}</div>
<div class="stack"><h2>{"Transcripción" if es else "Transcript"}</h2>
<p class="small muted">{"Transcripción automática de la grabación; corregimos solo puntuación y números escritos." if es else "Automatic transcript of the recording (in Spanish); we only fixed punctuation and written numbers."}</p>
<div class="transcript">{tr}</div>{tr_en}</div>
<div class="stack"><h2>{"Lo que pasó después de colgar" if es else "What happened after the call"}</h2>
<div class="card stack"><span class="eyebrow">{"Correo al dueño · 21 oct 2026, 1:16 a. m." if es else "Email to the owner · Oct 21, 2026, 1:16 a.m."}</span>
<h3>Llamada: Carlos Méndez (cita)</h3>
<p><b>Carlos Méndez agendó un corte de caballero para el jueves 22 de octubre a las 4:00 p. m.</b></p>
<ul class="small"><li>Llamó desde: +18137221120</li><li>Teléfono para devolver: 18137221120</li><li>Cita: Corte de caballero el jueves 22 de octubre de 2026 a las 4:00 p. m.</li><li>Conversación: (texto completo de la llamada)</li></ul>
{'' if es else '<p class="small muted">Shown as sent, in Spanish. It says: "Carlos Méndez booked a men\'s haircut for Thursday, October 22 at 4:00 p.m." with the number he called from, the callback number, the appointment and the full conversation.</p>'}</div>
<p class="muted">{"La cita quedó en el Google Calendar del negocio de prueba como \"Corte de caballero — Carlos Méndez\", con el teléfono en la descripción. El número desde el que \"llamó el cliente\" es nuestra línea de demo, porque desde ahí hicimos la llamada simulada." if es else "The appointment landed in the test business's Google Calendar as \"Corte de caballero — Carlos Méndez\", with the phone in the description. The number the \"customer\" called from is our demo line, because that's where we placed the simulated call."}</p></div>
<div class="stack"><h2>{"Pruébela usted" if es else "Try her yourself"}</h2>
<p class="muted">{"Llame a la línea de demo y hable con Sofía como si fuera un cliente suyo:" if es else "Call the demo line and talk to Sofía as if you were one of your customers:"} <a href="{TEL}"><b>(813) 722-1120</b></a></p></div>
<div class="stack"><h2>{"Video ilustrativo" if es else "Illustrative video"}</h2>
<p class="small muted">{"Animación de 55 segundos con voces sintéticas, no es una grabación. Para escuchar a Sofía de verdad, use el audio de arriba o llame a la demo." if es else "A 55-second animation with synthetic voices, in Spanish; it isn't a recording. To hear the real Sofía, use the audio above or call the demo."}</p>
<video controls playsinline preload="none" width="360" height="640" poster="/contesta-demo-poster.jpg" data-demo style="max-width:360px;width:100%;height:auto;border-radius:18px;background:#173D30"><source src="/contesta-demo.mp4" type="video/mp4"></video></div>
</div></section>
{cta_band(lang)}'''

    if key == 'calendar':
        flow = (['Pregunta qué servicio quiere y qué día.', 'Revisa en su Google Calendar las horas ocupadas de ese día.', 'Ofrece dos horas libres dentro de su horario, con la anticipación mínima y los minutos entre citas que usted puso, usando la duración del servicio.',
                 'Pide el nombre y confirma el teléfono (ofrece el número desde el que llaman).', 'Crea el evento. Solo dice "confirmada" si el calendario aceptó la cita; si la hora se ocupó, ofrece otras dos.', 'Si algo falla, toma la solicitud como mensaje y usted confirma.'] if es else
                ['Asks which service and which day.', 'Checks that day\'s busy times in your Google Calendar.', 'Offers two open times within your hours, with your minimum notice and buffer, using the service length.',
                 'Takes the name and confirms the phone (offers the number they\'re calling from).', 'Creates the event. She only says "confirmed" if the calendar accepted it; if the time got taken, she offers two others.', 'If anything fails, she takes the request as a message and you confirm.'])
        return page_head(lang, 'Google Calendar', 'Citas directo en su Google Calendar.' if es else 'Appointments straight into your Google Calendar.',
                         ('Sofía no agenda encima de nada: revisa sus horas ocupadas antes de ofrecer una hora y solo confirma cuando el evento quedó creado.' if es else
                          'Sofía never books over anything: she checks your busy times before offering a time and only confirms once the event exists.')) + f'''
<section class="tight"><div class="wrap narrow stack-lg">
<div class="stack"><h2>{"Así agenda en una llamada" if es else "How she books during a call"}</h2><ol>{''.join(f'<li>{E(x)}</li>' for x in flow)}</ol>
<p class="muted">{"Así fue en la llamada real de nuestra demo: ofreció 3:00 y 4:00 p. m. del jueves, el cliente eligió las 4:00 y el evento quedó creado." if es else "That's what happened in our real demo call: she offered Thursday 3:00 and 4:00 p.m., the caller chose 4:00 and the event was created."} <a href="{u('demo', lang)}">{"Escuchar" if es else "Listen"}</a></p></div>
<div class="card stack"><h2>{"Cómo se conecta" if es else "How it connects"}</h2>
<ol><li>{"En una computadora, abra Google Calendar → Configuración y elija su calendario." if es else "On a computer, open Google Calendar → Settings and pick your calendar."}</li>
<li>{"En \"Compartir con determinadas personas\", agregue hola@usecontesta.com con permiso \"Hacer cambios en eventos\"." if es else "Under \"Share with specific people\", add hola@usecontesta.com with \"Make changes to events\"."}</li>
<li>{"En su cuenta de Contesta, escriba el correo del calendario y toque Verificar: probamos lectura y escritura de verdad." if es else "In your Contesta account, enter the calendar email and tap Check: we really test reading and writing."}</li></ol>
<p class="small muted">{"Con ese permiso, Contesta puede ver los eventos de ese calendario y crear citas. Usamos las horas ocupadas para no agendar encima. Puede quitar el permiso cuando quiera; Sofía vuelve a tomar las citas como mensaje." if es else "With that permission, Contesta can see that calendar's events and create appointments. We use busy times to avoid double-booking. You can remove access any time; Sofía goes back to taking appointments as messages."}</p></div>
<div class="stack"><h2>{"Qué queda en el evento" if es else "What goes in the event"}</h2>
<p class="muted">{"Título: servicio y nombre del cliente. Descripción: \"Agendada por Contesta\", nombre, teléfono, servicio y, si aplica, la dirección del servicio y las respuestas a sus preguntas de agenda (por ejemplo, año, marca y modelo)." if es else "Title: service and caller name. Description: \"Agendada por Contesta\", name, phone, service and, when it applies, the service address and the answers to your booking questions (for example, year, make and model)."}</p></div>
<div class="note warn stack"><h2 style="font-size:1.2rem">{"Límites de hoy" if es else "Today's limits"}</h2><ul>
<li>{"Un solo calendario: una cita a la vez. Si tiene varias bahías, sillas o equipos, Sofía no agenda dos citas a la misma hora." if es else "One calendar: one appointment at a time. If you have several bays, chairs or crews, Sofía won't book two appointments at the same time."}</li>
<li>{"Solo Google Calendar. No conecta con otros sistemas de citas, de taller o de punto de venta." if es else "Google Calendar only. It doesn't connect to other booking, shop-management or point-of-sale systems."}</li>
<li>{"Agenda en hora del Este (Florida)." if es else "Books in Eastern time (Florida)."}</li>
<li>{"No cobra depósitos ni pagos." if es else "It doesn't take deposits or payments."}</li></ul></div>
</div></section>
{cta_band(lang)}'''

    if key == 'auto':
        return industry(lang, 'auto')
    if key == 'cleaning':
        return industry(lang, 'cleaning')

    if key == 'about':
        return page_head(lang, 'Nosotros' if es else 'About', 'Una recepcionista honesta, hecha en Tampa.' if es else 'An honest receptionist, made in Tampa.',
                         ('Contesta es una empresa pequeña de Tampa. Hacemos una recepcionista con IA en español primero para negocios locales que pierden clientes cuando no pueden contestar.' if es else
                          'Contesta is a small Tampa company. We build a Spanish-first AI receptionist for local businesses that lose customers when they can\'t pick up.')) + f'''
<section class="tight"><div class="wrap narrow stack-lg">
<div class="stack"><h2>{"Cómo trabajamos" if es else "How we work"}</h2><ul>
<li>{"Sofía siempre dice que es una asistente virtual y avisa que la llamada puede ser grabada." if es else "Sofía always says she's a virtual assistant and that the call may be recorded."}</li>
<li>{"Solo contesta con la información que usted aprobó. Si no sabe algo, toma el mensaje." if es else "She only answers with information you approved. If she doesn't know something, she takes a message."}</li>
<li>{"Usted ve cada llamada: el resumen y la conversación escrita le llegan por correo." if es else "You see every call: the summary and the written conversation arrive by email."}</li>
<li>{"Le decimos lo que todavía no hace, antes de que se registre." if es else "We tell you what she doesn't do yet, before you sign up."}</li></ul></div>
<div class="card stack"><h2>{"Contacto" if es else "Contact"}</h2>
<p>{"Correo:" if es else "Email:"} <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a></p>
<p>{"Demo en vivo:" if es else "Live demo:"} <a href="{TEL}">(813) 722-1120</a> <span class="muted small">{"(contesta Sofía)" if es else "(Sofía answers)"}</span></p>
<p class="muted">Contesta LLC · Tampa, Florida</p></div>
</div></section>
{cta_band(lang)}'''

    if key == 'guides':
        items = [('g_forward', 'Cómo desviar las llamadas de su negocio' if es else 'How to forward your business calls', 'Códigos oficiales de Verizon y T-Mobile, AT&T, líneas fijas, cómo probar y cómo quitarlo.' if es else 'Official Verizon and T-Mobile codes, AT&T, landlines, how to test and how to turn it off.'),
                 ('g_can', 'Qué puede y qué no puede hacer' if es else 'What it can and can\'t do', 'Lo que una recepcionista con IA bilingüe hace bien y lo que todavía no, con una llamada real.' if es else 'What a bilingual AI receptionist does well and what it doesn\'t yet, with a real call.'),
                 ('g_compare', 'IA, buzón de voz o servicio de contestadora' if es else 'AI vs voicemail vs answering service', 'Qué resuelve cada opción y cuándo conviene cada una.' if es else 'What each option solves and when each one fits.'),
                 ('calendar', 'Cómo funcionan las citas en Google Calendar' if es else 'How Google Calendar booking works', 'Horas ocupadas, anticipación, tiempo entre citas y permisos.' if es else 'Busy times, notice, buffers and permissions.')]
        cards = ''.join(f'<a class="card stack" href="{u(k, lang)}" style="text-decoration:none"><h2 style="font-size:1.3rem">{E(t)}</h2><p class="muted">{E(d)}</p></a>' for k, t, d in items)
        return page_head(lang, 'Guías' if es else 'Guides', 'Guías prácticas.' if es else 'Practical guides.',
                         'Respuestas concretas a lo que preguntan los dueños antes de empezar.' if es else 'Straight answers to what owners ask before they start.') + f'''
<section class="tight"><div class="wrap grid-2">{cards}</div></section>'''

    if key == 'g_forward':
        return page_head(lang, 'Guía' if es else 'Guide', 'Cómo desviar las llamadas de su negocio a una recepcionista.' if es else 'How to forward your business calls to a receptionist.',
                         ('Con el desvío "cuando no contesto", su teléfono suena primero. Si usted no contesta, la llamada pasa a la recepcionista. Su número no cambia y se quita con un código.' if es else
                          'With "forward when I don\'t answer", your phone rings first. If you don\'t pick up, the call goes to the receptionist. Your number doesn\'t change, and one code turns it off.')) + f'''
<section class="tight"><div class="wrap narrow article">
<h2>{"Antes de empezar" if es else "Before you start"}</h2>
<ul><li>{"Tenga a mano su número de Contesta (está en su cuenta después de construir su recepcionista)." if es else "Have your Contesta number handy (it's in your account once your receptionist is built)."}</li>
<li>{"Haga primero la llamada de prueba directo a ese número desde su celular. Así comprueba que todo funciona sin tocar su línea." if es else "First make the test call straight to that number from your cell. That proves everything works without touching your line."}</li>
<li>{"Marque los códigos desde el teléfono que quiere desviar: el del negocio." if es else "Dial the codes from the phone you want to forward: the business phone."}</li></ul>
<h2>{"Códigos por compañía" if es else "Codes by carrier"}</h2>
<p>{"Reemplace \"número\" por los 10 dígitos de su número de Contesta. Le recomendamos el desvío \"solo las que no contesta\": usted sigue contestando cuando puede." if es else "Replace \"number\" with the 10 digits of your Contesta number. We recommend \"only calls you don't answer\": you still pick up when you can."}</p>
{FWD_TABLE[lang]}
<h2>{"Ejemplo" if es else "Example"}</h2>
<p>{"Si su número de Contesta fuera (727) 555-0142 y su línea es de Verizon, marcaría" if es else "If your Contesta number were (727) 555-0142 and your line is on Verizon, you would dial"} <code>*717275550142</code> {"y tocaría llamar. En T-Mobile sería" if es else "and press call. On T-Mobile it would be"} <code>**61*17275550142#</code>. <span class="muted small">{"(Número de ejemplo.)" if es else "(Example number.)"}</span></p>
<h2>{"Cómo comprobar que quedó" if es else "How to check it worked"}</h2>
<p>{"Pida a alguien que llame a su número de negocio y no conteste. Debe escuchar a su recepcionista. Verizon dice que al activarlo o quitarlo puede oír un tono de confirmación que parece de ocupado." if es else "Ask someone to call your business number and don't pick up. They should hear your receptionist. Verizon notes you may hear a confirmation tone that sounds like a busy signal when you turn it on or off."}</p>
<h2>{"Costos" if es else "Costs"}</h2>
<p>{"Verizon y AT&T indican que las llamadas desviadas se facturan como llamadas normales de su plan; revise su plan si tiene minutos limitados." if es else "Verizon and AT&T say forwarded calls are billed like regular calls on your plan; check your plan if your minutes are limited."}</p>
<h2>{"Cómo pausar o quitarlo" if es else "How to pause or remove it"}</h2>
<p>{"Marque el código de \"Quitar\" de la tabla. Las llamadas vuelven a sonar solo en su teléfono. Puede activarlo otra vez cuando quiera." if es else "Dial the \"Turn it off\" code from the table. Calls ring only on your phone again. You can turn it back on whenever you like."}</p>
<p><a class="btn" href="{u('signup', lang)}">{E(cta_text(lang))}</a></p>{cta_note(lang)}
</div></section>'''

    if key == 'g_can':
        can = (['Contesta en español o en inglés, y cambia si quien llama cambia.', 'Contesta las preguntas de siempre con la información que usted aprobó: horario, precios, dirección.',
                'Agenda en su Google Calendar sin pisar horas ocupadas, y solo confirma cuando la cita quedó creada.', 'Toma mensajes con nombre, teléfono y motivo, y le manda el resumen por correo.',
                'Transfiere urgencias a su celular en horario (planes Pro y Máximo).', 'Reconoce el número desde el que llaman y lo ofrece para devolver la llamada.'] if es else
               ['Answers in Spanish or English, and switches if the caller switches.', 'Answers the usual questions from the information you approved: hours, prices, address.',
                'Books into your Google Calendar without overlapping busy times, and only confirms once the event exists.', 'Takes messages with name, number and reason, and emails you the summary.',
                'Transfers urgent calls to your cell during business hours (Pro and Max).', 'Recognizes the caller\'s number and offers it as the callback number.'])
        cant = (['No inventa precios, plazos ni promesas: si no está en su información, toma el mensaje.', 'No manda mensajes de texto todavía.', 'No cobra pagos ni depósitos.',
                 'No conecta con sistemas de citas que no sean Google Calendar, ni agenda dos citas a la misma hora.', 'No da consejos médicos, legales ni financieros.',
                 'En líneas con mucho ruido puede pedir que le repitan; nunca adivina nombres ni números.'] if es else
                ['It doesn\'t invent prices, timelines or promises: if it isn\'t in your information, she takes a message.', 'It doesn\'t send text messages yet.', 'It doesn\'t take payments or deposits.',
                 'It doesn\'t connect to booking systems other than Google Calendar, or book two appointments at the same time.', 'It doesn\'t give medical, legal or financial advice.',
                 'On very noisy lines she may ask the caller to repeat; she never guesses names or numbers.'])
        return page_head(lang, 'Guía' if es else 'Guide', 'Qué puede y qué no puede hacer una recepcionista con IA bilingüe.' if es else 'What a bilingual AI receptionist can and can\'t do.',
                         ('Lo que hace Sofía hoy, lo que no hace, y un ejemplo de una llamada real.' if es else 'What Sofía does today, what she doesn\'t, and an example from a real call.')) + f'''
<section class="tight"><div class="wrap narrow article">
<h2>{"Lo que hace bien" if es else "What she does well"}</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in can)}</ul>
<h2>{"Lo que no hace (todavía)" if es else "What she doesn't do (yet)"}</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in cant)}</ul>
<h2>{"Un ejemplo real" if es else "A real example"}</h2>
<p>{"En nuestra llamada de demo, Sofía revisó el calendario antes de ofrecer horas, confirmó el número leyéndolo dígito por dígito y solo dijo \"confirmada\" después de crear la cita:" if es else "In our demo call, Sofía checked the calendar before offering times, confirmed the number by reading it digit by digit, and only said \"confirmed\" after creating the appointment:"}</p>
{call_card(lang)}
<p><a href="{u('demo', lang)}">{"Escuchar la llamada completa" if es else "Hear the full call"}</a></p>
<h2>{"Cómo se prepara" if es else "How to prepare her"}</h2>
<p>{"Lo más importante es la lista de servicios con precio y duración, y sus respuestas a las preguntas frecuentes. Lo que no esté ahí, Sofía no lo dice." if es else "The most important part is your list of services with price and length, and your answers to frequent questions. Whatever isn't there, Sofía won't say."}</p>
</div></section>
{cta_band(lang)}'''

    if key == 'g_compare':
        rows = ([('Buzón de voz', 'Gratis o incluido en su plan.', 'Muchos clientes cuelgan sin dejar mensaje; usted devuelve la llamada después.', 'Pocas llamadas y clientes que no necesitan respuesta inmediata.'),
                 ('Servicio de contestadora con personas', 'Varía mucho según el proveedor y el volumen.', 'Una persona contesta, toma mensajes y a veces agenda. Puede tener horario limitado o costo por minuto.', 'Llamadas delicadas que necesitan criterio humano.'),
                 ('Recepcionista con IA (Contesta)', 'Desde $197 al mes con 150 minutos.', 'Contesta al instante, 24 horas, en español o inglés; agenda en Google Calendar y le manda el resumen. Solo sabe lo que usted le enseña.', 'Negocios con citas que pierden llamadas mientras trabajan o fuera de horario.')] if es else
                [('Voicemail', 'Free or included in your plan.', 'Many callers hang up without leaving a message; you call back later.', 'Few calls and customers who don\'t need an immediate answer.'),
                 ('Human answering service', 'Varies widely by provider and volume.', 'A person answers, takes messages and sometimes books. May have limited hours or per-minute pricing.', 'Sensitive calls that need human judgment.'),
                 ('AI receptionist (Contesta)', 'From $197 a month with 150 minutes.', 'Answers instantly, 24/7, in Spanish or English; books in Google Calendar and emails you the summary. Only knows what you teach her.', 'Appointment businesses that miss calls while working or after hours.')])
        head_cells = ['Opción', 'Costo', 'Qué resuelve', 'Cuándo conviene'] if es else ['Option', 'Cost', 'What it solves', 'Best fit']
        tbl = '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head_cells) + '</tr></thead><tbody>' + \
              ''.join('<tr>' + ''.join(f'<td>{E(c)}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>'
        return page_head(lang, 'Guía' if es else 'Guide', 'Recepcionista con IA, buzón de voz o servicio de contestadora.' if es else 'AI receptionist, voicemail or answering service.',
                         ('Ninguna opción es la mejor para todos. Esta es una comparación honesta, incluido cuándo no le conviene Contesta.' if es else
                          'No option is best for everyone. Here\'s an honest comparison, including when Contesta isn\'t the right fit.')) + f'''
<section class="tight"><div class="wrap narrow article">
{tbl}
<h2>{"Cuándo no le conviene Contesta" if es else "When Contesta isn't the right fit"}</h2>
<ul><li>{"Si casi no recibe llamadas, el buzón probablemente le basta." if es else "If you barely get calls, voicemail is probably enough."}</li>
<li>{"Si sus llamadas necesitan criterio humano (quejas complejas, casos delicados), una persona es mejor." if es else "If your calls need human judgment (complex complaints, sensitive cases), a person is better."}</li>
<li>{"Si agenda en un sistema que no es Google Calendar, o necesita varias citas a la misma hora, hoy no encaja." if es else "If you book in a system other than Google Calendar, or need several appointments at the same time, it doesn't fit today."}</li></ul>
<h2>{"Cómo decidir" if es else "How to decide"}</h2>
<p>{"Cuente cuántas llamadas pierde en una semana normal y cuántas de esas eran para una cita. Si son varias, escuche la llamada de demo y pruebe la línea en vivo:" if es else "Count how many calls you miss in a normal week and how many of those were for an appointment. If it's several, listen to the demo call and try the live line:"} <a href="{TEL}">(813) 722-1120</a>.</p>
<p class="small muted">{"No publicamos precios de otros proveedores porque cambian seguido; consulte directamente con ellos." if es else "We don't list other providers' prices because they change often; check with them directly."}</p>
</div></section>
{cta_band(lang)}'''


    if key in ('privacy', 'terms'):
        return legal(key, lang)
    if key == 'signup':
        return f'''<section class="hero"><div class="wrap grid-2" style="align-items:start">
<div class="stack"><p class="eyebrow">{"Paso 1 de 3" if es else "Step 1 of 3"}</p><h1 style="font-size:clamp(2rem,4.5vw,3rem)">{"Cree su cuenta." if es else "Create your account."}</h1>
<p class="lede">{"Solo pedimos lo necesario para crear la cuenta. Lo demás lo configura después, a su ritmo, y se guarda en cada paso." if es else "We only ask for what's needed to create the account. You set up the rest later, at your own pace, and it saves at every step."}</p>
<div class="card"><div id="app" data-page="signup"><noscript>{"Necesita JavaScript para crear la cuenta. También puede escribirnos a hola@usecontesta.com." if es else "JavaScript is needed to create the account. You can also email hola@usecontesta.com."}</noscript></div>
<p class="small muted" style="margin-top:14px">{"Usamos su correo para enviarle el enlace de su cuenta y los resúmenes de llamadas. Al crear su cuenta acepta los" if es else "We use your email to send your account link and call summaries. By creating an account you accept the"} <a href="{u('terms', lang)}">{"Términos" if es else "Terms"}</a> {"y la" if es else "and the"} <a href="{u('privacy', lang)}">{"Política de privacidad" if es else "Privacy policy"}</a>.</p></div>
<p class="small muted">{"¿Ya tiene cuenta?" if es else "Already have an account?"} <a href="{u('account', lang)}">{"Entrar" if es else "Sign in"}</a></p>
</div>
<div class="card sage stack"><h2 style="font-size:1.2rem">{"Qué pasa después" if es else "What happens next"}</h2>
<ol><li>{"Configura su negocio: servicios, horario, respuestas." if es else "Set up your business: services, hours, answers."}</li>
<li>{"Conecta Google Calendar y registra su tarjeta para empezar la prueba de 14 días (no se cobra durante la prueba)." if es else "Connect Google Calendar and add your card to start the 14-day trial (nothing is charged during the trial)."}</li>
<li>{"Prueba su número desde su celular y activa el desvío." if es else "Test your number from your cell and turn on forwarding."}</li></ol>
{cta_note(lang)}
<p class="small muted">{"¿Quiere escucharla antes?" if es else "Want to hear her first?"} <a href="{u('demo', lang)}">{"Escuche a Sofía" if es else "Hear Sofía"}</a></p></div>
</div></section>'''

    if key == 'account':
        return f'''<section class="hero"><div class="wrap narrow stack">
<h1 style="font-size:clamp(1.8rem,4vw,2.6rem)">{"Su cuenta" if es else "Your account"}</h1>
<div id="app" data-page="account"><noscript>{"Necesita JavaScript para ver su cuenta." if es else "JavaScript is needed to view your account."}</noscript></div>
</div></section>'''
    raise KeyError(key)


def industry(lang, kind):
    es = lang == 'es'
    if kind == 'auto':
        title = 'Recepcionista para talleres mecánicos y detailing.' if es else 'A receptionist for auto repair and detailing shops.'
        lede = ('Usted está debajo del carro o con las manos llenas de grasa. Sofía contesta, agenda el servicio en su Google Calendar y le deja anotado año, marca y modelo.' if es else
                'You\'re under a car or covered in grease. Sofía answers, books the service in your Google Calendar and notes year, make and model.')
        does = (['Agenda cambios de aceite, diagnósticos, alineaciones o lavados con la duración de cada servicio.', 'Pregunta año, marca y modelo (o lo que usted ponga en "preguntas al agendar") y lo deja en la cita.',
                 'Da sus precios "desde" y su horario, y explica cómo llegar.', 'Si piden un presupuesto de una reparación, toma los datos para que usted llame: no inventa precios.',
                 'Fuera de horario, toma el mensaje o agenda en la próxima hora libre, como usted prefiera.'] if es else
                ['Books oil changes, diagnostics, alignments or washes with each service\'s length.', 'Asks year, make and model (or whatever you set as booking questions) and saves it in the appointment.',
                 'Gives your "from" prices and hours, and explains how to get there.', 'If someone wants a repair quote, she takes the details for you to call back: she doesn\'t invent prices.',
                 'After hours, she takes a message or books the next open time, as you prefer.'])
        limits = (['Una cita a la vez: si tiene varias bahías, Sofía no agenda dos carros a la misma hora en el mismo calendario.', 'No consulta inventario de piezas ni el estado de un carro en reparación.',
                   'No conecta con programas de gestión de taller; solo con Google Calendar.'] if es else
                  ['One appointment at a time: if you have several bays, Sofía won\'t book two cars at the same time on the same calendar.', 'She doesn\'t check parts inventory or the status of a car in the shop.',
                   'She doesn\'t connect to shop-management software; only Google Calendar.'])
        example = ('Ejemplo de configuración (ilustrativo)', 'Cambio de aceite — $45 — 30 min\nDiagnóstico — $80 — 60 min\nDetailing interior — desde $120 — 2 h\nPreguntas al agendar: año, marca y modelo del carro') if es else \
                  ('Example setup (illustrative)', 'Oil change — $45 — 30 min\nDiagnostics — $80 — 60 min\nInterior detail — from $120 — 2 h\nBooking questions: year, make and model of the car')
    else:
        title = 'Recepcionista para servicios de limpieza.' if es else 'A receptionist for cleaning services.'
        lede = ('Usted está limpiando una casa y el teléfono no para. Sofía contesta, pide la dirección, revisa que esté en su zona y agenda la limpieza o el estimado en su calendario.' if es else
                'You\'re cleaning a house and the phone won\'t stop. Sofía answers, asks for the address, checks it\'s in your area and books the cleaning or estimate in your calendar.')
        does = (['Pide la dirección del servicio (calle, ciudad y código postal) y la lee de vuelta.', 'Revisa que esté dentro de la zona que usted puso; si no, toma el mensaje en vez de agendar.',
                 'Hace sus preguntas antes de agendar, por ejemplo cuántos cuartos y baños o si hay mascotas, y deja las respuestas en la cita.', 'Agenda limpiezas o estimados en su Google Calendar con la duración de cada servicio.',
                 'Da sus precios "desde" y explica qué incluye cada servicio, según lo que usted escribió.'] if es else
                ['Asks for the service address (street, city and ZIP) and reads it back.', 'Checks it\'s inside the area you set; if not, she takes a message instead of booking.',
                 'Asks your questions before booking, for example how many bedrooms and bathrooms or whether there are pets, and saves the answers in the appointment.', 'Books cleanings or estimates in your Google Calendar with each service\'s length.',
                 'Gives your "from" prices and explains what each service includes, based on what you wrote.'])
        limits = (['Una cita a la vez en un solo calendario: si tiene varios equipos, Sofía no agenda dos limpiezas a la misma hora.', 'No calcula precios a la medida: da sus precios "desde" y toma los datos para su cotización.',
                   'No cobra depósitos.'] if es else
                  ['One appointment at a time on one calendar: if you have several crews, Sofía won\'t book two cleanings at the same time.', 'She doesn\'t calculate custom prices: she gives your "from" prices and takes the details for your quote.',
                   'She doesn\'t take deposits.'])
        example = ('Ejemplo de configuración (ilustrativo)', 'Limpieza estándar (1-2 cuartos) — $120 — 2 h\nLimpieza profunda — desde $220 — 4 h\nEstimado en casa — gratis — 30 min\nZona: Tampa, Brandon y Riverview\nPreguntas al agendar: cuartos, baños y mascotas') if es else \
                  ('Example setup (illustrative)', 'Standard clean (1-2 bedrooms) — $120 — 2 h\nDeep clean — from $220 — 4 h\nIn-home estimate — free — 30 min\nArea: Tampa, Brandon and Riverview\nBooking questions: bedrooms, bathrooms and pets')
    return page_head(lang, 'Para quién es' if es else 'Who it\'s for', title, E(lede)) + f'''
<section class="tight"><div class="wrap grid-2">
<div class="stack"><h2>{"Lo que hace por usted" if es else "What she does for you"}</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in does)}</ul></div>
<div class="card stack"><span class="label-chip">{E(example[0])}</span><p class="preview">{E(example[1])}</p>
<p class="small muted">{"Usted escribe esto en su cuenta, con sus precios reales. Sofía solo da lo que está ahí." if es else "You write this in your account, with your real prices. Sofía only quotes what's there."}</p></div>
</div></section>
<section class="tight"><div class="wrap narrow stack">
<div class="note warn stack"><h2 style="font-size:1.2rem">{"Antes de registrarse, sepa esto" if es else "Before you sign up, know this"}</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in limits)}</ul></div>
<h2>{"Escúchela" if es else "Hear her"}</h2>
<p class="muted">{"La llamada de demo es de una barbería de prueba, pero el flujo es el mismo: revisa el calendario, ofrece dos horas, confirma datos y agenda." if es else "The demo call is from a test barbershop, but the flow is the same: check the calendar, offer two times, confirm details, book."}</p>
{audio(lang)}
<p><a href="{u('calendar', lang)}">{"Cómo funcionan las citas en Google Calendar" if es else "How Google Calendar booking works"}</a> · <a href="{u('g_forward', lang)}">{"Cómo desviar sus llamadas" if es else "How to forward your calls"}</a></p>
</div></section>
{cta_band(lang)}'''


LEGAL_TEXT = {
    ('privacy', 'es'): ('Política de privacidad', [
        ('Quiénes somos', ['Contesta LLC, Tampa, Florida. Contacto: <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.']),
        ('Qué datos recogemos', ['<b>De los negocios que usan Contesta:</b> correo, nombre del negocio y plan; la configuración que nos dan (servicios y precios, horario, dirección o zona de servicio, nombre del dueño, celular, teléfono del negocio, número para transferir, correo del calendario); y la actividad de la cuenta (pasos completados, fechas).',
                                 '<b>De las personas que llaman a esos negocios:</b> número de teléfono, la grabación de la llamada, una transcripción automática, lo que le dicen a la asistente (nombre, número para devolver la llamada, datos de la cita y, si aplica, la dirección del servicio) y un resumen de la llamada.',
                                 '<b>De quienes visitan este sitio:</b> un registro propio de páginas vistas, idioma, plan elegido, la fuente general de la visita (por ejemplo, "Google" o "directo") y un identificador de sesión al azar. No usamos cookies, y ese registro no incluye nombres, correos ni teléfonos. Su navegador guarda su idioma, cómo llegó la primera vez y su sesión de la página de cuenta.']),
        ('Para qué los usamos', ['Para contestar y dirigir las llamadas de nuestros clientes, agendar citas en su calendario, enviar los resúmenes de llamadas, permitir que entren a su cuenta con un enlace por correo, dar soporte y medir en conjunto cómo funcionan el sitio y el registro.']),
        ('Acceso al calendario', ['Si un negocio activa las citas, comparte un Google Calendar con hola@usecontesta.com. Leemos los eventos de ese calendario para ver las horas ocupadas y creamos las citas en él. Si deja de compartirlo, el acceso termina.']),
        ('Proveedores que procesan datos por nosotros', ['Retell AI (números de teléfono, voz con IA, grabaciones y transcripciones); Google Workspace (correo, calendario, hojas de cálculo y la automatización que hace funcionar el servicio); ' + ('Stripe (pagos con tarjeta y suscripciones; Contesta no ve ni guarda el número completo de su tarjeta); ' if ACTIVATION_LIVE else '') + 'GitHub (alojamiento del sitio); Namecheap (dominio).']),
        ('Venta de datos', ['No vendemos información personal ni la compartimos para publicidad.']),
        ('Cuánto tiempo guardamos los datos', ['Grabaciones y transcripciones completas de llamadas: se borran a los 90 días.',
                                               'Datos de la cuenta, incluido el registro de llamadas (fecha, número, nombre, motivo y un resumen corto): se borran 12 meses después de cancelar.',
                                               'Registro de visitas al sitio: hasta 24 meses.',
                                               'Los resúmenes que enviamos por correo al dueño de un negocio quedan en el buzón de ese dueño, que los controla. La grabación de demostración de este sitio es de un cliente simulado y se conserva.']),
        ('Sus opciones', ['Los negocios pueden actualizar su configuración en su cuenta y pedirnos que borremos sus datos. Quien llamó a un negocio puede pedirle al negocio, o a nosotros en hola@usecontesta.com, que borre sus registros de llamada. Respondemos en un plazo de 30 días.']),
        ('Menores', ['El servicio es para negocios y no está dirigido a menores de 13 años.']),
        ('Cambios', ['Publicaremos los cambios en esta página con su fecha.']),
    ]),
    ('privacy', 'en'): ('Privacy policy', [
        ('Who we are', ['Contesta LLC, Tampa, Florida. Contact: <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.']),
        ('What we collect', ['<b>From businesses that use Contesta:</b> email, business name and plan; the setup they give us (services and prices, hours, address or service area, owner name, cell, business phone, transfer number, calendar email); and account activity (steps completed, dates).',
                             '<b>From people who call those businesses:</b> phone number, a recording of the call, an automatic transcript, what they tell the assistant (name, callback number, appointment details and, when relevant, the service address) and a call summary.',
                             '<b>From visitors to this site:</b> a first-party record of pages viewed, language, plan clicked, the general source of the visit (for example "Google" or "direct") and a random session ID. We use no cookies, and that record has no names, emails or phone numbers. Your browser stores your language choice, how you first arrived and your sign-in session for the account page.']),
        ('How we use it', ['To answer and route calls for our customers, book appointments in their calendar, send call summaries, let customers sign in with an emailed link, provide support, and measure in aggregate how the site and signup perform.']),
        ('Calendar access', ['If a business turns on booking, it shares one Google Calendar with hola@usecontesta.com. We read that calendar\'s events to find busy times and create appointments in it. Removing the share ends access.']),
        ('Service providers that process data for us', ['Retell AI (phone numbers, voice AI, call recordings and transcripts); Google Workspace (email, calendar, spreadsheets and the automation that runs the service); ' + ('Stripe (card payments and subscriptions; Contesta never sees or stores your full card number); ' if ACTIVATION_LIVE else '') + 'GitHub (website hosting); Namecheap (domain).']),
        ('Selling data', ['We do not sell personal information and do not share it for advertising.']),
        ('How long we keep data', ['Call recordings and full transcripts: deleted after 90 days.',
                                   'Account data, including the call log (date, number, name, reason and a short summary): deleted 12 months after cancellation.',
                                   'Website visit records: up to 24 months.',
                                   'Summaries we email to a business owner stay in that owner\'s inbox, which they control. The demo recording on this site is of a simulated caller and is kept.']),
        ('Your choices', ['Businesses can update their setup in their account and ask us to delete their data. Someone who called a business can ask that business, or us at hola@usecontesta.com, to delete their call records. We respond within 30 days.']),
        ('Children', ['The service is for businesses and isn\'t directed to children under 13.']),
        ('Changes', ['We\'ll post changes on this page with their date.']),
    ]),
    ('terms', 'es'): ('Términos del servicio', [
        ('El servicio', ['Contesta ofrece una recepcionista virtual con IA que contesta las llamadas desviadas de su negocio, responde con la información que usted aprueba, agenda citas en un Google Calendar que usted comparte, toma mensajes, puede transferir llamadas en los planes que lo incluyen y le envía por correo un resumen de cada llamada. La asistente siempre dice que es una asistente virtual y que la llamada puede ser grabada.']),
        ('Quién puede usarlo', ['Negocios ubicados en Florida, en hora del Este.']),
        ('Su cuenta', ['Entra a su cuenta con un enlace que le enviamos por correo. Cuide el acceso a ese correo.']),
        ('Planes, prueba y pago', ['Inicial $197, Pro $297 y Máximo $597 al mes, con 150, 400 y 1,000 minutos. Para empezar la prueba gratis de 14 días se pide una tarjeta; no se cobra nada durante la prueba y la mensualidad empieza al terminar, salvo que cancele antes. El plan se cobra mensualmente.',
                                   'Instalación: $297, pago único, sin costo para los primeros cinco negocios que empiecen su prueba. Se cobra junto con el primer pago mensual, al terminar la prueba; nunca durante la configuración, mientras espera la activación ni durante la prueba. Si cancela durante la prueba, no se cobra.']),
        ('Si se pasa de los minutos', ['Los minutos son el tiempo que la asistente está en llamadas, sumado por mes calendario (hora del Este). Si se pasa, Sofía sigue contestando. Le escribimos y le sugerimos un plan más grande; no cobramos nada extra sin su acuerdo.']),
        ('Cancelación', ['No hay contrato. Puede cancelar cuando quiera ' + ('desde su cuenta ("Administrar pago o cancelar") o ' if ACTIVATION_LIVE else '') + 'escribiendo a hola@usecontesta.com. Si cancela durante la prueba, no se cobra nada. Después, el servicio sigue hasta el final del mes pagado y no hay reembolsos por meses parciales. Para que las llamadas dejen de llegar a la asistente de inmediato, quite el desvío de llamadas en su teléfono.']),
        ('Sus responsabilidades', ['Dar información correcta de su negocio y mantenerla al día; usar el servicio de forma legal; cumplir las leyes que le apliquen sobre grabación y manejo de la información de quienes le llaman (la asistente avisa al inicio de cada llamada que puede ser grabada); no usar el servicio para emergencias; revisar los resúmenes y confirmar lo importante.']),
        ('Límites del servicio', ['La asistente puede entender mal a quien llama, sobre todo con mala conexión; no da consejos médicos, legales ni financieros; las citas dependen del acceso a su calendario; solo se conecta con Google Calendar. No garantizamos un número de citas ni de clientes.']),
        ('Disponibilidad', ['El servicio depende de proveedores externos (Retell AI, Google y las compañías telefónicas). Se ofrece "tal cual" y según disponibilidad, sin garantía de tiempo de funcionamiento, en la medida que la ley lo permita.']),
        ('Responsabilidad', ['En la medida que la ley lo permita, la responsabilidad total de Contesta por cualquier reclamo se limita a lo que usted pagó en los 3 meses anteriores al reclamo.']),
        ('Cambios de precio o de términos', ['Le avisaremos por correo al menos 30 días antes de que un cambio de precio entre en vigor. Otros cambios a estos términos se publican en esta página con su fecha.']),
        ('Ley aplicable y contacto', ['Florida. Contacto: <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.']),
    ]),
    ('terms', 'en'): ('Terms of service', [
        ('The service', ['Contesta provides an AI virtual receptionist that answers your business\'s forwarded calls, answers from the information you approve, books appointments in a Google Calendar you share, takes messages, can transfer calls on plans that include transfers and emails you a summary of each call. The assistant always says it is a virtual assistant and that the call may be recorded.']),
        ('Who can use it', ['Businesses located in Florida, on Eastern time.']),
        ('Your account', ['You sign in with a link we email you. Keep access to that email secure.']),
        ('Plans, trial and payment', ['Starter $197, Pro $297 and Max $597 per month, with 150, 400 and 1,000 minutes. A card is required to start the 14-day free trial; nothing is charged during the trial, and the monthly plan starts when it ends unless you cancel before. Plans are billed monthly.',
                                      'Setup: $297, one-time, waived for the first five businesses to start a trial. It is charged with the first monthly payment, when the trial ends; never during setup, while waiting for activation or during the trial. Cancel during the trial and it isn\'t charged.']),
        ('If you go over your minutes', ['Minutes are the time the assistant spends on calls, added up per calendar month (Eastern time). If you go over, Sofía keeps answering. We email you and suggest a bigger plan; nothing extra is charged unless you agree.']),
        ('Cancellation', ['No contract. Cancel any time ' + ('from your account ("Manage billing or cancel") or ' if ACTIVATION_LIVE else '') + 'by emailing hola@usecontesta.com. Cancel during the trial and nothing is charged. After that, service runs to the end of the paid month and partial months aren\'t refunded. To stop calls reaching the assistant right away, turn off call forwarding on your phone.']),
        ('Your responsibilities', ['Give accurate business information and keep it current; use the service lawfully; comply with the laws that apply to you on recording and handling your callers\' information (the assistant announces at the start of each call that it may be recorded); don\'t use the service for emergencies; review summaries and confirm anything important.']),
        ('Limits of the service', ['The assistant can misunderstand callers, especially on poor connections; it doesn\'t give medical, legal or financial advice; bookings depend on your calendar access; it connects only to Google Calendar. We don\'t guarantee any number of bookings or customers.']),
        ('Availability', ['The service relies on third-party providers (Retell AI, Google and phone carriers). It is provided "as is" and as available, with no uptime guarantee, to the extent the law allows.']),
        ('Liability', ['To the extent the law allows, Contesta\'s total liability for any claim is limited to the fees you paid in the 3 months before the claim.']),
        ('Changes to prices or terms', ['We\'ll email you at least 30 days before a price change takes effect. Other changes to these terms are posted on this page with their date.']),
        ('Governing law and contact', ['Florida. Contact: <a href="mailto:hola@usecontesta.com">hola@usecontesta.com</a>.']),
    ]),
}


def legal(key, lang):
    es = lang == 'es'
    title, sections = LEGAL_TEXT[(key, lang)]
    body = ''
    for h, paras in sections:
        if len(paras) > 1:
            body += f'<h2>{E(h)}</h2><ul>' + ''.join(f'<li>{p}</li>' for p in paras) + '</ul>'
        else:
            body += f'<h2>{E(h)}</h2><p>{paras[0]}</p>'
    other = 'terms' if key == 'privacy' else 'privacy'
    return f'''<section class="hero"><div class="wrap narrow stack"><!--CRUMBS-->
<h1>{E(title)}</h1><p class="muted">{"Vigente desde el 21 de octubre de 2026." if es else "Effective October 21, 2026."}</p></div></section>
<section class="tight"><div class="wrap narrow article">{body}
<p class="muted small">{"Vea también:" if es else "See also:"} <a href="{u(other, lang)}">{PAGES[other][lang]['crumb']}</a></p></div></section>'''
