# -*- coding: utf-8 -*-
"""Genera las paginas internas de gva-web con cabecera y pie comunes."""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

HEAD = """<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css">
</head>
<body>
<div class="barra-grad"></div>
<header class="sitio">
  <div class="wrap nav">
    <a class="logo" href="index.html" aria-label="GVA Group, inicio">
      <img src="assets/img/GVA_Logo_Principal.svg" alt="GVA Group">
    </a>
    <ul>
      <li><a href="index.html"{a1}>Inicio</a></li>
      <li><a href="firma.html"{a2}>Nuestra firma</a></li>
      <li><a href="servicios.html"{a3}>Servicios</a></li>
      <li><a href="casos.html"{a4}>Casos de éxito</a></li>
      <li><a href="contacto.html"{a5}>Contacto</a></li>
    </ul>
    <div class="acciones">
      <a class="btn btn-primario" href="contacto.html">Hablemos</a>
      <button class="menu-btn" aria-label="Menú">&#9776;</button>
    </div>
  </div>
</header>
<main>
"""

FOOT = """
</main>
<footer class="pie">
  <div class="wrap">
    <div class="columnas">
      <div class="col-logo">
        <img src="assets/img/GVA_Logo_Negativo.png" alt="GVA Group">
        <p>Contaduría, impuestos y ciencia de datos. Tecnología que simplifica.</p>
      </div>
      <div>
        <h4>Explorar</h4>
        <ul>
          <li><a href="index.html">Inicio</a></li>
          <li><a href="firma.html">Nuestra firma</a></li>
          <li><a href="casos.html">Casos de éxito</a></li>
          <li><span class="pronto">Blog · pronto</span></li>
          <li><a href="privacidad.html">Política de privacidad</a></li>
          <li><span class="pronto">Foro · pronto</span></li>
        </ul>
      </div>
      <div>
        <h4>Consultoría</h4>
        <ul>
          <li><a href="servicios.html">Servicios</a></li>
          <li><span class="pronto">Recursos · pronto</span></li>
          <li><span class="pronto">Mercado · pronto</span></li>
          <li><span class="pronto">Estrategia · pronto</span></li>
        </ul>
      </div>
      <div>
        <h4>Síguenos</h4>
        <ul>
          <li><a href="#">Facebook</a></li>
          <li><a href="#">X</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">Instagram</a></li>
        </ul>
      </div>
      <div>
        <h4>Contáctenos</h4>
        <ul>
          <li class="con-ico"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></li>
          <li class="con-ico"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4h4l2 5-3 2a12 12 0 006 6l2-3 5 2v4a2 2 0 01-2 2A18 18 0 012 6a2 2 0 012-2z"/></svg><a href="tel:+573219101850">+57 321 910 1850</a></li>
          <li style="margin-top:18px">
            <h4>Ubicación</h4>
            <span style="color:rgba(255,255,255,.72)">Calle 60B Sur # 44-100,<br>Sabaneta, Antioquia, 055457<br>Colombia</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="linea-pie">
      <span>© 2026 GVA Group S.A.S. Todos los derechos reservados.</span>
      <span><a href="privacidad.html">Tratamiento de datos personales</a></span>
    </div>
  </div>
</footer>
<script src="js/menu.js"></script>
</body>
</html>
"""


def page(fname, title, desc, body, cur):
    marks = {"a%d" % i: (' aria-current="page"' if i == cur else "") for i in range(1, 6)}
    html = HEAD.format(title=title, desc=desc, **marks) + body + FOOT
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("ok", fname, len(html))


