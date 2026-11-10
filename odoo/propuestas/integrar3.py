# -*- coding: utf-8 -*-
"""Version 3: luz direccional, oclusion de contacto y sombra proyectada coherente."""
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

BASE = Image.open("opcion-C-oficina.png").convert("RGB")
W, H = BASE.size


def integrar(recorte, salida, alto_rel, x_rel, y_rel, luz_desde_izq=True):
    samu = Image.open(recorte).convert("RGBA")
    alto = int(H * alto_rel)
    ancho = int(samu.width * alto / samu.height)
    samu = samu.resize((ancho, alto), Image.LANCZOS)

    x = int(W * x_rel) - ancho // 2
    y = int(H * y_rel) - alto
    x = max(8, min(x, W - ancho - 8))
    y = max(8, min(y, H - alto - 2))

    lienzo = BASE.copy().convert("RGBA")
    alfa = samu.split()[3]

    # ---------- sombra proyectada (direccion de la ventana) --------------
    proy_h = max(10, int(alto * 0.16))
    proy = alfa.resize((ancho, proy_h), Image.LANCZOS)
    proy = proy.filter(ImageFilter.GaussianBlur(13)).point(lambda v: int(v * 0.50))
    capa = Image.new("RGBA", proy.size, (22, 32, 44, 0)); capa.putalpha(proy)
    dx = int(ancho * 0.32) if luz_desde_izq else -int(ancho * 0.32)
    lienzo.alpha_composite(capa, (max(0, min(x + dx, W - proy.size[0])), y + alto - int(proy_h * 0.55)))

    # ---------- oclusion de contacto -------------------------------------
    ew, eh = int(ancho * 0.80), max(6, int(alto * 0.045))
    zona = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(zona)
    d.ellipse([x + (ancho - ew) // 2, y + alto - eh, x + (ancho + ew) // 2, y + alto + eh // 2], fill=175)
    zona = zona.filter(ImageFilter.GaussianBlur(6))
    cont = Image.new("RGBA", (W, H), (14, 20, 28, 0)); cont.putalpha(zona)
    lienzo.alpha_composite(cont)

    # ---------- reflejo tenue -------------------------------------------
    refl = samu.transpose(Image.FLIP_TOP_BOTTOM)
    r_alto = int(alto * 0.45)
    refl = refl.resize((ancho, r_alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(4))
    ra = refl.split()[3].point(lambda v: int(v * 0.13))
    refl.putalpha(ra)
    lienzo.alpha_composite(refl, (x, y + alto - int(r_alto * 0.10)))

    # ---------- luz sobre Samu (degradado direccional) -------------------
    rgb = np.asarray(samu.convert("RGB")).astype(np.float32)
    grad = np.linspace(1.10, 0.86, ancho)[None, :, None] if luz_desde_izq \
        else np.linspace(0.86, 1.10, ancho)[None, :, None]
    rgb = rgb * (1 + (grad - 1) * 0.85)
    # sombra en la base (la luz viene de arriba)
    ven = np.linspace(0.90, 1.0, alto)[:, None, None]
    rgb = rgb * ven
    s = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA")
    s = ImageEnhance.Color(s).enhance(0.90)
    s = ImageEnhance.Contrast(s).enhance(0.96)
    s.putalpha(alfa.filter(ImageFilter.GaussianBlur(0.6)))
    lienzo.alpha_composite(s, (x, y))

    # ---------- grano ----------------------------------------------------
    final = np.asarray(lienzo.convert("RGB")).astype(np.int16)
    ruido = np.random.default_rng(3).normal(0, 2.0, final.shape[:2])[..., None]
    Image.fromarray(np.clip(final + ruido, 0, 255).astype(np.uint8)).save(salida, quality=94)
    print(salida, "samu", (ancho, alto), "pos", (x, y), "sombra dx", dx)


integrar("samu-fino-a.png", "final-A.png", 0.70, 0.745, 0.975)
integrar("samu-fino-c.png", "final-C.png", 0.58, 0.585, 0.945)
