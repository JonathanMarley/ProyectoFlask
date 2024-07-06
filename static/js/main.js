// Selecciona todos los elementos con la clase 'btn-delete'
const btnDelete = document.querySelectorAll('.btn-delete');

// Comprueba si hay elementos seleccionados
if (btnDelete.length > 0) {
    // Convierte la NodeList a un array
    const btnArray = Array.from(btnDelete);
    
    // Itera sobre cada botón en el array
    btnArray.forEach((btn) => {
        // Añade un evento 'click' a cada botón
        btn.addEventListener('click', (e) => {
            // Muestra una ventana de confirmación al usuario
            if (!confirm('¿Quieres borrar este registro?')) {
                // Si el usuario cancela, previene la acción predeterminada (la eliminación)
                e.preventDefault();
            }
        });
    });
}
