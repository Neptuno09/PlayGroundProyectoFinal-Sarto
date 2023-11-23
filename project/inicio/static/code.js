document.getElementById('imagenAumentable').addEventListener('click', function() {
    this.classList.toggle('ampliada');
  });
$(document).foundation();

$(function() {
$('.button-like')
    .bind('click', function(event) {
    $(".button-like").toggleClass("liked");
    })
});