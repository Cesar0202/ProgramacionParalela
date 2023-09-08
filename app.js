var segundosTranscurridos = 0;
var cronometroInterval;

function iniciarCronometro() {
    cronometroInterval = setInterval(function() {
        segundosTranscurridos++;
        document.getElementById('cronometro').innerText = 'Tiempo transcurrido: ' + segundosTranscurridos + ' segundos';
    }, 1000); // Actualizar cada segundo (1000 ms)
}

$(document).ready(function() {
    iniciarCronometro(); // Iniciar el cronómetro al cargar la página

    // Definir las categorías disponibles
    var categoriasDisponibles = [
        "age", "alone", "amazing", "anger", "architecture", "art", "attitude",
        "beauty", "best", "birthday", "business", "car", "change", "communications",
        "computers", "cool", "courage", "dad", "dating", "death", "design", "dreams",
        "education", "environmental", "equality", "experience", "failure", "faith",
        "family", "famous", "fear", "fitness", "food", "forgiveness", "freedom",
        "friendship", "funny", "future", "god", "good", "government", "graduation",
        "great", "happiness", "health", "history", "home", "hope", "humor", "imagination",
        "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning",
        "legal", "life", "love", "marriage", "medical", "men", "mom", "money", "morning",
        "movies", "success"
    ];

    // Inicializar el cuadro de búsqueda con autocompletado
    $("#categoria").autocomplete({
        source: categoriasDisponibles
    });

    $("#obtenerFrases").click(function() {
        // Obtener la categoría seleccionada por el usuario
        var categoria = $("#categoria").val();

        // Construir la URL con la categoría seleccionada
        var url = 'https://api.api-ninjas.com/v1/quotes?category=' + categoria;
