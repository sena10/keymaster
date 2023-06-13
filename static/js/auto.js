
function countdown(seconds) {
    var countdownElement = document.getElementById('countdown');

    var interval = setInterval(function() {
      countdownElement.innerHTML = seconds;

      seconds--;

      if (seconds < 0) {
        clearInterval(interval);
        // Redirecionar para outra página após a contagem regressiva
        window.location.href ="";
      }
    }, 1000);
  }

  // Chamar a função countdown ao carregar a página
  window.onload = function() {
    countdown(5); // Iniciar a contagem regressiva com 5 segundos
  };