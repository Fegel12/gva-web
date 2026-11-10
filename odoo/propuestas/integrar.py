# -*- coding: utf-8 -*-
"""Integra a Samu en la foto de oficina con un acabado mas natural."""
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

BASE = Image.open("opcion-C-oficina.png").convert("RGB")
W, H = BASE.size


def integrar(recorte, salida, alto_rel, x_rel, y_rel):
    samu = Image.open(recorte).convert("RGBA")
    alto = int(H * alto_rel)
    ancho = int(samu.width * alto / samu.height)
    samu = samu.resize((ancho, alto), Image.LANCZOS)

    x = int(W * x_rel) - ancho // 2
    y = int(H * y_rel) - alto
    x = max(8, min(x, W - ancho - 8))
    y = max(8, min(y, H - alto - 2))

    lienzo = BASE.copy().convert("RGBA")

    # --- 1. reflejo en el piso (el suelo es satinado) ---------------------
    refl = samu.transpose(Image.FLIP_TOP_BOTTOM)
    r_alto = int(alto * 0.55)
    refl = refl.resize((ancho, r_alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(3))
    r_alfa = refl.split()[3].point(lambda v: int(v * 0.16))
    refl.putalpha(r_alfa)
    lienzo.alpha_composite(refl, (x, y + alto - int(r_alto * 0.06)))

    # --- 2. sombra proyectada suave (la luz entra por la ventana izquierda)
    proy_h = max(8, int(alto * 0.22))
    proy = samu.split()[3].resize((int(ancho * 1.02), proy_h), Image.LANCZOS)
    proy = proy.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * 0.42))
    capa = Image.new("RGBA", proy.size, (24, 34, 46, 0))
    capa.putalpha(proy)
    lienzo.alpha_composite(capa, (max(0, x + 28), y + alto - int(proy_h * 0.45)))

    # --- 3. sombra de contacto bajo los pies -----------------------------
    ew, eh = int(ancho * 0.92), max(8, int(alto * 0.075))
    zona = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(zona)
    d.ellipse([x + (ancho - ew) // 2, y + alto - eh // 2,
               x + (ancho + ew) // 2, y + alto + eh // 2], fill=125)
    zona = zona.filter(ImageFilter.GaussianBlur(11))
    cont = Image.new("RGBA", (W, H), (16, 24, 32, 0))
    cont.putalpha(zona)
    lienzo.alpha_composite(cont)

    # --- 4. ajuste de color y contraste para que case con la foto --------
    s = samu.convert("RGB")
    s = ImageEnhance.Color(s).enhance(0.88)                 # menos saturado
    s = ImageEnhance.Contrast(s).enhance(0.94)              # menos "render"
    s = ImageEnhance.Brightness(s).enhance(1.01)
    arr = np.asarray(s).astype(np.float32)
    arr[..., 0] *= 1.012                                     # un pelo mas calido
    arr[..., 2] *= 0.988
    s = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    s = s.convert("RGBA")
    alfa = samu.split()[3].filter(ImageFilter.GaussianBlur(0.7))
    s.putalpha(alfa)
    lienzo.alpha_composite(s, (x, y))

    # --- 5. grano fino uniforme -----------------------------------------
    final = np.asarray(lienzo.convert("RGB")).astype(np.int16)
    rng = np.random.default_rng(7)
    ruido = rng.normal(0, 2.2, final.shape[:2])[..., None]
    final = np.clip(final + ruido, 0, 255).astype(np.uint8)
    Image.fromarray(final).save(salida, quality=94)
    print(salida, "samu", (ancho, alto), "pos", (x, y))


integrar("samu-fino-a.png", "pulida-A.png", 0.70, 0.745, 0.975)
integrar("samu-fino-c.png", "pulida-C.png", 0.58, 0.585, 0.945)