FIRMA = """
<section>
  <div class="wrap">
    <span class="eyebrow">Nuestra firma</span>
    <h1 style="max-width:820px">Lo financiero y lo tributario no tienen que ser complejos si se miran a través de los datos.</h1>
    <p class="lead" style="max-width:760px">GVA Group nace de una convicción: la precisión normativa de la contaduría, unida a la capacidad de la analítica para encontrar patrones y anticipar riesgos.</p>
  </div>
</section>

<section class="suave">
  <div class="wrap dos-col">
    <div>
      <h2>Nuestra historia</h2>
      <p>Su fundador, Edgar Fernando Gelvis Vega, es contador público especialista en impuestos y magíster en análisis de datos. Esa combinación define la firma: rigor normativo y capacidad analítica en el mismo encargo.</p>
      <p>Desde el inicio de su carrera ha sostenido una política que hoy es el ADN de GVA Group: <strong>todo debe estar sustentado en datos</strong>. Una cifra sin soporte es una opinión; una cifra con soporte es una decisión.</p>
      <p>Por eso cada mensaje, propuesta o informe se respalda con evidencia verificable, y traducimos lo técnico a un lenguaje que el cliente entiende y puede usar.</p>
    </div>
    <div>
      <div class="bloque">
        <h3>Misión</h3>
        <p>Simplificar la gestión financiera, tributaria y tecnológica de las empresas mediante análisis de datos, automatización e inteligencia artificial, con decisiones siempre sustentadas en evidencia.</p>
      </div>
      <div class="bloque">
        <h3>Visión</h3>
        <p>Ser reconocidos en Colombia como el aliado que une contaduría, impuestos y ciencia de datos para que las empresas crezcan con información confiable y menos complejidad.</p>
      </div>
      <div class="bloque">
        <h3>Valores</h3>
        <ul class="lista-check">
          <li><strong>Evidencia:</strong> los datos sustentan cada recomendación.</li>
          <li><strong>Claridad:</strong> explicamos lo complejo en términos simples.</li>
          <li><strong>Integridad:</strong> cumplimiento normativo y ética profesional sin excepciones.</li>
          <li><strong>Innovación útil:</strong> adoptamos tecnología cuando resuelve un problema real.</li>
          <li><strong>Cercanía:</strong> acompañamos al cliente; no solo entregamos informes.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap dos-col">
    <div>
      <h2>Quién responde</h2>
      <p class="lead">Edgar Fernando Gelvis Vega · Director</p>
      <p>Contador público, especialista en impuestos y magíster en análisis de datos. Dirige personalmente los encargos de auditoría, planeación tributaria y analítica.</p>
      <p>La firma trabaja con un equipo de contadores y analistas que conoce el sector de cada cliente: salud, industria, servicios, transporte, inmobiliario y cultura.</p>
    </div>
    <div>
      <h2>La firma</h2>
      <table class="tabla-datos">
        <tr><td>Razón social</td><td>GVA GROUP S.A.S.</td></tr>
        <tr><td>NIT</td><td>901.841.984-9</td></tr>
        <tr><td>Actividad</td><td>Consultoría contable, tributaria y de gestión</td></tr>
        <tr><td>Matrícula</td><td>Cámara de Comercio de Medellín para Antioquia</td></tr>
        <tr><td>Oficina</td><td>Calle 60B Sur # 44-100, Sabaneta, Antioquia</td></tr>
        <tr><td>Correo</td><td><a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a></td></tr>
        <tr><td>Teléfono</td><td><a href="tel:+573219101850">+57 321 910 1850</a></td></tr>
      </table>
      <p style="margin-top:22px"><a class="btn btn-primario" href="contacto.html">Hablemos de su empresa</a></p>
    </div>
  </div>
</section>
"""

