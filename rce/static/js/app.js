function mostrarContenido(contenidoId) {
    // Ocultar todos los contenidos
    var contenidos = document.getElementsByClassName('contenido');
    for (var i = 0; i < contenidos.length; i++) {
        contenidos[i].style.display = 'none';
    }

    // Mostrar el contenido seleccionado
    var contenido = document.getElementById(contenidoId);
    contenido.style.display = 'block';
}
