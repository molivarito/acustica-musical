# Capítulo 6 — Sonoridad y decibel: medir lo fuerte

*Lectura previa a la sesión 06. Objetivos: OA4.2 (principal), OA2.1.
Traer a la sesión: celular con la app de medición SPL instalada (lista
en el material de apps del curso) y audífonos.*

## La pregunta que dejó su ticket

Al salir de la sesión 5 usted escribió dos predicciones. La primera —
¿pueden dos sonidos de la misma frecuencia oírse a distinto volumen? —
seguramente le pareció regalada: por supuesto, para eso existe el
matiz, del pianissimo al fortissimo. Pero la segunda era una trampa
fina: un sonido grave y uno agudo que llevan **exactamente la misma
energía física**, ¿suenan igual de fuertes?

Piense en su experiencia antes que en la física. ¿Por qué el bajista
necesita un amplificador más grande que el guitarrista? ¿Por qué al
bajar mucho el volumen de una grabación lo primero que se pierde parece
ser... algo, abajo? Este capítulo le da el vocabulario y la aritmética
para convertir esas sospechas en afirmaciones medibles, porque la
sesión 6 es la sesión en que el curso **sale a medir**: la tercera pata
del oficio, junto al oído y al modelo.

## Un rango de un millón de millones

Del lado físico, lo que llega a su tímpano es una oscilación de
**presión**: el aire empuja y afloja, unas decenas o miles de veces por
segundo, alrededor de la presión atmosférica. Esa presión sonora $p$ se
mide en pascales, y la **intensidad** — la energía que pasa por segundo
— crece con su cuadrado.

Ahora, el dato que obliga a todo lo demás: entre el sonido más débil
que un oído sano detecta y el nivel que empieza a doler hay un factor
de alrededor de **10¹² en intensidad** — un millón de millones (Benade
1990, sec. 13.1). El umbral de audición ronda una presión de **20
millonésimas de pascal**; Benade, para impresionar con justicia, lo
escribe como 1/3.530.000.000 de la presión atmosférica. Un aparato — o
un oído — que quisiera cubrir ese rango con una escala lineal
necesitaría un dial de doce ceros. Nadie razona así. Ni usted: cuando
compara volúmenes, su oído no suma cantidades, **compara por factores**
— "esto es como el doble de aquello" —, igual que con la altura
comparaba por razones de frecuencia.

## La gramática del decibel

La acústica adoptó la misma estrategia y la llamó **decibel (dB)**. El
decibel no es una cantidad de sonido: expresa la *razón* entre dos
sonidos (Benade 1990, sec. 13.2). Toda su gramática, en tres reglas de
aritmética simple:

- **+10 dB = ×10 en intensidad.** Cada 10 dB agregan un cero al factor:
  +20 dB es ×100, +30 dB es ×1000.
- **+3 dB = ×2 en intensidad.** Duplicar la energía es un paso de solo
  3 dB — y al oído le parece un cambio más bien discreto.
- Para que algo se oiga aproximadamente **el doble de fuerte** hace
  falta cerca de **+10 dB**: diez veces la energía (Benade 1990,
  sec. 13.4).

Lea esas reglas dos veces, porque son el corazón del capítulo y de la
prueba: **duplicar la energía casi no se nota; para doblar la sensación
hay que multiplicar la energía por diez.** El oído comprime — otra vez
un par físico↔perceptual que no es lineal ni unívoco, como el de la
altura en el capítulo 5.

Para pasar de comparaciones a niveles absolutos solo falta fijar contra
qué se compara. La referencia universal es el umbral: $p_0 = 20\ \mu$Pa.
El **nivel de presión sonora** se escribe $L_p$ y se expresa en **dB SPL
re 20 µPa** — cuando en este curso diga "dB SPL", esa referencia va
implícita, pero un dato profesional siempre la declara. Con la
referencia en el umbral, la escala se vuelve amable: 0 dB SPL apenas se
oye; un susurro ronda los 30 dB; una conversación, los 60; una orquesta
en fortissimo vive cerca de los 95–100, y alrededor de 120 dB SPL el
sonido empieza a doler (Benade 1990, secs. 13.1 y 13.8; ROS cap. 6 —
valores típicos aproximados; los de nuestras salas los mediremos
nosotros).

![**Figura 1.** La escala de niveles de presión sonora con hitos musicales, del umbral de audición al umbral del dolor. Los valores son típicos y redondeados. A la derecha, la gramática del decibel: +10 dB multiplican por diez la intensidad (y suenan como el doble), +3 dB la duplican (cambio chico).](../figuras/s06_escala_decibel.svg)

> **Recuadro opcional (la fórmula, para quien la quiera).**
> $L_p = 20\log_{10}(p/p_0)$, o $10\log_{10}(I/I_0)$ en intensidades.
> La intensidad va como el cuadrado de la presión: por eso ×10 en
> presión son +20 dB, y duplicar la amplitud de presión da +6 dB
> (Benade 1990, sec. 13.2). En clase bastan las reglas; la fórmula no
> se evalúa.

## Tres preguntas que conviene traer pensadas

**Primera**: si junto **dos guitarras idénticas** tocando igual de
fuerte, ¿cuántos dB sube el nivel — y suena eso "el doble de fuerte"?
La aritmética ingenua dice una cosa; las reglas de arriba insinúan
otra; y las presiones de dos fuentes independientes, además, no se
suman de frente (se combinan estadísticamente: Benade 1990, secs.
13.2 y 13.5). No le damos el número: en la sesión lo va a **medir**,
con dos celulares como fuentes gemelas. Prediga antes.

