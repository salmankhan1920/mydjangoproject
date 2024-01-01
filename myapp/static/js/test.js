setInterval(function() {
    document.querySelector('.dot1').classList.toggle('blink');
    setTimeout(function() {
      document.querySelector('.dot2').classList.toggle('blink');
    }, 250);
    setTimeout(function() {
      document.querySelector('.dot3').classList.toggle('blink');
    }, 500);
  }, 1000);