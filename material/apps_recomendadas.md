# Apps recomendadas — análisis de sonido en el celular

**Publicación**: esta lista se publica junto con la lectura previa de
s02 (la semana anterior a esa sesión), porque en s02 se estrena el
espectrograma como "microscopio del curso" (OA4.1). Todas las apps
listadas son gratuitas (o con versión gratuita suficiente para el
curso). Basta UNA app de cada tipo por celular; el mínimo operativo es
2 celulares funcionando por grupo.

## Espectrograma (se usa desde s02: talleres "microscopio", "la sartén" s03, "mapa de la cuerda" s04)

| App | Plataforma | Nota |
|---|---|---|
| Spectroid (verificado jul-2026: activa en Play Store, actualizada, gratuita, +1 M descargas) | Android | Espectro + espectrograma en tiempo real; permite congelar y leer frecuencias con el cursor — lo que piden las guías. |
| phyphox (RWTH Aachen) | Android e iOS | Suite de física con herramientas de audio (espectro, historial de frecuencia); gratuita y sin publicidad; buena opción única si no se quiere instalar varias apps. |
| SpectrumView (verificado jul-2026: nombre exacto confirmado, de Oxford Wave Research Ltd.) | iOS | Espectrograma con eje de frecuencia (lineal o logarítmico), cursor de lectura y congelado de pantalla. La versión gratuita cubre el mínimo del curso; funciones extra (zoom por pinza, triple peak-hold, exportar snapshot) son compras dentro de la app (US$0,99–1,99 c/u), no imprescindibles. |

Requisito mínimo para el curso (cualquier app sirve si lo cumple): ejes
visibles de tiempo y frecuencia, posibilidad de congelar/capturar la
pantalla, y lectura de la frecuencia de un parcial (cursor o retícula).

## Afinador (se usa desde s04: armónicos naturales, "estirar, acortar, engordar", y en el proyecto)

| App | Plataforma | Nota |
|---|---|---|
| GuitarTuna (verificado jul-2026: el modo cromático viene incluido en la versión gratuita, sin muro de pago; la suscripción Premium solo saca publicidad y agrega canciones/acordes, no el modo cromático) | Android e iOS | Afinador cromático de uso masivo; para el curso debe usarse en modo cromático (lectura en Hz o nota+cents), no en modo "6 cuerdas". Revisar en clase que la pantalla muestre el valor en Hz y no solo nota+cents (varía según skin/versión). |
| Cualquier afinador cromático que muestre **la frecuencia en Hz** | ambas | Las guías de s04 piden anotar Hz y calcular razones: un afinador que solo muestra la nota no basta. |

## Medidor de nivel sonoro / SPL (se usa desde s06: decibel y sonoridad; salida de medición, formato 8)

| App | Plataforma | Nota |
|---|---|---|
| NIOSH Sound Level Meter | iOS | Desarrollada por el instituto NIOSH (EE. UU.) con calibración de referencia documentada; la opción más confiable en celular. |
| **Sound Meter**, de rootApps (paquete `com.gamebasic.decibel`) (verificado jul-2026: app fijada — hay varias homónimas en Play Store; esta tiene ~4,5★ sobre 180 mil reseñas, +10 M instalaciones, gratuita, con calibración por dispositivo y gráfico de min/prom/máx) | Android | Medidor SPL básico; suficiente para comparaciones relativas. Usar siempre esta ficha específica (no otra "Sound Meter") para que todos los grupos midan con la misma app. |
| Decibel X (verificado jul-2026: la versión gratuita **solo mide dB(Z)**, no dB(A) — la ponderación A/C queda tras compra dentro de la app; además limita exportación de audio a ~2 clips/1 min) | Android e iOS | Medidor SPL con ponderaciones A/C e historial. Si la actividad de s06 requiere dB(A) específicamente, usar NIOSH Sound Level Meter (gratis y con dB(A) sin restricciones) en su lugar, o Decibel X solo para comparaciones relativas sin ponderar. |

## Tiempo de reverberación / RT60 (se usa en s14: salida de medición)

| App | Plataforma | Nota |
|---|---|---|
| **ClapIR — Acoustics Measurement**, de Stephen Tarzia (verificado jul-2026: gratuita, sin compras dentro de la app, código abierto, basada en investigación de Northwestern University — Seetharaman & Tarzia) | iOS | Mide RT60 y respuesta en frecuencia analizando un aplauso grabado con el micrófono. Sin costo y sin publicidad; la mejor opción iOS para esta salida por su origen académico documentado. |
| **Room Acoustics: RT60 Meter** (paquete `com.simonj.roomacoustics`), del mismo desarrollador de otras utilidades de física/audio bien evaluadas (Frequency Counter, Tone Generator, AudioScope) | Android | Mide RT60 con un aplauso, muestra curva de decaimiento, ruido de fondo y estimación de bandas de frecuencia; funciona sin hardware extra. **[POR VERIFICAR: modelo de precios exacto (gratis/con anuncios vs. compra) — no se pudo confirmar con certeza desde las fichas indexadas; revisar directamente en Play Store antes de recomendarla en la guía de s14]**. |

Advertencia pedagógica: ambas apps miden RT60 mediante el método del
aplauso, que la literatura de acústica de salas considera aproximado
(el aplauso es un impulso débil y poco reproducible comparado con una
fuente calibrada). Para el objetivo de s14 —que el grupo compare
espacios y discuta el efecto de materiales y volumen— es suficiente;
no reportar los valores como medición certificada de laboratorio.

## Advertencias de calibración (leerlas antes de confiar en un número)

- **El micrófono del celular no está calibrado.** Los valores absolutos
  de SPL pueden variar sensiblemente según el aparato: el estudio de
  referencia (Kardous & Shaw, 2014, *J. Acoust. Soc. Am.*, "Evaluation
  of smartphone sound measurement applications") evaluó 130 apps iOS y
  62 Android contra un sonómetro de referencia y encontró que solo un
  puñado (4 de cada plataforma) se acercaba a ±2 dB(A); la mayoría del
  resto se desviaba más, con peor desempeño y más variabilidad en
  Android sin calibración externa **(verificado jul-2026, cita
  confirmada; el rango "±5–10 dB" de esta guía es una simplificación
  razonable del hallazgo general del estudio, no una cifra textual del
  paper)**. Regla del curso: las mediciones absolutas se toman como
  aproximadas; las **comparaciones
  relativas hechas con el MISMO celular** (¿cuánto sube al acercarse?,
  ¿cuál fuente es más intensa?) sí son confiables.
- **Respuesta en frecuencia limitada**: los micrófonos de celular
  atenúan los graves (bajo ~100 Hz) y los muy agudos; un bajo "débil"
  en la app puede ser un micrófono sordo, no un sonido débil.
- **Techo de muestreo**: el espectrograma llega hasta ~22 kHz porque la
  app muestrea a 44,1 kHz — es un límite de la herramienta, no del
  sonido (se discute explícitamente en el taller de s02).
- **Control automático de ganancia (AGC)**: muchos celulares ajustan
  solos la sensibilidad del micrófono; si la app lo permite,
  desactivarlo. Con AGC activo, las comparaciones de nivel entre
  momentos distintos no valen.
- **La disparidad entre apps es dato, no estorbo**: en s02 la guía pide
  anotar qué app y qué celular se usó junto a cada observación; los
  distintos techos y resoluciones alimentan la discusión de límites de
  la herramienta (OA4.1).
