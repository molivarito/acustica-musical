# Ondas y representación: dibujar el sonido

**Sesión 02** · Curso Acústica Musical UC
**Objetivos que cubre**: OA4.1 (leer forma de onda, espectro y
espectrograma con sus ejes, unidades y limitaciones), OA1.1 (relacionar
la vibración con el espectro; propagación y $v = \lambda f$), OA3.1
(vocabulario para la escucha argumentada).

## ¿Cómo se dibuja un golpe?

En el ticket de salida de la sesión pasada usted dejó una predicción:
cómo se *vería* un pulso si pudiéramos dibujarlo. La mayoría de las
respuestas del curso — es lo habitual — dibujó algo parecido a lo que se
ve en las películas: una montañita, un zigzag, "ondas" concéntricas como
las de una piedra en el agua. La sesión partió por ahí porque la
pregunta es más seria de lo que parece: **el sonido no se ve**, y todo
lo que este curso va a "mirar" de aquí en adelante son traducciones —
gráficos que convierten presión de aire en imagen. Quien no sabe leer
los ejes de esas traducciones está mirando decoración.

La primera traducción es la **forma de onda**: un gráfico con el
**tiempo en el eje horizontal** (en segundos o milisegundos) y en el
vertical la **presión sonora** — cuánto se aparta el aire de su presión
de reposo en cada instante, hacia la compresión (arriba) o hacia el
enrarecimiento (abajo). Es el sonido visto como historia: qué pasó
primero, qué pasó después. Un golpe seco aparece como una sacudida
breve que se apaga; la nota de flauta, como una oscilación pareja que
se repite página tras página. Benade (1990, cap. 3, secs. 3.1–3.3)
introduce esta representación con un aparato mecánico — la aguja que
raya una tira de papel en movimiento, el antecesor del osciloscopio — y
vale la pena retener esa imagen: la forma de onda es lo que dejaría
dibujado su tímpano si arrastrara un lápiz.

Lo que la sesión mostró en vivo, con el micrófono conectado a la demo,
es que la forma de onda dice mucho y esconde mucho. El golpe y el
silbido se distinguen a simple vista (una sacudida contra un vaivén
regular). Pero la vocal "aaa" y la "ooo" cantadas en la misma nota se
ven desconcertantemente parecidas: dos ondulaciones periódicas con el
mismo período. Lo que las diferencia — el timbre — está *dentro* de la
forma del vaivén, y ahí el ojo no llega.

## ¿Qué muestra el espectro que el tiempo esconde?

La segunda traducción cambia la pregunta. En vez de "¿qué pasa en cada
instante?", el **espectro** pregunta: "¿de qué frecuencias está hecho
este sonido, y con cuánta fuerza está presente cada una?". El eje
horizontal ahora es la **frecuencia** (Hz); el vertical, el nivel de
cada componente (en la práctica, decibeles relativos — la sesión 06
hará justicia al decibel; por ahora basta leerlo como "más arriba =
componente más fuerte").

En el espectro, el silbido es casi un solo pico angosto: una frecuencia
y poco más. La vocal cantada es una peineta de picos regularmente
espaciados — los **parciales** del sonido, que en la voz están en
razones enteras con el más grave. La "sss" es una nube ancha sin picos
definidos: energía repartida en muchas frecuencias a la vez, sin
periodicidad, y por eso sin altura cantable. Y el golpe seco reparte su
energía en una franja amplia que se extingue enseguida. Las dos vistas
son el mismo sonido: **la forma de onda es el sonido como historia; el
espectro, como receta de ingredientes.** Ninguna es "la verdadera";
cada una responde preguntas que la otra no puede.

Este vocabulario ya es exigible en la escucha del día: "oigo un sonido
con parciales fuertes en la zona aguda" es una descripción (dimensión
D1 de la rúbrica); "suena brillante" es el punto de partida que hay que
aprender a traducir.

## ¿Y si queremos las dos cosas a la vez? El espectrograma

