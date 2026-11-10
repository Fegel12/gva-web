# -*- coding: utf-8 -*-
"""Genera las paginas de la Fase 1 segun el Manual de diseno web GVA (nov-2026)."""
import os

SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fase1")
os.makedirs(SALIDA, exist_ok=True)

IMG = {  # id del adjunto en Odoo -> /web/image/<id>
    "01": 1596, "02": 1597, "03": 1598, "04": 1599, "05": 1600, "06": 1601,
    "07": 1602, "08": 1603, "09": 1604, "10": 1605, "11": 1606, "12": 1607,
    "13": 1608, "14": 1609, "15": 1610, "16": 1611,
}

ESTILO = """
<style>
  .gva { font-family: Inter, 'Segoe UI', system-ui, sans-serif; color: #2E3540; }
  .gva h1, .gva h2, .gva h3 { color:#2E3540; letter-spacing:-.02em; }
  .gva .eyebrow { font-size:.78rem; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:#007A78; }
  .gva .lead { font-size:1.1rem; color:#4B5563; }
  .gva-hero { position:relative; background-size:cover; background-position:center; overflow:hidden; }
  .gva-hero .velo { background:linear-gradient(90deg, rgba(255,255,255,.97) 0%, rgba(255,255,255,.93) 45%, rgba(255,255,255,.55) 70%, rgba(255,255,255,0) 100%); }
  .gva-hero .contenido { padding: 72px 0; max-width: 620px; }
  .gva-hero h1 { font-size: clamp(1.9rem, 3.6vw, 2.9rem); font-weight:700; }
  .gva-btn { display:inline-block;padding:13px 24px;border-radius:11px;font-weight:600;text-decoration:none;
      background:linear-gradient(135deg,#00B7B5,#00B140);color:#fff !important;border:1.5px solid transparent }
  .gva-btn:hover { filter:brightness(1.06); color:#fff }
  .gva-btn-2 { display:inline-block;padding:13px 24px;border-radius:11px;font-weight:600;text-decoration:none;
      border:1.5px solid #CBD5DC;color:#2E3540 !important;background:#fff }
  .gva-card { background:#fff;border:1px solid #E4E9EF;border-radius:16px;height:100%;padding:26px 24px;transition:.2s }
  .gva-card:hover { box-shadow:0 14px 30px rgba(14,26,43,.09); transform:translateY(-2px) }
  .gva-card h3 { font-size:1.05rem; margin-bottom:8px }
  .gva-card p { font-size:.94rem; color:#4B5563; margin-bottom:10px }
  .gva-card .para { font-size:.8rem;font-weight:600;color:#007A78;border-top:1px solid #E4E9EF;padding-top:12px;margin:0 }
  .gva-ico { width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;
      background:linear-gradient(135deg,#00B7B5,#00B140);color:#fff;margin-bottom:16px;font-weight:700 }
  .gva-suave { background:#F6F9FA }
  .gva-num { width:44px;height:44px;border-radius:50%;border:2px solid #00B7B5;color:#007A78;
      display:flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:14px }
  .gva-banda { background:linear-gradient(135deg,#00B7B5,#00B140);color:#fff }
  .gva-banda h2 { color:#fff }
  .gva-lista { list-style:none;padding:0;margin:0 }
  .gva-lista li { position:relative;padding-left:26px;margin-bottom:10px;color:#4B5563;font-size:.95rem }
  .gva-lista li::before { content:"";position:absolute;left:0;top:.5em;width:10px;height:10px;border-radius:50%;
      background:linear-gradient(135deg,#00B7B5,#00B140) }
  .gva-nota { font-size:.86rem;color:#4B5563;background:#F6F9FA;border-left:3px solid #00B7B5;padding:12px 16px;border-radius:8px }
  @media (max-width: 768px) {
    .gva-hero { background-position: 72% center; }
    .gva-hero .velo { background: linear-gradient(180deg, rgba(255,255,255,.97) 0%, rgba(255,255,255,.94) 52%, rgba(255,255,255,.62) 78%, rgba(255,255,255,.15) 100%); }
    .gva-hero .contenido { padding: 42px 0; max-width: 100%; }
    .gva-hero h1 { font-size: 1.6rem; }
    .gva .lead { font-size: 1rem; }
  }
</style>
"""


def metricas(total=6):
    return total


def tarjeta(titulo, texto, para="", icono="•"):
    return (f'<div class="col-md-6 col-lg-4"><div class="gva-card d-flex flex-column">'
            f'<div class="gva-ico">{icono}</div><h3>{titulo}</h3><p>{texto}</p>'
            f'<p class="para mt-auto">{para}</p></div></div>')


