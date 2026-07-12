# Convenciones para demos interactivas HTML

## Principios
- Una demo = un concepto. Si la demo intenta ilustrar dos ideas, dividirla.
- La demo debe sonar: en acústica musical el audio no es opcional. Usar
  Web Audio API para síntesis y reproducción en tiempo real.
- Debe funcionar como archivo único, sin servidor ni dependencias
  externas obligatorias (solo CDN si es imprescindible, p. ej. una
  librería de gráficos).

## Estructura del archivo
- Un solo archivo `.html` autocontenido (CSS y JS embebidos).
- Nombre: `demo_<tema>.html` en minúsculas con guiones bajos
  (ej: `demo_modos_cuerda.html`), guardado en `sesiones/sXX/demos/`.
- Encabezado visible: título, sesión y una frase que diga qué explorar.
- Panel de controles (sliders, botones) claramente rotulados con unidades.
- Incluir un bloque breve "¿Qué observar?" con 2-3 preguntas guía para el
  uso en clase (aprendizaje activo, no demostración pasiva).

## Estética
- Editorial/científica y sobria: fondo claro, tipografía serif para texto
  y sans-serif para controles y ejes, paleta contenida (2-3 colores).
- Gráficos con ejes rotulados y unidades; nada de decoración gratuita.
- Responsive básico: usable en el proyector de la sala y en un notebook.

## Técnica
- JavaScript vanilla; Canvas o SVG para visualización.
- Audio: iniciar el AudioContext solo tras interacción del usuario
  (requerimiento de los navegadores) y proveer botón de detener.
- Comentarios en el código en español, suficientes para que el profesor
  pueda modificar parámetros sin ayuda.