La música cambia en el tiempo — esa es casi su definición — y el
espectro de la sección anterior es una foto sin fecha. La tercera
traducción, el **espectrograma**, junta ambas vistas: **tiempo en el
eje horizontal, frecuencia en el vertical, y el nivel codificado como
color o intensidad** (más oscuro o más encendido = más fuerte). Cada
columna vertical del espectrograma es un espectro instantáneo; leídas
de izquierda a derecha, cuentan la película completa.

![**Figura 1.** Una misma señal (un tono con cuatro parciales, como una vocal cantada) vista en sus tres representaciones. La *forma de onda* la cuenta como historia (presión vs. tiempo); el *espectro*, como receta de ingredientes (nivel vs. frecuencia: la peineta de parciales); el *espectrograma* junta ambas (tiempo–frecuencia–color) y muestra los parciales como líneas horizontales, con el breve "golpe" inicial como una columna vertical. Ninguna es la verdadera: cada una responde lo que la otra esconde.](../../assets/figuras/s02_tres_retratos.svg)

En el espectrograma, el silbido con glissando es una línea delgada que
sube; la vocal cantada, una familia de líneas horizontales paralelas
(sus parciales); la "sss", una banda difusa y alta; el golpe, una
columna vertical delgada: todo el rango de frecuencias, casi ningún
tiempo. Esta herramienta será el **microscopio del curso**: la usaremos
para mirar instrumentos, salas y su proyecto de aquí a la sesión 15.
Por eso la sesión insistió en un chequeo mínimo antes de creer nada:
identificar en su app cuál eje es tiempo, cuál es frecuencia y qué
significa el color. Espectrograma sin ejes leídos no es evidencia.

## ¿Por qué su app no muestra nada sobre 22 000 Hz?

Al explorar los límites de las apps apareció un techo: casi todas las
pantallas se cortan cerca de los 22 000 Hz (a veces 20 000, a veces
24 000). Ese techo no es una propiedad del sonido ni de su oído: es una
propiedad **de la herramienta**, y entenderlo requiere la única noción
de audio digital que este curso necesita.

El celular no guarda la presión del aire en forma continua: la **mide
muchas veces por segundo** y guarda la lista de valores. Cada medición
es una *muestra*, y la tasa típica es de 44 100 o 48 000 muestras por
segundo. Una regla fundamental del muestreo dice que con $f_s$ muestras
por segundo solo se puede representar fielmente el contenido **por
debajo de $f_s/2$**: con 44 100 muestras/s, nada sobre 22 050 Hz. De ahí
el techo de su app. Las frecuencias que llegan al micrófono por encima
de ese límite no desaparecen limpiamente: pueden colarse disfrazadas de
frecuencias más bajas (el fenómeno se llama *aliasing*), y por eso los
equipos filtran lo muy agudo antes de muestrear (Rossing et al. 2002,
cap. 21, secciones de muestreo y aliasing).

> **Recuadro opcional (límites del microscopio).** Hay un segundo
> límite, más sutil: el espectrograma se calcula analizando la señal
> por ventanas de tiempo. Ventana larga → frecuencias finamente
> resueltas pero eventos emborronados en el tiempo; ventana corta → lo
> contrario. Por eso dos golpes muy seguidos pueden verse como uno, y
> por eso el ajuste "tamaño de ventana/FFT" de las apps cambia el
> dibujo sin que cambie el sonido. No hay ajuste "correcto": hay
> ajustes apropiados para preguntas distintas. Este tratamiento es
> deliberadamente instrumental; el detalle cuantitativo (teorema del
> muestreo) excede el curso y puede consultarse en Rossing et al.
> (2002, cap. 21).

## ¿Qué es lo que viaja (y a qué velocidad)?

Queda el otro asunto de la sesión: entre la fuente y el oído, ¿qué se
mueve? No el aire en bloque — nadie siente viento al escuchar — sino
una **perturbación de presión** que se pasa de mano en mano: cada
porción de aire empuja a la siguiente y vuelve casi a su lugar. Lo que
viaja es el empujón, no el material, como la ola del estadio viaja sin
que nadie cambie de asiento.

