#!/usr/bin/env python3
"""Stingers en HTML para OBS (Titulación UCSH).
Genera:
  out/UCSH_Stinger.html            → fuente única con los 6 diseños; la dispara CONTROL_EN_VIVO y corta la escena en el momento justo
  out/UCSH_Stinger_<Diseño>.html   → un archivo por diseño; se reproduce solo al hacerse visible en OBS (o con ?loop=1 para verlo)
  stinger_render.html              → para renderizar las versiones en video (.webm con transparencia)"""
import base64, io
F = 'node_modules/@fontsource/'
FACES = ''.join('@font-face{font-family:"%s";font-weight:%d;font-display:block;src:url(data:font/woff2;base64,%s) format("woff2")}' % (f, w, base64.b64encode(open(F + p, 'rb').read()).decode())
                for f, w, p in [('Cormorant Garamond', 700, 'cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2'), ('Ubuntu', 500, 'ubuntu/files/ubuntu-latin-500-normal.woff2')])
from PIL import Image

def png(p, w):
    im = Image.open(p); im.thumbnail((w, w)); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
LOGO = png('../Logo_UCSH_blanco.png', 420)
BLOB = ''
DESIGNS = [('telon', 'Telon'), ('destello', 'Destello'), ('franjas', 'Franjas'), ('marco', 'Marco')]