def paso(n, titulo, texto):
    return (f'<div class="col-md-6 col-lg-3"><div class="gva-num">{n}</div>'
            f'<h3 class="h6">{titulo}</h3><p style="font-size:.93rem;color:#4B5563">{texto}</p></div>')


def bloque(contenido, clases="pt-5 pb-5"):
    return f'<section class="{clases}"><div class="container">{contenido}</div></section>'


def hero(img, h1, lead, cta, cta_url, secundario=None, secundario_url=None):
    sec = (f'<a class="gva-btn-2 ms-2" href="{secundario_url}">{secundario}</a>'
           if secundario else "")
    return f"""
<section class="gva-hero" style="background-image:url('/web/image/{IMG[img]}')">
  <div class="velo">
    <div class="container">
      <div class="contenido">
        <h1 class="mb-3">{h1}</h1>
        <p class="lead mb-4">{lead}</p>
        <a class="gva-btn" href="{cta_url}">{cta}</a> {sec}
      </div>
    </div>
  </div>
</section>"""


def banda(titulo, texto, cta="Escribir a GVA Group", url="/contacto"):
    return f"""
<section class="gva-banda pt-5 pb-5">
  <div class="container text-center">
    <h2 class="h2 mb-2">{titulo}</h2>
    <p class="mb-4" style="color:rgba(255,255,255,.94)">{texto}</p>
    <a class="btn btn-light fw-semibold" href="{url}">{cta}</a>
    <a class="btn btn-outline-light fw-semibold ms-2" href="tel:+573219101850">+57 321 910 1850</a>
  </div>
</section>"""


def pruebas(puntos):
    items = "".join(f"<li>{p}</li>" for p in puntos)
    return bloque(f"""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <p class="eyebrow mb-1">Prueba de confianza</p>
      <h2 class="h3 mb-3">Cómo puede verificarnos</h2>
      <ul class="gva-lista">{items}</ul>
    </div>
    <div class="col-lg-6">
      <div class="gva-nota">No publicamos cifras, clientes ni certificaciones que no podamos sustentar.
      Cuando un dato requiere autorización del cliente, se comparte en la conversación y no en la página.</div>
    </div>
  </div>""", "gva-suave pt-5 pb-5")