SERV = """
<section>
  <div class="wrap">
    <span class="eyebrow">Servicios</span>
    <h1 style="max-width:760px">Seis líneas de trabajo que se combinan según su empresa</h1>
    <p class="lead" style="max-width:780px">No vendemos paquetes cerrados. Revisamos su situación, identificamos qué le está costando dinero o tiempo, y armamos el trabajo con alcance y honorarios claros.</p>
  </div>
</section>

<section class="suave" style="padding-top:0">
  <div class="wrap" style="padding-top:70px">
    <div class="servicios">

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h10M7 13h6M7 17h4"/></svg></div>
        <h3>Outsourcing contable y BPO financiero</h3>
        <p>Contabilidad al día, cierres mensuales oportunos, conciliaciones, nómina y obligaciones. Usted recibe información lista para decidir, no solo documentos para archivar.</p>
        <span class="para">Sectores: transporte, industrial, inmobiliario, salud, financiero y comercial</span>
      </article>

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.4-3 7.9-7 9-4-1.1-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg></div>
        <h3>Revisoría fiscal y auditoría externa</h3>
        <p>Evaluación independiente del control interno y de los estados financieros, con hallazgos priorizados por riesgo y recomendaciones ejecutables. Informe para la junta, no un trámite.</p>
        <span class="para">Experiencia en transporte, industria, servicios financieros y comercio</span>
      </article>

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h4"/></svg></div>
        <h3>Planeación y auditoría tributaria</h3>
        <p>Revisión de lo declarado, detección de beneficios vigentes, atención de requerimientos y calendario fiscal controlado. Cada posición con su norma y su soporte.</p>
        <span class="para">Empresas nacionales y extranjeras, todos los sectores</span>
      </article>

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5m0 14h16"/><path d="M8 15l4-6 4 3 4-7"/></svg></div>
        <h3>NIIF: implementación y auditoría</h3>
        <p>Adopción con políticas contables que se sostienen años después del primer informe. Implementaciones desde 600 horas y auditorías desde 250 horas de trabajo.</p>
        <span class="para">Todos los sectores de la economía</span>
      </article>

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M14 17.5h7M17.5 14v7"/></svg></div>
        <h3>Datos y analítica (BI)</h3>
        <p>Tableros de margen, cartera, flujo de caja y costo, conciliados con la contabilidad. Una sola versión de la verdad para gerencia, socios y bancos.</p>
        <span class="para">Para gerencias que deciden con números</span>
      </article>

      <article class="tarjeta">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><circle cx="12" cy="12" r="3.2"/><path d="M12 5V3M12 21v-2"/></svg></div>
        <h3>IA y automatización</h3>
        <p>Automatizamos causación, conciliación, extracción de facturas y armado de reportes. La misma tarea, en menos horas y con menos errores de digitación.</p>
        <span class="para">Equipos contables con volumen alto de documentos</span>
      </article>

    </div>
  </div>
</section>

<section>
  <div class="wrap dos-col">
    <div>
      <h2>Servicios complementarios</h2>
      <ul class="lista-check">
        <li>Asesoría en régimen cambiario e inversión extranjera.</li>
        <li>Actualización tributaria en sus instalaciones (grupos de hasta 5 personas).</li>
        <li>Auditorías financieras, tributarias y operativas.</li>
        <li>Interventoría en proyectos específicos.</li>
        <li>Manejo de recursos humanos y liquidación de nómina.</li>
      </ul>
    </div>
    <div>
      <h2>Cómo se contrata</h2>
      <p>Primero una conversación de diagnóstico sin costo. Luego una propuesta con alcance, entregables, horas y honorarios. Nada empieza sin que usted tenga claro qué recibe y cuánto cuesta.</p>
      <p><a class="btn btn-primario" href="contacto.html">Solicitar propuesta</a></p>
    </div>
  </div>
</section>
"""

