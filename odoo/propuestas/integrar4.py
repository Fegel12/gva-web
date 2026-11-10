# -*- coding: utf-8 -*-
"""Version 4: sombra por elipses (contacto en cada bota + proyeccion larga)."""
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
    alfa = np.array(samu.split()[3])

    lienzo = BASE.copy().convert("RGBA")

    # ---- proyeccion larga y muy suave hacia la derecha -------------------
    proy = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(proy)
    pw, ph = int(ancho * 1.15), max(8, int(alto * 0.09))
    cx = x + ancho // 2 + int(ancho * 0.42)
    cy = y + alto - int(ph * 0.25)
    d.ellipse([cx - pw // 2, cy - ph // 2, cx + pw // 2, cy + ph // 2], fill=80)
    proy = proy.filter(ImageFilter.GaussianBlur(26))
    capa = Image.new("RGBA", (W, H), (20, 30, 42, 0)); capa.putalpha(proy)
    lienzo.alpha_composite(capa)

    # ---- contacto: una elipse por bota -----------------------------------
    filas = alfa[-int(alto * 0.06):, :]
    cols = np.where((filas > 40).any(axis=0))[0]
    grupos = []
    if len(cols):
        cortes = np.where(np.diff(cols) > ancho * 0.12)[0]
        inicio = 0
        for corte in list(cortes) + [len(cols) - 1]:
            grupos.append((cols[inicio], cols[corte])); inicio = corte + 1
    if not grupos:
        grupos = [(int(ancho * 0.2), int(ancho * 0.45)), (int(ancho * 0.55), int(ancho * 0.8))]

    zona = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(zona)
    for izq, der in grupos:
        an = max(14, int((der - izq) * 1.35))
        al = max(5, int(an * 0.30))
        cxx = x + (izq + der) // 2
        cyy = y + alto - al // 3
        d.ellipse([cxx - an // 2, cyy - al // 2, cxx + an // 2, cyy + al // 2], fill=190)
    zona = zona.filter(ImageFilter.GaussianBlur(5))
    cont = Image.new("RGBA", (W, H), (12, 18, 26, 0)); cont.putalpha(zona)
    lienzo.alpha_composite(cont)

    # ---- reflejo tenue ---------------------------------------------------
    refl = samu.transpose(Image.FLIP_TOP_BOTTOM)
    r_alto = int(alto * 0.42)
    refl = refl.resize((ancho, r_alto), Image.LANCZOS).filter(ImageFilter.GaussianBlur(5))
    refl.putalpha(refl.split()[3].point(lambda v: int(v * 0.12)))
    lienzo.alpha_composite(refl, (x, y + alto - int(r_alto * 0.12)))

    # ---- luz direccional sobre Samu -------------------------------------
    rgb = np.asarray(samu.convert("RGB")).astype(np.float32)
    grad = np.linspace(1.08, 0.90, ancho)[None, :, None]
    rgb = rgb * (1 + (grad - 1) * 0.75)
    rgb = rgb * np.linspace(0.93, 1.0, alto)[:, None, None]
    s = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA")
    s = ImageEnhance.Color(s).enhance(0.90)
    s.putalpha(samu.split()[3].filter(ImageFilter.GaussianBlur(0.6)))
    lienzo.alpha_composite(s, (x, y))

    # ---- grano -----------------------------------------------------------
    final = np.asarray(lienzo.convert("RGB")).astype(np.int16)
    final = final + np.random.default_rng(11).normal(0, 2.0, final.shape[:2])[..., None]
    Image.fromarray(np.clip(final, 0, 255).astype(np.uint8)).save(salida, quality=94)
    print(salida, "bota-grupos", grupos)


integrar("samu-fino-a.png", "natural-A.png", 0.70, 0.745, 0.975)
integrar("samu-fino-c.png", "natural-C.png", 0.58, 0.585, 0.945)