def pagina(nombre, titulo_seo, desc, contenido):
    html = f"""<!DOCTYPE html>
<html lang="es-CO"><head><meta charset="utf-8">
<title>{titulo_seo}</title><meta name="description" content="{desc}">
</head><body>{ESTILO}<div class="gva">{contenido}</div></body></html>"""
    with open(os.path.join(SALIDA, nombre + ".html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(nombre + ".html", len(html), "bytes")


# ---------------------------------------------------------------- INICIO
INICIO = hero("01", "Conocimiento que genera confianza. Soluciones que transforman.",
              "Combinamos experiencia tributaria, contable, financiera y de auditoría con análisis de datos "
              "y tecnología para acompañar las decisiones de su empresa.",
              "Conozca nuestros servicios", "/servicios") + bloque("""
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Capacidades</p>
    <h2 class="h1">Seis frentes de trabajo, un mismo estándar de evidencia</h2>
  </div>
  <div class="row g-4">
    """ + tarjeta("Auditoría y control", "Evaluación independiente del control interno y de los estados financieros, con hallazgos priorizados por riesgo.", "Ver auditoría", "✓")
    + tarjeta("Tributación", "Planeación y cumplimiento con sustento técnico: cada posición con su norma y su soporte.", "Ver tributación", "%")
    + tarjeta("Finanzas y analítica", "Información financiera convertida en indicadores, presupuestos y decisiones.", "Ver finanzas", "▤")
    + tarjeta("Consultoría", "Diagnóstico, opciones estratégicas y acompañamiento en la ejecución.", "Ver consultoría", "◈")
    + tarjeta("Internacional", "Operaciones con el exterior: régimen cambiario, inversión extranjera y estructura.", "Ver internacional", "◎")
    + tarjeta("Riesgos y cumplimiento", "Mapas de riesgo, controles y gobierno para anticipar contingencias.", "Ver cumplimiento", "⚑")
    + """</div>
</section>""") + bloque("""
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Cómo trabajamos</p>
    <h2 class="h1">Entendemos, analizamos, recomendamos y acompañamos</h2>
  </div>
  <div class="row g-4">
    """ + paso(1, "Entendemos", "Escuchamos el negocio, su operación y sus restricciones antes de proponer.")
    + paso(2, "Analizamos", "Revisamos cifras, contratos y normas aplicables. Sin datos no hay recomendación.")
    + paso(3, "Recomendamos", "Entregamos la decisión, su sustento y el efecto esperado en caja.")
    + paso(4, "Acompañamos", "Ejecutamos con su equipo y medimos el resultado en un tablero.")
    + """</div>
</section>""", "gva-suave pt-5 pb-5") + bloque("""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <p class="eyebrow mb-1">Innovación</p>
      <h2 class="h3 mb-3">Datos, automatización e inteligencia artificial con supervisión profesional</h2>
      <p>Automatizamos lo repetitivo —causación, conciliación, extracción de documentos— y reservamos el
        criterio humano para lo que no se automatiza: validar el soporte, cuestionar la cifra y decidir.</p>
      <a class="gva-btn-2" href="/inteligencia-artificial">Ver innovación</a>
    </div>
    <div class="col-lg-6">
      <ul class="gva-lista">
        <li>Tableros conciliados con la contabilidad, no cifras paralelas.</li>
        <li>Procesos documentados antes de automatizar.</li>
        <li>Datos del cliente tratados con reserva y sin uso para entrenar modelos sin autorización.</li>
      </ul>
    </div>
  </div>""") + pruebas([
    "Metodología documentada en cada trabajo.",
    "Hallazgos con evidencia y trazabilidad.",
    "Informes con fuente, fecha y responsable.",
]) + banda("Conversemos sobre las necesidades de su empresa",
           "Le decimos qué revisar primero, sin costo y sin compromiso.")

pagina("inicio", "GVA Group | Conocimiento que genera confianza",
       "Consultoría contable, tributaria, financiera y de datos. Auditoría, planeación tributaria, analítica e innovación.",
       INICIO)

# ---------------------------------------------------------------- SERVICIOS (hub)
SERVICIOS = hero("03", "Soluciones integradas para retos empresariales complejos.",
                 "Articulamos asesoría tributaria, contabilidad, auditoría, finanzas y consultoría para responder "
                 "a necesidades concretas con rigor técnico y enfoque práctico.",
                 "Ver servicios", "#frentes") + f"""
<section id="frentes" class="pt-5 pb-5"><div class="container">
  <div class="text-center mb-5">
    <p class="eyebrow mb-1">Frentes de servicio</p>
    <h2 class="h1">Seis especialidades que se combinan según su empresa</h2>
  </div>
  <div class="row g-4">
    {tarjeta("Auditoría y control", "Evidencia, control y criterio para fortalecer sus decisiones.", "Ver auditoría", "✓")}
    {tarjeta("Tributación", "Planeación y cumplimiento tributario con sustento técnico.", "Ver tributación", "%")}
    {tarjeta("Finanzas y analítica", "Información financiera en decisiones mejor fundamentadas.", "Ver finanzas", "▤")}
    {tarjeta("Consultoría", "Estrategia y acompañamiento para impulsar su organización.", "Ver consultoría", "◈")}
    {tarjeta("Consultoría internacional", "Visión local y comprensión de operaciones internacionales.", "Ver internacional", "◎")}
    {tarjeta("Riesgos y cumplimiento", "Controles y prevención para fortalecer el gobierno empresarial.", "Ver cumplimiento", "⚑")}
  </div>
  <div class="row g-4 mt-4">
    <div class="col-lg-6"><div class="gva-card h-100">
      <h3>Servicios de apoyo</h3>
      <ul class="gva-lista">
        <li>Outsourcing contable y BPO financiero.</li>
        <li>Implementación y auditoría NIIF.</li>
        <li>Formación y actualización tributaria en su empresa.</li>
        <li>Analítica, tableros e inteligencia artificial aplicada.</li>
      </ul></div></div>
    <div class="col-lg-6"><div class="gva-card h-100">
      <h3>Cómo se contrata</h3>
      <p>Primero una conversación de diagnóstico sin costo. Luego una propuesta con alcance, entregables,
        horas y honorarios. Nada empieza sin que usted tenga claro qué recibe y cuánto cuesta.</p>
      <a class="gva-btn" href="/contacto">Solicitar propuesta</a></div></div>
  </div>
</div></section>""" + pruebas([
    "Alcance y entregables por escrito antes de empezar.",
    "Honorarios cerrados por trabajo, no por sorpresa.",
    "Informes con hallazgos priorizados por riesgo.",
]) + banda("¿Por dónde empezamos?", "Cuéntenos su situación y le proponemos el primer paso.")

pagina("servicios", "Servicios | GVA Group",
       "Auditoría, tributación, finanzas, consultoría, internacional y cumplimiento. Soluciones integradas para empresas.",
       SERVICIOS)


# ---------------------------------------------------------------- paginas de servicio
def servicio(nombre, img, h1, lead, problema, valor, metodo, prueba_puntos, relacionados):
    cont = hero(img, h1, lead, "Solicitar un diagnóstico", "/contacto") + bloque(f"""
  <div class="row g-5">
    <div class="col-lg-7">
      <p class="eyebrow mb-1">La necesidad</p>
      <h2 class="h3 mb-3">{problema[0]}</h2>
      <p>{problema[1]}</p>
      <p class="mb-0">{problema[2]}</p>
    </div>
    <div class="col-lg-5"><div class="gva-nota">{problema[3]}</div></div>
  </div>""") + bloque(f"""
  <div class="text-center mb-5"><p class="eyebrow mb-1">Oferta de valor</p>
    <h2 class="h1">Qué incluye el trabajo</h2></div>
  <div class="row g-4">{valor}</div>""", "gva-suave pt-5 pb-5") + bloque(f"""
  <div class="text-center mb-5"><p class="eyebrow mb-1">Metodología</p>
    <h2 class="h1">Cómo lo hacemos</h2></div>
  <div class="row g-4">{metodo}</div>""") + pruebas(prueba_puntos) + bloque(f"""
  <div class="row g-4">
    <div class="col-lg-6"><div class="gva-card h-100"><h3>Servicios relacionados</h3>
      <ul class="gva-lista">{''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in relacionados)}</ul></div></div>
    <div class="col-lg-6"><div class="gva-card h-100"><h3>Siguiente paso</h3>
      <p>Una conversación de diagnóstico, sin costo. Revisamos su caso y le decimos qué mirar primero.</p>
      <a class="gva-btn" href="/contacto">Hablar con un especialista</a></div></div>
  </div>""") + banda("Conversemos sobre su caso", "Le decimos qué revisar primero y qué puede esperar.")
    pagina(nombre, f"{h1.split('.')[0]} | GVA Group", lead[:150], cont)


servicio(
    "auditoria", "04",
    "Evidencia, control y criterio para fortalecer sus decisiones.",
    "Evaluación independiente del control interno y de los estados financieros, con hallazgos priorizados "
    "por riesgo y recomendaciones que se pueden ejecutar.",
    ("Cuando el control es débil, el número deja de ser confiable",
     "Una cifra sin soporte es una opinión. Cuando los procesos no están documentados, la información se "
     "vuelve difícil de defender ante una junta, un banco o una autoridad.",
     "La auditoría no busca culpables: busca que la información resista preguntas. Ese es el estándar con el que trabajamos.",
     "Este servicio no sustituye la revisoría fiscal cuando la ley la exige; sí la complementa y prepara la evidencia."),
    tarjeta("Diagnóstico de control interno", "Evaluamos ciclos de ingresos, compras, nómina y tesorería con pruebas selectivas.", "Punto de partida", "1")
    + tarjeta("Auditoría de estados financieros", "Revisión de saldos, soportes y políticas contables aplicadas.", "Para juntas y bancos", "2")
    + tarjeta("Hallazgos priorizados", "Cada hallazgo con riesgo, efecto potencial y recomendación ejecutable.", "Entregable central", "3")
    + tarjeta("Plan de acción", "Acompañamos la corrección y verificamos el cierre de cada punto.", "Seguimiento", "4")
    + tarjeta("Informe ejecutivo", "Versión para dirección y versión técnica, con anexos de evidencia.", "Comunicación clara", "5")
    + tarjeta("Preparación para revisión externa", "Dejamos el soporte listo antes de que llegue el requerimiento.", "Prevención", "6"),
    paso(1, "Entendimiento", "Procesos, sistemas y responsables. Qué se hace y quién lo autoriza.")
    + paso(2, "Pruebas", "Selección de muestras, revisión documental y verificación de controles clave.")
    + paso(3, "Informe", "Hallazgos, efecto y prioridad. Sin tecnicismos innecesarios.")
    + paso(4, "Cierre", "Acompañamiento hasta que cada recomendación queda implementada."),
    ["Alcance definido por escrito y aceptado antes de iniciar.",
     "Papeles de trabajo disponibles para revisión del cliente.",
     "Independencia declarada cuando el trabajo lo exige."],
    [("Tributación", "/tributacion"), ("Finanzas y analítica", "/finanzas"),
     ("Riesgos y cumplimiento", "/riesgos-y-cumplimiento"), ("Servicios", "/servicios")])

servicio(
    "tributacion", "05",
    "Planeación y cumplimiento tributario con sustento técnico.",
    "Revisamos lo declarado, identificamos beneficios vigentes y ordenamos el calendario fiscal antes de "
    "que llegue el requerimiento.",
    ("El error más caro no es aplicar mal una norma: es aplicarla antes de leer el texto oficial",
     "Un resumen de prensa no sirve como soporte de una declaración. La diferencia entre una posición "
     "defendible y una sanción suele estar en la fecha de vigencia y en el documento que la respalda.",
     "Cada recomendación se entrega con norma, fecha, cálculo y efecto en caja.",
     "No aplicamos una reforma por lo que dice un resumen: verificamos el texto publicado antes de mover un registro."),
    tarjeta("Diagnóstico tributario", "Revisión de renta, IVA, retenciones y obligaciones formales del período.", "Punto de partida", "1")
    + tarjeta("Planeación", "Decisiones antes de que ocurra la operación: contrato, momento y forma.", "Prevención", "2")
    + tarjeta("Calendario fiscal", "Vencimientos por NIT y tipo de contribuyente, con responsables asignados.", "Control", "3")
    + tarjeta("Atención de requerimientos", "Respuesta documentada ante requerimientos y emplazamientos.", "Defensa", "4")
    + tarjeta("Beneficios vigentes", "Identificación de beneficios aplicables con su requisito de procedencia.", "Oportunidad", "5")
    + tarjeta("Formación al equipo", "Capacitación práctica a contabilidad y administración.", "Transferencia", "6"),
    paso(1, "Diagnóstico", "Qué se declaró, con qué soporte y qué quedó pendiente.")
    + paso(2, "Análisis normativo", "Texto oficial, vigencia y efecto en la empresa.")
    + paso(3, "Recomendaciones", "Opciones con costo, riesgo y efecto en caja.")
    + paso(4, "Implementación", "Ajustes contables, soportes y calendario bajo control."),
    ["Norma, fecha y fuente en cada posición asumida.",
     "Cálculos reproducibles y conciliados con la contabilidad.",
     "Advertencia expresa cuando el caso requiere consulta a la autoridad."],
    [("Auditoría", "/auditoria"), ("Finanzas y analítica", "/finanzas"),
     ("Consultoría internacional", "/consultoria-internacional"), ("Servicios", "/servicios")])

servicio(
    "finanzas", "06",
    "Convertimos información financiera en decisiones mejor fundamentadas.",
    "Indicadores, presupuestos y proyecciones que se entienden en la junta y se sostienen con la contabilidad.",
    ("La información existe, pero no llega a tiempo ni en el formato que se necesita",
     "Muchas empresas tienen contabilidad al día y, aun así, deciden a ciegas: el informe llega tarde, "
     "no distingue líneas de negocio o no explica qué cambió respecto al mes anterior.",
     "Ordenamos la información en pocos indicadores, con la misma cifra para gerencia, socios y bancos.",
     "No prometemos ahorros: entregamos la lectura de sus números y las decisiones que habilitan."),
    tarjeta("Tablero de indicadores", "Margen, cartera, flujo y costo, conciliados con la contabilidad.", "Visión gerencial", "1")
    + tarjeta("Presupuesto y seguimiento", "Presupuesto anual con comparación mensual y explicación de desvíos.", "Control", "2")
    + tarjeta("Proyección de caja", "Escenarios a 12 meses con supuestos explícitos y revisables.", "Decisión", "3")
    + tarjeta("Análisis de costos", "Costeo por línea, producto o sede, sin cifras fiscales que distorsionen.", "Rentabilidad", "4")
    + tarjeta("Informe para terceros", "Preparación de paquetes para bancos, socios o inversionistas.", "Financiación", "5")
    + tarjeta("Automatización", "Extracción y consolidación de datos sin transcripción manual.", "Eficiencia", "6"),
    paso(1, "Fuentes", "De dónde sale cada cifra y quién la valida.")
    + paso(2, "Modelo", "Una sola versión de la verdad, documentada.")
    + paso(3, "Tablero", "Publicación mensual con notas de variación.")
    + paso(4, "Revisión", "Ajustes trimestrales con la dirección."),
    ["Cifras conciliadas contra el balance del período.",
     "Supuestos escritos y versionados.",
     "Entrega mensual con fecha fija acordada."],
    [("Auditoría", "/auditoria"), ("Tributación", "/tributacion"),
     ("Inteligencia artificial", "/inteligencia-artificial"), ("Servicios", "/servicios")])

servicio(
    "consultoria", "07",
    "Estrategia y acompañamiento para impulsar su organización.",
    "Diagnóstico, opciones estratégicas y acompañamiento en la ejecución, con indicadores que permiten "
    "saber si la decisión funcionó.",
    ("Las decisiones grandes se toman sin método",
     "Abrir una sede, cambiar de proveedor, contratar un canal nuevo o entrar a otro mercado son decisiones "
     "que comprometen caja y tiempo. Sin diagnóstico previo, se decide por intuición.",
     "Nuestro trabajo es poner el problema en números y comparar opciones con criterios explícitos.",
     "No garantizamos resultados: garantizamos método, evidencia y seguimiento."),
    tarjeta("Diagnóstico empresarial", "Revisión de operación, finanzas y mercado con hallazgos priorizados.", "Punto de partida", "1")
    + tarjeta("Opciones estratégicas", "Alternativas comparadas por costo, riesgo y tiempo de retorno.", "Decisión", "2")
    + tarjeta("Modelo económico", "Qué tiene que pasar en ventas y costos para que la apuesta funcione.", "Viabilidad", "3")
    + tarjeta("Plan de implementación", "Responsables, hitos y presupuesto por etapa.", "Ejecución", "4")
    + tarjeta("Tablero de seguimiento", "Indicadores acordados para medir el avance real.", "Control", "5")
    + tarjeta("Acompañamiento a la dirección", "Sesiones de trabajo con el equipo directivo.", "Cercanía", "6"),
    paso(1, "Diagnóstico", "Entendemos el negocio y sus restricciones reales.")
    + paso(2, "Opciones", "Comparamos alternativas con supuestos explícitos.")
    + paso(3, "Decisión", "La dirección elige; nosotros dejamos el sustento por escrito.")
    + paso(4, "Seguimiento", "Medimos y ajustamos con datos del período."),
    ["Cada recomendación con su supuesto y su fuente.",
     "Modelo económico entregado y editable por el cliente.",
     "Actas de decisión y responsables nombrados."],
    [("Finanzas y analítica", "/finanzas"), ("Riesgos y cumplimiento", "/riesgos-y-cumplimiento"),
     ("Transformación digital", "/transformacion-digital"), ("Servicios", "/servicios")])

servicio(
    "consultoria-internacional", "14",
    "Visión local y comprensión de operaciones internacionales.",
    "Estructura, régimen cambiario e inversión extranjera para empresas colombianas que operan o piensan "
    "operar con el exterior.",
    ("Operar con el exterior sin mapa tributario y cambiario",
     "Importar, exportar, pagar servicios desde el exterior o recibir inversión implica obligaciones "
     "distintas en cada operación. Un error de clasificación se convierte en contingencia cambiaria o fiscal.",
     "Trabajamos la operación concreta: quién paga, por qué concepto, en qué moneda y con qué soporte.",
     "Cada jurisdicción tiene su norma: validamos por caso y no extrapolamos conclusiones de un país a otro."),
    tarjeta("Diagnóstico cambiario", "Clasificación de operaciones y obligaciones ante el régimen cambiario.", "Base", "1")
    + tarjeta("Inversión extranjera", "Registro, reportes y soportes de aportes y reinversión.", "Cumplimiento", "2")
    + tarjeta("Precios de transferencia", "Documentación de operaciones con vinculados económicos.", "Riesgo", "3")
    + tarjeta("Estructura de pagos", "Concepto, retención y soporte de cada pago internacional.", "Operación", "4")
    + tarjeta("Doble tributación", "Aplicación de convenios vigentes cuando existan y procedan.", "Optimización", "5")
    + tarjeta("Acompañamiento en auditorías", "Respuesta a requerimientos de origen cambiario o fiscal.", "Defensa", "6"),
    paso(1, "Mapa de operaciones", "Qué se hace hoy y cómo está documentado.")
    + paso(2, "Riesgos", "Dónde hay exposición cambiaria, fiscal o de reporte.")
    + paso(3, "Plan", "Correcciones, registros y calendario.")
    + paso(4, "Seguimiento", "Revisión periódica con cambios normativos."),
    ["Norma aplicable citada por jurisdicción.",
     "Validación por operación, no por analogía.",
     "Soportes listos para una revisión externa."],
    [("Tributación", "/tributacion"), ("Consultoría", "/consultoria"),
     ("Finanzas y analítica", "/finanzas"), ("Servicios", "/servicios")])

servicio(
    "riesgos-y-cumplimiento", "15",
    "Controles y prevención para fortalecer el gobierno empresarial.",
    "Mapas de riesgo, controles y políticas que permiten anticipar contingencias en lugar de reaccionar "
    "cuando ya ocurrieron.",
    ("El riesgo se descubre cuando ya costó dinero",
     "La mayoría de las contingencias no son sorpresas técnicas: son procesos sin dueño, permisos "
     "informales y decisiones sin soporte. Se ven al final, cuando llega el requerimiento o el reclamo.",
     "Ordenamos el gobierno de la empresa: quién decide, quién controla y cómo se deja evidencia.",
     "No instalamos matrices de 200 riesgos que nadie lee: trabajamos pocos riesgos, con control asignado."),
    tarjeta("Mapa de riesgos", "Identificación y valoración de riesgos por proceso y por impacto.", "Base", "1")
    + tarjeta("Matriz de controles", "Control, responsable, evidencia y frecuencia de verificación.", "Diseño", "2")
    + tarjeta("Políticas y manuales", "Documentos breves que el equipo pueda usar, no adornos.", "Gobierno", "3")
    + tarjeta("Cumplimiento normativo", "Matriz de obligaciones legales con responsable y fecha.", "Prevención", "4")
    + tarjeta("Canal de reporte", "Mecanismo para reportar irregularidades con reserva.", "Integridad", "5")
    + tarjeta("Seguimiento", "Revisión periódica del estado de cada control.", "Sostenibilidad", "6"),
    paso(1, "Diagnóstico", "Procesos críticos y puntos de exposición.")
    + paso(2, "Valoración", "Probabilidad e impacto, con criterio explícito.")
    + paso(3, "Diseño de controles", "Simples, verificables y con dueño.")
    + paso(4, "Seguimiento", "Evidencia periódica y ajuste del mapa."),
    ["Mapa de riesgos priorizado, no exhaustivo por cumplir.",
     "Cada control con evidencia verificable.",
     "Revisión con la dirección y acta de aprobación."],
    [("Auditoría", "/auditoria"), ("Tributación", "/tributacion"),
     ("Consultoría", "/consultoria"), ("Servicios", "/servicios")])

servicio(
    "inteligencia-artificial", "08",
    "Analítica e inteligencia artificial aplicadas a desafíos reales.",
    "Automatizamos procesos de información y análisis manteniendo el juicio profesional y la protección "
    "de los datos.",
    ("La tecnología sin criterio solo acelera el error",
     "Herramientas de IA pueden procesar miles de documentos en minutos; también pueden reproducir un "
     "error mil veces más rápido. La diferencia está en quién valida y con qué regla.",
     "Usamos automatización donde el proceso ya está definido y el resultado se puede verificar.",
     "No prometemos automatización total ni auditorías sin intervención humana."),
    tarjeta("Diagnóstico de procesos", "Qué tarea es repetitiva, cuánto cuesta y si vale automatizarla.", "Punto de partida", "1")
    + tarjeta("Extracción de documentos", "Facturas, extractos y soportes convertidos en datos estructurados.", "Eficiencia", "2")
    + tarjeta("Conciliaciones automáticas", "Cruce de información con reglas explícitas y alertas de excepción.", "Control", "3")
    + tarjeta("Modelos de análisis", "Clasificación, priorización y detección de anomalías con validación humana.", "Analítica", "4")
    + tarjeta("Tableros con datos vivos", "Información actualizada sin armado manual de reportes.", "Visibilidad", "5")
    + tarjeta("Reglas de uso y privacidad", "Qué datos se tratan, dónde y con qué autorización.", "Gobierno", "6"),
    paso(1, "Proceso", "Documentamos la tarea tal como se hace hoy.")
    + paso(2, "Regla", "Definimos qué resultado es correcto y cómo se comprueba.")
    + paso(3, "Automatización", "Implementamos con registro de cada ejecución.")
    + paso(4, "Supervisión", "Revisión por muestreo y ajuste continuo."),
    ["Cada automatización con registro y trazabilidad.",
     "Validación humana definida por escrito.",
     "Datos del cliente tratados con reserva y sin uso para entrenar modelos sin autorización."],
    [("Transformación digital", "/transformacion-digital"), ("Finanzas y analítica", "/finanzas"),
     ("Auditoría", "/auditoria"), ("Servicios", "/servicios")])

servicio(
    "transformacion-digital", "09",
    "Tecnología y procesos conectados para trabajar mejor.",
    "Ordenamos procesos y sistemas para que la información fluya sin retranscripción y con control del cambio.",
    ("Los sistemas no se conectan y el equipo hace de puente",
     "Cuando cada área tiene su archivo, la misma cifra se digita tres veces y nadie sabe cuál es la buena. "
     "El costo no es el software: es el tiempo y el error.",
     "Primero el proceso, después la herramienta. Automatizar un proceso mal definido solo lo hace más rápido y más caro.",
     "No vendemos licencias ni prometemos implantaciones sin alcance definido."),
    tarjeta("Mapa de procesos", "Qué se hace, en qué orden, con qué documento y quién autoriza.", "Base", "1")
    + tarjeta("Diseño del flujo", "Proceso objetivo documentado antes de tocar el sistema.", "Diseño", "2")
    + tarjeta("Integración de datos", "Una fuente por dato, sin doble digitación.", "Eficiencia", "3")
    + tarjeta("Control de cambios", "Versiones, responsables y pruebas antes de publicar.", "Gobierno", "4")
    + tarjeta("Capacitación", "Entrenamiento al equipo con manual de uso.", "Adopción", "5")
    + tarjeta("Medición", "Indicadores de tiempo, error y volumen antes y después.", "Resultado", "6"),
    paso(1, "Diagnóstico", "Procesos actuales, cuellos de botella y retrabajos.")
    + paso(2, "Diseño", "Flujo objetivo con reglas y responsables.")
    + paso(3, "Implantación", "Configuración, pruebas y migración controlada.")
    + paso(4, "Adopción", "Capacitación y medición del cambio."),
    ["Proceso documentado y aprobado antes de implantar.",
     "Pruebas registradas con evidencia.",
     "Indicadores comparables antes y después."],
    [("Inteligencia artificial", "/inteligencia-artificial"), ("Finanzas y analítica", "/finanzas"),
     ("Consultoría", "/consultoria"), ("Servicios", "/servicios")])

# ---------------------------------------------------------------- CONTACTO
CONTACTO = hero("16", "Cuéntenos qué necesita. Construyamos una respuesta.",
                "Revisamos su solicitud e identificamos el tipo de acompañamiento profesional más adecuado. "
                "La primera conversación es de diagnóstico, sin costo.",
                "Escribir a GVA Group", "mailto:gerencia@gvagroup.com.co",
                "Llamar ahora", "tel:+573219101850") + bloque("""
  <div class="row g-4">
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">✉</div><h3>Correo</h3>
      <p class="mb-0"><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></p></div></div>
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">☎</div><h3>Teléfono y WhatsApp</h3>
      <p class="mb-0"><a href="https://wa.me/573219101850">+57 321 910 1850</a></p></div></div>
    <div class="col-md-4"><div class="gva-card"><div class="gva-ico">◎</div><h3>Oficina</h3>
      <p class="mb-0">Calle 60B Sur # 44-100<br>Sabaneta, Antioquia, 055457<br>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Calle+60B+Sur+44-100+Sabaneta+Antioquia" target="_blank" rel="noopener">Ver en el mapa</a></p></div></div>
  </div>
  <p class="gva-nota mt-4">Sus datos se tratan conforme a nuestra
    <a href="/privacy">política de tratamiento de datos personales</a> y se usan solo para responder su solicitud.</p>
</div></section>""") + bloque("""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Qué pasa después de escribirnos</h2>
      <div class="row g-3">
        <div class="col-12"><strong>1.</strong> Confirmamos la recepción de su mensaje.</div>
        <div class="col-12"><strong>2.</strong> Una conversación breve para entender el caso.</div>
        <div class="col-12"><strong>3.</strong> Le decimos si podemos ayudar y con qué alcance.</div>
        <div class="col-12"><strong>4.</strong> Si aplica, enviamos propuesta con honorarios cerrados.</div>
      </div>
    </div>
    <div class="col-lg-6 text-center">
      <a class="gva-btn" href="/contactus">Ir al formulario de contacto</a>
      <p class="mt-3" style="font-size:.9rem;color:#4B5563">Formulario con nombre, correo, empresa, asunto y mensaje.</p>
    </div>
  </div>""", "gva-suave pt-5 pb-5")

pagina("contacto", "Contacto | GVA Group",
       "Escríbanos: gerencia@gvagroup.com.co · +57 321 910 1850 · Calle 60B Sur # 44-100, Sabaneta, Antioquia.",
       CONTACTO)
print("listo")
