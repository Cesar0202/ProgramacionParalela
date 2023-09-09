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

        // Realizar la solicitud AJAX
        $.ajax({
            method: 'GET',
            url: url,
            headers: { 'X-Api-Key': 'BZCMTy/nqeOpgxpRMBrRHg==LD9hEceJAiy7y2cW' },
            contentType: 'application/json',
            success: function(result) {
                // Manejar la respuesta exitosa
                mostrarResultado(result);
            },
            error: function(jqXHR) {
                // Manejar errores de la solicitud
                console.error('Error: ', jqXHR.responseText);
                mostrarResultadoError();
            }
        });
    });
});

function mostrarResultado(data) {
    // Limpiar el contenido anterior de la lista
    $("#listaResultado").empty();

    // Mostrar cada uno de los elementos del JSON en la lista
    data.forEach(function(frase) {
        $("#listaResultado").append("<li><strong>Frase:</strong> " + frase.quote + "</li>");
        $("#listaResultado").append("<li><strong>Autor:</strong> " + frase.author + "</li>");
        $("#listaResultado").append("<li><strong>Categoría:</strong> " + frase.category + "</li>");
    });
}

function mostrarResultadoError() {
    // Limpiar el contenido anterior de la lista
    $("#listaResultado").empty();

    // Mostrar un mensaje de error en la lista
    $("#listaResultado").append("<li>Error al obtener las frases. Por favor, intenta de nuevo más tarde.</li>");
}