# Kit de transmisión · Ceremonia de Titulación UCSH

Gráficos en vivo para OBS con la identidad de la Universidad Católica Silva Henríquez: azul `#004577` / `#012A4A`, el oro del logo `#F0B808`, nombres en Cormorant Garamond y textos en Ubuntu (la letra de ucsh.cl). Los colores y el logo se tomaron del sitio ucsh.cl porque no se contaba con el manual de marca; si llega, conviene revisar tonos y usos del logo contra él.

## Contenido

| Archivo / carpeta | Para qué sirve |
|---|---|
| `MATERIAL_UCSH.html` | Panel de muestra de todo el material: pantallas, gráficos en vivo, PiP, transiciones y control. |
| `CONTROL_EN_VIVO.html` | Página de control. Se conecta a OBS y maneja la lista de titulados, lower thirds, carrera en pantalla, mensajes, mosca, PiP, pantallas, repeticiones y transiciones. |
| `PANEL_MIDI.html` | Controlar todo desde un controlador MIDI. Ábrelo en el mismo Chrome que el control. |
| `Paneles/` | Gráficos para OBS: Inicio, Carrera, Nómina, Pausa, Final, overlays (lower third, carrera en pantalla, mensaje, mosca, repetición), los 5 marcos PiP y los stingers HTML. |
| `Transiciones/` | Telón, Destello, Franjas y Marco en video con transparencia y sonido para la transición Stinger nativa de OBS: 4 s (corte 2000 ms) y **Corta** de 2 s (corte 1000 ms), en 1080p y `720p/`. |
| `Logos/` | Logo UCSH a color y versión blanco y oro para fondos azules. |

## La lista de titulados

Cada fila es un titulado: **carrera, nombre completo y distinción** (la distinción es opcional). En la tarjeta **Titulados por carrera** abre *Pegar la lista de titulados* y usa cualquiera de estas formas:

- Tres columnas copiadas desde Excel (Carrera · Nombre · Distinción).
- Una línea por titulado: `Trabajo Social | Nombre Apellido Apellido | Distinción máxima`
- El nombre de la carrera en una línea, los titulados debajo (uno por línea) y una línea en blanco antes de la carrera siguiente.

El orden de la lista es el orden de llamado. Mientras no tengas la lista, **↺ Lista de ejemplo** carga seis titulados de prueba.

## Puesta en marcha (una vez, en el PC de OBS)

1. Descomprime el kit en una carpeta fija, por ejemplo Documentos.
2. En OBS: **Herramientas → Ajustes del servidor WebSocket** → habilitar → copiar la contraseña.
3. Abre `CONTROL_EN_VIVO.html` en Chrome, pega la contraseña y pulsa **CONECTAR**.
4. Pulsa **⚙ Instalar gráficos en OBS**. Se crean las escenas INICIO, ESTUDIO, CARRERA, NOMINA, PAUSA, REPLAY, FINAL y las cinco PIP_ con sus gráficos, y la fuente del stinger HTML encima de todo. No se borra nada de lo que ya tengas.
5. En ESTUDIO agrega tus cámaras **debajo** de los gráficos.
6. En **Datos del evento** completa nombre, fecha, hora, lugar y la línea bajo "Titulación" (por ejemplo la facultad).

## Durante la ceremonia

- **SIGUIENTE ▶** pasa al titulado que sigue y muestra su lower third (nombre, carrera y distinción). Se puede desactivar en la tarjeta de la lista.
- Al cambiar de carrera, la **carrera en pantalla** se actualiza sola. Pon **CARRERA** para presentarla y **NOMINA** para ver a todos sus titulados, con el actual marcado en oro.
- **PAUSA** muestra la carrera que viene; **FINAL** cierra con felicitaciones.
- **Teclado**: `1`–`9` ponen la escena en vista previa, `Shift` + número la pasa directo al aire, `P` repite y `M` guarda un momento.

## Picture in picture (PiP)

Cinco marcos en `Paneles/UCSH_PIP_<Formato>.html`, con ventanas transparentes para lo que pongas debajo en OBS:

| Escena | Formato | Ventanas |
|---|---|---|
| `PIP_PRESENTACION` | Presentación + cámara | 1340×754 y 420×236 |
| `PIP_DOS` | Dos cámaras | 885×498 cada una |
| `PIP_TRES` | Tres cámaras | 580×326 cada una |
| `PIP_VERTICAL` | Cámara + video vertical (celular) | 1150×647 y 460×818 |
| `PIP_ESQUINA` | Cámara chica sobre una pantalla completa | 420×236 |

*Instalar gráficos* deja una fuente de color del tamaño exacto en cada ventana: reemplázala por tu cámara o presentación. En la tarjeta **Picture in picture** escribes el título y el nombre y cargo de cada ventana (por ejemplo el rector y la decana).

## Transiciones en HTML (stingers)

Cuatro diseños: **Telón**, **Destello**, **Franjas** y **Marco**, con el sello "Ceremonia de Titulación" y el logo. Cada uno tapa la pantalla a la mitad de su duración y trae su sonido. En la tarjeta **Transiciones HTML** eliges diseño, duración y sonido; **🎬 Vista previa al aire con esta** lanza la animación y cambia de escena justo cuando la pantalla está tapada. Para usar los videos de `Transiciones/` crea en OBS transiciones Stinger llamadas **UCSH Telon**, **UCSH Destello**, **UCSH Franjas** o **UCSH Marco** (o su versión **Corta**) y pulsa **🎬 Ajustar transiciones**.
