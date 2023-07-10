
document.addEventListener("DOMContentLoaded", function() {
  var todos = document.getElementById("todos");
  var sillones = document.getElementById("sillones");
  var mesas = document.getElementById("mesas");
  var escritorios = document.getElementById("escritorios");
  var tecnologia = document.getElementById("tecnologia");

  todos.addEventListener("click", function() {
    showElements(".card-sillones", ".card-escritorios", ".card-mesas", ".card-tecnologia");
    removeClasses("escritorios", "mesas", "tecnologia", "sillones");
    toggleClasses(todos, "active-tab");
  });

  sillones.addEventListener("click", function() {
    showElements(".card-sillones");
    hideElements(".card-escritorios", ".card-mesas", ".card-tecnologia");
    removeClasses("escritorios", "mesas", "tecnologia", "todos");
    toggleClasses(sillones, "active-tab");
  });

  mesas.addEventListener("click", function() {
    showElements(".card-mesas");
    hideElements(".card-escritorios", ".card-sillones", ".card-tecnologia");
    removeClasses("escritorios", "sillones", "tecnologia", "todos");
    toggleClasses(mesas, "active-tab");
  });

  escritorios.addEventListener("click", function() {
    showElements(".card-escritorios");
    hideElements(".card-sillones", ".card-mesas", ".card-tecnologia");
    removeClasses("sillones", "mesas", "tecnologia", "todos");
    toggleClasses(escritorios, "active-tab");
  });

  tecnologia.addEventListener("click", function() {
    showElements(".card-tecnologia");
    hideElements(".card-sillones", ".card-mesas", ".card-escritorios");
    removeClasses("sillones", "mesas", "escritorios", "todos");
    toggleClasses(tecnologia, "active-tab");
  });
});

// Muestra los elementos
function showElements() {
  var selectors = Array.prototype.slice.call(arguments);
  selectors.forEach(function(selector) {
    var elements = document.querySelectorAll(selector);
    elements.forEach(function(element) {
      element.style.display = "block";
    });
  });
}
//Oculta los elementos
function hideElements() {
  var selectors = Array.prototype.slice.call(arguments);
  selectors.forEach(function(selector) {
    var elements = document.querySelectorAll(selector);
    elements.forEach(function(element) {
      element.style.display = "none";
    });
  });
}
//elimina las clases
function removeClasses() {
  var ids = Array.prototype.slice.call(arguments);
  ids.forEach(function(id) {
    var element = document.getElementById(id);
    element.classList.remove("active-tab");
  });
}
//color amarillo
function toggleClasses(element, className) {
  element.classList.toggle(className);
}


//posicionar botones menu
window.addEventListener('scroll', function() {
  var menu = document.getElementById('catalogo-menu');
  var alturaLimite = 500; 

  if (window.pageYOffset > alturaLimite) {
    menu.classList.add('fixed');
  } else {
    menu.classList.remove('fixed');
  }
});




//Efecto carrusel a los botones
const botones = document.querySelector('#catalogo-menu');
const btnIzq = document.querySelector('.izquierdo');
const btnDer = document.querySelector('.derecho');

btnIzq.addEventListener('click', () => {
  botones.scrollBy({
    left: -botones.offsetWidth,
    behavior: 'smooth'
  });
});

btnDer.addEventListener('click', () => {
  botones.scrollBy({
    left: botones.offsetWidth,
    behavior: 'smooth'
  });
});


