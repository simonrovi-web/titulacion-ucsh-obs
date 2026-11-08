#!/usr/bin/env python3
"""Arma el kit final en ../kit: control, panel MIDI, gráficos, transiciones y fuentes."""
import base64, os, shutil, glob
OUT = '/home/claude/ucsh/kit'
B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = 'node_modules/@fontsource/'
FONTS = ''.join('@font-face{font-family:"%s";font-weight:%d;src:url(data:font/woff2;base64,%s) format("woff2");}' % (f, w, B(F + p)) for f, p, w in [
    ('Ubuntu', 'ubuntu/files/ubuntu-latin-400-normal.woff2', 400),
    ('Ubuntu', 'ubuntu/files/ubuntu-latin-500-normal.woff2', 500),
    ('Ubuntu', 'ubuntu/files/ubuntu-latin-700-normal.woff2', 700)])
from PIL import Image
import io
_im = Image.open('../Logo_UCSH_blanco.png'); _im.thumbnail((400, 400)); _b = io.BytesIO(); _im.save(_b, 'PNG', optimize=True)
LOGO = 'data:image/png;base64,' + base64.b64encode(_b.getvalue()).decode()
for d in ['Paneles', 'fuente', 'Logos']:
    os.makedirs(OUT + '/' + d, exist_ok=True)
for src, dst in [('control_template.html', 'CONTROL_EN_VIVO.html'), ('midi_template.html', 'PANEL_MIDI.html')]:
    open(OUT + '/' + dst, 'w').write(open(src).read().replace('__FONTS__', FONTS).replace('__LOGO__', LOGO))
for f in glob.glob('out/UCSH_*.html'):
    shutil.copy(f, OUT + '/Paneles/')
shutil.copy('../Logo_UCSH_color.png', OUT + '/Logos/UCSH_logo_color.png')
shutil.copy('../Logo_UCSH_blanco.png', OUT + '/Logos/UCSH_logo_blanco_oro.png')
for f in ['build.py', 'build_stingers.py', 'rebrand.py', 'ucsh_rebrand.py', 'make_control.py', 'make_midi.py', 'control_head.html', 'control_a.js', 'hst.js', 'assemble.py']:
    shutil.copy(f, OUT + '/fuente/')
print('ok')
