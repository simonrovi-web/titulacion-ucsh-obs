// ---------- utilidades ----------
function $(i){return document.getElementById(i)}
function toast(t){var e=$('toast');e.textContent=t;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(function(){e.classList.remove('on')},1900)}
function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v))}catch(e){return null}}
function U(s){return (s||'').toString().trim().toUpperCase()}
function T(s){return (s||'').toString().trim()}
function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;')}
function fmt(s){s=Math.max(0,Math.ceil(s));return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}
function wait(ms){return new Promise(function(r){setTimeout(r,ms)})}
__SHA__

// ---------- estado ----------
var DEMO=[{t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:''},
 {t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:'Distinción máxima'},
 {t:'Pedagogía en Historia y Geografía',o:'Nombre Apellido Apellido',c:''},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:''},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:'Mejor promedio de la carrera'},
 {t:'Trabajo Social',o:'Nombre Apellido Apellido',c:''}];
var S=ls('ucsh-ctl')||{};
S.ev=S.ev||{nombre:'Ceremonia de Titulación 2026',lema:'Universidad Católica Silva Henríquez',fecha:'Fecha de la ceremonia',hora:'19:00',lugar:'Lugar de la ceremonia',dir:'Dirección, Santiago',web:'ucsh.cl',hashtag:'#TitulaciónUCSH',kicker_ini:'Ceremonia de'};
S.ag=S.ag||JSON.parse(JSON.stringify(DEMO));S.cur=S.cur||0;
S.show=S.show||{lt:false,mosca:true,tema:false,msg:false};
S.ltp=S.ltp||[];S.ltAuto=S.ltAuto==null?8:S.ltAuto;
S.tema=S.tema||{k:'Carrera',t:'',sub:false};
S.msgz=S.msgz||{label:'Felicitaciones',items:['Felicitaciones a todas y todos los titulados de la UCSH','Envía tu saludo por el chat de la transmisión'],every:10};
S.mo=S.mo||{pos:'tr',scale:1,op:1,live:true,msgs:true,estado:'EN VIVO',list:['#TitulaciónUCSH','ucsh.cl']};
S.ini=S.ini||{mode:'hora',min:10,target:null};
S.pau=S.pau||{titulo:'Volvemos en unos minutos',sub:'',min:10,end:null,next:true};
S.fin=S.fin||{titulo:'Gracias por acompañarnos'};S.ora=S.ora||{kicker:'Titulado'};
S.opt=S.opt||{autolt:true,autotema:true};
function save(){ls('ucsh-ctl',S)}
function curItem(){return S.ag[S.cur]||{}}

// ---------- mensaje a los gráficos ----------
function iniTarget(){if(S.ini.mode==='none')return null;if(S.ini.mode==='min')return S.ini.target||null;
 var m=(S.ev.hora||'').match(/(\d{1,2})[:.](\d{2})/);if(!m)return null;var d=new Date();d.setHours(+m[1],+m[2],0,0);return d.getTime()}
function msg(){var it=curItem(),ev=Object.assign({},S.ev);ev.hora_txt=ev.hora?'Inicio '+ev.hora+' h':'';
 var tt=T(S.tema.t)||it.t||'';
 return{ts:Date.now(),ev:ev,
  ag:{items:S.ag.map(function(x){var y=Object.assign({},x);delete y.f;return y}),cur:S.cur,next:S.cur+1,reveal:S.opt.reveal!==false},
  ini:{target:iniTarget(),label:'COMENZAMOS EN'},
  pau:{titulo:S.pau.titulo,sub:S.pau.sub,end:S.pau.end,next:S.pau.next},
  fin:{titulo:S.fin.titulo,sub:S.ev.nombre},
  ora:Object.assign({},it,{kicker:S.ora.kicker,foto:it.f||S.ora.foto||''}),
  lt:S.lt||{},tema:{kicker:T(S.tema.k)||'Carrera',titulo:tt,sub:''},
  msg:{label:T(S.msgz.label),items:S.msgz.items,every:S.msgz.every},
  mosca:Object.assign({},S.mo,{estado:U(S.mo.estado)||'EN VIVO',avoid:S.show.msg?110:0}),
  replay:{texto:T(S.rp)||'Repetición'},
  show:{lt:!!S.show.lt,mosca:!!S.show.mosca,tema:!!S.show.tema,msg:!!S.show.msg}}}
var bc=null;try{bc=new BroadcastChannel('ucsh')}catch(e){}
function push(){var m=msg();
 try{localStorage.setItem('ucsh-live',JSON.stringify(m))}catch(e){}
 if(bc)try{bc.postMessage(m)}catch(e){}
 if(WS.ok)req('CallVendorRequest',{vendorName:'obs-browser',requestType:'emit_event',requestData:{event_name:'ucsh',event_data:m}});
 renderAir()}
