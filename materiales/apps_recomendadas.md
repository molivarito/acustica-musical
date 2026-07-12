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
| Spectroid **[POR VERIFICAR: disponibilidad actual en Play Store]** | Android | Espectro + espectrograma en tiempo real; permite congelar y leer frecuencias con el cursor — lo que piden las guías. |
| phyphox (RWTH Aachen) | Android e iOS | Suite de física con herramientas de audio (espectro, historial de frecuencia); gratuita y sin publicidad; buena opción única si no se quiere instalar varias apps. |
| SpectrumView **[POR VERIFICAR: nombre exacto y versión gratuita en App Store]** | iOS | Espectrograma con eje de frecuencia legible y captura de pantalla. |

Requisito mínimo para el curso (cualquier app sirve si lo cumple): ejes
visibles de tiempo y frecuencia, posibilidad de congelar/capturar la
pantalla, y lectura de la frecuencia de un parcial (cursor o retícula).

## Afinador (se usa desde s04: armónicos naturales, "estirar, acortar, engordar", y en el proyecto)

| App | Plataforma | Nota |
|---|---|---|
| GuitarTuna **[POR VERIFICAR: que la versión gratuita muestre el modo cromático]** | Android e iOS | Afinador cromático de uso masivo; para el curso debe usarse en modo cromático (lectura en Hz o nota+cents), no en modo "6 cuerdas". |
| Cualquier afinador cromático que muestre **la frecuencia en Hz** | ambas | Las guías de s04 piden anotar Hz y calcular razones: un afinador que solo muestra la nota no basta. |

## Medidor de nivel sonoro / SPL (se usa desde s06: decibel y sonoridad; salida de medición, formato 8)

| App | Plataforma | Nota |
|---|---|---|
| NIOSH Sound Level Meter | iOS | Desarrollada por el instituto NIOSH (EE. UU.) con calibración de referencia documentada; la opción más confiable en celular. |
| Sound Meter **[POR VERIFICAR: hay varias apps homónimas en Play Store; elegir una y fijarla para todo el curso]** | Android | Medidor SPL básico; suficiente para comparaciones relativas. |
| Decibel X **[POR VERIFICAR: límites de la versión gratuita]** | Android e iOS | Medidor SPL con ponderaciones A/C e historial. |

## Advertencias de calibración (leerlas antes de confiar en un número)

- **El micrófono del celular no está calibrado.** Los valores absolutos
  de SPL pueden errar en ±5–10 dB según el aparato **[POR VERIFICAR:
  rango exacto según estudios de apps SPL]**. Regla del curso: las
  mediciones absolutas se toman como aproximadas; las **comparaciones
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
