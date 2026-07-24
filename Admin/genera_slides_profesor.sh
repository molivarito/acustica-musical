#!/bin/bash
# Genera los decks de slides del profesor (HTML autocontenidos) en
# Admin/slides_profesor/ — carpeta PRIVADA (gitignored, solo en Drive).
#
# Las slides están excluidas del sitio público: este script es la única
# vía de "publicación". Cada deck se renderiza con recursos embebidos
# (un solo archivo .html, se abre con doble clic) y con las demos
# apuntando al sitio público por URL absoluta (las demos SÍ son material
# de alumnos, así que cargarlas desde el sitio no expone nada).
#
# Uso:  bash Admin/genera_slides_profesor.sh          (los 15 decks)
#       bash Admin/genera_slides_profesor.sh 05       (solo la sesión 05)
set -e
cd "$(dirname "$0")/.."
SITIO="https://molivarito.github.io/acustica-musical"
mkdir -p Admin/slides_profesor

SESIONES="${1:+s$1}"
[ -z "$SESIONES" ] && SESIONES=$(seq -f "s%02g" 1 15)

for s in $SESIONES; do
  src="sesiones/$s/slides/slides_$s.qmd"
  [ -f "$src" ] || { echo "no existe $src, salto"; continue; }
  tmp="sesiones/$s/slides/slides_${s}_profesor.qmd"
  # iframes de demos: de ruta relativa a URL absoluta del sitio
  sed -E \
    -e "s|background-iframe=\"\.\./demos/|background-iframe=\"$SITIO/sesiones/$s/demos/|g" \
    -e "s|background-iframe=\"\.\./\.\./(s[0-9]+)/demos/|background-iframe=\"$SITIO/sesiones/\1/demos/|g" \
    "$src" > "$tmp"
  conda run -n base quarto render "$tmp" --to revealjs -M embed-resources:true
  # la salida puede quedar junto al fuente o bajo _site según el contexto
  out="sesiones/$s/slides/slides_${s}_profesor.html"
  [ -f "$out" ] || out="_site/sesiones/$s/slides/slides_${s}_profesor.html"
  mv "$out" "Admin/slides_profesor/slides_$s.html"
  rm -f "$tmp"
  rm -rf "sesiones/$s/slides/slides_${s}_profesor_files" \
         "_site/sesiones/$s/slides/slides_${s}_profesor_files"
  echo "✓ $s"
done
echo "Listo: abra Admin/slides_profesor/index.html"
