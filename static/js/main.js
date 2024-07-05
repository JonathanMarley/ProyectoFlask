const btnDelete = document.querySelectorAll('.btn-delete')

if (btnElimbtnDeleteinar) {
   const btnArray =  Array.from(btnDelete);
   btnArray.forEach((btn) => {
    btn.addEventListener('click',(e) =>{
        if (!confirm('Quieres borrar este registro ??')) {
            e.preventDefault();
        }
    });
   });
}