setInterval(push,5000);

__WS__

// ---------- en pantalla ----------
function air(id,on,t1,t0){var e=$(id);e.textContent=on?t1:t0;e.className='onair'+(on?' v':'')}
function renderAir(){air('air-lt',S.show.lt,'EN PANTALLA','OCULTO');air('air-tema',S.show.tema,'EN PANTALLA','OCULTO');air('air-msg',S.show.msg,'EN PANTALLA','OCULTO');air('air-mosca',S.show.mosca,'EN PANTALLA','OCULTA');
 var it=curItem();$('air-blk').textContent='TITULADO '+(S.cur+1)+' DE '+S.ag.length;$('m_n').textContent='TITULADO '+(S.cur+1);$('m_t').textContent=(it.o||'—')+(it.t?' · '+it.t:'');$('hev').textContent='· '+(S.ev.nombre||'Evento')}

// ---------- programa (agenda) ----------
var COLS=['t','o','c'];
function renderAg(){$('fl').innerHTML=S.ag.map(function(f,i){return '<tr class="'+(i===S.cur?'cur':'')+'"><td class="n">'+(i+1)+'</td>'+
 COLS.map(function(k){return '<td><input data-i="'+i+'" data-k="'+k+'" value="'+esc(f[k])+'" placeholder="'+({t:'Carrera',o:'Nombre del titulado',c:'Distinción (opcional)'})[k]+'"></td>'}).join('')+
 '<td style="white-space:nowrap"><button data-load="'+i+'" class="'+(i===S.cur?'on':'')+'">'+(i===S.cur?'Al aire':'Cargar')+'</button> <button data-lt="'+i+'" title="Mostrar su lower third"'+(f.o?'':' disabled')+'>LT</button> <button data-del="'+i+'" title="Quitar fila">✕</button></td></tr>'}).join('');renderPpl()}
$('fl').addEventListener('input',function(e){var t=e.target;if(t.dataset.i==null)return;S.ag[+t.dataset.i][t.dataset.k]=t.value;save();clearTimeout(window._agd);window._agd=setTimeout(function(){push();renderPpl()},300)});
var FOTOI=-1;$('ag_foto').onchange=function(){var f=this.files[0];if(!f||FOTOI<0)return;var i=FOTOI,r=new FileReader();r.onload=function(){var im=new Image();im.onload=function(){var c=document.createElement('canvas'),k=Math.min(1,900/Math.max(im.width,im.height));c.width=Math.round(im.width*k);c.height=Math.round(im.height*k);c.getContext('2d').drawImage(im,0,0,c.width,c.height);S.ag[i].f=c.toDataURL('image/jpeg',.82);save();renderAg();push();toast('Foto cargada: '+(S.ag[i].o||S.ag[i].t||''))};im.src=r.result};r.readAsDataURL(f);this.value=''};
$('fl').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 if(b.dataset.foto!=null){var i=+b.dataset.foto;if(S.ag[i].f&&e.shiftKey){delete S.ag[i].f;save();renderAg();push();return toast('Foto quitada')}FOTOI=i;$('ag_foto').click();return}
 if(b.dataset.load!=null)loadBlock(+b.dataset.load);
 else if(b.dataset.lt!=null)ltPerson(S.ag[+b.dataset.lt]);
 else if(b.dataset.del!=null){var i=+b.dataset.del;if(b.dataset.ok!=='1'){b.dataset.ok='1';b.textContent='¿Seguro?';setTimeout(function(){if(b.isConnected){b.dataset.ok='';b.textContent='✕'}},2200);return}
  S.ag.splice(i,1);if(S.cur>=S.ag.length)S.cur=Math.max(0,S.ag.length-1);save();renderAg();push()}});
function loadBlock(i){if(i<0||i>=S.ag.length)return;S.cur=i;var it=curItem();
 if(S.opt.autotema&&S.show.tema){/* el overlay de tema toma el título nuevo solo */}
 save();renderAg();push();toast('Titulado '+(i+1)+': '+(it.o||''));
 if(S.opt.autolt&&it.o)setTimeout(function(){ltPerson(it)},1200);
 if(window.renderHL)renderHL();if(window.applyPrefix)setTimeout(applyPrefix,400)}
