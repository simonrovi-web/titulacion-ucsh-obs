#!/usr/bin/env python3
"""Adapta las fuentes del kit Espíritu Imperial a la Ceremonia de Titulación UCSH (una vez, sobre las copias).
Modelo de datos: un ítem por titulado → t = carrera, o = nombre, c = distinción (opcional)."""
import re
def R(s, a, b, n=1):
    c = s.count(a); assert c == n, (a[:90], c); return s.replace(a, b)
GLOBAL = [('Espíritu Imperial', 'Titulación UCSH'), ('#EspírituImperial', '#TitulaciónUCSH'), ('IMP_', 'UCSH_'), ('IMP ', 'UCSH '), ("'imp'", "'ucsh'"), ('"imp"', '"ucsh"'),
          ('imp-', 'ucsh-'), ('imperial.cl', 'ucsh.cl'), ('IMPERIAL', 'UCSH'), ('Imperial', 'UCSH')]
def glob(s):
    for a, b in GLOBAL: s = s.replace(a, b)
    return s

# ------------------------------------------------------------------ control_a.js
s = glob(open('control_a.js').read())
i = s.index('var DEMO=['); j = s.index('var S=ls(', i)
s = s[:i] + """var DEMO=[{t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:''},
 {t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:'Distinción máxima'},
 {t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:''},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:''},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:'Mejor promedio de la carrera'},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:''}];
""" + s[j:]
s = R(s, "S.ev=S.ev||{nombre:'Titulación UCSH 2026',lema:'Reconocemos a quienes hacen grande cada sucursal',fecha:'Fecha del evento',hora:'19:00',lugar:'Lugar del evento',dir:'Dirección, ciudad',web:'ucsh.cl',hashtag:'#TitulaciónUCSH',kicker_ini:'Espíritu'};",
      "S.ev=S.ev||{nombre:'Ceremonia de Titulación 2026',lema:'Universidad Católica Silva Henríquez',fecha:'Fecha de la ceremonia',hora:'19:00',lugar:'Lugar de la ceremonia',dir:'Dirección, Santiago',web:'ucsh.cl',hashtag:'#TitulaciónUCSH',kicker_ini:'Ceremonia de'};")
s = R(s, "S.tema=S.tema||{k:'Sucursal',t:'',sub:true};", "S.tema=S.tema||{k:'Carrera',t:'',sub:false};")
s = R(s, "S.msgz=S.msgz||{label:'Saludos',items:['Felicitaciones a todos los destacados de Titulación UCSH','Envía tu saludo por el chat de la transmisión'],every:10};",
      "S.msgz=S.msgz||{label:'Felicitaciones',items:['Felicitaciones a todas y todos los titulados de la UCSH','Envía tu saludo por el chat de la transmisión'],every:10};")
s = R(s, "S.ora=S.ora||{kicker:'Trabajador destacado'};", "S.ora=S.ora||{kicker:'Titulado'};")
s = R(s, "S.opt=S.opt||{autolt:false,autotema:true};", "S.opt=S.opt||{autolt:true,autotema:true};")
s = R(s, "tema:{kicker:T(S.tema.k)||'Sucursal',titulo:tt,sub:S.tema.sub&&!T(S.tema.t)?(it.e||''):''},", "tema:{kicker:T(S.tema.k)||'Carrera',titulo:tt,sub:''},")
s = R(s, "$('air-blk').textContent='SUCURSAL '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='SUCURSAL '+(S.cur+1);$('m_t').textContent=(it.t||'—')+(it.o?' · '+it.o:'');",
      "$('air-blk').textContent='TITULADO '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='TITULADO '+(S.cur+1);$('m_t').textContent=(it.o||'—')+(it.t?' · '+it.t:'');")
s = R(s, "var COLS=['t','o','c','e','h','m'];", "var COLS=['t','o','c'];")
s = R(s, "COLS.map(function(k){return '<td'+(k==='h'?' style=\"width:64px\"':'')+'><input data-i=\"'+i+'\" data-k=\"'+k+'\" value=\"'+esc(f[k])+'\" placeholder=\"'+({t:'Sucursal',o:'Nombre del destacado',c:'Cargo',e:'Ciudad',h:'Años',m:'Motivo (opcional)'})[k]+'\"></td>'}).join('')+'<td><button data-foto=\"'+i+'\" class=\"'+(f.f?'on':'')+'\" title=\"Foto del destacado\">'+(f.f?'Foto ✓':'Foto')+'</button></td>'+",
      "COLS.map(function(k){return '<td><input data-i=\"'+i+'\" data-k=\"'+k+'\" value=\"'+esc(f[k])+'\" placeholder=\"'+({t:'Carrera',o:'Nombre del titulado',c:'Distinción (opcional)'})[k]+'\"></td>'}).join('')+")