**Segunda**: ¿es el oído un medidor plano — le da lo mismo la
frecuencia con tal de que la energía sea la misma? Aquí vuelve el
ticket. Los acústicos responden con las **curvas isofónicas** (curvas
de *igual sonoridad*, graduadas en **fones**): mapas de cuántos dB SPL
hacen falta, en cada frecuencia, para igualar la sonoridad de un tono
de 1000 Hz (Benade 1990, secs. 13.3–13.4; C&G cap. 3; ROE sec. 3.4).
No le mostramos todavía su forma: en la sesión usted va a **dibujar la
suya propia**, igualando tonos de oído con una demo. Lo que sí
adelantamos es que la forma no es plana, que no es igual a todo
volumen, y que en ella está la respuesta a por qué las mezclas suaves
parecen perder algo. Escriba su predicción: para sonar igual de fuerte
que 1000 Hz, ¿un tono de 125 Hz necesitará más, igual o menos nivel?

**Tercera**: si el sonómetro — o su app — quisiera parecerse al oído,
¿debería medir todos los componentes por igual? Los diseñadores de los
años treinta decidieron que no, y le incorporaron un filtro que
descuenta lo que el oído descuenta: la **ponderación A** (Benade 1990,
sec. 13.8). Por eso su app reporta **dB(A)**. En el curso basta con
saber leer la etiqueta; la teoría del filtro no es materia.

Ya que hablamos de sonoridad de verdad: su unidad perceptual es el
**son** (1 son = la sonoridad de 1000 Hz a 40 dB SPL), y su gracia es
que — al revés que los decibeles — los sones se suman como cantidades
normales: 2 sones junto a 3 sones se oyen como 5 (Benade 1990,
sec. 13.4). En este curso los sones se usan solo así, cualitativamente,
para poder decir "doble de sonoridad" con la conciencia limpia.

## El oído no tiene párpados

Los ojos se cierran; los oídos no. La aritmética del dB tiene una
consecuencia directa para cualquiera que pase horas al lado de fuentes
sonoras — es decir, para usted. El criterio ocupacional de referencia
admite del orden de **8 horas diarias a 85 dB(A)**, y cada **+3 dB**
— recuerde: el doble de energía — **reduce el tiempo admisible a la
mitad**: 88 dB(A) → 4 horas, 91 → 2, 94 → 1 (criterio NIOSH; ROS caps.
30–31). Un ensayo enérgico puede vivir sobre los 90 dB(A); las cifras
de la norma chilena vigente las revisaremos con cuidado en clase
**[POR VERIFICAR: DS 594]**. El daño por dosis acumulada no duele
mientras ocurre y no se recupera después. En la sesión hay una estación
dedicada a esta cuenta — cuánto "tiempo de oído" gasta su semana
musical — porque es, literalmente, aritmética de supervivencia
profesional.

## Medir con juicio

Última advertencia antes de la sesión: el micrófono de su celular **no
está calibrado**. Dos celulares lado a lado pueden discrepar en varios
dB, y ninguno le garantiza el valor absoluto (el material de apps del
curso detalla los límites). Eso no invalida la herramienta: las
**comparaciones relativas hechas con el mismo aparato** — ¿cuánto
subió?, ¿qué punto de la sala es más ruidoso? — son confiables, y un
dato honesto siempre viaja con sus condiciones: qué app, qué aparato, a
qué distancia, qué ponderación. Esa disciplina — el número *y* sus
condiciones — es la mitad de lo que la sesión evalúa.

## Preguntas que la sesión va a responder

1. ¿Cuántos dB sube el nivel al duplicar las fuentes — y cuántas
   fuentes iguales hacen falta para que algo suene *el doble* de
   fuerte?
2. ¿Qué forma tiene SU curva isofónica: cuánto nivel extra le pide su
   oído a un grave (y a un muy agudo) para sonar igual de fuerte que
   1000 Hz? ¿Coincide con la de su compañero?
3. ¿Qué le pasa a una mezcla musical cuando se reproduce muy suave, y
   por qué?
4. ¿Cuánto discrepan dos apps SPL midiendo lo mismo — y qué se puede
   afirmar honestamente con un micrófono sin calibrar?
5. ¿Cuántas horas de ensayo "caben" en un día a 91 dB(A), y qué compra,
   en tiempo, un protector auditivo?

## Referencias del capítulo

- Benade (1990), cap. 13: secs. 13.1–13.5 (umbrales, decibel, sones,
  sonoridad combinada) y 13.8 (el sonómetro y sus ponderaciones); los
  experimentos de 13.9 (EEQ) son la fuente de varias estaciones.
- Campbell & Greated (1987), cap. 3, sección *Loudness* — sonoridad
  dentro de la anatomía de la nota musical.
- Roederer (1997), cap. 3, secs. 3.4–3.5 (pp. 79–119) — intensidad,
  nivel y el mecanismo de percepción de la sonoridad; en español.
- Rossing, Moore & Wheeler (2002), cap. 6 — decibeles, fones y sones
  con ejercicios; caps. 30–31 — ruido ambiental y salud auditiva.
