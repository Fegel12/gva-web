/* Menú móvil: abre y cierra la navegación en pantallas pequeñas */
document.addEventListener('click', function (e) {
  var boton = e.target.closest('.menu-btn');
  if (boton) {
    document.querySelector('.nav').classList.toggle('abierto');
    return;
  }
  var enlace = e.target.closest('.nav.abierto ul a');
  if (enlace) document.querySelector('.nav').classList.remove('abierto');
});

/* Formulario de contacto: arma el correo con los datos del formulario */
var form = document.getElementById('form-contacto');
if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form);
    var linea = function (k) { return (d.get(k) || '').toString().trim(); };
    var asunto = 'Solicitud desde el sitio web - ' + (linea('empresa') || linea('nombre'));
    var cuerpo = [
      'Nombre: ' + linea('nombre'),
      'Empresa: ' + linea('empresa'),
      'Correo: ' + linea('correo'),
      'Teléfono: ' + linea('telefono'),
      'Tema: ' + linea('tema'),
      '',
      'Situación:',
      linea('mensaje')
    ].join('\n');
    window.location.href = 'mailto:gerencia@gvagroup.com.co?subject=' +
      encodeURIComponent(asunto) + '&body=' + encodeURIComponent(cuerpo);
  });
}
