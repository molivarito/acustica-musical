# Batidos: la ondulación que delata la desafinación

**Sesión 07** (módulo 2) · Curso Acústica Musical UC
**Objetivos que cubre**: OA2.2 (batidos de primer orden: primera
experiencia del fenómeno, que s08 desarrolla), OA2.1 (un caso más donde
lo percibido no copia lo físico: dos frecuencias → una sola altura que
ondula). Apunte breve por diseño: el módulo 1 de esta sesión fue la
Prueba 1 y casi no se introdujo contenido nuevo.

## ¿Qué es esa ondulación?

Dos flautas tocaron la misma nota, y una quedó apenas desafinada. Lo
que se oyó — y lo que la mayoría del curso había anticipado a medias en
su ticket de s06 — no fue "dos notas", ni exactamente "una nota
desafinada": fue **una sola nota cuya sonoridad ondula**, un
*guau–guau–guau* regular, como si alguien subiera y bajara el volumen
varias veces por segundo. Ese vaivén tiene nombre: **batido** (en
rigor, *batido de primer orden*, porque hay parientes más sutiles que
aparecerán más adelante en el curso).

En la sesión lo contamos: con $f_1 = 440$ Hz fija y $f_2 = 443$ Hz, el
curso contó tres ondulaciones por segundo. Con 442 Hz, dos. Con
437 Hz, tres de nuevo — da lo mismo hacia qué lado está la
desafinación. La regla empírica quedó a la vista en la demo:

$$f_b = |f_2 - f_1|$$

**Los batidos por segundo son la diferencia entre las dos
frecuencias.** Un batido por segundo por cada hertz de diferencia. Es
una de las relaciones más limpias de todo el curso: no es aproximada,
no depende del instrumento ni del oyente, y se verifica contando con
los dedos.

![**Figura 1.** Suma de dos tonos cercanos: una sola onda rápida (a la frecuencia promedio) encerrada por una envolvente lenta (rojo) que sube y baja $f_b = |f_2 - f_1|$ veces por segundo. Se usan $f_1 = 40$ Hz y $f_2 = 43$ Hz para que el ciclo sea visible; la regla es la misma a cualquier altura.](../../../figuras/s07_batido_forma_onda.svg)

## ¿Por qué dos tonos casi iguales laten?

No hace falta trigonometría para entenderlo; basta la imagen de dos
trenes de empujones al aire (así describimos toda nota desde s01).

Suponga $f_1 = 440$ y $f_2 = 441$ Hz. En el instante en que ambas
ondas empujan el aire *a la vez* — están **en fase** — sus empujones se
suman: el sonido se refuerza. Pero la segunda onda completa un ciclo
más que la primera en cada segundo, así que se le va adelantando
poquito a poco. Medio segundo después le lleva *medio ciclo* de
ventaja: cuando una empuja, la otra succiona — están **en
contrafase** — y los empujones se cancelan: el sonido casi desaparece.
Al completar el segundo, la ventaja acumulada es un ciclo entero y
todo vuelve a empezar: refuerzo, silencio, refuerzo, silencio.

Con 1 Hz de diferencia, ese ciclo completo de refuerzo y cancelación
ocurre exactamente una vez por segundo. Con 3 Hz de diferencia, la
segunda onda "adelanta" tres ciclos por segundo y el patrón se repite
tres veces: tres batidos. De ahí la regla $f_b = |f_2 - f_1|$. La
envolvente que dibuja la demo — esa curva que encierra a la onda y
sube y baja lentamente — es el retrato de este juego de fases
(figura 2).

![**Figura 2.** El mecanismo del batido. A la izquierda, dos ondas *en fase*: sus empujones se suman y la resultante tiene el doble de amplitud. A la derecha, *en contrafase*: cuando una empuja la otra succiona y la suma casi se anula. Dos tonos de frecuencias distintas pasan lentamente de una situación a la otra, y ese vaivén es el batido.](../../../figuras/s07_fases_batido.svg)

> **Recuadro opcional (para quienes quieran la cuenta exacta).** La
> suma de dos sinusoides de igual amplitud se puede reescribir como
> $$\sin(2\pi f_1 t) + \sin(2\pi f_2 t) = 2\cos\!\big(2\pi \tfrac{f_2-f_1}{2} t\big)\,\sin\!\big(2\pi \tfrac{f_1+f_2}{2} t\big),$$
> es decir, una onda "rápida" a la frecuencia promedio
> $\tfrac{f_1+f_2}{2}$, multiplicada por una envolvente "lenta" que
> oscila a $\tfrac{|f_2-f_1|}{2}$. Como la sonoridad no distingue si la
> envolvente es positiva o negativa, oímos **dos** máximos por cada
> ciclo de la envolvente: los batidos audibles ocurren a
> $|f_2 - f_1|$ por segundo, no a la mitad. Compare con Roederer
> (1997), sec. 2.4.