ENGINE = r'''
var LOGO="__LOGO__",BLOB="__BLOB__";
var OR='#F0B808',OR2='#FFD24D',ORD='#C99A06',AZ='#004577',AZ2='#012A4A',BL='#ffffff';
function cl(x){return Math.max(0,Math.min(1,x))}
function eio(x){x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
function eo(x){x=cl(x);return 1-Math.pow(1-x,3)}
function ei(x){x=cl(x);return x*x*x}
function back(x){x=cl(x);var c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}
// fases: entrada (EIN), pantalla tapada, salida (EOUT). El corte de escena va a la mitad (TOTAL/2).
function phases(TOTAL){var e=Math.min(.62,TOTAL*.32);return{EIN:e,EOUT:e,o:TOTAL-e}}
function logo(T,TOTAL,w){var P=phases(TOTAL),li=back((T-P.EIN*.7)/.35),lo=ei((T-(P.o-.12))/.25),op=cl((T-P.EIN*.7)/.15)*(1-lo),sc=li*(1-lo*.5);
 return '<div style="position:absolute;left:50%;top:50%;opacity:'+op+';transform:translate(-50%,-50%) scale('+sc+');display:flex;flex-direction:column;align-items:center;gap:28px"><div style="font:700 170px/0.95 &quot;Cormorant Garamond&quot;,serif;color:#fff;white-space:nowrap;text-align:center"><span style="display:block;font:500 34px/1 Ubuntu,sans-serif;letter-spacing:14px;margin-right:-14px;margin-bottom:14px;color:'+OR2+'">CEREMONIA DE</span>Titulación</div><img src="'+LOGO+'" style="width:'+(w||240)+'px"></div>'}
function wavePanel(x,col,amp,ph,dir){var p,y;if(dir>0){p='M-300 -60 L'+x+' -60 ';for(y=-60;y<=1140;y+=30)p+='L'+(x+Math.sin(y/140+ph)*amp).toFixed(1)+' '+y+' ';p+='L-300 1140 Z'}
 else{p='M2220 -60 L'+x+' -60 ';for(y=-60;y<=1140;y+=30)p+='L'+(x-Math.sin(y/140+ph)*amp).toFixed(1)+' '+y+' ';p+='L2220 1140 Z'}return '<path d="'+p+'" fill="'+col+'"/>'}
var D={
 telon:function(T,TOTAL){var P=phases(TOTAL),a=eio(T/P.EIN),b=eio((T-P.o)/P.EOUT),k=b>0?1-b:a,w=980*k,s='';
  s+='<rect x="'+(w-980)+'" y="0" width="980" height="1080" fill="'+AZ+'"/><rect x="'+(1920-w)+'" y="0" width="980" height="1080" fill="'+AZ+'"/>';
  for(var f=0;f<7;f++){var x=(w-980)+f*140+40;s+='<rect x="'+x+'" y="0" width="22" height="1080" fill="'+AZ2+'" opacity=".55"/>';x=(1920-w)+f*140+80;s+='<rect x="'+x+'" y="0" width="22" height="1080" fill="'+AZ2+'" opacity=".55"/>'}
  var so=cl((1-k)*5);if(so>0)s+='<rect x="'+(w-14)+'" y="0" width="14" height="1080" fill="'+OR+'" opacity="'+so+'"/><rect x="'+(1920-w)+'" y="0" width="14" height="1080" fill="'+OR+'" opacity="'+so+'"/>';
  return svg(s)+logo(T,TOTAL)},
 destello:function(T,TOTAL){var P=phases(TOTAL),a=eio(T/P.EIN),b=eio((T-P.o)/P.EOUT),R=1200,s='';
  var r1=R*a,ri=R*b*1.02,rl=R*eio((T-.06)/P.EIN);
  if(r1>ri)s+='<path fill-rule="evenodd" fill="'+AZ+'" d="M'+(960-r1)+' 540a'+r1+' '+r1+' 0 1 0 '+(2*r1)+' 0a'+r1+' '+r1+' 0 1 0 '+(-2*r1)+' 0'+(ri>0?'M'+(960-ri)+' 540a'+ri+' '+ri+' 0 1 0 '+(2*ri)+' 0a'+ri+' '+ri+' 0 1 0 '+(-2*ri)+' 0':'')+'Z"/>';
  var rr=Math.max(r1,ri)+6;if(a<1||b>0)s+='<circle cx="960" cy="540" r="'+rr+'" fill="none" stroke="'+BL+'" stroke-opacity=".85" stroke-width="10"/><circle cx="960" cy="540" r="'+(rr+24)+'" fill="none" stroke="'+OR+'" stroke-width="8"/>';
  return svg(s)+logo(T,TOTAL)},
 franjas:function(T,TOTAL){var P=phases(TOTAL),N=6,s='',cols=[AZ,OR,AZ2,AZ,OR,AZ2];
  for(var i=0;i<N;i++){var d=i*.05,a=eio((T-d)/(P.EIN-.25)),b=eio((T-P.o-d)/(P.EOUT-.25)),x=b<=0?(-3200+a*3200):(b*3400),y=-400+i*330;
   s+='<g transform="translate('+x+' 0) skewX(-20)"><rect x="-200" y="'+y+'" width="3000" height="'+(330+4)+'" fill="'+cols[i%cols.length]+'"/></g>'}
  return svg(s)+logo(T,TOTAL)},
 marco:function(T,TOTAL){var P=phases(TOTAL),s='',cols=[OR,AZ2,AZ];
  for(var i=0;i<3;i++){var a=eio((T-i*.07)/(P.EIN-.14)),b=eio((T-P.o-(2-i)*.06)/(P.EOUT-.12)),k=b>0?1-b:a,mx=960*k,my=540*k;
   var o='M0 0H1920V1080H0Z',inr=k>=1?'':'M'+mx+' '+my+'H'+(1920-mx)+'V'+(1080-my)+'H'+mx+'Z';s+='<path fill-rule="evenodd" fill="'+cols[i]+'" d="'+o+inr+'"/>'}
  return svg(s)+logo(T,TOTAL)}};
function svg(s){return '<svg viewBox="0 0 1920 1080" width="1920" height="1080" style="position:absolute;inset:0">'+s+'</svg>'}
function drawAt(root,design,T,TOTAL){root.innerHTML=(T<0||T>TOTAL)?'':(D[design]||D.ola)(T,TOTAL)}
// sonido: "whoosh" de entrada y salida + campanita al tapar (Web Audio, sin archivos)
var AC=null;function sfx(TOTAL){try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();var t0=AC.currentTime+.02,P=phases(TOTAL);
 function whoosh(at,dur,f0,f1,g){var n=AC.sampleRate*dur,buf=AC.createBuffer(1,n,AC.sampleRate),d=buf.getChannelData(0);for(var i=0;i<n;i++)d[i]=Math.random()*2-1;
  var src=AC.createBufferSource();src.buffer=buf;var bp=AC.createBiquadFilter();bp.type='bandpass';bp.Q.value=1.2;bp.frequency.setValueAtTime(f0,at);bp.frequency.exponentialRampToValueAtTime(f1,at+dur*.6);
  var gn=AC.createGain();gn.gain.setValueAtTime(0,at);gn.gain.linearRampToValueAtTime(g,at+dur*.55);gn.gain.linearRampToValueAtTime(0,at+dur);src.connect(bp);bp.connect(gn);gn.connect(AC.destination);src.start(at);src.stop(at+dur)}
 function ding(at,f,g){var o=AC.createOscillator(),gn=AC.createGain();o.type='sine';o.frequency.value=f;gn.gain.setValueAtTime(g,at);gn.gain.exponentialRampToValueAtTime(.0001,at+1.1);o.connect(gn);gn.connect(AC.destination);o.start(at);o.stop(at+1.2)}
 whoosh(t0,P.EIN+.15,500,5000,.5);ding(t0+P.EIN*.75,880,.12);ding(t0+P.EIN*.82,1318.5,.07);whoosh(t0+P.o-.05,P.EOUT+.1,4500,600,.4)}catch(e){}}
// reproductor (el logo se decodifica al cargar para que el primer cuadro no se atrase)
try{var _li=new Image();_li.src=LOGO;if(_li.decode)_li.decode()}catch(e){}
var PLAY=null;function play(design,TOTAL,sound){PLAY={d:design,T0:performance.now(),TOT:TOTAL};if(sound)sfx(TOTAL);
 var root=document.getElementById('st');(function f(){if(!PLAY)return;var T=(performance.now()-PLAY.T0)/1000;drawAt(root,PLAY.d,T,PLAY.TOT);if(T<=PLAY.TOT)requestAnimationFrame(f);else{PLAY=null;root.innerHTML='';if(window.onDone)window.onDone()}})()}
'''

