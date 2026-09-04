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

- **`e05_bajo_parlante_chico.wav`** y **`e05_bajo_cuerdas_al_aire.wav`**
  — grabación propia del profesor (2026-09-04): contrabajo pizzicato en
  su casa, iPhone 15 con Notas de Voz en calidad sin pérdida (ALAC
  48 kHz mono). Toma cruda: `ediciones/2026-2/estimulos_candidatos/bajo_casa_toma1.m4a`.
  La primera es la línea E1 E1 G1 G1 A1 A1 E1 (escucha del día de s05);
  la segunda, las cuerdas al aire E1 E1 A1 D2 G2. Modificaciones: recorte,
  desvanecidos, WAV mono 44,1 kHz, normalización a −1 dBFS. Sin
  restricciones.
- **`e05_octavas_piano.wav`** — derivada de las notas `Piano.mf.C2`,
  `Piano.mf.C3`, `Piano.mf.C6` y `Piano.mf.C7` de los *Musical
  Instrument Samples* de la University of Iowa (Lawrence Fritts,
  Electronic Music Studios), <https://theremin.music.uiowa.edu/MISpiano.html>,
  licencia: "may be downloaded and used for any projects, without
  restrictions" (<https://theremin.music.uiowa.edu/MIS.html>).
  Modificaciones: recorte a 3,6 s con desvanecido, mono 44,1 kHz,
  ataques alineados, cada nota normalizada al mismo pico (las agudas
  son mucho más débiles en el original), mezcla de los pares
  simultáneos C2+C3 y C6+C7, normalización global a −1 dBFS.
  Atribución: "University of Iowa Musical Instrument Samples (L. Fritts)".

- **`e05_tonos_220_440.wav`**, **`e05_tonos_440_880.wav`**,
  **`e05_shepard_escala.wav`**, **`e05_shepard_glissando.wav`** y
  **`e05_tritono_deutsch.wav`** — sintetizados con NumPy el 2026-09-04
  (script en el historial de la sesión; senos puros de 3 s + 1 s + 3 s;
  tonos de Shepard: pila de senos por octavas de ~33 Hz a 8 kHz con
  envolvente gaussiana en log-frecuencia centrada en 500 Hz, σ = 1,3
  octavas; escala de 12 semitonos × 0,45 s × 3 vueltas; glissando de
  1 octava cada 4 s durante 20 s; tritono: 12 pares C–F♯, D–G♯, E–A♯,
  F♯–C, G♯–D, A♯–E, C♯–G, D♯–A, F–B, G–C♯, A–D♯, B–F, 0,5 s cada tono,
  2,5 s entre pares; aproximación a Shepard 1964 y Deutsch 1986). Sin
  restricciones.

- **`e05_campana.wav`** — derivada de "Strike of the hour of St. Georgen
  church in St. Gallen SG 01" de Martin Thurnherr (Matutinho), Wikimedia
  Commons, <https://commons.wikimedia.org/wiki/File:Strike_of_the_hour_of_St._Georgen_church_in_St._Gallen_SG_01.wav>,
  licencia **CC-BY-SA 4.0** (el derivado queda CC-BY-SA 4.0).
  Modificaciones: recorte a los dos últimos golpes (27,8–34,4 s del
  original), WAV mono 44,1 kHz, desvanecidos, normalización a −1 dBFS.
  Uso: nota de golpe de la campana (s05, módulo 1). Atribución: "Martin
  Thurnherr, Wikimedia Commons, CC-BY-SA 4.0".

Los `*_lamina.png` son las fichas de validación (forma de onda +
espectrograma) generadas con
`ediciones/2026-2/estimulos_candidatos/validar_estimulos.py`.
