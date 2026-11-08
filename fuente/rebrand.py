#!/usr/bin/env python3
"""Adapta las fuentes del control, panel MIDI y transiciones (copiadas del kit Abastible) al evento Espíritu Imperial.
Se ejecuta una vez sobre las copias; todas las fuentes adaptadas quedan en esta carpeta."""
import re

def R(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (a[:80], c)
    return s.replace(a, b)

GLOBAL = [('ABAS_', 'IMP_'), ('ABAS ', 'IMP '), ("'abas'", "'imp'"), ('"abas"', '"imp"'), ('abas-', 'imp-'), ('abastible.cl', 'imperial.cl'),
          ('ABASTIBLE', 'IMPERIAL'), ('Abastible', 'Imperial'), ('#Imperial', '#EspírituImperial')]
def glob(s):
    for a, b in GLOBAL:
        s = s.replace(a, b)
    return s

# ------------------------------------------------------------------ control_a.js
s = glob(open('control_a.js').read())
i = s.index('var DEMO=['); j = s.index('var S=ls(', i)
s = s[:i] + """var DEMO=[{t:'Maipú',o:'Nombre Apellido',c:'Vendedora especialista',e:'Santiago',h:'12',m:''},
 {t:'Viña del Mar',o:'Nombre Apellido',c:'Jefe de bodega',e:'Valparaíso',h:'8',m:''},
 {t:'Concepción',o:'Nombre Apellido',c:'Asesora de proyectos',e:'Biobío',h:'15',m:''},
 {t:'La Florida',o:'Nombre Apellido',c:'Cajero',e:'Santiago',h:'5',m:''},
 {t:'Temuco',o:'Nombre Apellido',c:'Vendedor de maderas',e:'Araucanía',h:'10',m:''},
 {t:'Antofagasta',o:'Nombre Apellido',c:'Jefa de tienda',e:'Antofagasta',h:'18',m:''}];
""" + s[j:]
s = R(s, "S.ev=S.ev||{nombre:'Nombre del evento',lema:'Energía que nos mueve',fecha:'FECHA DEL EVENTO',hora:'09:00',lugar:'LUGAR DEL EVENTO',dir:'DIRECCIÓN · CIUDAD',web:'imperial.cl',hashtag:'#EspírituImperial',kicker_ini:'TRANSMISIÓN EN VIVO'};",
      "S.ev=S.ev||{nombre:'Espíritu Imperial 2026',lema:'Reconocemos a quienes hacen grande cada sucursal',fecha:'Fecha del evento',hora:'19:00',lugar:'Lugar del evento',dir:'Dirección, ciudad',web:'imperial.cl',hashtag:'#EspírituImperial',kicker_ini:'Espíritu'};")
s = R(s, "S.tema=S.tema||{k:'AHORA',t:'',sub:true};", "S.tema=S.tema||{k:'Sucursal',t:'',sub:true};")
s = R(s, "S.msgz=S.msgz||{label:'PREGUNTAS',items:['Envía tus preguntas por el chat de la transmisión','Síguenos en imperial.cl'],every:10};",
      "S.msgz=S.msgz||{label:'Saludos',items:['Felicitaciones a todos los destacados de Espíritu Imperial','Envía tu saludo por el chat de la transmisión'],every:10};")
s = R(s, "list:['imperial.cl']};", "list:['#EspírituImperial','imperial.cl']};")
s = R(s, "S.pau=S.pau||{titulo:'VOLVEMOS EN UNOS MINUTOS',", "S.pau=S.pau||{titulo:'Volvemos en unos minutos',")
s = R(s, "S.fin=S.fin||{titulo:'GRACIAS POR ACOMPAÑARNOS'};S.ora=S.ora||{kicker:'A CONTINUACIÓN'};", "S.fin=S.fin||{titulo:'Gracias por acompañarnos'};S.ora=S.ora||{kicker:'Trabajador destacado'};")
s = R(s, "ev.hora_txt=ev.hora?'INICIO '+ev.hora+' HRS':'';", "ev.hora_txt=ev.hora?'Inicio '+ev.hora+' h':'';")
s = R(s, "ag:{items:S.ag,cur:S.cur,next:S.cur+1},", "ag:{items:S.ag.map(function(x){var y=Object.assign({},x);delete y.f;return y}),cur:S.cur,next:S.cur+1,reveal:S.opt.reveal!==false},")
s = R(s, "ora:Object.assign({kicker:S.ora.kicker,foto:S.ora.foto||''},it),", "ora:Object.assign({},it,{kicker:S.ora.kicker,foto:it.f||S.ora.foto||''}),")
s = s.replace("delete y.f;return y}),cur:S.cur", "delete y.f;return y}),cur:S.cur")
s = R(s, "tema:{kicker:U(S.tema.k)||'AHORA',titulo:tt,sub:S.tema.sub&&!T(S.tema.t)?(it.o||''):''},", "tema:{kicker:T(S.tema.k)||'Sucursal',titulo:tt,sub:S.tema.sub&&!T(S.tema.t)?(it.e||''):''},")
s = R(s, "msg:{label:U(S.msgz.label),", "msg:{label:T(S.msgz.label),")
s = R(s, "replay:{texto:U(S.rp)||'REPETICIÓN'},", "replay:{texto:T(S.rp)||'Repetición'},")
s = R(s, "$('air-blk').textContent='BLOQUE '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='BLOQUE '+(S.cur+1);$('m_t').textContent=(it.h?it.h+' · ':'')+(it.t||'—');",
      "$('air-blk').textContent='SUCURSAL '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='SUCURSAL '+(S.cur+1);$('m_t').textContent=(it.t||'—')+(it.o?' · '+it.o:'');")
s = R(s, "var COLS=['h','t','o','c','e'];", "var COLS=['t','o','c','e','h','m'];")
s = R(s, "COLS.map(function(k){return '<td'+(k==='h'?' style=\"width:74px\"':'')+'><input data-i=\"'+i+'\" data-k=\"'+k+'\" value=\"'+esc(f[k])+'\" placeholder=\"'+({h:'09:00',t:'Título',o:'Orador',c:'Cargo',e:'Empresa'})[k]+'\"></td>'}).join('')+",
      "COLS.map(function(k){return '<td'+(k==='h'?' style=\"width:64px\"':'')+'><input data-i=\"'+i+'\" data-k=\"'+k+'\" value=\"'+esc(f[k])+'\" placeholder=\"'+({t:'Sucursal',o:'Nombre del destacado',c:'Cargo',e:'Ciudad',h:'Años',m:'Motivo (opcional)'})[k]+'\"></td>'}).join('')+'<td><button data-foto=\"'+i+'\" class=\"'+(f.f?'on':'')+'\" title=\"Foto del destacado\">'+(f.f?'Foto ✓':'Foto')+'</button></td>'+")
s = R(s, "S.cur=i;S.ora.foto='';var it=curItem();", "S.cur=i;var it=curItem();")
s = R(s, "toast('Bloque '+(i+1)+': '+(it.t||''));", "toast('Sucursal '+(i+1)+': '+(it.t||''));")
s = R(s, "$('badd').onclick=function(){S.ag.push({h:'',t:'',o:'',c:'',e:''});save();renderAg()};", "$('badd').onclick=function(){S.ag.push({t:'',o:'',c:'',e:'',h:'',m:''});save();renderAg()};")
s = R(s, "toast('Programa de ejemplo cargado')", "toast('Sucursales de ejemplo cargadas')")
i = s.index(" S.ag=L.map(function(l){var p=l.split('|')"); j = s.index("toast(S.ag.length+' bloques cargados')};", i)
s = s[:i] + " S.ag=L.map(function(l){var p=l.split('|').map(function(x){return x.trim()});return{t:p[0]||'',o:p[1]||'',c:p[2]||'',e:p[3]||'',h:(p[4]||'').replace(/\\s*años?$/i,''),m:p[5]||''}});\n S.cur=0;save();renderAg();push();" + s[j:]
s = R(s, "toast(S.ag.length+' bloques cargados')};", "toast(S.ag.length+' sucursales cargadas')};")
s = R(s, "function ltPerson(p){if(!p||!T(p.o||p.n))return toast('Ese bloque no tiene orador');ltShow({nombre:T(p.o||p.n),cargo:T(p.c),empresa:T(p.e)})}",
      "function ltPerson(p){if(!p||!T(p.o||p.n))return toast('Esa sucursal no tiene destacado');ltShow({nombre:T(p.o||p.n),cargo:T(p.c),empresa:T(p.n?p.e:p.t)})}")
s = R(s, "var n=T(it.o);if(!n||/^panelistas|^invitad/i.test(n))return;var k=n+'|'+T(it.c);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.e),src:'ag',i:i})",
      "var n=T(it.o);if(!n)return;var k=n+'|'+T(it.c)+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.t),src:'ag',i:i})")
# foto por destacado (se guarda reducida en el control; a los gráficos solo viaja la del destacado al aire)
s = R(s, "$('fl').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;\n if(b.dataset.load!=null)loadBlock(+b.dataset.load);",
      "var FOTOI=-1;$('ag_foto').onchange=function(){var f=this.files[0];if(!f||FOTOI<0)return;var i=FOTOI,r=new FileReader();r.onload=function(){var im=new Image();im.onload=function(){var c=document.createElement('canvas'),k=Math.min(1,900/Math.max(im.width,im.height));c.width=Math.round(im.width*k);c.height=Math.round(im.height*k);c.getContext('2d').drawImage(im,0,0,c.width,c.height);S.ag[i].f=c.toDataURL('image/jpeg',.82);save();renderAg();push();toast('Foto cargada: '+(S.ag[i].o||S.ag[i].t||''))};im.src=r.result};r.readAsDataURL(f);this.value=''};\n"
      "$('fl').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;\n if(b.dataset.foto!=null){var i=+b.dataset.foto;if(S.ag[i].f&&e.shiftKey){delete S.ag[i].f;save();renderAg();push();return toast('Foto quitada')}FOTOI=i;$('ag_foto').click();return}\n if(b.dataset.load!=null)loadBlock(+b.dataset.load);")
s = R(s, "$('autolt').checked=!!S.opt.autolt;$('autotema').checked=S.opt.autotema!==false;\n$('autolt').onchange=$('autotema').onchange=function(){S.opt={autolt:$('autolt').checked,autotema:$('autotema').checked};save()};",
      "$('autolt').checked=!!S.opt.autolt;$('autotema').checked=S.opt.autotema!==false;$('reveal').checked=S.opt.reveal!==false;\n$('autolt').onchange=$('autotema').onchange=$('reveal').onchange=function(){S.opt={autolt:$('autolt').checked,autotema:$('autotema').checked,reveal:$('reveal').checked};save();push()};")
open('control_a.js', 'w').write(s)

# ------------------------------------------------------------------ control_head.html
h = glob(open('control_head.html').read())
h = R(h, ":root{--or:#FE5000;--or2:#FF7A33;--az:#001489;--az2:#003594;--ink:#F3F5FB;--mute:#9AA3C7;--line:rgba(255,255,255,.12);--card:#0B1442;--bg:#050A2C;",
      ":root{--or:#E0283C;--or2:#FF464B;--az:#063661;--az2:#163B66;--ink:#F2F5FA;--mute:#A3B4CB;--line:rgba(255,255,255,.12);--card:#0B2747;--bg:#041A33;")
h = h.replace('font-family:"Ubuntu Sans"', 'font-family:"Roboto"').replace('"Titillium Web"', '"Roboto Condensed"')
h = R(h, '<h2>Programa del evento <span class="sp"><span class="onair v" id="air-blk">BLOQUE 1</span>', '<h2>Sucursales y destacados <span class="sp"><span class="onair v" id="air-blk">SUCURSAL 1</span>')
h = h.replace('<th>#</th><th>HORA</th><th>CHARLA / BLOQUE</th><th>ORADOR</th><th>CARGO</th><th>EMPRESA</th><th></th>', '<th>#</th><th>Sucursal</th><th>Destacado</th><th>Cargo</th><th>Ciudad</th><th>Años</th><th>Motivo</th><th>Foto</th><th></th>')
h = R(h, '<p class="hint" style="margin:6px 0">Formato: <kbd>09:30 | Título de la charla | Orador | Cargo | Empresa</kbd> (orador, cargo y empresa son opcionales)</p>',
      '<p class="hint" style="margin:6px 0">Formato: <kbd>Sucursal | Nombre | Cargo | Ciudad | Años | Motivo</kbd> (ciudad, años y motivo son opcionales). La foto se carga con el botón Foto de cada fila; Shift + clic la quita.</p>')
h = R(h, 'placeholder="10:00 | Resultados 2026 | Nombre Apellido | Gerente Comercial | Imperial"', 'placeholder="Maipú | Nombre Apellido | Vendedora especialista | Santiago | 12 | Su conocimiento de terminaciones ayuda a cada cliente"')
h = R(h, 'Orador del bloque actual', 'Destacado de la sucursal actual')
h = R(h, '<h2>Tema en pantalla ', '<h2>Sucursal en pantalla ')
h = R(h, '<label>Etiqueta pantalla orador</label><input id="or_k" value="A CONTINUACIÓN">', '<label>Etiqueta pantalla destacado</label><input id="or_k" value="Trabajador destacado">')
h = R(h, '<label>Foto del orador actual (opcional)</label>', '<label>Foto temporal del destacado al aire (si su fila no tiene)</label>')
h = R(h, '<label class="sw" style="flex:2"><input type="checkbox" id="autolt"> Al pasar de bloque, mostrar el lower third del orador</label>',
      '<label class="sw" style="flex:2"><input type="checkbox" id="autolt"> Al pasar de sucursal, mostrar el lower third del destacado</label><label class="sw" style="flex:2"><input type="checkbox" id="reveal" checked> En el tablero, ocultar los nombres de las sucursales que vienen</label><input type="file" id="ag_foto" accept="image/*" hidden>')
h = R(h, 'Al pasar de bloque, actualizar el tema en pantalla', 'Al pasar de sucursal, actualizar la sucursal en pantalla')
open('control_head.html', 'w').write(h)

# ------------------------------------------------------------------ make_control.py
m = glob(open('make_control.py').read())
i = m.index("INST = R(INST, INST[INST.index('var PLAN=['):INST.index('function li(')], \"\"\"var PLAN=["); j = m.index('""")', i) + 4
m = m[:i] + '''INST = R(INST, INST[INST.index('var PLAN=['):INST.index('function li(')], """var PLAN=[
 {scene:'INICIO',src:[['IMP Inicio','IMP_Inicio']]},
 {scene:'ESTUDIO',src:[['IMP Sucursal en pantalla','IMP_Overlay_Tema'],['IMP Lower Third','IMP_Overlay_LowerThird'],['IMP Mensaje','IMP_Overlay_Mensaje'],['IMP Mosca','IMP_Overlay_Mosca']]},
 {scene:'SUCURSAL',src:[['IMP Sucursal','IMP_Sucursal']]},
 {scene:'DESTACADO',src:[['IMP Destacado','IMP_Destacado']]},
 {scene:'DESTACADOS',src:[['IMP Destacados','IMP_Destacados']]},
 {scene:'PAUSA',src:[['IMP Pausa','IMP_Pausa']]},
 {scene:'REPLAY',src:[['IMP Repeticion','IMP_Overlay_Replay'],['IMP Mosca','IMP_Overlay_Mosca']]},
 {scene:'FINAL',src:[['IMP Final','IMP_Final']]}];
""")''' + m[j:]
m = m.replace("var need=['IMP_Inicio','IMP_Orador','IMP_Agenda','IMP_Pausa','IMP_Final','IMP_Overlay_LowerThird','IMP_Overlay_Mosca','IMP_Overlay_Tema','IMP_Overlay_Mensaje','IMP_Overlay_Replay'];",
              "var need=['IMP_Inicio','IMP_Sucursal','IMP_Destacado','IMP_Destacados','IMP_Pausa','IMP_Final','IMP_Overlay_LowerThird','IMP_Overlay_Mosca','IMP_Overlay_Tema','IMP_Overlay_Mensaje','IMP_Overlay_Replay'];")
m = m.replace("\"var M=[[/ola/,'Ola'],[/burbuja|circ/,'Burbuja'],[/c[aá]psula/,'Capsulas'],[/llama/,'Llama'],[/anillo/,'Anillos'],[/mosaico/,'Mosaico']];",
              "\"var M=[[/tel[oó]n/,'Telon'],[/destello|luz/,'Destello'],[/franja/,'Franjas'],[/marco/,'Marco']];")
m = m.replace("Ponle Ola, Burbuja, Cápsulas, Llama, Anillos o Mosaico en el nombre.", "Ponle Telon, Destello, Franjas o Marco en el nombre.")
m = m.replace("nómbrala <b>IMP Ola</b> (repite para <b>IMP Burbuja</b>, <b>IMP Ola Corta</b> y <b>IMP Burbuja Corta</b>)", "nómbrala <b>IMP Telon</b> (repite para <b>IMP Destello</b>, <b>IMP Franjas</b>, <b>IMP Marco</b> o su versión <b>Corta</b>)")
m = m.replace("\"return ('IMP B'+n+' '+(it.t||'').slice(0,40))\"", "\"return ('IMP S'+n+' '+(it.t||'').slice(0,40))\"")
m = m.replace("return ('IMP B'+n+' '+(it.t||'').slice(0,40))", "return ('IMP S'+n+' '+(it.t||'').slice(0,40))")
m = m.replace("<b>BLOQUE '+g.num+(cur?' · AL AIRE':'')+'</b>", "<b>SUCURSAL '+g.num+(cur?' · AL AIRE':'')+'</b>")
m = m.replace("' bloques)':''", "' sucursales)':''")
open('make_control.py', 'w').write(m)

# ------------------------------------------------------------------ hst.js (transiciones HTML)
t = glob(open('hst.js').read())
t = R(t, "var HST_D=[['ola','Ola'],['burbuja','Burbuja'],['capsulas','Cápsulas'],['llama','Llama'],['anillos','Anillos'],['mosaico','Mosaico']];",
      "var HST_D=[['telon','Telón'],['destello','Destello'],['franjas','Franjas'],['marco','Marco']];")
t = R(t, "S.hst=Object.assign({d:'ola',", "S.hst=Object.assign({d:'telon',")
t = R(t, "STG={last:{id:0,d:'ola',", "STG={last:{id:0,d:'telon',")
t = t.replace(".replace('á','a')", ".replace('ó','o')")
open('hst.js', 'w').write(t)
print('ok')