s = R(s, "toast('Sucursal '+(i+1)+': '+(it.t||''));", "toast('Titulado '+(i+1)+': '+(it.o||''));")
s = R(s, "$('badd').onclick=function(){S.ag.push({t:'',o:'',c:'',e:'',h:'',m:''});save();renderAg()};",
      "$('badd').onclick=function(){var l=S.ag[S.ag.length-1];S.ag.push({t:l?l.t:'',o:'',c:''});save();renderAg()};")
s = R(s, "toast('Sucursales de ejemplo cargadas')", "toast('Lista de ejemplo cargada')")
s = R(s, "S.ag=L.map(function(l){var p=l.split('|').map(function(x){return x.trim()});return{t:p[0]||'',o:p[1]||'',c:p[2]||'',e:p[3]||'',h:(p[4]||'').replace(/\\s*años?$/i,''),m:p[5]||''}});",
      "var CA='';S.ag=L.map(function(l){var p=l.split(/\\t|\\|/).map(function(x){return x.trim()});if(p.length===1){p=[CA,p[0],'']}if(p[0])CA=p[0];return{t:p[0]||CA,o:p[1]||'',c:p[2]||''}}).filter(function(x){return x.o});")
s = R(s, "toast(S.ag.length+' sucursales cargadas')};", "toast(S.ag.length+' titulados cargados en '+carreras().length+' carreras')};")
s = R(s, "function ltPerson(p){if(!p||!T(p.o||p.n))return toast('Esa sucursal no tiene destacado');ltShow({nombre:T(p.o||p.n),cargo:T(p.c),empresa:T(p.n?p.e:p.t)})}",
      "function carreras(){var o=[];S.ag.forEach(function(x){if(o.indexOf(x.t)<0)o.push(x.t)});return o}\n"
      "function ltPerson(p){if(!p||!T(p.o||p.n))return toast('Esa fila no tiene nombre');ltShow(p.n?{nombre:T(p.n),cargo:T(p.e),empresa:T(p.c)}:{nombre:T(p.o),cargo:T(p.t),empresa:T(p.c)})}")
s = R(s, "var n=T(it.o);if(!n)return;var k=n+'|'+T(it.c)+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.t),src:'ag',i:i})",
      "var n=T(it.o);if(!n)return;var k=n+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.t),src:'ag',i:i})")
s = R(s, "$('autolt').checked=!!S.opt.autolt;", "$('autolt').checked=S.opt.autolt!==false;")
open('control_a.js', 'w').write(s)
left = re.findall(r'.{30}(?:[Ss]ucursal|estacad|Cargo|Años|Motivo).{30}', s)
print('control_a restos', len(left)); [print('  ', x) for x in left[:12]]

