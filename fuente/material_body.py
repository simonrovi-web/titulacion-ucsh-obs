SCREENS = [('inicio', 'Inicio', 'Escena INICIO', 'Ceremonia de Titulación con la cuenta regresiva hasta la hora de inicio.'),
 ('carrera', 'Carrera', 'Escena CARRERA', 'Presenta cada carrera antes de llamar a sus titulados, con cuántos se titulan.'),
 ('nomina', 'Nómina', 'Escena NOMINA', 'Todos los titulados de la carrera en curso; quien está recibiendo su título se marca en oro.'),
 ('pausa', 'Pausa', 'Escena PAUSA', '“Volvemos en unos minutos” con cuenta regresiva y la carrera que viene.'),
 ('final', 'Final', 'Escena FINAL', 'Cierre de la ceremonia con felicitaciones a los titulados.')]
tabs = ''.join('<button type="button" role="tab" id="t-%s" aria-controls="p-%s" aria-selected="%s"%s>%s</button>' % (k, k, 'true' if i == 0 else 'false', '' if i == 0 else ' tabindex="-1"', n) for i, (k, n, _, _) in enumerate(SCREENS))
panes = ''.join('<div class="pane" role="tabpanel" id="p-%s" aria-labelledby="t-%s">%s<div class="cap"><h3>%s</h3><small>%s</small><p>%s</p></div></div>' % (k, k, media(k, n), n, tag, d) for k, n, tag, d in SCREENS)
STG = [('telon', 'Telón', 'Dos paneles azules se cierran como un telón de escenario y vuelven a abrirse.'),
 ('destello', 'Destello', 'Un círculo azul se expande desde el centro con un anillo de oro.'),
 ('franjas', 'Franjas', 'Franjas diagonales azules y oro cruzan la pantalla.'),
 ('marco', 'Marco', 'Marcos rectangulares se cierran hacia el centro y luego se abren.')]
stg = ''.join('<li><button type="button" class="stage" data-hst="%s" aria-label="Reproducir la transición %s otra vez"><div aria-hidden="true"></div></button><h3>%s</h3><p>%s</p><code>UCSH_Stinger_%s.html</code></li>' % (k, n, n, d, n.replace('ó', 'o')) for k, n, d in STG)

