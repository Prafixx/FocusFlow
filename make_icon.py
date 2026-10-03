# make_icon.py
# Disegna l'icona di FocusFlow con Pillow e la salva in assets/icon.ico (e icon.png).
# Si lancia una volta sola:  python make_icon.py
from pathlib import Path

from PIL import Image, ImageDraw

ROSSO = (229, 83, 61, 255)
BIANCO = (255, 255, 255, 255)


def disegna(lato):
    img = Image.new("RGBA", (lato, lato), (0, 0, 0, 0))     # sfondo trasparente
    d = ImageDraw.Draw(img)

    margine = lato // 16
    d.rounded_rectangle(
        (margine, margine, lato - margine, lato - margine),
        radius=lato // 4, fill=ROSSO,
    )

    centro = lato / 2
    raggio = lato * 0.28
    spessore = max(2, lato // 14)
    d.ellipse(                                               # il quadrante dell'orologio
        (centro - raggio, centro - raggio, centro + raggio, centro + raggio),
        outline=BIANCO, width=spessore,
    )
    d.line((centro, centro, centro, centro - raggio * 0.7), fill=BIANCO, width=spessore)   # lancetta lunga
    d.line((centro, centro, centro + raggio * 0.5, centro), fill=BIANCO, width=spessore)   # lancetta corta
    return img


def main():
    cartella = Path(__file__).parent / "assets"
    cartella.mkdir(exist_ok=True)

    grande = disegna(256)
    grande.save(cartella / "icon.png")
    grande.save(
        cartella / "icon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )
    print("Icona creata in:", cartella)


if __name__ == "__main__":
    main()
