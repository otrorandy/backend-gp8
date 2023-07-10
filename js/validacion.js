function validarFormulario() {
var nombre = document.getElementById("nombre").value.trim();
var correo = document.getElementById("correo").value.trim();
var telefono = document.getElementById("telefono").value.trim();

if (nombre === "" || correo === "" || telefono === "") {
    alert("Por favor, complete todos los campos del formulario.");
    return false;
  }



for (var i = 0; i < nombre.length; i++) {
    var charCode = nombre.charCodeAt(i);
    if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32)) {
      alert("El campo 'nombre' solo puede contener caracteres alfabéticos y espacios.");
      return false;
    }
  }

var regexEmail = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,4})+$/;

if (!regexEmail.test(correo)) {
  alert("El campo correo solo puede contener direcciones validas ejemplo@ejemlo.com");
  return false;
}


var regexTel = /^\(?(\d{5})\)?[-]?(\d{4})[-]?(\d{4})$/;


if (!regexTel.test(telefono)) {
  alert("El campo telefono solo puede contener numeros validos 54911-xxxx-xxxx");
  return false;
}

 
  alert("Formulario enviado correctamente.");
  return true;
}