BODY = '''<a class="skip" href="#main">Saltar al contenido</a>
<div class="top">
 <header class="container nav">
  <img src="__LOGOW__" alt="Universidad Católica Silva Henríquez" width="1720" height="742" style="height:56px;width:auto">
  <nav aria-label="Secciones"><ul>
   <li><a href="#identidad">Identidad</a></li><li><a href="#pantallas">Pantallas</a></li><li><a href="#overlays">Gráficos en vivo</a></li><li><a href="#pip">PiP</a></li><li><a href="#transiciones">Transiciones</a></li><li><a href="#control">Control</a></li><li><a href="#obs">En OBS</a></li>
  </ul></nav>
 </header>
 <section class="hero" aria-labelledby="h-hero">
  <div class="container grid12">
   <div class="intro">
    <h1 id="h-hero">Titulación UCSH en pantalla</h1>
    <p class="lead">El kit para transmitir la ceremonia, titulado por titulado.</p>
    <div class="hero-actions"><a class="btn" href="#pantallas">Ver las pantallas</a></div>
   </div>
   <figure class="hero-visual" data-loop>
    <div class="screen" id="hero-screen">
     <img src="__ESTUDIO__" alt="Escena ESTUDIO con carrera en pantalla, lower third del titulado, mensaje y mosca" data-on="1" width="1600" height="900" fetchpriority="high">
     <img src="__CARRERA__" alt="Pantalla Carrera" data-on="0" aria-hidden="true" width="1280" height="720">
     <img src="__NOMINA__" alt="Pantalla Nómina" data-on="0" aria-hidden="true" width="1280" height="720">
     <div class="stage-layer" aria-hidden="true"><div></div></div>
    </div>
    <figcaption class="hero-cap"><span id="hero-now">Escena ESTUDIO, pasando a CARRERA con la transición Telón.</span><button class="btn btn--quiet btn--small" type="button" data-loop-toggle>Pausar</button></figcaption>
   </figure>
  </div>
 </section>
</div>
<main id="main">
<section class="sec sec--l" id="identidad" aria-labelledby="h-id">
 <div class="container">
  <div class="head"><h2 id="h-id">Identidad visual</h2><p class="lead">Colores y logo tomados de ucsh.cl, en clave académica: azul institucional, el oro del logo y nombres con serifa.</p></div>
  <div class="grid12 id-body">
   <table class="swatches">
    <thead><tr><th scope="col"><span class="visually-hidden">Muestra</span></th><th scope="col">Color</th><th scope="col">Código</th><th scope="col">Uso</th></tr></thead>
    <tbody>
     <tr><td><i class="chip" style="background:var(--imp-1)"></i></td><td class="nm">Azul UCSH</td><td><code>#004577</code></td><td class="use">Fondos, tarjetas y barras</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-2)"></i></td><td class="nm">Azul profundo</td><td><code>#012A4A</code></td><td class="use">Degradados y barra inferior</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-3)"></i></td><td class="nm">Oro</td><td><code>#F0B808</code></td><td class="use">Marcos finos, etiquetas y el titulado actual</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-4)"></i></td><td class="nm">Celeste</td><td><code>#14A2F1</code></td><td class="use">Luz suave en los fondos</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-5)"></i></td><td class="nm">Blanco</td><td><code>#FFFFFF</code></td><td class="use">Nombres y textos</td></tr>
     <tr><td><i class="chip" style="background:var(--imp-6)"></i></td><td class="nm">Gris</td><td><code>#7E7E7E</code></td><td class="use">Texto secundario</td></tr>
    </tbody>
   </table>
   <div class="specimens">
    <div class="spec"><small>Nombres y títulos</small><span class="face">Cormorant Garamond</span><p>Nombres de los titulados, carreras y títulos de pantalla.</p></div>
    <div class="spec"><small>Texto</small><span class="face face--alt">Ubuntu</span><p class="alt">La letra de ucsh.cl: etiquetas, fechas y datos.</p></div>
   </div>
   <ul class="logos" style="grid-template-columns:minmax(0,1fr) minmax(0,1fr)">
    <li><div class="tile t-white"><img src="__LOGOC__" alt="Logo UCSH a color" width="1720" height="742"></div><span>Logo de ucsh.cl, a color</span></li>
    <li><div class="tile t-blue"><img src="__LOGOW__" alt="Logo UCSH en blanco y oro" width="1720" height="742"></div><span>Versión blanco y oro para fondos azules</span></li>
   </ul>
  </div>
 </div>
</section>

<section class="sec" id="pantallas" aria-labelledby="h-pa">
 <div class="container">
  <div class="head"><h2 id="h-pa">Pantallas completas</h2><p class="lead">Por cada carrera: primero la carrera, después la nómina mientras pasan sus titulados. La lista se pega en CONTROL_EN_VIVO.</p></div>
  <div data-switch>
   <div class="seg" role="tablist" aria-label="Pantallas">__TABS__</div>
   <div class="panels">__PANES__</div>
  </div>
  <p class="hint" style="margin-top:var(--space-lg)">Haz clic en cualquier imagen para verla en grande.</p>
 </div>
</section>

<section class="band" id="overlays" aria-labelledby="h-ov">
 <div class="container">
  <div class="head"><h2 id="h-ov">Gráficos en vivo sobre cámara</h2><p class="lead">Se superponen a las cámaras en la escena ESTUDIO. La imagen de fondo es solo de referencia.</p></div>
  <div class="bento">
   <figure class="b-lead">__M_ESTUDIO__<figcaption><h3>Todo junto en ESTUDIO</h3><span>Carrera en pantalla, lower third del titulado, mensaje y mosca al mismo tiempo.</span></figcaption></figure>
   <figure class="b-side">__M_LT__<figcaption><h3>Lower third del titulado</h3><span>Nombre, carrera y distinción. Con SIGUIENTE pasa solo al titulado que sigue.</span></figcaption></figure>
   <figure class="b-side">__M_REPLAY__<figcaption><h3>Repetición</h3><span>Marca de repetición durante los replays (escena REPLAY).</span></figcaption></figure>
   <figure class="b-third">__M_TEMA__<figcaption><h3>Carrera en pantalla</h3><span>La carrera que se está titulando, arriba a la izquierda.</span></figcaption></figure>
   <figure class="b-third">__M_MENSAJE__<figcaption><h3>Mensaje inferior</h3><span>Felicitaciones y avisos; si el texto es largo, se desplaza.</span></figcaption></figure>
   <figure class="b-third">__M_MOSCA__<figcaption><h3>Mosca</h3><span>Logo, EN VIVO y mensajes que rotan.</span></figcaption></figure>
  </div>
 </div>
</section>

<section class="sec" id="pip" aria-labelledby="h-pip">
 <div class="container">
  <div class="head"><h2 id="h-pip">Picture in picture</h2><p class="lead">Cinco marcos para discursos, presentaciones y saludos. Las ventanas quedan transparentes y el control escribe los nombres.</p></div>
  <div class="bento">
   <figure class="b-lead">__M_PIP1__<figcaption><h3>Presentación + cámara</h3><span>Discurso con presentación, y quien habla al lado con su nombre y cargo.</span></figcaption></figure>
   <figure class="b-side">__M_PIP5__<figcaption><h3>Esquina</h3><span>Una cámara chica sobre cualquier pantalla completa, como la nómina.</span></figcaption></figure>
   <figure class="b-side">__M_PIP4__<figcaption><h3>Cámara + video vertical</h3><span>Para saludos de familias grabados con el celular.</span></figcaption></figure>
   <figure class="b-half">__M_PIP2__<figcaption><h3>Dos cámaras</h3><span>Quien entrega el título y quien lo recibe.</span></figcaption></figure>
   <figure class="b-half">__M_PIP3__<figcaption><h3>Tres cámaras</h3><span>Autoridades en la testera con el título arriba.</span></figcaption></figure>
  </div>
  <p class="hint" style="margin-top:var(--space-lg)">Instalar gráficos crea las escenas PIP_PRESENTACION, PIP_DOS, PIP_TRES, PIP_VERTICAL y PIP_ESQUINA, con una fuente de color del tamaño justo en cada ventana para reemplazarla por tu cámara.</p>
 </div>
</section>

<section class="sec sec--l" id="transiciones" aria-labelledby="h-tr">
 <div class="container">
  <div class="head"><h2 id="h-tr">Transiciones</h2><p class="lead">Cuatro transiciones hechas en HTML para OBS, aquí tal como corren. Tapan la pantalla a la mitad y el control cambia la escena en ese momento. También vienen en video con transparencia (4 s y 2 s, en 1080p y 720p).</p></div>
  <div data-loop id="tr-loop">
   <div class="tr-tools"><p class="hint">Toca una transición para verla de nuevo.</p><button class="btn btn--quiet btn--small" type="button" data-loop-toggle>Pausar</button></div>
   <ul class="stingers stingers--two">__STG__</ul>
  </div>
 </div>
</section>

<section class="well" id="control" aria-labelledby="h-ct">
 <div class="container">
  <div class="head"><h2 id="h-ct">Herramientas de control</h2><p class="lead">Se abren en Chrome en el PC de la transmisión y se conectan a OBS.</p></div>
  <div class="ctl">
   <figure class="media c-main" style="margin:0"><img src="__CONTROL__" alt="CONTROL_EN_VIVO" tabindex="0" role="button" aria-label="Ver CONTROL_EN_VIVO en grande" loading="lazy" width="1400" height="887"></figure>
   <div class="c-main-tx"><h3>CONTROL_EN_VIVO</h3><p>La lista de titulados por carrera, lower thirds, carrera en pantalla, mensajes, mosca, PiP, pantallas, escenas, transiciones y repeticiones.</p></div>
   <figure class="media c-midi" style="margin:0"><img src="__MIDI__" alt="PANEL_MIDI" tabindex="0" role="button" aria-label="Ver PANEL_MIDI en grande" loading="lazy" width="1400" height="1000"></figure>
   <div class="c-midi-tx"><h3>PANEL_MIDI</h3><p>Cualquier acción en un pad del controlador: titulado siguiente, lower third, escenas a vista previa, transiciones y repeticiones.</p></div>
  </div>
 </div>
</section>

<section class="obs" id="obs" aria-labelledby="h-obs">
 <div class="container">
  <div class="head"><h2 id="h-obs">Cómo queda en OBS</h2><p class="lead">El botón INSTALAR crea estas escenas con sus gráficos; en ESTUDIO y en las PiP van tus cámaras.</p></div>
  <ul class="scenes" aria-label="Escenas que crea INSTALAR"><li>INICIO</li><li>ESTUDIO</li><li>CARRERA</li><li>NOMINA</li><li>PAUSA</li><li>REPLAY</li><li>FINAL</li><li>PIP_…</li></ul>
  <ol class="steps">
   <li><span>Descomprimir el kit en una carpeta fija y abrir <b>CONTROL_EN_VIVO.html</b> en Chrome.</span></li>
   <li><span>En OBS activar el <b>servidor WebSocket</b>, copiar la contraseña y pulsar <b>CONECTAR</b>.</span></li>
   <li><span>Pulsar <b>Instalar gráficos en OBS</b> y agregar las cámaras en ESTUDIO y en las escenas PiP.</span></li>
   <li><span>Pegar la <b>lista de titulados</b> desde Excel: carrera, nombre y distinción.</span></li>
   <li><span>Durante la ceremonia: <b>SIGUIENTE ▶</b> por cada titulado; CARRERA y NOMINA al cambiar de carrera.</span></li>
  </ol>
 </div>
</section>
</main>
<footer class="foot">
 <div class="container"><img src="__LOGOW__" alt="UCSH" width="1720" height="742" style="height:64px;width:auto"><p>Kit de transmisión de la Ceremonia de Titulación UCSH. Identidad tomada de ucsh.cl.</p></div>
</footer>
<div id="lb" role="dialog" aria-label="Imagen ampliada"><img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></div>
'''
rep = {'__LOGOW__': P3('../Logo_UCSH_blanco.png', 520), '__LOGOC__': P3('../Logo_UCSH_color.png', 520), '__ESTUDIO__': J('estudio'), '__CARRERA__': J('carrera'), '__NOMINA__': J('nomina'),
 '__TABS__': tabs, '__PANES__': panes, '__STG__': stg, '__CONTROL__': J('control'), '__MIDI__': J('midi'),
 '__M_ESTUDIO__': media('estudio', 'Todo junto en ESTUDIO'), '__M_LT__': media('lt', 'Lower third del titulado'), '__M_REPLAY__': media('replay', 'Repetición'),
 '__M_TEMA__': media('tema', 'Carrera en pantalla'), '__M_MENSAJE__': media('mensaje', 'Mensaje inferior'), '__M_MOSCA__': media('mosca', 'Mosca'),
 '__M_PIP1__': media('pip_Presentacion', 'PiP presentación más cámara'), '__M_PIP2__': media('pip_Dos', 'PiP dos cámaras'), '__M_PIP3__': media('pip_Tres', 'PiP tres cámaras'), '__M_PIP4__': media('pip_Vertical', 'PiP cámara más video vertical'), '__M_PIP5__': media('pip_Esquina', 'PiP esquina')}