Ese empujón avanza en el aire a $v \approx 343$ m/s a 20 °C (la
velocidad crece levemente con la temperatura; el valor redondo del
curso es ese). El trueno del módulo 2 lo volvió aritmética: 3 segundos
de retraso ≈ 1 kilómetro de distancia.

Si la fuente vibra periódicamente con frecuencia $f$, cada nuevo empujón
sale cuando el anterior ya avanzó un trecho fijo: la distancia entre
crestas sucesivas viajando por el aire. Esa distancia es la **longitud
de onda** $\lambda$, y las tres cantidades quedan atadas por la relación
más reutilizada del semestre:

$$v = \lambda f$$

![**Figura 2.** Lo que viaja por el aire es una perturbación de presión: cada porción de aire se comprime y se enrarece y vuelve casi a su lugar (arriba, densidad de moléculas; el aire no viaja en bloque). La curva de presión vs. posición (abajo) fija la **longitud de onda** $\lambda$ como la distancia entre dos compresiones sucesivas. Con la rapidez $v \approx 343$ m/s, las tres cantidades quedan atadas por $v = \lambda f$.](../../assets/figuras/s02_propagacion_lambda.svg)

Con ella y proporciones: el La4 (440 Hz) mide en el aire
$343/440 \approx 0{,}78$ m; el límite grave audible (20 Hz), unos 17 m —
del porte de la sala —; el agudo (20 000 Hz), unos 17 mm. Que los
sonidos musicales midan entre centímetros y metros, justo la escala de
los instrumentos y de las salas, no es coincidencia: es el tema de casi
todo lo que sigue (Campbell & Greated 1987, cap. 1; Roederer 1997,
cap. 3, para el detalle de ondas y energía).

## Síntesis

- Forma de onda (presión vs. tiempo), espectro (nivel vs. frecuencia) y
  espectrograma (tiempo–frecuencia–color) son tres traducciones del
  mismo sonido; cada una revela lo que otra esconde. Leer sus ejes y
  unidades es requisito antes de sacar conclusiones.
- El espectrograma es el microscopio del curso, y tiene límites de
  fábrica: techo en $f_s/2$ (muestreo) y compromiso entre resolución
  temporal y frecuencial (ventana). Conocer los límites es parte de
  saber medir (OA4.1).
- El sonido se propaga como perturbación de presión, a $v \approx 343$
  m/s en aire a 20 °C, y $v = \lambda f$ conecta la rapidez, el tamaño
  espacial y la frecuencia de una onda. Los sonidos musicales miden
  entre centímetros y metros.

## Hacia la sesión 03

Su ticket de salida quedó apostado: el vaso golpeado, ¿una línea o
varias en el espectrograma? La sesión 03 lo golpea de verdad: los
objetos no vibran de cualquier manera sino en un repertorio de formas
propias — sus *modos* — y el espectro es la huella digital de ese
repertorio. Con esa idea se lanza, además, el proyecto del curso.

## Referencias y lectura complementaria

- Benade, A. H. (1990). *Fundamentals of Musical Acoustics*, 2.ª ed.
  Dover — cap. 3 ("Simple Relations of Sounds and Motions"), secs.
  3.1–3.3 (representar el movimiento; strip chart y osciloscopio) y los
  experimentos de la sec. 3.5 (EEQ).
- Campbell, M. & Greated, C. (1987). *The Musician's Guide to
  Acoustics*. Oxford UP — cap. 1, pp. 5–38 (transmisión del sonido:
  ondas, velocidad, presión).
- Roederer, J. G. (1997). *Acústica y Psicoacústica de la Música*.
  Ricordi — cap. 3, pp. 79–119 (ondas sonoras, velocidad y longitud de
  onda, superposición). Lectura alternativa en español.
- Rossing, T. D., Moore, F. R. & Wheeler, P. A. (2002). *The Science of
  Sound*, 3.ª ed. — cap. 3 (ondas, ejercicios de $v = \lambda f$) y
  cap. 21 (muestreo y aliasing; las secciones de hardware están
  datadas, las de fundamentos siguen vigentes).
