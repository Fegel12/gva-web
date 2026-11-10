# -*- coding: utf-8 -*-
"""Fase 2: Nuestra firma, Formacion, Casos de exito, Publicaciones e Investigacion."""
import os, importlib.util, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("f1", os.path.join(RAIZ, "fase1", "generar_fase1.py"))
f1 = importlib.util.module_from_spec(spec)
sys.modules["f1"] = f1
spec.loader.exec_module(f1)          # carga ESTILO, hero, bloque, tarjeta, paso, pruebas, banda, pagina

SALIDA = os.path.join(RAIZ, "fase2")
os.makedirs(SALIDA, exist_ok=True)


def pagina(nombre, titulo, desc, contenido):
    html = f"""<!DOCTYPE html>
<html lang="es-CO"><head><meta charset="utf-8">
<title>{titulo}</title><meta name="description" content="{desc}">
</head><body>{f1.ESTILO}<div class="gva">{contenido}</div></body></html>"""
    with open(os.path.join(SALIDA, nombre + ".html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print(nombre + ".html", len(html))


# ------------------------------------------------------------------ NUESTRA FIRMA
RETRATO = "https://fegel12.github.io/gva-web/odoo-web/img/retrato.jpg"
FIRMA = f1.hero("02", "Experiencia profesional para decisiones empresariales más sólidas.",
                "GVA Group une contaduría, impuestos y ciencia de datos. Cada cifra con soporte, cada decisión con evidencia.",
                "Conozca nuestra firma", "#historia") + f1.bloque(f"""
  <div class="row justify-content-center"><div class="col-lg-10 text-center">
    <p class="eyebrow mb-2">Qué hacemos</p>
    <p style="font-size:clamp(1.1rem,2vw,1.4rem);line-height:1.55;color:#2E3540;font-weight:500;margin:0">
      En GVA Group las cifras de su empresa se sostienen. Auditamos, ordenamos los procesos que las producen y
      automatizamos lo repetitivo: menos retrabajo, riesgos vistos a tiempo y decisiones con evidencia.
      <strong>Contabilidad, impuestos, finanzas y datos, sobre una misma base.</strong>
    </p>
  </div></div>""") + f1.bloque(f"""
  <div class="row g-5" id="historia">
    <div class="col-lg-7">
      <p class="eyebrow mb-1">Nuestra historia</p>
      <h2 class="h3 mb-3">Lo financiero y lo tributario no tienen que ser complejos si se miran a través de los datos</h2>
      <p>El fundador, Edgar Fernando Gelvis Vega, es contador público especialista en impuestos y magíster en
        análisis de datos. Esa combinación define la firma: rigor normativo y capacidad analítica en el mismo trabajo.</p>
      <p>Desde el inicio de su carrera ha sostenido una política que hoy es el ADN de GVA Group:
        <strong>todo debe estar sustentado en datos</strong>. Una cifra sin soporte es una opinión;
        una cifra con soporte es una decisión.</p>
      <p class="mb-0">Por eso cada mensaje, propuesta o informe se respalda con evidencia verificable, y lo técnico
        se traduce a un lenguaje que el cliente entiende y puede usar.</p>
    </div>
    <div class="col-lg-5">
      <div class="gva-card mb-4"><h3>Misión</h3>
        <p class="mb-0">Simplificar la gestión financiera, tributaria y tecnológica de las empresas mediante
          análisis de datos, automatización e inteligencia artificial, con decisiones sustentadas en evidencia.</p></div>
      <div class="gva-card"><h3>Visión</h3>
        <p class="mb-0">Ser reconocidos en Colombia como el aliado que une contaduría, impuestos y ciencia de
          datos para que las empresas crezcan con información confiable y menos complejidad.</p></div>
    </div>
  </div>""") + f1.bloque("""
  <div class="text-center mb-4"><p class="eyebrow mb-1">Valores</p>
    <h2 class="h1">Cinco reglas que no se negocian</h2></div>
  <div class="row g-3">
    <div class="col-6 col-lg"><div class="gva-card"><h3>Evidencia</h3><p>Los datos sustentan cada recomendación.</p></div></div>
    <div class="col-6 col-lg"><div class="gva-card"><h3>Claridad</h3><p>Explicamos lo complejo en términos simples.</p></div></div>
    <div class="col-6 col-lg"><div class="gva-card"><h3>Integridad</h3><p>Cumplimiento y ética profesional sin excepciones.</p></div></div>
    <div class="col-6 col-lg"><div class="gva-card"><h3>Innovación útil</h3><p>Tecnología cuando resuelve un problema real.</p></div></div>
    <div class="col-6 col-lg"><div class="gva-card"><h3>Cercanía</h3><p>Acompañamos; no solo entregamos informes.</p></div></div>
  </div>""", "gva-suave pt-5 pb-5") + f1.bloque("""
  <div class="row g-5">
    <div class="col-lg-2 text-center text-lg-start">
      <img src="/web/image/1636" alt="Edgar Fernando Gelvis Vega, director de GVA Group" loading="eager"
           style="width:150px;height:150px;object-fit:cover;border-radius:50%;box-shadow:0 12px 28px rgba(26,60,70,.18);border:4px solid #fff">
    </div>
    <div class="col-lg-4">
      <h2 class="h3 mb-2">Quién responde</h2>
      <p class="lead mb-2">Edgar Fernando Gelvis Vega · Director</p>
      <p>Contador público, especialista en impuestos y magíster en análisis de datos. Dirige personalmente los
        trabajos de auditoría, planeación tributaria y analítica.</p>
      <p class="mb-0">El equipo conoce el sector de cada cliente: salud, industria, servicios, transporte,
        inmobiliario y cultura.</p>
    </div>
    <div class="col-lg-6">
      <div class="gva-card"><h3>Datos de la firma</h3>
        <table class="table table-sm mb-0" style="font-size:.93rem">
          <tr><td style="color:#4B5563;width:38%">Razón social</td><td>GVA GROUP S.A.S.</td></tr>
          <tr><td style="color:#4B5563">NIT</td><td>901.841.984-9</td></tr>
          <tr><td style="color:#4B5563">Actividad</td><td>Consultoría contable, tributaria y de gestión</td></tr>
          <tr><td style="color:#4B5563">Matrícula</td><td>Cámara de Comercio de Medellín para Antioquia</td></tr>
          <tr><td style="color:#4B5563">Oficina</td><td>Calle 60B Sur # 44-100, Sabaneta, Antioquia</td></tr>
          <tr><td style="color:#4B5563">Correo</td><td><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></td></tr>
          <tr><td style="color:#4B5563">Teléfono</td><td><a href="tel:+573219101850">+57 321 910 1850</a></td></tr>
          <tr><td style="color:#4B5563">Datos personales</td><td><a href="/privacy">Política de tratamiento</a></td></tr>
        </table></div>
    </div>
  </div>""") + f1.pruebas([
    "Metodología documentada en cada trabajo.",
    "Informes con fuente, fecha y responsable.",
    "Datos del cliente tratados con reserva profesional.",
]) + f1.bloque("""
  <div class="row g-5">
    <div class="col-lg-6">
      <p class="eyebrow mb-1">Cómo trabajamos</p>
      <h2 class="h3 mb-3">Escuchamos antes de proponer</h2>
      <p>Preguntamos lo incómodo temprano: qué no está documentado, quién depende de quién, qué pasaría si esa
        persona falta. Esas preguntas molestan al principio y ahorran problemas después.</p>
      <p>Después decimos tres cosas con claridad: <strong>qué podemos resolver, qué no, y qué necesitamos de
        usted</strong> para hacerlo. Si su caso no es para nosotros, se lo decimos antes de cobrar, no al final.</p>
      <p class="mb-0">La primera conversación es de diagnóstico, no de venta.</p>
    </div>
    <div class="col-lg-6">
      <div class="gva-card h-100">
        <h3 class="h5 mb-3">Lo que necesitamos de usted</h3>
        <ul class="gva-lista">
          <li>Acceso a la información real, aunque esté desordenada.</li>
          <li>Una persona responsable que pueda decidir, no solo opinar.</li>
          <li>Disposición a corregir el proceso, no solo el número.</li>
          <li>Tiempo del equipo para las preguntas que vamos a hacer.</li>
        </ul>
        <p class="mb-0 mt-3" style="font-size:.92rem;color:#4B5563">Con eso, cualquier firma seria puede ayudarle.
          Sin eso, ninguna puede.</p>
      </div>
    </div>
  </div>""") + f1.banda("Conozca cómo trabajamos", "Una conversación de diagnóstico, sin costo.")

pagina("nuestra-firma", "Nuestra firma | GVA Group",
       "GVA Group: contaduría, impuestos y ciencia de datos. Misión, visión, valores y dirección de la firma.",
       FIRMA)

# ------------------------------------------------------------------ FORMACION
FORMACION = f1.hero("10", "Aprendizaje aplicado para equipos y profesionales.",
                    "Formación en materias tributarias, contables, financieras y tecnológicas, orientada al "
                    "ejercicio profesional y a decisiones concretas.",
                    "Ver cursos disponibles", "/slides") + f1.bloque("""
  <div class="text-center mb-5"><p class="eyebrow mb-1">Oferta</p>
    <h2 class="h1">Tres formas de aprender con nosotros</h2></div>
  <div class="row g-4">
    """ + f1.tarjeta("Curso en línea", "Lecciones cortas, con ejemplos y ejercicios sobre casos reales de empresa.", "Estudie a su ritmo", "▶")
    + f1.tarjeta("Capacitación en su empresa", "Actualización tributaria y contable en sus instalaciones, hasta grupos de cinco personas.", "Presencial", "◇")
    + f1.tarjeta("Acompañamiento técnico", "Sesiones de trabajo con su equipo sobre un caso concreto: cierre, reforma o implementación.", "Aplicado", "◎")
    + """</div>
</section>""") + f1.bloque("""
  <div class="row g-5 align-items-center">
    <div class="col-lg-6">
      <p class="eyebrow mb-1">Cómo enseñamos</p>
      <h2 class="h3 mb-3">Primero el criterio, después la herramienta</h2>
      <ul class="gva-lista">
        <li>Cada tema con su norma, su fecha y su fuente.</li>
        <li>Ejemplos con cifras de trabajo, no con teoría suelta.</li>
        <li>Ejercicios que se corrigen y se explican.</li>
        <li>Material actualizado cuando cambia la norma.</li>
      </ul>
    </div>
    <div class="col-lg-6"><div class="gva-card">
      <h3>Cursos disponibles</h3>
      <p>El catálogo está en la plataforma de formación: hoy incluye <strong>Planeación tributaria básica</strong>,
        con tres lecciones publicadas.</p>
      <a class="gva-btn" href="/slides">Entrar a los cursos</a></div></div>
  </div>""", "gva-suave pt-5 pb-5") + f1.pruebas([
    "Contenido revisado por el director de la firma.",
    "Norma y fecha en cada afirmación.",
    "Actualización cuando cambia la norma aplicable.",
]) + f1.banda("¿Necesita formar a su equipo?", "Diseñamos la capacitación sobre su caso concreto.")

pagina("formacion", "Formación | GVA Group",
       "Cursos y capacitaciones en materia tributaria, contable, financiera y tecnológica.",
       FORMACION)

# ------------------------------------------------------------------ CASOS DE EXITO
CASOS = f1.hero("13", "Resultados y aprendizajes de proyectos documentados.",
                "Trabajamos con empresas de salud, industria, servicios, cultura y gremios. Por confidencialidad, "
                "el detalle se comparte en la conversación y siempre con autorización del cliente.",
                "Ver experiencias", "#sectores") + f1.bloque("""
  <div class="row g-5" id="sectores">
    <div class="col-lg-7">
      <p class="eyebrow mb-1">Dónde hemos trabajado</p>
      <h2 class="h3 mb-3">Sectores y tipo de trabajo</h2>
      <table class="table" style="font-size:.95rem">
        <tr><td style="width:34%;color:#4B5563"><strong>Salud</strong></td><td>Clínica ISIS · Laboratorio Espinosa Gómez</td></tr>
        <tr><td style="color:#4B5563"><strong>Industria y consumo</strong></td><td>Pintuco · Indumuebles · Alsina</td></tr>
        <tr><td style="color:#4B5563"><strong>Cultura y medios</strong></td><td>Discos Fuentes</td></tr>
        <tr><td style="color:#4B5563"><strong>Servicios y gremios</strong></td><td>Francisco Murillo · Cámara de Comercio de Medellín · Cootrasenvi · Adida · Zaponti · HC Ingeniería</td></tr>
      </table>
    </div>
    <div class="col-lg-5"><div class="gva-nota">
      Publicamos el detalle de un caso solo con autorización escrita del cliente: situación, trabajo realizado
      y resultado. Mientras no exista esa autorización, el caso se conversa, no se publica.
    </div></div>
  </div>""") + f1.bloque("""
  <div class="text-center mb-5"><p class="eyebrow mb-1">Qué aprende el cliente</p>
    <h2 class="h1">El resultado no es un informe: es una decisión mejor sustentada</h2></div>
  <div class="row g-4">
    """ + f1.tarjeta("Orden que resiste revisión", "Contabilidad y soportes listos antes de que llegue el requerimiento.", "Auditoría y control", "1")
    + f1.tarjeta("Impuesto explicado", "Cada posición tributaria con norma, fecha y cálculo.", "Tributación", "2")
    + f1.tarjeta("Cifras que llegan a tiempo", "Tableros mensuales conciliados con el balance.", "Finanzas", "3")
    + """</div>
</section>""", "gva-suave pt-5 pb-5") + \
    f1.bloque("""
  <div class="text-center mb-2"><p class="eyebrow mb-1">Trayectoria</p><h2 class="h1">Clientes que han confiado en nosotros</h2><p class="lead mb-0">Empresas de salud, industria, cultura, construcción, servicios y gremios que nos han confiado su información en distintos momentos.</p></div>
  <div class="row g-3 text-center align-items-center">
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1612" alt="Clínica ISIS"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1613" alt="Discos Fuentes"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1614" alt="Francisco Murillo"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1615" alt="Cámara de Comercio de Medellín"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1616" alt="Pintuco"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1617" alt="Alsina"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1618" alt="Zaponti"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1619" alt="HC Ingeniería"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1620" alt="Laboratorio Espinosa Gómez"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1621" alt="Camacol"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1622" alt="Estrategas en Formación"></div>
    <div class="col-6 col-md-4 col-lg-3 text-center"><img loading="eager" style="height:64px;width:auto;filter:grayscale(100%)" src="/web/image/1638" alt="Schindler"></div>
  </div>""") + f1.banda("¿Su empresa se parece a alguno de estos casos?",
                       "Cuéntenos su situación y le decimos qué revisaríamos primero.")

pagina("casos-de-exito", "Casos de éxito | GVA Group",
       "Sectores y empresas que trabajan con GVA Group: salud, industria, cultura, servicios y gremios.",
       CASOS)

# ------------------------------------------------------------------ PUBLICACIONES (hub)
PUBLICACIONES = f1.hero("12", "Ideas, análisis y conocimiento para estar mejor informado.",
                        "Publicamos lo que aprendemos trabajando con empresas colombianas: cifras con soporte, "
                        "normas explicadas sin rodeos y decisiones que se pueden sustentar.",
                        "Leer el blog", "/blog") + f1.bloque("""
  <div class="row g-4">
    <div class="col-lg-6"><div class="gva-card h-100">
      <h3>Blog</h3>
      <p>Artículos sobre profesión contable, tributación y datos. Escritos para decidir, no para archivar.</p>
      <a class="gva-btn" href="/blog">Ver artículos</a></div></div>
    <div class="col-lg-6"><div class="gva-card h-100">
      <h3>Investigación</h3>
      <p>Análisis técnico y normativo con trazabilidad: fuente, fecha y jurisdicción en cada afirmación.</p>
      <a class="gva-btn-2" href="/investigacion">Ver investigaciones</a></div></div>
  </div>""") + f1.bloque("""
  <div class="row g-5 align-items-center">
    <div class="col-lg-7">
      <p class="eyebrow mb-1">Cómo escribimos</p>
      <h2 class="h3 mb-3">Si no se puede sustentar, no se publica</h2>
      <ul class="gva-lista">
        <li>Norma con artículo, fecha y fuente.</li>
        <li>Sin promesas de ahorro ni cifras inventadas.</li>
        <li>Advertencia expresa cuando el caso requiere análisis particular.</li>
      </ul>
    </div>
    <div class="col-lg-5"><div class="gva-card"><h3>¿Quiere que escribamos sobre un tema?</h3>
      <p class="mb-3">Escríbanos y lo evaluamos con el equipo técnico.</p>
      <a class="gva-btn" href="/contacto">Sugerir un tema</a></div></div>
  </div>""", "gva-suave pt-5 pb-5") + f1.banda("Reciba nuestros análisis",
                                          "Escríbanos y le compartimos las publicaciones nuevas.")

pagina("publicaciones", "Publicaciones | GVA Group",
       "Blog e investigación técnica de GVA Group: tributación, contabilidad, finanzas y datos.",
       PUBLICACIONES)

# ------------------------------------------------------------------ INVESTIGACION
INVESTIGACION = f1.hero("11", "Análisis técnico y normativo con trazabilidad documental.",
                        "Cada afirmación con su fuente, su fecha y su jurisdicción. Sin conclusiones que no se "
                        "puedan verificar.",
                        "Consultar publicaciones", "/contacto") + f1.bloque("""
  <div class="text-center mb-5"><p class="eyebrow mb-1">Líneas de trabajo</p>
    <h2 class="h1">Qué investigamos</h2></div>
  <div class="row g-4">
    """ + f1.tarjeta("Cambios normativos", "Qué cambió, desde cuándo rige y a quién afecta.", "Tributario", "1")
    + f1.tarjeta("Criterios de la administración", "Conceptos y doctrina, con su alcance real.", "Normativo", "2")
    + f1.tarjeta("Datos y analítica aplicada", "Métodos de análisis sobre información contable.", "Técnico", "3")
    + f1.tarjeta("Buenas prácticas de control", "Qué controles funcionan y por qué.", "Auditoría", "4")
    + f1.tarjeta("Operaciones internacionales", "Régimen cambiario y tributación de operaciones con el exterior.", "Internacional", "5")
    + f1.tarjeta("Casos documentados", "Situaciones reales, anonimizadas y con autorización.", "Aplicado", "6")
    + """</div>
</section>""") + f1.bloque("""
  <div class="row g-5">
    <div class="col-lg-6">
      <h2 class="h3 mb-3">Reglas de publicación</h2>
      <ul class="gva-lista">
        <li>Fecha de publicación y fecha de última revisión visibles.</li>
        <li>Documento fuente citado: norma, concepto o jurisprudencia.</li>
        <li>Estado de vigencia declarado.</li>
        <li>Advertencia de que no sustituye una asesoría sobre el caso concreto.</li>
      </ul>
    </div>
    <div class="col-lg-6"><div class="gva-nota">
      Este espacio está en construcción. Las investigaciones se publican cuando cumplen las cuatro reglas
      anteriores; mientras tanto, el análisis se comparte en la conversación con el cliente.
    </div></div>
  </div>""", "gva-suave pt-5 pb-5") + f1.banda("¿Necesita el análisis de una norma concreta?",
                                             "Lo revisamos con usted y le entregamos la conclusión con su fuente.")

pagina("investigacion", "Investigación | GVA Group",
       "Análisis técnico y normativo con trazabilidad documental. Reglas de publicación y líneas de investigación.",
       INVESTIGACION)
print("fase 2 lista")
