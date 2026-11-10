# -*- coding: utf-8 -*-
"""Genera los bloques HTML listos para Odoo (autocontenidos, imágenes en data URI)."""
import base64, io, os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "odoo")
os.makedirs(SALIDA, exist_ok=True)

TURQ, VERDE, GRIS, NOCHE = "#00B7B5", "#00B140", "#2E3540", "#0E1A2B"


def data_uri(ruta, ancho=700, calidad=82):
    im = Image.open(ruta).convert("RGB")
    if im.width > ancho:
        im = im.resize((ancho, int(im.height * ancho / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=calidad, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def cliente(nombre):
    im = Image.open(os.path.join(RAIZ, "assets", "clientes", nombre + ".png")).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


SAMU = data_uri(os.path.join(RAIZ, "assets", "img", "samu-a.png"), 620, 80)
SAMU2 = data_uri(os.path.join(RAIZ, "assets", "img", "samu-portada.png"), 560, 78)
LOGO = "data:image/svg+xml;base64," + base64.b64encode(
    open(os.path.join(RAIZ, "assets", "img", "GVA_Logo_Principal.svg"), "rb").read()).decode()

CLIENTES = [(n, cliente(n)) for n in
            ["clinica-isis", "discos-fuentes", "francisco-murillo", "camara-comercio-mde", "cootrasenvi",
             "pintuco", "alsina", "zaponti", "hc-ingenieria", "espinosa-gomez"]]

ESTILO = f"""
<style>
  .gva {{ font-family: Inter, 'Segoe UI', system-ui, sans-serif; color: {GRIS}; }}
  .gva h1, .gva h2, .gva h3 {{ color: {GRIS}; letter-spacing: -.02em; }}
  .gva .eyebrow {{ font-size:.78rem; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:#007A78; }}
  .gva .lead {{ font-size:1.1rem; color:#4B5563; }}
  .gva-hero {{ background: linear-gradient(140deg,#F2FAFA 0%,#FFFFFF 60%); }}
  .gva-hero img.samu {{ border-radius:22px; box-shadow:0 18px 40px rgba(14,26,43,.12); }}
  .gva-punto {{ width:10px;height:10px;border-radius:50%;background:{VERDE};display:inline-block;margin-right:8px }}
  .gva-sello {{ background:#fff;border:1px solid #E4E9EF;border-radius:14px;padding:12px 16px;
      box-shadow:0 10px 24px rgba(14,26,43,.08);font-weight:600;font-size:.85rem;display:inline-flex;align-items:center }}
  .gva-card {{ background:#fff;border:1px solid #E4E9EF;border-radius:16px;height:100%;
      transition:.2s; padding:26px 24px; }}
  .gva-card:hover {{ box-shadow:0 14px 30px rgba(14,26,43,.09); transform:translateY(-2px); }}
  .gva-card h3 {{ font-size:1.05rem;margin-bottom:8px }}
  .gva-card p {{ font-size:.94rem;color:#4B5563;margin-bottom:10px }}
  .gva-card .para {{ font-size:.8rem;font-weight:600;color:#007A78;border-top:1px solid #E4E9EF;padding-top:12px;margin:0 }}
  .gva-ico {{ width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;
      background:linear-gradient(135deg,{TURQ},{VERDE});color:#fff;margin-bottom:16px;font-weight:700 }}
  .gva-pilar .gva-ico {{ background:#F1F7F8;color:{TURQ} }}
  .gva-suave {{ background:#F6F9FA }}
  .gva-cliente {{ background:#fff;border:1px solid #E4E9EF;border-radius:12px;height:104px;
      display:flex;align-items:center;justify-content:center;padding:8px }}
  .gva-cliente img {{ max-height:80px;max-width:100%;filter:grayscale(100%);opacity:.85 }}
  .gva-cliente:hover img {{ filter:none;opacity:1 }}
  .gva-btn {{ display:inline-block;padding:13px 24px;border-radius:11px;font-weight:600;text-decoration:none;
      background:linear-gradient(135deg,{TURQ},{VERDE});color:#fff !important;border:1.5px solid transparent }}
  .gva-btn:hover {{ filter:brightness(1.06);color:#fff }}
  .gva-btn-2 {{ display:inline-block;padding:13px 24px;border-radius:11px;font-weight:600;text-decoration:none;
      border:1.5px solid #E4E9EF;color:{GRIS} !important;background:#fff }}
  .gva-num {{ width:44px;height:44px;border-radius:50%;border:2px solid {TURQ};color:#007A78;
      display:flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:14px }}
  .gva-banda {{ background:linear-gradient(135deg,{TURQ},{VERDE});color:#fff }}
  .gva-banda h2 {{ color:#fff }}
  .gva-tabla td {{ padding:12px 0;border-bottom:1px solid #E4E9EF;font-size:.95rem }}
  .gva-tabla td:first-child {{ width:38%;color:#4B5563 }}
</style>
"""


def seccion(contenido, clases="pt-5 pb-5"):
    return f'<section class="{clases}"><div class="container">{contenido}</div></section>'


HERO = f"""
<section class="gva-hero pt-5 pb-5">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        <p class="eyebrow mb-2">Consultoría financiera · Tributaria · Datos</p>
        <h1 class="display-5 fw-bold mb-3">Tecnología que simplifica lo complejo.</h1>
        <p class="lead mb-4">Unimos contaduría, impuestos y analítica de datos para que su empresa decida con
          información confiable. Cada cifra con soporte, cada decisión con evidencia.</p>
        <a class="gva-btn me-2" href="/contacto">Hablemos de su empresa</a>
        <a class="gva-btn-2" href="/servicios">Ver servicios</a>
      </div>
      <div class="col-lg-6">
        <img class="samu img-fluid" src="{SAMU}" alt="Samu, la mascota de GVA Group">
        <div class="mt-3"><span class="gva-sello"><span class="gva-punto"></span>Juntos hacemos más simple lo complejo</span></div>
      </div>
    </div>
  </div>
</section>
"""

PILARES = seccion(f"""
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Nuestros pilares</p>
    <h2 class="h1">Cuatro ideas sostienen cada trabajo que entregamos</h2>
  </div>
  <div class="row g-4">
    <div class="col-md-6 col-lg-3"><div class="gva-card gva-pilar"><div class="gva-ico">👥</div>
      <h3>Personas</h3><p>Talento que transforma. La tecnología sirve a las personas, no al revés.</p></div></div>
    <div class="col-md-6 col-lg-3"><div class="gva-card gva-pilar"><div class="gva-ico">▮▮</div>
      <h3>Datos</h3><p>Información con propósito. Toda decisión se sustenta en evidencia.</p></div></div>
    <div class="col-md-6 col-lg-3"><div class="gva-card gva-pilar"><div class="gva-ico">✦</div>
      <h3>Innovación</h3><p>Ideas que generan valor: IA y automatización aplicadas a problemas reales.</p></div></div>
    <div class="col-md-6 col-lg-3"><div class="gva-card gva-pilar"><div class="gva-ico">↗</div>
      <h3>Crecimiento</h3><p>Resultados sostenibles. Medimos el impacto en el negocio del cliente.</p></div></div>
  </div>""", "gva-suave pt-5 pb-5")


ICONOS = {
    "doc": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
    "escudo": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.4-3 8-7 9-4-1-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "impuesto": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 2h9l4 4v16H6z"/><path d="M14 2v5h5"/><circle cx="10.5" cy="13" r="1.4"/><circle cx="13.5" cy="17" r="1.4"/><path d="M14 11.5l-5 7"/></svg>',
    "grafico": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V6M4 20h16"/><path d="M8 16l4-5 3 3 4-6"/></svg>',
    "tablero": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>',
    "chip": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="6" y="6" width="12" height="12" rx="3"/><circle cx="12" cy="12" r="2.4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>'
}


def tarjeta(titulo, texto, para, icono="doc"):
    return f"""<div class="col-md-6 col-lg-4"><div class="gva-card d-flex flex-column">
      <div class="gva-ico">{ICONOS[icono]}</div><h3>{titulo}</h3><p>{texto}</p>
      <p class="para mt-auto">{para}</p></div></div>"""


SERVICIOS = seccion(f"""
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Servicios</p>
    <h2 class="h1">Todo lo contable, tributario y tecnológico, en una sola firma</h2>
    <p class="lead">Seis líneas de trabajo que se combinan según el tamaño y el momento de su empresa.</p>
  </div>
  <div class="row g-4">
    {tarjeta("Outsourcing contable y BPO financiero",
             "Contabilidad al día, cierres mensuales oportunos, conciliaciones, nómina y obligaciones. Información lista para decidir, no solo documentos para archivar.",
             "Para empresas que necesitan orden sin cargar nómina", "doc")}
    {tarjeta("Revisoría fiscal y auditoría externa",
             "Evaluación independiente del control interno y de los estados financieros, con hallazgos priorizados por riesgo y recomendaciones ejecutables.",
             "Para juntas, socios e inversionistas", "escudo")}
    {tarjeta("Planeación y auditoría tributaria",
             "Revisión de lo declarado, beneficios vigentes, atención de requerimientos y calendario fiscal controlado. Cada posición con su norma y su soporte.",
             "Para empresas con operación nacional o extranjera", "impuesto")}
    {tarjeta("NIIF: implementación y auditoría",
             "Adopción con políticas contables que se sostienen años después del primer informe. Implementaciones desde 600 horas; auditorías desde 250 horas.",
             "Para empresas que reportan a terceros", "grafico")}
    {tarjeta("Datos y analítica (BI)",
             "Tableros de margen, cartera, flujo de caja y costo, conciliados con la contabilidad. Una sola versión de la verdad para gerencia, socios y bancos.",
             "Para gerencias que deciden con números", "tablero")}
    {tarjeta("IA y automatización de procesos",
             "Automatizamos causación, conciliación, extracción de facturas y armado de reportes. La misma tarea, en menos horas y con menos errores.",
             "Para equipos contables con volumen alto", "chip")}
  </div>""", "pt-5 pb-5")


PASOS = seccion(f"""
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Cómo trabajamos</p>
    <h2 class="h1">Tres pasos, siempre con el mismo estándar</h2>
  </div>
  <div class="row g-4">
    <div class="col-md-4"><div class="gva-num">1</div><h3>Diagnóstico con datos</h3>
      <p>Revisamos sus estados financieros, sus declaraciones y sus procesos actuales. Antes de opinar, miramos las cifras.</p></div>
    <div class="col-md-4"><div class="gva-num">2</div><h3>Plan sustentado</h3>
      <p>Le entregamos qué se hace, por qué, con qué norma y qué esperar. Sin promesas que no podamos explicar.</p></div>
    <div class="col-md-4"><div class="gva-num">3</div><h3>Ejecución y seguimiento</h3>
      <p>Ejecutamos, medimos y le informamos en un tablero. Usted siempre sabe en qué va su empresa.</p></div>
  </div>""", "gva-suave pt-5 pb-5")

_logos = "".join(f'<div class="col-6 col-md-4 col-lg-2"><div class="gva-cliente"><img src="{u}" alt="{n}"></div></div>'
                 for n, u in CLIENTES)

CLIENTES_SEC = seccion(f"""
  <div class="text-center mb-4">
    <p class="eyebrow mb-1">Confianza</p>
    <h2 class="h1">Empresas que nos confían su información</h2>
    <p class="lead">Sectores de salud, industria, servicios y cultura.</p>
  </div>
  <div class="row g-3">{_logos}</div>
  <div class="text-center mt-4"><a class="gva-btn-2" href="/casos-de-exito">Ver casos de éxito</a></div>""", "pt-5 pb-5")

BANDA = f"""
<section class="gva-banda pt-5 pb-5">
  <div class="container text-center">
    <h2 class="h1 mb-2">¿Empezamos por una conversación?</h2>
    <p class="mb-4" style="color:rgba(255,255,255,.94)">Cuéntenos cómo está hoy su empresa. Le decimos, sin costo, qué revisar primero.</p>
    <a class="btn btn-light me-2 fw-semibold" href="/contacto">Escribir a GVA Group</a>
    <a class="btn btn-outline-light fw-semibold" href="tel:+573219101850">+57 321 910 1850</a>
  </div>
</section>
"""

HOME = ESTILO + '<div class="gva">' + HERO + PILARES + SERVICIOS + PASOS + CLIENTES_SEC + BANDA + "</div>"

FIRMA = ESTILO + '<div class="gva">' + seccion(f"""
  <p class="eyebrow mb-2">Nuestra firma</p>
  <h1 class="display-6 fw-bold mb-3" style="max-width:860px">Lo financiero y lo tributario no tienen que ser complejos si se miran a través de los datos.</h1>
  <p class="lead" style="max-width:760px">GVA Group nace de una convicción: la precisión normativa de la contaduría, unida a la
    capacidad de la analítica para encontrar patrones y anticipar riesgos.</p>""") + seccion(f"""
  <div class="row g-5">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Nuestra historia</h2>
      <p>Su fundador, Edgar Fernando Gelvis Vega, es contador público especialista en impuestos y magíster en
        análisis de datos. Esa combinación define la firma: rigor normativo y capacidad analítica en el mismo trabajo.</p>
      <p>Desde el inicio de su carrera ha sostenido una política que hoy es el ADN de GVA Group:
        <strong>todo debe estar sustentado en datos</strong>. Una cifra sin soporte es una opinión;
        una cifra con soporte es una decisión.</p>
      <p>Por eso cada mensaje, propuesta o informe se respalda con evidencia verificable, y traducimos lo técnico
        a un lenguaje que el cliente entiende y puede usar.</p>
    </div>
    <div class="col-lg-6">
      <h3>Misión</h3>
      <p>Simplificar la gestión financiera, tributaria y tecnológica de las empresas mediante análisis de datos,
        automatización e inteligencia artificial, con decisiones siempre sustentadas en evidencia.</p>
      <h3>Visión</h3>
      <p>Ser reconocidos en Colombia como el aliado que une contaduría, impuestos y ciencia de datos para que las
        empresas crezcan con información confiable y menos complejidad.</p>
      <h3>Valores</h3>
      <ul>
        <li><strong>Evidencia:</strong> los datos sustentan cada recomendación.</li>
        <li><strong>Claridad:</strong> explicamos lo complejo en términos simples.</li>
        <li><strong>Integridad:</strong> cumplimiento normativo y ética profesional sin excepciones.</li>
        <li><strong>Innovación útil:</strong> adoptamos tecnología cuando resuelve un problema real.</li>
        <li><strong>Cercanía:</strong> acompañamos al cliente; no solo entregamos informes.</li>
      </ul>
    </div>
  </div>""", "gva-suave pt-5 pb-5") + seccion(f"""
  <div class="row g-5">
    <div class="col-lg-6">
      <h2 class="h3 mb-2">Quién responde</h2>
      <p class="lead mb-2">Edgar Fernando Gelvis Vega · Director</p>
      <p>Contador público, especialista en impuestos y magíster en análisis de datos. Dirige personalmente los
        trabajos de auditoría, planeación tributaria y analítica.</p>
      <p>La firma trabaja con un equipo de contadores y analistas que conoce el sector de cada cliente:
        salud, industria, servicios, transporte, inmobiliario y cultura.</p>
    </div>
    <div class="col-lg-6">
      <h2 class="h3 mb-3">La firma</h2>
      <table class="gva-tabla w-100">
        <tr><td>Razón social</td><td>GVA GROUP S.A.S.</td></tr>
        <tr><td>NIT</td><td>901.841.984-9</td></tr>
        <tr><td>Actividad</td><td>Consultoría contable, tributaria y de gestión</td></tr>
        <tr><td>Matrícula</td><td>Cámara de Comercio de Medellín para Antioquia</td></tr>
        <tr><td>Oficina</td><td>Calle 60B Sur # 44-100, Sabaneta, Antioquia</td></tr>
        <tr><td>Correo</td><td>gerencia@gvagroup.com.co</td></tr>
        <tr><td>Teléfono</td><td>+57 321 910 1850</td></tr>
      </table>
    </div>
  </div>""") + BANDA + "</div>"

SERVICIOS_LIMPIO = SERVICIOS.replace('<p class="eyebrow mb-1">Servicios</p>', '')
SERVICIOS_LIMPIO = SERVICIOS_LIMPIO.replace('<h2 class="h1">Todo lo contable, tributario y tecnológico, en una sola firma</h2>',
                                            '<h2 class="h1">Portafolio de servicios</h2>')
SERVICIOS_LIMPIO = SERVICIOS_LIMPIO.replace('<p class="lead">Seis líneas de trabajo que se combinan según el tamaño y el momento de su empresa.</p>',
                                            '<p class="lead">Cada línea se adapta al tamaño y al momento de su empresa.</p>')

SERV = ESTILO + '<div class="gva">' + seccion(f"""
  <p class="eyebrow mb-2">Servicios</p>
  <h1 class="display-6 fw-bold mb-3" style="max-width:800px">Seis líneas de trabajo que se combinan según su empresa</h1>
  <p class="lead" style="max-width:800px">No vendemos paquetes cerrados. Revisamos su situación, identificamos qué le
    está costando dinero o tiempo, y armamos el trabajo con alcance y honorarios claros.</p>""") + \
    SERVICIOS_LIMPIO + seccion(f"""
  <div class="row g-5">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Servicios complementarios</h2>
      <ul>
        <li>Asesoría en régimen cambiario e inversión extranjera.</li>
        <li>Actualización tributaria en sus instalaciones (grupos de hasta 5 personas).</li>
        <li>Auditorías financieras, tributarias y operativas.</li>
        <li>Interventoría en proyectos específicos.</li>
        <li>Manejo de recursos humanos y liquidación de nómina.</li>
      </ul>
    </div>
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Cómo se contrata</h2>
      <p>Primero una conversación de diagnóstico sin costo. Luego una propuesta con alcance, entregables, horas y
        honorarios. Nada empieza sin que usted tenga claro qué recibe y cuánto cuesta.</p>
      <a class="gva-btn" href="/contacto">Solicitar propuesta</a>
    </div>
  </div>""", "gva-suave pt-5 pb-5") + BANDA + "</div>"

CASOS = ESTILO + '<div class="gva">' + seccion(f"""
  <p class="eyebrow mb-2">Casos de éxito</p>
  <h1 class="display-6 fw-bold mb-3" style="max-width:820px">Trabajos con nombre propio, no promesas genéricas</h1>
  <p class="lead" style="max-width:820px">Trabajamos con empresas de salud, industria, servicios, cultura y gremios.
    Por confidencialidad, el detalle de cada trabajo se comparte en la conversación y siempre con autorización del cliente.</p>""") + \
    seccion(f"""
  <table class="gva-tabla w-100">
    <tr><td><strong>Sector salud</strong></td><td>Clínica ISIS · Laboratorio Espinosa Gómez</td></tr>
    <tr><td><strong>Industria y consumo</strong></td><td>Pintuco · Indumuebles · Alsina</td></tr>
    <tr><td><strong>Cultura y medios</strong></td><td>Discos Fuentes</td></tr>
    <tr><td><strong>Servicios y gremios</strong></td><td>Francisco Murillo · Cámara de Comercio de Medellín · Cootrasenvi · Adida · Zaponti · HC Ingeniería</td></tr>
  </table>""", "gva-suave pt-5 pb-5") + CLIENTES_SEC + BANDA + "</div>"

CONTACTO = ESTILO + '<div class="gva">' + seccion(f"""
  <p class="eyebrow mb-2">Contacto</p>
  <h1 class="display-6 fw-bold mb-3">Hablemos de su empresa</h1>
  <p class="lead" style="max-width:720px">Escríbanos o llame. La primera conversación es de diagnóstico,
    sin costo y sin compromiso: le decimos qué revisar primero.</p>
  <div class="row g-4 mt-2">
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">✉</div>
      <h3>Correo</h3><p class="mb-0"><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></p></div></div>
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">☎</div>
      <h3>Teléfono y WhatsApp</h3><p class="mb-0"><a href="https://wa.me/573219101850">+57 321 910 1850</a></p></div></div>
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">◎</div>
      <h3>Oficina</h3><p class="mb-0">Calle 60B Sur # 44-100<br>Sabaneta, Antioquia, 055457<br>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Calle+60B+Sur+44-100+Sabaneta+Antioquia" target="_blank" rel="noopener">Ver en el mapa</a></p></div></div>
  </div>""") + seccion(f"""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Prefiere que lo llamemos</h2>
      <p>Déjenos sus datos en el formulario de contacto y le respondemos el mismo día hábil. También puede
        escribirnos directo a <a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a>.</p>
      <a class="gva-btn" href="/contactus">Ir al formulario</a>
    </div>
    <div class="col-lg-6 text-center"><img src="{SAMU2}" alt="GVA Group" class="img-fluid" style="max-width:320px;border-radius:18px"></div>
  </div>""", "gva-suave pt-5 pb-5") + "</div>"

import re as _re

def xml_seguro(html):
    """Odoo guarda el archivo como XML: los elementos vacios deben ir cerrados."""
    def cerrar(m):
        et = m.group(0)
        return et if et.rstrip().endswith("/>") else et[:-1] + "/>"
    return _re.sub(r"<(?:img|br|hr|input|meta|link|source)[^>]*>", cerrar, html)


for nombre, contenido in [("home", HOME), ("firma", FIRMA), ("servicios", SERV),
                           ("casos", CASOS), ("contacto", CONTACTO)]:
    contenido = xml_seguro(contenido)
    ruta = os.path.join(SALIDA, nombre + ".html")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(contenido)
    print(f"{nombre}.html  {len(contenido)/1024:.0f} KB")


# ---------------------------------------------------------------------------
# Versión amigable de «Nuestra firma», con imágenes
# ---------------------------------------------------------------------------
def retrato(ruta, lado=460, calidad=82):
    im = Image.open(ruta).convert("RGB")
    w, h = im.size
    lado_min = min(w, h)
    izq = int((w - lado_min) * 0.35)          # el sujeto está a la izquierda
    arriba = int((h - lado_min) * 0.05)
    im = im.crop((izq, arriba, izq + lado_min, arriba + lado_min))
    im = im.resize((lado, lado), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=calidad, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


RETRATO = retrato(r"C:\Users\egelv\OneDrive\Mis documentos\GV TRIBUTARISTA SAS\Pagina WEB\Datos socios"
                  r"\Edgar Fernando Gelvis Vega\Fotos\Fernando 2.jpeg")

ESTILO_EXTRA = """
  .gva-valor {{ background:#fff;border:1px solid #E4E9EF;border-radius:14px;padding:22px 18px;height:100% }}
  .gva-valor .ico {{ width:34px;height:34px;border-radius:10px;background:#F1F7F8;color:#007A78;
      display:flex;align-items:center;justify-content:center;margin-bottom:12px;font-weight:700 }}
  .gva-valor h4, .gva-valor h3 {{ font-size:.98rem;margin-bottom:6px }}
  .gva-valor p {{ font-size:.86rem;color:#4B5563;margin:0 }}
  .gva-retrato {{ width:220px;height:220px;border-radius:50%;object-fit:cover;
      box-shadow:0 18px 40px rgba(14,26,43,.16);border:6px solid #fff }}
  .gva-marco {{ border-radius:20px;overflow:hidden;box-shadow:0 18px 40px rgba(14,26,43,.12) }}
  .gva-marco img {{ width:100%;display:block }}
  .gva-marco.gva-hero-img {{ background:#F6F9FA;display:flex;align-items:center;justify-content:center }}
  .gva-marco.gva-hero-img img {{ width:auto;max-width:100%;max-height:480px;object-fit:contain }}
  .gva-mision {{ background:#fff;border:1px solid #E4E9EF;border-radius:16px;padding:26px 24px;height:100% }}
  .gva-mision h3 {{ font-size:1.05rem }}
  .gva-mision p {{ font-size:.94rem;color:#4B5563;margin:0 }}
  .gva-foto-pie {{ font-size:.85rem;color:#4B5563;margin-top:12px }}
"""

VALORES = [
    ("Evidencia", "Los datos sustentan cada recomendación.", "▮"),
    ("Claridad", "Explicamos lo complejo en términos simples.", "≈"),
    ("Integridad", "Cumplimiento y ética profesional sin excepciones.", "✓"),
    ("Innovación útil", "Tecnología cuando resuelve un problema real.", "✦"),
    ("Cercanía", "Acompañamos; no solo entregamos informes.", "◎"),
]
_val = "".join(
    f'<div class="col-6 col-md-4 col-lg"><div class="gva-valor"><div class="ico">{i}</div>'
    f'<h3>{t}</h3><p>{d}</p></div></div>' for t, d, i in VALORES)

ESTILO_EXTRA = ESTILO_EXTRA.replace('{{', '{').replace('}}', '}')
FIRMA2 = ESTILO.replace('</style>', ESTILO_EXTRA + '</style>') + '<div class="gva">' + f"""
<section class="gva-hero pt-5 pb-5">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6">
        <p class="eyebrow mb-2">Nuestra firma</p>
        <h1 class="display-5 fw-bold mb-3">Contaduría, impuestos y datos en el mismo trabajo.</h1>
        <p class="lead mb-0">GVA Group nace de una convicción: lo financiero y lo tributario no tienen que ser
          complejos si se miran a través de los datos.</p>
      </div>
      <div class="col-lg-6">
        <div class="gva-marco gva-hero-img"><img src="{SAMU}" alt="Samu, la mascota de GVA Group"></div>
      </div>
    </div>
  </div>
</section>
""" + seccion(f"""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Nuestra historia</h2>
      <p>El fundador, Edgar Fernando Gelvis Vega, es contador público especialista en impuestos y magíster en
        análisis de datos. Esa combinación define la firma: rigor normativo y capacidad analítica en el mismo trabajo.</p>
      <p>Desde el inicio de su carrera ha sostenido una política que hoy es el ADN de GVA Group:
        <strong>todo debe estar sustentado en datos</strong>. Una cifra sin soporte es una opinión;
        una cifra con soporte es una decisión.</p>
      <p class="mb-0">Por eso cada mensaje, propuesta o informe se respalda con evidencia verificable, y lo técnico
        se traduce a un lenguaje que el cliente entiende y puede usar.</p>
    </div>
    <div class="col-lg-6">
      <div class="gva-marco"><img src="{SAMU2}" alt="GVA Group: soluciones para un futuro más inteligente"></div>
      <p class="gva-foto-pie">Personas · Datos · Innovación · Crecimiento</p>
    </div>
  </div>""", "pt-5 pb-5") + seccion(f"""
  <div class="row g-4">
    <div class="col-md-6"><div class="gva-mision"><div class="gva-ico">◎</div>
      <h3>Misión</h3><p>Simplificar la gestión financiera, tributaria y tecnológica de las empresas mediante
      análisis de datos, automatización e inteligencia artificial, con decisiones siempre sustentadas en evidencia.</p></div></div>
    <div class="col-md-6"><div class="gva-mision"><div class="gva-ico">↗</div>
      <h3>Visión</h3><p>Ser reconocidos en Colombia como el aliado que une contaduría, impuestos y ciencia de
      datos para que las empresas crezcan con información confiable y menos complejidad.</p></div></div>
  </div>""", "gva-suave pt-5 pb-5") + seccion(f"""
  <div class="text-center mb-4">
    <p class="eyebrow mb-1">Valores</p>
    <h2 class="h1">Cinco reglas que no se negocian</h2>
  </div>
  <div class="row g-3">{_val}</div>""", "pt-5 pb-5") + seccion(f"""
  <div class="row g-5 align-items-center">
    <div class="col-lg-4 text-center">
      <img class="gva-retrato" src="{RETRATO}" alt="Edgar Fernando Gelvis Vega">
      <p class="gva-foto-pie mt-3 mb-0"><strong>Edgar Fernando Gelvis Vega</strong><br>Director</p>
    </div>
    <div class="col-lg-8">
      <h2 class="h3 mb-3">Quién responde</h2>
      <p>Contador público, especialista en impuestos y magíster en análisis de datos. Dirige personalmente los
        trabajos de auditoría, planeación tributaria y analítica.</p>
      <p>La firma trabaja con un equipo de contadores y analistas que conoce el sector de cada cliente:
        salud, industria, servicios, transporte, inmobiliario y cultura.</p>
      <table class="gva-tabla w-100">
        <tr><td>Razón social</td><td>GVA GROUP S.A.S.</td></tr>
        <tr><td>NIT</td><td>901.841.984-9</td></tr>
        <tr><td>Actividad</td><td>Consultoría contable, tributaria y de gestión</td></tr>
        <tr><td>Matrícula</td><td>Cámara de Comercio de Medellín para Antioquia</td></tr>
        <tr><td>Oficina</td><td>Calle 60B Sur # 44-100, Sabaneta, Antioquia</td></tr>
        <tr><td>Correo</td><td><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></td></tr>
        <tr><td>Teléfono</td><td><a href="tel:+573219101850">+57 321 910 1850</a></td></tr>
      </table>
    </div>
  </div>""", "gva-suave pt-5 pb-5") + CLIENTES_SEC + BANDA + "</div>"

with open(os.path.join(SALIDA, "firma2.html"), "w", encoding="utf-8") as fh:
    fh.write(xml_seguro(FIRMA2))
print(f"firma2.html  {len(FIRMA2)/1024:.0f} KB")
