#!/bin/bash
# Abre el panel de sesión: lo arranca si no está corriendo y abre el navegador.
#
# Toda la lógica del lanzador vive aquí, en el repo, y no dentro de la app de
# macOS: así se puede probar desde el terminal (`bash panel/abrir-panel.sh`) y
# se versiona con el resto. La app del Dock es solo un envoltorio que llama a
# este script.
#
# Es idempotente: si el panel ya responde, no levanta una segunda instancia —
# solo abre la pestaña.
#
# Uso:  abrir-panel.sh [--permitir-publicar]

set -u

PUERTO=8767
URL="http://127.0.0.1:${PUERTO}/"
EXTRA="${1:-}"

# La raíz del repo se deduce de dónde está este script, para que la app siga
# funcionando si la carpeta del curso cambia de lugar (basta reinstalarla).
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Ruta absoluta: una app lanzada desde el Finder no hereda el PATH del shell,
# así que `python3` a secas no encontraría el de miniforge.
PY="/Users/pdelac/miniforge3/bin/python3"
[ -x "$PY" ] || PY="$(command -v python3 || true)"

vivo() { /usr/bin/curl -s -o /dev/null --max-time 1 "$URL"; }

if ! vivo; then
  [ -n "$PY" ] && [ -x "$PY" ] || { echo "No se encontró python3." >&2; exit 1; }
  [ -f "$REPO/panel/panel.py" ] || { echo "No está $REPO/panel/panel.py" >&2; exit 1; }
  cd "$REPO" || exit 1
  # Desacoplado: el servidor sobrevive a que termine la app del Dock.
  /usr/bin/nohup "$PY" "$REPO/panel/panel.py" \
      --puerto "$PUERTO" --no-abrir $EXTRA >/dev/null 2>&1 &
  # El primer arranque lee el índice desde Google Drive: puede tardar.
  for _ in $(seq 1 40); do
    sleep 0.5
    vivo && break
  done
fi

if vivo; then
  /usr/bin/open "$URL"
  exit 0
fi

echo "El panel no respondió en 20 s." >&2
exit 1