CASOS = """
<section>
  <div class="wrap">
    <span class="eyebrow">Casos de éxito</span>
    <h1 style="max-width:780px">Trabajos con nombre propio, no promesas genéricas</h1>
    <p class="lead" style="max-width:800px">Acompañamos a empresas de salud, industria, servicios, cultura y gremios. Por confidencialidad, el detalle de cada encargo se comparte en la conversación y siempre con autorización del cliente.</p>
  </div>
</section>

<section class="suave" style="padding-top:0">
  <div class="wrap" style="padding-top:70px">
    <table class="tabla-datos">
      <tr><td><strong>Sector salud</strong></td><td>Clínica ISIS · Laboratorio Espinosa Gómez</td></tr>
      <tr><td><strong>Industria y consumo</strong></td><td>Pintuco · Indumuebles · Alsina</td></tr>
      <tr><td><strong>Cultura y medios</strong></td><td>Discos Fuentes</td></tr>
      <tr><td><strong>Servicios y gremios</strong></td><td>Francisco Murillo · Cámara de Comercio de Medellín · Cootrasenvi · Adida</td></tr>
    </table>
    <p class="nota" style="margin-top:28px">¿Quiere ver un caso parecido al suyo? Escríbanos y le mostramos el alcance del trabajo, las cifras y las referencias que el cliente haya autorizado publicar.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="centrado">
      <h2>Clientes que confían en GVA Group</h2>
    </div>
    <div class="clientes">
      <div class="cliente"><img src="assets/clientes/clinica-isis.png" alt="Clínica ISIS"></div>
      <div class="cliente"><img src="assets/clientes/discos-fuentes.png" alt="Discos Fuentes"></div>
      <div class="cliente"><img src="assets/clientes/francisco-murillo.png" alt="Francisco Murillo"></div>
      <div class="cliente"><img src="assets/clientes/hc-ingenieria.png" alt="HC Ingeniería"></div>
      <div class="cliente"><img src="assets/clientes/camara-comercio-mde.png" alt="Cámara de Comercio de Medellín"></div>
      <div class="cliente"><img src="assets/clientes/pintuco.png" alt="Pintuco"></div>
      <div class="cliente"><img src="assets/clientes/cootrasenvi.png" alt="Cootrasenvi"></div>
      <div class="cliente"><img src="assets/clientes/alsina.png" alt="Alsina"></div>
      <div class="cliente"><img src="assets/clientes/zaponti.png" alt="Zaponti Consultores"></div>
      <div class="cliente"><img src="assets/clientes/espinosa-gomez.png" alt="Laboratorio Espinosa Gómez"></div>
    </div>
  </div>
</section>

<section class="banda">
  <div class="wrap">
    <h2>¿Su empresa se parece a alguno de estos casos?</h2>
    <p>Cuéntenos su situación y le decimos qué revisaríamos primero.</p>
    <div class="acciones">
      <a class="btn btn-claro" href="contacto.html">Escribir a GVA Group</a>
    </div>
  </div>
</section>
"""

CONT = """
<section>
  <div class="wrap">
    <span class="eyebrow">Contacto</span>
    <h1>Hablemos de su empresa</h1>
    <p class="lead" style="max-width:720px">Escríbanos o llame. La primera conversación es de diagnóstico, sin costo y sin compromiso: le decimos qué revisar primero.</p>

    <div class="tarjetas-contacto" style="margin-top:44px">
      <div class="contacto-card">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></div>
        <strong>Correo</strong>
        <a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a>
      </div>
      <div class="contacto-card">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M4 4h4l2 5-3 2a12 12 0 006 6l2-3 5 2v4a2 2 0 01-2 2A18 18 0 012 6a2 2 0 012-2z"/></svg></div>
        <strong>Teléfono y WhatsApp</strong>
        <a href="https://wa.me/573219101850">+57 321 910 1850</a>
      </div>
      <div class="contacto-card">
        <div class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 21s7-6.2 7-11a7 7 0 10-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg></div>
        <strong>Oficina</strong>
        <span>Calle 60B Sur # 44-100<br>Sabaneta, Antioquia, 055457<br><a href="https://www.google.com/maps/search/?api=1&amp;query=Calle+60B+Sur+44-100+Sabaneta+Antioquia" target="_blank" rel="noopener">Ver en el mapa</a></span>
      </div>
    </div>

    <h2>O déjenos sus datos</h2>
    <form class="formulario" id="form-contacto" action="mailto:gerencia@gvagroup.com.co" method="post" enctype="text/plain">
      <div><label for="n">Nombre y apellido</label><input id="n" name="nombre" required></div>
      <div><label for="e">Correo</label><input id="e" name="correo" type="email" required></div>
      <div><label for="emp">Empresa</label><input id="emp" name="empresa"></div>
      <div><label for="t">Teléfono</label><input id="t" name="telefono"></div>
      <div class="ancho"><label for="s">Tema</label>
        <select id="s" name="tema">
          <option>Contabilidad / outsourcing</option>
          <option>Revisoría fiscal o auditoría</option>
          <option>Tributario</option>
          <option>NIIF</option>
          <option>Datos y analítica</option>
          <option>Automatización con IA</option>
        </select>
      </div>
      <div class="ancho"><label for="m">Cuéntenos brevemente su situación</label><textarea id="m" name="mensaje" rows="5"></textarea></div>
      <div class="ancho"><button class="btn btn-primario" type="submit">Enviar mensaje</button></div>
    </form>
    <p class="nota" style="margin-top:22px;max-width:720px">Sus datos se usan solo para responder su solicitud y se tratan conforme a nuestra <a href="privacidad.html">política de tratamiento de datos</a>.</p>
  </div>
</section>
"""

