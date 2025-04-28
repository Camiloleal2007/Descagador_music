const parrafo = document.getElementById('parrafo');
const boton = document.getElementById('download-button');
const formulario = document.getElementById('download-form');
const barraProgreso = document.querySelector('.progreso');
formulario.addEventListener("submit", function(event) {
    event.preventDefault();
    boton.disabled = true;
    parrafo.textContent = '¡Descargando Música! Espere...';
    let url = document.getElementById("url-input").value;
    fetch("/download", {
        method: "POST",
        body: new URLSearchParams({url: url}),
        headers: {"Content-Type": "application/x-www-form-urlencoded"}
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error); 
            parrafo.textContent = 'Listo para descargar';
            boton.disabled = false;
        }
    })
    .catch(error => {
        alert("Exito: Musica Descargada Con Exito!!!");
        parrafo.textContent = 'Listo para descargar';
        document.getElementById("url-input").value = '';
    })
    .finally(() => {
    boton.disabled = false;
    document.getElementById("url-input").value = '';
});
});