## ¿Por qué oímos una sola nota y no dos?

Aquí asoma la parte perceptual — y la más provocadora. Físicamente hay
*dos* frecuencias presentes en el aire; un espectro suficientemente
fino mostraría dos picos. Pero el oído no oye dos notas: oye **una**,
de altura intermedia, que ondula. Cuando dos frecuencias caen muy
cerca una de otra, el sistema auditivo no logra separarlas y las
funde en una sola sensación — y la "pelea" entre ambas se percibe como
esa fluctuación de sonoridad.

¿Y qué pasa cuando la diferencia crece? En el cierre de la sesión lo
escuchamos sin explicarlo: en algún punto los batidos se vuelven
demasiado rápidos para contarlos, la ondulación se convierte en una
aspereza, y más allá, en algún momento, aparecen por fin *dos notas*
distinguibles. Dónde están esas fronteras, por qué existen y qué
tienen que ver con la consonancia y con la construcción de acordes es
exactamente el tema de la sesión 08. Por ahora, guarde la observación
de su propio oído (quedó en su ticket de salida).

## ¿Cómo se convierte el batido en una herramienta de afinación?

Esta es la lectura práctica del fenómeno, y es la que los afinadores
de teclados explotan desde hace siglos: **el batido es un detector de
desafinación más fino que el oído melódico.** Si dos cuerdas difieren
en 1 Hz, ningún oído las distingue como dos alturas — pero *cualquier*
oído cuenta un batido por segundo sin esfuerzo. La receta del unísono
es entonces: toque las dos fuentes juntas, escuche la ondulación y
ajuste una de ellas de modo que el batido se haga cada vez más lento
— un batido por segundo, uno cada dos segundos, uno cada cuatro… —
hasta que se detenga. **Batido detenido = unísono.** En el juego de
afinación de la sesión, los voluntarios llegaron rutinariamente a
menos de 1 Hz de error solo escuchando; con paciencia, el método llega
a fracciones de hertz.

En la sesión 09 esta herramienta pasa de truco a oficio: veremos que
no solo los unísonos, sino los intervalos (octavas, quintas, terceras)
también producen batidos característicos cuando están desafinados, y
que contando batidos se puede afinar un temperamento completo — el
procedimiento histórico de los afinadores de piano (Benade 1990,
cap. 16, lo describe paso a paso; lo probaremos).

## Síntesis

- Dos tonos casi iguales no se oyen como dos notas: se oyen como una
  sola nota cuya sonoridad ondula — el **batido de primer orden**.
- La regla es exacta y simple: $f_b = |f_2 - f_1|$; un batido por
  segundo por cada hertz de diferencia.
- El mecanismo físico es el juego de fases: dos ondas casi iguales
  entran y salen de paso, alternando refuerzo y cancelación.
- El batido detenido es el detector de unísono más fino disponible sin
  instrumentos: la base de la afinación de oído (s09).
- Lo que aparece cuando la diferencia crece — aspereza, y luego dos
  notas — quedó oído pero no explicado: es el punto de partida de s08.

## Hacia la sesión 08

Su ticket de salida quedó en la frontera: ¿qué se oye cuando la
diferencia crece más allá de lo que "batea", y dónde termina eso? La
sesión 08 responde con el concepto de **banda crítica** — la
resolución del oído — y con él explica la rugosidad, por qué algunos
intervalos suenan ásperos y otros no, y qué tiene que decir la física
sobre la consonancia. La misma demo de hoy vuelve a escena; traiga
audífonos. Y desde s08 comienzan los talleres de medición sobre el
objeto del proyecto de su grupo: traiga el objeto (o su avance
medible).

## Referencias y lectura complementaria

- Roederer, J. G. (1997). *Acústica y Psicoacústica de la Música*.
  Ricordi — cap. 2, sec. 2.4 ("Batidos de primer orden", dentro de
  pp. 24–78): el tratamiento perceptual que este apunte sigue.
- Benade, A. H. (1990). *Fundamentals of Musical Acoustics*, 2.ª ed.
  Dover — cap. 13, sec. 13.5 (batidos y sonoridad de sonidos
  combinados); cap. 14 (introducción) y cap. 16 (afinación práctica
  por batidos) como anticipo de s08–s09.
- Campbell, M. & Greated, C. (1987). *The Musician's Guide to
  Acoustics*. Oxford UP — cap. 3 (pp. 69–164), sección "Pitch", para
  la superposición de tonos puros.
- Rossing, T. D., Moore, F. R. & Wheeler, P. A. (2002). *The Science
  of Sound*, 3.ª ed. — cap. 8, secs. 8.1–8.4, para quien quiera
  ejercicios numéricos de batidos.
