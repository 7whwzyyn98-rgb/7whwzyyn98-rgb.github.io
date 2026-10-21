#!/usr/bin/env python3
"""One-off image assets in the new palette: share images (es/en) and a 512px logo. Needs Pillow and the two fonts."""
import pathlib, sys
from PIL import Image, ImageDraw, ImageFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = pathlib.Path(sys.argv[1])
FOREST, LIME, CREAM, SAGE = (23, 61, 48), (217, 239, 139), (247, 245, 238), (233, 238, 226)
def F(kind, size, w):
    f = ImageFont.truetype(str(FONTS / ('Gabarito[wght].ttf' if kind == 'd' else 'HankenGrotesk[wght].ttf')), size)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
def phone(d, x, y, s, fill):
    # handset drawn from the same 24-unit path, approximated with a polygon via the SVG points
    pts = [(6.6,10.8),(13.2,17.4),(15.4,15.2),(16.4,14.95),(20,15.52),(21,16.52),(21,20),(20,21),(15,20),(10,18),(6,14),(3.5,9),(3,4),(4,3),(7.5,3),(8.5,4),(9.07,7.57),(8.82,8.57)]
    d.polygon([(x + px * s, y + py * s) for px, py in pts], fill=fill)
def logo(size):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=int(size * .28), fill=FOREST)
    phone(d, size * .19, size * .19, size * .82 / 32 * 1.0 * (32 / 24) * .75, LIME)
    return im
(ROOT / 'assets').mkdir(exist_ok=True)
logo(512).save(ROOT / 'assets' / 'logo-512.png')
for lang, l1, l2, sub, demo in [('es', 'Su recepcionista con IA,', 'en español e inglés.', 'Agenda en Google Calendar · Resumen por correo · Florida', 'Escuche a Sofía: (813) 722-1120'),
                                ('en', 'Your AI receptionist,', 'in English and Spanish.', 'Books in Google Calendar · Email summaries · Florida', 'Hear Sofía: (813) 722-1120')]:
    im = Image.new('RGB', (1200, 630), CREAM); d = ImageDraw.Draw(im)
    d.rounded_rectangle((72, 64, 72 + 64, 64 + 64), radius=18, fill=FOREST)
    phone(d, 72 + 12, 64 + 12, 1.75, LIME)
    d.text((156, 70), 'Contesta', font=F('d', 46, 'ExtraBold'), fill=FOREST)
    f = F('d', 78, 'ExtraBold')
    d.text((72, 200), l1, font=f, fill=FOREST)
    w = f.getlength(l2)
    d.rectangle((72, 300 + 52, 72 + w, 300 + 82), fill=LIME)
    d.text((72, 296), l2, font=f, fill=FOREST)
    d.text((72, 430), sub, font=F('b', 32, 'Medium'), fill=(88, 105, 96))
    pf = F('d', 40, 'Bold'); pw = pf.getlength(demo)
    d.rounded_rectangle((72, 500, 72 + pw + 60, 572), radius=36, fill=FOREST)
    d.text((102, 510), demo, font=pf, fill=CREAM)
    im.save(ROOT / 'assets' / f'og-{lang}.png', optimize=True)
print('ok')