# ------------------------------------------------------------------ control_head.html
h = glob(open('control_head.html').read())
h = R(h, ":root{--or:#C8102E;--or2:#FF464B;--az:#063661;--az2:#163B66;", ":root{--or:#F0B808;--or2:#FFD24D;--az:#004577;--az2:#0A5A92;")
h = h.replace('font-family:"Roboto"', 'font-family:"Ubuntu"').replace('"Roboto Condensed"', '"Ubuntu"')
h = R(h, 'button.pri:hover{background:#A50D25;border-color:#A50D25}', 'button.pri:hover{background:#D9A400;border-color:#D9A400}')
h = h.replace('/* UCSH: la tabla de sucursales necesita más ancho que el programa original */', '/* UCSH: la tabla de titulados necesita más ancho que el programa original */')
h = R(h, '<h2>Sucursales y destacados <span class="sp"><span class="onair v" id="air-blk">SUCURSAL 1</span>', '<h2>Titulados por carrera <span class="sp"><span class="onair v" id="air-blk">TITULADO 1</span>')
h = R(h, '<th>#</th><th>Sucursal</th><th>Destacado</th><th>Cargo</th><th>Ciudad</th><th>Años</th><th>Motivo</th><th>Foto</th><th></th>', '<th>#</th><th>Carrera</th><th>Titulado</th><th>Distinción</th><th></th>')
h = R(h, '> Al pasar de sucursal, mostrar el lower third del destacado</label>', '> Al pasar al siguiente titulado, mostrar su lower third</label>')
h = re.sub(r'<label class="sw" style="flex:2"><input type="checkbox" id="reveal" checked>[^<]*</label>', '<input type="checkbox" id="reveal" hidden>', h)
assert 'id="reveal"' in h
h = R(h, '> Al pasar de sucursal, actualizar la sucursal en pantalla</label>', '> Al cambiar de carrera, actualizar la carrera en pantalla</label>')
h = R(h, '<summary>Pegar todas las sucursales (una por línea)</summary>', '<summary>Pegar la lista de titulados (uno por línea, desde Excel o texto)</summary>')
i = h.index('<p class="hint" style="margin:6px 0">Formato: <kbd>Sucursal'); j = h.index('</p>', i) + 4
h = h[:i] + '<p class="hint" style="margin:6px 0">Formato: <kbd>Carrera | Nombre completo | Distinción</kbd>. La distinción es opcional. También sirve copiar tres columnas desde Excel, o escribir el nombre de la carrera en una línea y los titulados debajo, uno por línea.</p>' + h[j:]
h = re.sub(r'placeholder="Maipú \| Nombre Apellido[^"]*"', 'placeholder="Trabajo Social | Nombre Apellido Apellido | Distinción máxima"', h)
h = R(h, '>Cargar sucursales</button>', '>Cargar titulados</button>')
h = R(h, '>↺ Sucursales de ejemplo</button>', '>↺ Lista de ejemplo</button>')
h = R(h, 'Destacado de la sucursal actual', 'Titulado actual')
h = R(h, '<input id="lt_emp" placeholder="Sucursal">', '<input id="lt_emp" placeholder="Distinción (opcional)">')
h = R(h, '<h2>Sucursal en pantalla ', '<h2>Carrera en pantalla ')
h = h.replace('Etiqueta arriba a la izquierda con la sucursal que se está premiando. Se actualiza sola al pasar de sucur', 'Etiqueta arriba a la izquierda con la carrera que se está titulando. Se actualiza sola al cambiar de carr')
h = h.replace('Texto (vacío = sucursal actual)', 'Texto (vacío = carrera actual)').replace('placeholder="Sucursal actua', 'placeholder="Carrera actua')
h = R(h, '<label>Etiqueta pantalla destacado</label><input id="or_k" value="Trabajador destacado">', '<label>Etiqueta (uso interno)</label><input id="or_k" value="Titulado">')
h = R(h, 'Momentos por sucursal', 'Momentos por titulado')
h = R(h, 'con el nombre de la sucursal (UCSH S03 …)', 'con el número del titulado (UCSH T003 …)')
h = R(h, '▶ Resumen de la sucursal', '▶ Resumen del titulado')
h = R(h, '🗑 Borrar otras sucursales', '🗑 Borrar otros titulados')
h = h.replace('<b>UCSH Telon</b>, <b>UCSH Destello</b>, <b>UCSH Franjas</b> o <b>UCSH', '<b>UCSH Telon</b>, <b>UCSH Destello</b>, <b>UCSH Franjas</b> o <b>UCSH')
open('control_head.html', 'w').write(h)
left = re.findall(r'.{30}(?:[Ss]ucursal|estacad|Cargo|Años|Motivo|Roboto).{30}', h)
print('head restos', len(left)); [print('  ', x) for x in left[:14]]

# ------------------------------------------------------------------ make_control.py
m = glob(open('make_control.py').read())
i = m.index("{scene:'INICIO'"); j = m.index("{scene:'PIP_PRESENTACION'")
m = m[:i] + """{scene:'INICIO',src:[['UCSH Inicio','UCSH_Inicio']]},
 {scene:'ESTUDIO',src:[['UCSH Carrera en pantalla','UCSH_Overlay_Tema'],['UCSH Lower Third','UCSH_Overlay_LowerThird'],['UCSH Mensaje','UCSH_Overlay_Mensaje'],['UCSH Mosca','UCSH_Overlay_Mosca']]},
 {scene:'CARRERA',src:[['UCSH Carrera','UCSH_Carrera']]},
 {scene:'NOMINA',src:[['UCSH Nomina','UCSH_Nomina']]},
 {scene:'PAUSA',src:[['UCSH Pausa','UCSH_Pausa']]},
 {scene:'REPLAY',src:[['UCSH Repeticion','UCSH_Overlay_Replay'],['UCSH Mosca','UCSH_Overlay_Mosca']]},
 {scene:'FINAL',src:[['UCSH Final','UCSH_Final']]},
 """ + m[j:]
m = R(m, "var need=['UCSH_Inicio','UCSH_Sucursal','UCSH_Destacado','UCSH_Destacados','UCSH_Pausa','UCSH_Final',", "var need=['UCSH_Inicio','UCSH_Carrera','UCSH_Nomina','UCSH_Pausa','UCSH_Final',")
m = m.replace("return ('UCSH S'+n+' '+(it.t||'').slice(0,40))", "return ('UCSH T'+('0'+n).slice(-3)+' '+(it.o||'').slice(0,40))")
m = m.replace("<b>SUCURSAL '+g.num+(cur?' · AL AIRE':'')+'</b>", "<b>TITULADO '+g.num+(cur?' · AL AIRE':'')+'</b>")
m = m.replace("' sucursales)':''", "' titulados)':''")
m = m.replace("'/home/claude/pip_ctl.js').read()", "'/home/claude/pip_ctl.js').read()").replace(".replace('__P__', 'IMP')", ".replace('__P__', 'UCSH')")
open('make_control.py', 'w').write(m)
print('make_control', re.findall(r'SUCURSAL|DESTACADO|IMP\b', m))

# ------------------------------------------------------------------ hst.js
t = glob(open('hst.js').read())
open('hst.js', 'w').write(t)
print('ok')
