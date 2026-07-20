# canvas — integración con Canvas (MUC860-1 Acústica Musical)

Sincroniza la estructura de módulos en Canvas
(`https://cursos.canvas.uc.cl`) a partir de un archivo de configuración
(`canvas.yml`). Pensado para el profesor: se corre a mano cuando cambia
el material o antes de cada semana.

## Archivos

- `publicar_canvas.py` — el CLI. Solo requiere stdlib + PyYAML (usa
  `urllib.request`, no `requests`).
- `canvas.yml` — la estructura de módulos e ítems (fuente de verdad).
  Generada a partir de la sidebar de `_quarto.yml`: 15 sesiones +
  información del curso + libro + materiales. **No incluye** las pautas
  de evaluación ni el guión del profesor (excluidos del sitio público en
  `_quarto.yml`) ni la bitácora de diseño (documento de proceso interno).
- `README.md` — esto.

## El token de Canvas

El script lee el token de acceso de la API en este orden:

1. Variable de entorno `CANVAS_TOKEN`.
2. Si no está definida, el archivo `~/.canvas_token` (un archivo de
   texto con el token y nada más, fuera del repo). Es el mismo token
   personal usado para IEE2103; sirve para cualquier curso donde el
   profesor esté matriculado como docente.

**El token nunca debe escribirse en `canvas.yml`, en el código, ni en
ningún archivo dentro de este repo.**

## Regla de oro: nunca se publica nada solo

- Crea todo lo nuevo (módulos e ítems) con `published: false`.
- **Nunca** cambia el estado de publicación de algo que ya existía en
  Canvas.
- **Nunca** borra ni despublica nada — si algo está en Canvas pero no
  en `canvas.yml`, se lista como "extra" y no se toca.
- Publicar cada módulo/ítem cuando corresponda es una acción manual
  del profesor, hecha desde la interfaz de Canvas.

Curso: `curso_id: 112005` (MUC860-1, 2do semestre 2026).

## Uso

```bash
cd canvas

# ver el estado actual del curso en Canvas (módulos, ítems, publicación)
python3 publicar_canvas.py estado

# ver qué haría sync sin escribir nada
python3 publicar_canvas.py sync --dry-run

# aplicar los cambios (crea/actualiza; nunca borra ni publica)
python3 publicar_canvas.py sync

# revisar que las URL del sitio público no estén rotas (HEAD/GET, reporta 404s)
python3 publicar_canvas.py verificar
```

Ver el README de `SyS/canvas/` para el detalle completo del
funcionamiento del script (formato de `canvas.yml`, semántica de
`sync`, etc.) — es el mismo script sin modificaciones más allá del
texto de ayuda.