$('bnext').onclick=$('m_next').onclick=function(){loadBlock(S.cur+1)};$('bprev').onclick=$('m_prev').onclick=function(){loadBlock(S.cur-1)};
$('badd').onclick=function(){var l=S.ag[S.ag.length-1];S.ag.push({t:l?l.t:'',o:'',c:''});save();renderAg()};
$('bdemo').onclick=function(){S.ag=JSON.parse(JSON.stringify(DEMO));S.cur=0;save();renderAg();push();toast('Lista de ejemplo cargada')};
$('bpaste').onclick=function(){var RAW=$('paste').value.split(/\n/).map(function(l){return l.trim()}),L=RAW.filter(Boolean);if(!L.length)return;
 var CA='',OUT=[],nb=true;RAW.forEach(function(l){if(!l){nb=true;return}var p=l.split(/\t|\|/).map(function(x){return x.trim()});if(p.length===1){var h=/:$/.test(p[0]);if(nb||h||!CA){CA=p[0].replace(/:$/,'').trim();nb=false;return}OUT.push({t:CA,o:p[0],c:''});return}nb=false;if(p[0])CA=p[0];OUT.push({t:p[0]||CA,o:p[1]||'',c:p[2]||''})});S.ag=OUT.filter(function(x){return x.o});
 S.cur=0;save();renderAg();push();toast(S.ag.length+' titulados cargados en '+carreras().length+' carreras')};
$('autolt').checked=S.opt.autolt!==false;$('autotema').checked=S.opt.autotema!==false;$('reveal').checked=S.opt.reveal!==false;
$('autolt').onchange=$('autotema').onchange=$('reveal').onchange=function(){S.opt={autolt:$('autolt').checked,autotema:$('autotema').checked,reveal:$('reveal').checked};save();push()};

// ---------- lower third ----------
var LTT=null;
function ltShow(o){o.t=Date.now();S.lt=o;S.show.lt=true;save();push();renderPpl();clearTimeout(LTT);var a=+S.ltAuto||0;if(a)LTT=setTimeout(function(){S.show.lt=false;save();push();renderPpl()},(a+1.6)*1000)}
function carreras(){var o=[];S.ag.forEach(function(x){if(o.indexOf(x.t)<0)o.push(x.t)});return o}
function ltPerson(p){if(!p||!T(p.o||p.n))return toast('Esa fila no tiene nombre');ltShow(p.n?{nombre:T(p.n),cargo:T(p.e),empresa:T(p.c)}:{nombre:T(p.o),cargo:T(p.t),empresa:T(p.c)})}
$('blt_cur').onclick=function(){ltPerson(curItem())};
$('blth').onclick=function(){clearTimeout(LTT);S.show.lt=false;save();push();renderPpl()};
$('blt').onclick=function(){var n=T($('lt_nombre').value);if(!n)return toast('Escribe un nombre');ltShow({nombre:n,cargo:T($('lt_cargo').value),empresa:T($('lt_emp').value)})};
$('bltsave').onclick=function(){var n=T($('lt_nombre').value);if(!n)return;S.ltp.push({n:n,c:T($('lt_cargo').value),e:T($('lt_emp').value)});save();renderPpl();toast('Guardado en la lista')};
$('lt_auto').value=String(S.ltAuto);$('lt_auto').onchange=function(){S.ltAuto=+this.value;save()};
function people(){var seen={},L=[];S.ag.forEach(function(it,i){var n=T(it.o);if(!n)return;var k=n+'|'+T(it.t);if(seen[k])return;seen[k]=1;L.push({n:n,c:T(it.c),e:T(it.t),src:'ag',i:i})});
 S.ltp.forEach(function(p,j){L.push({n:p.n,c:p.c,e:p.e,src:'x',j:j})});return L}
function renderPpl(){var L=people(),cur=S.show.lt&&S.lt?S.lt.nombre+'|'+(S.lt.cargo||''):'';
 $('ppl').innerHTML=L.map(function(p,i){return '<button data-p="'+i+'" class="'+(cur===p.n+'|'+p.c?'on':'')+'"'+(p.src==='x'?' data-x="'+p.j+'"':'')+'>'+esc(p.n)+'<small>'+esc([p.c,p.e].filter(Boolean).join(' · ')||'—')+'</small></button>'}).join('')||'<span class="hint">Agrega oradores en el programa.</span>'}
$('ppl').addEventListener('click',function(e){var b=e.target.closest('[data-p]');if(!b)return;var p=people()[+b.dataset.p];ltShow({nombre:p.n,cargo:p.c,empresa:p.e})});
$('ppl').addEventListener('contextmenu',function(e){var b=e.target.closest('[data-x]');if(!b)return;e.preventDefault();S.ltp.splice(+b.dataset.x,1);save();renderPpl()});

