document.getElementById('theme-toggle').addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
});

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

// Funcion copiar ID pedido
function copyToClipboard(id) {
  var textToCopy = id; // Texto específico que quieres copiar
  
  // Crea un elemento de textarea temporal
  var textarea = document.createElement("textarea");
  textarea.value = textToCopy;
  
  // Añade el elemento de textarea al documento
  document.body.appendChild(textarea);
  
  // Selecciona y copia el contenido del textarea
  textarea.select();
  document.execCommand("copy");
  
  // Elimina el elemento de textarea temporal
  document.body.removeChild(textarea);
}

const myOffcanvas = document.getElementById('myOffcanvas')
myOffcanvas.addEventListener('hidden.bs.offcanvas', event => {
  // do something...
})