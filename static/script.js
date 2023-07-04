
function mostrarAlerta() {
    alert("¡Se ha presionado el Botón 5!");
}

function startTimer() { 
    var segundos = 60; // Tiempo en segundos
    var temporizador = document.getElementById("temporizador");

    function actualizarTemporizador() {
        var minutos = Math.floor(segundos / 60);
        var segundosRestantes = segundos % 60;

        // Formatear los minutos y segundos para mostrarlos con dos dígitos
        var formatoMinutos = minutos < 10 ? "0" + minutos : minutos;
        var formatoSegundos = segundosRestantes < 10 ? "0" + segundosRestantes : segundosRestantes;

        // Mostrar el temporizador en el elemento 'temporizador'
        temporizador.innerHTML = formatoMinutos + ":" + formatoSegundos;

        // Reducir el tiempo en 1 segundo
        segundos--;

        // Si el tiempo llega a cero, mostrar un mensaje o realizar una acción
        if (segundos < 0) {
            temporizador.innerHTML = "Tiempo finalizado";
            var boton = document.getElementById("reinicio");
            boton.style.display = "block";
            // Aquí puedes realizar una acción adicional cuando el tiempo se agote
        } else {
            // Volver a actualizar el temporizador después de 1 segundo
            setTimeout(actualizarTemporizador, 1000);
        }
    }

    // Iniciar el temporizador al cargar la página
    actualizarTemporizador();
};

function playMusic() {
  var audios = [
    document.getElementById("audio1"),
    document.getElementById("audio2"),
    document.getElementById("audio3"),
    document.getElementById("audio4"),
    document.getElementById("audio5"),
    document.getElementById("audio6")
    // Agrega más elementos de audio para las demás músicas
  ];
  var currentIndex = 0;
  
  function playNextMusic() {
  // Reproducir la música actual
  audios[currentIndex].play();
  
  // Esperar hasta que la música actual termine de reproducirse
  audios[currentIndex].onended = function() {
    // Pausar la música actual
    audios[currentIndex].pause();
    
    // Incrementar el índice para pasar a la siguiente música
    currentIndex++;
    
    // Verificar si hay más músicas
    if (currentIndex < audios.length) {
      // Reproducir la siguiente música después de una pausa de 10 segundos
      setTimeout(function() {
        playNextMusic();
      }, 10000);
    }
  };// Iniciar la secuencia de reproducción
 
}
 playNextMusic();
  
}

function playAudio() {
  var audioPlayer = document.getElementById('audioPlayer');
  audioPlayer.play();
}


function incremental() {
    var words = [
    document.getElementById("word1"),
    document.getElementById("word2"),
    document.getElementById("word3"),
    document.getElementById("word4"),
    document.getElementById("word5"),
    document.getElementById("word6"),
    document.getElementById("word7"),
    document.getElementById("word8")

    
    ]; // Agrega aquí las palabras que deseas mostrar
    
    var interval;
    var counter = 0;
    var wordElement = document.getElementById("word");
    
    function changeWord() {
        if (counter < 2) {
            var element = words[counter];
            var contenidoTexto=element.textContent;
            console.log(contenidoTexto);
            wordElement.innerText= contenidoTexto;
            counter++;
        } else {
            clearInterval(interval);
            interval = setInterval(changeWord, 5000); // Cambiar cada 5 segundos después de los primeros 30 segundos
            var element = words[counter];
            var contenidoTexto=element.textContent;
            console.log(contenidoTexto);
            wordElement.innerText= contenidoTexto;
            counter++;
        }
    }
    
    interval = setInterval(changeWord, 10000); // Cambiar cada 10 segundos inicialmente
    
    setTimeout(function() {
        clearInterval(interval);
    }, 60000); // Detener el cambio después de 60 segundos
}   

function kickback() {
    var words = [
    document.getElementById("p1"),
    document.getElementById("p2"),
    document.getElementById("p3"),
    document.getElementById("p4"),
    document.getElementById("p5"),
    document.getElementById("p6"),
    document.getElementById("p7"),
    document.getElementById("p8")

    
    ]; // Agrega aquí las palabras que deseas mostrar
    
    var interval;
    var counter = 0;
    var wordElement = document.getElementById("pregunta");
    
    function changeWord() {
        
            var element = words[counter];
            var contenidoTexto=element.textContent;
            console.log(contenidoTexto);
            wordElement.innerText= contenidoTexto;
            counter++;
        
    }
    
    interval = setInterval(changeWord, 10000); // Cambiar cada 10 segundos inicialmente
    
    setTimeout(function() {
        clearInterval(interval);
    }, 60000); // Detener el cambio después de 60 segundos
}   


function terminacion() {
    var words = [
    document.getElementById("t1"),
    document.getElementById("t2"),
    document.getElementById("t3"),
    document.getElementById("t4"),
    document.getElementById("t5"),
    document.getElementById("t6"),
    document.getElementById("t7"),
    document.getElementById("t8")

    
    ]; // Agrega aquí las palabras que deseas mostrar
    
    var interval;
    var counter = 0;
    var wordElement = document.getElementById("terminacion");
    
    function changeWord() {
        
            var element = words[counter];
            var contenidoTexto=element.textContent;
            console.log(contenidoTexto);
            wordElement.innerText= contenidoTexto;
            counter++;
        
    }
    
    interval = setInterval(changeWord, 10000); // Cambiar cada 10 segundos inicialmente
    
    setTimeout(function() {
        clearInterval(interval);
    }, 60000); // Detener el cambio después de 60 segundos
}   





