var video = document.querySelector('video');

navigator.mediaDevices.getUserMedia({video: true})
.then(stream=> {
    video.srcObject = stream;
    video.play();
})
.catch(error => {
    console.log(error);
});

document.querySelector('button').addEventListener('click', () => {
    var canvas = document.querySelector('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0);

    var link = document.createElement('a');
    link.download = 'foto.png';
    link.href = canvas.toDataURL();
    link.textContent = 'Download Image';
    link.click();
    // Preciso fazer com que a foto vá para o banco de dados
});