HEAD = '<!doctype html><html lang="es"><head><meta charset="utf-8"><title>%s</title><style>' + FACES + '*{margin:0;padding:0}html,body{width:1920px;height:1080px;overflow:hidden;background:transparent}#st{position:absolute;inset:0}</style></head><body><div id="st"></div><script>'
ENG = ENGINE.replace('__LOGO__', LOGO).replace('__BLOB__', BLOB)

# 1) fuente única controlada desde CONTROL_EN_VIVO
CTL = HEAD % 'Titulación UCSH · Stinger HTML' + ENG + r'''
var Q=new URLSearchParams(location.search),LASTID=null;
// solo órdenes recientes: si OBS recarga la fuente no repite la última animación
function onLive(d){var s=d&&d.stinger;if(!s||!s.id||s.id===LASTID)return;LASTID=s.id;if(Math.abs(Date.now()-s.id)>8000)return;play(s.d,+s.dur||2,s.sound!==false)}
window.addEventListener('ucsh',function(e){onLive(e.detail)});
try{new BroadcastChannel('ucsh').onmessage=function(e){onLive(e.data)}}catch(e){}
if(Q.get('demo')){var dd=Q.get('demo'),tt=+(Q.get('dur')||2);(function lp(){play(dd,tt,false);setTimeout(lp,(tt+1)*1000)})()}
</script></body></html>'''
open('out/UCSH_Stinger.html', 'w').write(CTL)

# 2) un archivo por diseño: se reproduce cuando la fuente se hace visible en OBS
for key, name in DESIGNS:
    one = HEAD % ('Titulación UCSH · Stinger ' + name) + ENG + r'''
var Q=new URLSearchParams(location.search),DES="__KEY__",DUR=+(Q.get('dur')||2),SND=Q.get('sound')!=='0';
function go(){play(DES,DUR,SND)}
window.addEventListener('obsSourceVisibleChanged',function(e){if(e.detail&&e.detail.visible)go()});
window.addEventListener('obsSourceActiveChanged',function(e){if(e.detail&&e.detail.active&&Q.get('onactive')==='1')go()});
document.addEventListener('keydown',function(e){if(e.key===' ')go()});
if(Q.get('loop')==='1'){(function lp(){go();setTimeout(lp,(DUR+1)*1000)})()}else if(!window.obsstudio)setTimeout(go,300);
</script></body></html>'''.replace('__KEY__', key)
    open('out/UCSH_Stinger_%s.html' % name, 'w').write(one)

# 3) página para renderizar a video
REN = HEAD % 'render' + ENG + r'''
var Q=new URLSearchParams(location.search);window.render2=function(T){drawAt(document.getElementById('st'),Q.get('m'),T,+(Q.get('total')||2))};
</script></body></html>'''
open('stinger_render.html', 'w').write(REN)
print('ok', [d[1] for d in DESIGNS])
