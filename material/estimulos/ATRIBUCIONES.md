# Atribuciones de los estímulos de audio

Registro de origen y licencia de cada archivo (los derivados conservan
la licencia de su fuente). Búsqueda y validación: 2026-08-13/14, ver
`ediciones/2026-2/estimulos_candidatos/README_VALIDACION.md`.

- **`e01_linea_base.wav`** — captura del golpe que el profesor dio EN
  VIVO en la sala durante la línea base de s01 (2026-08-07, sin sesión
  de grabación formal): los estudiantes oyeron el golpe directo, no
  este archivo. El archivo es el registro de ese evento y el candidato
  natural para la re-escucha de s15 (ver pendiente en CLAUDE.md).
  Sin restricciones.
- **`e02_flauta_ataque_soploso.wav`** — derivada de "Flute C4" del
  dataset *good-sounds* (Music Technology Group, UPF), publicada por el
  usuario MTG en Freesound, <https://freesound.org/people/MTG/sounds/354638/>,
  licencia **CC-BY 3.0**. Modificaciones: recorte de silencios,
  conversión a WAV mono 44,1 kHz, normalización a −1 dBFS.
  Atribución: "MTG (dataset good-sounds), Freesound, CC-BY 3.0".
- **`e03_trueno_retardo.wav`** — derivada de "Thunder crack 2B" de
  Jud McCranie, Wikimedia Commons,
  <https://commons.wikimedia.org/wiki/File:Thunder_crack_2B.ogg>,
  licencia **CC-BY-SA 4.0** (el derivado queda CC-BY-SA 4.0).
  Modificaciones: conversión a WAV mono 44,1 kHz, normalización a
  −1 dBFS. Atribución: "Jud McCranie, Wikimedia Commons, CC-BY-SA 4.0".
- **`e04_guitarra_pulsada.wav`** y
  **`e04_guitarra_pulsada_invertida.wav`** — el par del gancho "la nota
  al revés" (s04, módulo 2). Derivadas de la muestra
  `MartinGM2_052__E3_1.wav` (nota E3 de una Martin HD28 Vintage Series)
  de **Jeff Learman** para el *Discord SFZ GM Bank*,
  <https://github.com/sfzinstruments/Discord-SFZ-GM-Bank>, licencia
  **CC0** (dominio público), declarada en el encabezado de
  `026-Acoustic Guitar (steel).sfz` y en la política del README del
  proyecto ("Only CC0, CC-BY, and equivalent licences are allowed").
  Modificaciones: WAV mono 44,1 kHz, desvanecidos de 8 ms en los
  extremos (sin clics), normalización a −1 dBFS y, en la segunda,
  inversión temporal. **Las dos quedan al MISMO nivel a propósito**
  (pico −1,0 dBFS, RMS −21,1 dBFS): en clase el contraste debe oírse
  como cambio de ENVOLVENTE, no de volumen. CC0 no exige atribución;
  por buena práctica: "Jeff Learman, Discord SFZ GM Bank, CC0".

Los `*_lamina.png` son las fichas de validación (forma de onda +
espectrograma) generadas con
`ediciones/2026-2/estimulos_candidatos/validar_estimulos.py`.