// ---------- tema, mensaje, mosca ----------
$('tm_show').onclick=function(){S.show.tema=true;save();push()};$('tm_hide').onclick=function(){S.show.tema=false;save();push()};
$('tm_k').value=S.tema.k;$('tm_t').value=S.tema.t;$('tm_sub').checked=!!S.tema.sub;
['tm_k','tm_t','tm_sub'].forEach(function(id){$(id).addEventListener('input',rt);$(id).addEventListener('change',rt)});
function rt(){S.tema={k:$('tm_k').value,t:$('tm_t').value,sub:$('tm_sub').checked};save();clearTimeout(window._td);window._td=setTimeout(push,300)}
$('ms_show').onclick=function(){S.show.msg=true;save();push()};$('ms_hide').onclick=function(){S.show.msg=false;save();push()};
$('ms_l').value=S.msgz.label;$('ms_e').value=S.msgz.every;$('ms_list').value=(S.msgz.items||[]).join('\n');
['ms_l','ms_e','ms_list'].forEach(function(id){$(id).addEventListener('input',rm)});
function rm(){S.msgz={label:$('ms_l').value,every:+$('ms_e').value||10,items:$('ms_list').value.split(/\n/).map(T).filter(Boolean)};save();clearTimeout(window._md);window._md=setTimeout(push,400)}
function renderMo(){$('mo_pos').value=S.mo.pos;$('mo_scale').value=String(S.mo.scale);$('mo_op').value=S.mo.op;$('mo_live').checked=!!S.mo.live;$('mo_msgs').checked=!!S.mo.msgs;$('mo_estado').value=S.mo.estado||'EN VIVO';$('mo_list').value=(S.mo.list||[]).join('\n')}
function readMo(){S.mo={pos:$('mo_pos').value,scale:+$('mo_scale').value,op:+$('mo_op').value,live:$('mo_live').checked,msgs:$('mo_msgs').checked,estado:$('mo_estado').value,list:$('mo_list').value.split(/\n/).map(T).filter(Boolean)};save();clearTimeout(window._mo);window._mo=setTimeout(push,200)}
['mo_pos','mo_scale','mo_op','mo_live','mo_msgs','mo_estado','mo_list'].forEach(function(id){$(id).addEventListener('input',readMo);$(id).addEventListener('change',readMo)});
$('mo_show').onclick=function(){S.show.mosca=true;save();push()};$('mo_hide').onclick=function(){S.show.mosca=false;save();push()};

// ---------- pantallas completas ----------
$('ini_mode').value=S.ini.mode;$('ini_min').value=S.ini.min||10;
$('ini_mode').onchange=function(){S.ini.mode=this.value;save();push()};$('ini_min').onchange=function(){S.ini.min=+this.value||10;save()};
$('ini_go').onclick=function(){S.ini.mode=$('ini_mode').value;if(S.ini.mode==='min')S.ini.target=Date.now()+(+$('ini_min').value||10)*60000;save();push();toast(S.ini.mode==='min'?'Cuenta de '+$('ini_min').value+' min iniciada':S.ini.mode==='hora'?'Cuenta hasta las '+(S.ev.hora||'—'):'Inicio sin cuenta')};
$('pa_t').value=S.pau.titulo;$('pa_s').value=S.pau.sub||'';$('pa_min').value=S.pau.min||10;$('pa_next').checked=S.pau.next!==false;
['pa_t','pa_s','pa_next'].forEach(function(id){$(id).addEventListener('input',rp);$(id).addEventListener('change',rp)});
function rp(){S.pau.titulo=$('pa_t').value;S.pau.sub=$('pa_s').value;S.pau.next=$('pa_next').checked;save();clearTimeout(window._pd);window._pd=setTimeout(push,300)}
$('pa_go').onclick=function(){var m=+$('pa_min').value||0;S.pau.min=m;S.pau.end=m?Date.now()+m*60000:null;save();push();toast(m?'Cuenta de pausa: '+m+' min':'Pausa sin cuenta')};
$('pa_stop').onclick=function(){S.pau.end=null;save();push()};
$('or_k').value=S.ora.kicker;$('fi_t').value=S.fin.titulo;
$('or_k').oninput=function(){S.ora.kicker=this.value;save();push()};$('fi_t').oninput=function(){S.fin.titulo=this.value;save();push()};
$('or_foto').onchange=function(){var f=this.files[0];if(!f)return;var r=new FileReader();r.onload=function(){var im=new Image();im.onload=function(){var c=document.createElement('canvas'),s=Math.min(1,700/Math.max(im.width,im.height));c.width=im.width*s;c.height=im.height*s;c.getContext('2d').drawImage(im,0,0,c.width,c.height);S.ora.foto=c.toDataURL('image/jpeg',.85);save();push();toast('Foto cargada para '+(curItem().o||'el orador'))};im.src=r.result};r.readAsDataURL(f)};
$('or_fx').onclick=function(){S.ora.foto='';$('or_foto').value='';save();push()};

// ---------- datos del evento ----------
document.querySelectorAll('.ev').forEach(function(el){var k=el.id.slice(3);el.value=S.ev[k]||'';el.addEventListener('input',function(){S.ev[k]=el.value;save();clearTimeout(window._ed);window._ed=setTimeout(push,250)})});