PRIV = """
<section>
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Legal</span>
    <h1 style="font-size:clamp(1.7rem,3vw,2.4rem)">Política de tratamiento de datos personales</h1>
    <p class="lead">GVA GROUP S.A.S. trata los datos personales conforme a la Ley 1581 de 2012 y al Decreto 1377 de 2013.</p>

    <h3 style="margin-top:38px">¿Quién es el responsable?</h3>
    <p>GVA GROUP S.A.S., con oficina en Calle 60B Sur # 44-100, Sabaneta, Antioquia, Colombia. Correo de atención: <a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a>.</p>

    <h3>¿Qué datos tratamos?</h3>
    <p>Los que usted nos entrega voluntariamente al escribirnos o contratar un servicio: nombre, empresa, correo, teléfono y la información necesaria para prestar el servicio contratado. En desarrollo de trabajos contables y tributarios tratamos información financiera de la empresa cliente, sujeta a deber de reserva profesional.</p>

    <h3>¿Para qué los usamos?</h3>
    <p>Para responder su solicitud, elaborar propuestas, ejecutar el servicio contratado, cumplir obligaciones legales y contables, y enviarle información de interés profesional cuando lo haya autorizado.</p>

    <h3>Sus derechos</h3>
    <p>Como titular puede conocer, actualizar, rectificar y suprimir sus datos, revocar la autorización y presentar quejas ante la Superintendencia de Industria y Comercio. Para ejercerlos escriba a <a href="mailto:gerencia@gvagroup.com.co">gerencia@gvagroup.com.co</a>; respondemos en los términos de ley.</p>

    <h3>Seguridad y conservación</h3>
    <p>Aplicamos medidas técnicas y administrativas razonables para proteger la información. Los datos se conservan mientras exista la relación comercial y durante los plazos exigidos por la normativa contable y tributaria.</p>

    <h3>Cookies</h3>
    <p>Este sitio no usa cookies de publicidad ni de seguimiento. Si en el futuro se incorporan herramientas de medición, se informará en esta misma página.</p>

    <p class="nota" style="margin-top:36px">Última actualización: noviembre de 2026. Cualquier cambio en esta política se publicará en esta misma página.</p>
  </div>
</section>
"""

page("firma.html", "Nuestra firma | GVA Group",
     "Quiénes somos: GVA Group une contaduría, impuestos y ciencia de datos. Misión, visión, valores y dirección de la firma.",
     FIRMA, 2)

page("servicios.html", "Servicios | GVA Group",
     "Outsourcing contable, revisoría fiscal, planeación tributaria, NIIF, analítica de datos e IA para empresas.",
     SERV, 3)

page("casos.html", "Casos de éxito | GVA Group",
     "Sectores y empresas que confían en GVA Group: salud, industria, cultura y servicios.",
     CASOS, 4)

page("contacto.html", "Contacto | GVA Group",
     "Escríbanos: gerencia@gvagroup.com.co · +57 321 910 1850 · Calle 60B Sur # 44-100, Sabaneta, Antioquia.",
     CONT, 5)

page("privacidad.html", "Política de privacidad | GVA Group",
     "Política de tratamiento de datos personales de GVA Group S.A.S. conforme a la Ley 1581 de 2012.",
     PRIV, 0)
