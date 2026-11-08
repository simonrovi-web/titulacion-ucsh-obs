#!/usr/bin/env python3
"""PANEL_MIDI de la Titulación UCSH: parte del panel probado del kit Abastible y cambia canal, marca, escenas y acciones."""
import re
s = open('/home/claude/abastible/midi_template.html').read()
def R(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:70], c); s = s.replace(a, b)
for a, b in [('ABAS_', 'UCSH_'), ('ABAS ', 'UCSH '), ("'abas-cmd'", "'ucsh-cmd'"), ('abas-midi', 'ucsh-midi'), ('abastible.cl', 'ucsh.cl'), ('ABASTIBLE', 'UCSH'), ('Abastible', 'UCSH')]:
    s = s.replace(a, b)
R(':root{--red:#FE5000;--red2:#FF7A33;--ink:#F3F5FB;--mute:#9AA3C7;--line:rgba(255,255,255,.12);--card:#0B1442;--bg:#050A2C;',
  ':root{--red:#F0B808;--red2:#FFD24D;--ink:#F2F5FA;--mute:#A9BCD2;--line:rgba(255,255,255,.12);--card:#06335A;--bg:#012440;')
s = s.replace('"Ubuntu Sans"', '"Ubuntu"')
s = s.replace("['prev','◀ Bloque anterior'],['next','Bloque siguiente ▶']", "['prev','◀ Titulado anterior'],['next','Titulado siguiente ▶']")
s = s.replace("prev:'◀ BLOQUE',next:'BLOQUE ▶'", "prev:'◀ TITULADO',next:'TITULADO ▶'")
s = s.replace("['lt_cur','👤 Lower third del orador actual']", "['lt_cur','👤 Lower third del titulado actual']").replace("lt_cur:'👤 ORADOR'", "lt_cur:'👤 TITULADO'")
s = s.replace("['tgl_tema','Mostrar/ocultar tema']", "['tgl_tema','Mostrar/ocultar carrera en pantalla']").replace("tgl_tema:'TEMA'", "tgl_tema:'CARRERA'")
s = s.replace("['reel','▶ Resumen del bloque']", "['reel','▶ Resumen del titulado']")
i = s.index("['hst_go','🎬 Con la animación elegida']"); j = s.index("]]]", i)
s = s[:i] + "['hst_go','🎬 Con la animación elegida'],['hst_telon','Telón'],['hst_destello','Destello'],['hst_franjas','Franjas'],['hst_marco','Marco']]]" + s[j + 3:]
s = s.replace("hst_ola:'TRANSICIÓN HTML',hst_burbuja:'TRANSICIÓN HTML',hst_capsulas:'TRANSICIÓN HTML',hst_llama:'TRANSICIÓN HTML',hst_anillos:'TRANSICIÓN HTML',hst_mosaico:'TRANSICIÓN HTML'",
              "hst_telon:'TRANSICIÓN HTML',hst_destello:'TRANSICIÓN HTML',hst_franjas:'TRANSICIÓN HTML',hst_marco:'TRANSICIÓN HTML'")
s = s.replace("hst_ola:'🎬 OLA',hst_burbuja:'🎬 BURBUJA',hst_capsulas:'🎬 CÁPSULAS',hst_llama:'🎬 LLAMA',hst_anillos:'🎬 ANILLOS',hst_mosaico:'🎬 MOSAICO'",
              "hst_telon:'🎬 TELÓN',hst_destello:'🎬 DESTELLO',hst_franjas:'🎬 FRANJAS',hst_marco:'🎬 MARCO'")
s = s.replace("case 'hst_ola':case 'hst_burbuja':case 'hst_capsulas':case 'hst_llama':case 'hst_anillos':case 'hst_mosaico':", "case 'hst_telon':case 'hst_destello':case 'hst_franjas':case 'hst_marco':")
s = s.replace("'hst_go','hst_mosaico'],", "'hst_go','hst_telon'],")
R("var TRD=['UCSH Ola','UCSH Ola Corta','UCSH Burbuja','UCSH Burbuja Corta','UCSH Capsulas','UCSH Llama','UCSH Anillos','UCSH Mosaico','Corte','Desvanecer']",
  "var TRD=['UCSH Telon','UCSH Telon Corta','UCSH Destello','UCSH Destello Corta','UCSH Franjas','UCSH Marco','Corte','Desvanecer']")
s = s.replace("['INICIO','ESTUDIO','ORADOR','AGENDA','PAUSA','REPLAY','FINAL']", "['INICIO','ESTUDIO','CARRERA','NOMINA','PAUSA','REPLAY','FINAL','PIP_PRESENTACION','PIP_ESQUINA']")
left = re.findall(r'.{25}(?:ola\b|burbuja|mosaico|Orador|ORADOR|charla).{25}', s)
s = s.replace('button.pri{background:var(--red);border-color:var(--red);color:var(--bg)}','button.pri{background:var(--red);border-color:var(--red);color:var(--bg)}')
s = s.replace('.ab.sel{background:var(--red);border-color:#fff;color:var(--bg)}','.ab.sel{background:var(--red);border-color:#fff;color:var(--bg)}')
s = s.replace('</style>', 'button.pri:hover{background:#D9A400;border-color:#D9A400;color:var(--bg)}\n</style>', 1)
print('restos:', len(left)); [print('  ', x) for x in left[:8]]
open('midi_template.html', 'w').write(s)
