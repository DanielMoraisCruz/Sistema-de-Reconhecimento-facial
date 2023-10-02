var video = document.querySelector('video');

navigator.mediaDevices.getUserMedia({video: true})
.then(stream=> {
    video.srcObject = stream;
    video.play();
})
.catch(error => {
    console.log(error);
});

// Path: script/reconFace.js
// Executa um codigo python de reconhecimento facial

