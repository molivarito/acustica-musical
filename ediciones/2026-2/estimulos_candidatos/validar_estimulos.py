# validar_estimulos.py — ficha técnica + lámina (forma de onda y espectrograma)
# para cada audio candidato a estímulo del curso AM.
#
# Uso: python3 validar_estimulos.py <archivo-o-directorio> [...]
# Por cada audio genera <nombre>_lamina.png junto al archivo e imprime la ficha.

import subprocess, sys, json, tempfile, os
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import spectrogram
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

EXTS = {".wav", ".mp3", ".ogg", ".oga", ".flac", ".aiff", ".aif", ".m4a", ".opus"}


def ficha_ffprobe(ruta):
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", "-show_streams", str(ruta)],
        capture_output=True, text=True).stdout
    info = json.loads(out or "{}")
    st = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), {})
    return {
        "codec": st.get("codec_name"),
        "fs": int(st.get("sample_rate") or 0),
        "canales": st.get("channels"),
        "dur_s": float(info.get("format", {}).get("duration") or 0),
        "bitrate": info.get("format", {}).get("bit_rate"),
    }


def a_mono_wav(ruta):
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    subprocess.run(["ffmpeg", "-y", "-v", "quiet", "-i", str(ruta),
                    "-ac", "1", "-ar", "44100", tmp.name], check=True)
    fs, x = wavfile.read(tmp.name)
    os.unlink(tmp.name)
    x = x.astype(np.float64)
    if x.size and np.abs(x).max() > 0:
        x = x / np.abs(x).max() * 10 ** (-0.5 / 20)  # normaliza solo para graficar
    return fs, x


def analizar(ruta):
    ruta = Path(ruta)
    meta = ficha_ffprobe(ruta)
    fs, x = a_mono_wav(ruta)
    t = np.arange(x.size) / fs

    # niveles del archivo original (sin la normalización de arriba)
    raw = subprocess.run(
        ["ffmpeg", "-i", str(ruta), "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    niveles = {k: l.split(":")[-1].strip()
               for l in raw.splitlines()
               for k in ("mean_volume", "max_volume") if k in l}

    f, tt, S = spectrogram(x, fs, nperseg=2048, noverlap=1536)
    SdB = 10 * np.log10(S + 1e-12)

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 7),
                                 gridspec_kw={"height_ratios": [1, 2]})
    a1.plot(t, x, lw=0.4, color="#1f4e79")
    a1.set_xlim(0, t[-1] if t.size else 1)
    a1.set_ylabel("presión (norm.)")
    a1.set_title(f"{ruta.name} — {meta['dur_s']:.1f} s · {meta['codec']} · "
                 f"{meta['fs']} Hz · {meta['canales']} can.")
    im = a2.pcolormesh(tt, f, SdB, shading="auto", cmap="magma",
                       vmin=SdB.max() - 80, vmax=SdB.max())
    a2.set_ylim(0, 8000)
    a2.set_xlabel("tiempo (s)")
    a2.set_ylabel("frecuencia (Hz)")
    fig.colorbar(im, ax=a2, label="nivel (dB)")
    fig.tight_layout()
    png = ruta.with_name(ruta.stem + "_lamina.png")
    fig.savefig(png, dpi=110)
    plt.close(fig)

    print(f"\n== {ruta.name}")
    print(f"   {meta['dur_s']:.1f} s · {meta['codec']} · {meta['fs']} Hz · "
          f"{meta['canales']} canales · bitrate {meta['bitrate']}")
    print(f"   niveles: {niveles}")
    print(f"   lámina: {png}")


if __name__ == "__main__":
    objetivos = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        objetivos += sorted(q for q in p.iterdir() if q.suffix.lower() in EXTS) \
            if p.is_dir() else [p]
    if not objetivos:
        sys.exit("sin archivos de audio que analizar")
    for o in objetivos:
        try:
            analizar(o)
        except Exception as e:
            print(f"\n== {o} — ERROR: {e}")
