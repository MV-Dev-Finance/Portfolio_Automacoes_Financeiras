# -*- coding: utf-8 -*-
"""Prepara a foto do portfólio: recorta em quadrado (centrando no rosto) e salva em assets/foto.jpg
Uso:  python tools/foto.py caminho/da/sua-foto.jpg
Depois: python tools/build_site.py --pdf
"""
import sys, os
from PIL import Image, ImageOps
try:
    import cv2, numpy as np
except Exception:
    cv2 = None

def main(src):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB"); w, h = im.size
    cx, cy = w / 2, h * 0.42
    if cv2 is not None:
        g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
        casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = casc.detectMultiScale(g, 1.1, 5, minSize=(max(60, w // 12), max(60, w // 12)))
        if len(faces):
            x, y, fw, fh = max(faces, key=lambda f: f[2] * f[3]); cx, cy = x + fw / 2, y + fh / 2 + fh * 0.08
            side = min(min(w, h), int(fw * 3.1))
        else: side = min(w, h)
    else: side = min(w, h)
    side = int(side); l = int(min(max(cx - side / 2, 0), w - side)); t = int(min(max(cy - side / 2, 0), h - side))
    out = im.crop((l, t, l + side, t + side)).resize((640, 640), Image.LANCZOS)
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "foto.jpg")
    out.save(dst, quality=90); print("foto salva em", os.path.abspath(dst))

if __name__ == "__main__":
    main(sys.argv[1])
