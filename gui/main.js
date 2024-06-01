$(document).ready(function () {
  $('.siri-message').textillate({
    loop: true,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync:true,
    },
    out: {
      effect: "fadeOutUp",
      sync:true,
    },
  });

  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    color: '#A020F0'
  });
  siriWave.start();
});

