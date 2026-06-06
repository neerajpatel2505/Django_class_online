document.addEventListener('DOMContentLoaded', function () {
    const playBtn = document.getElementById('playBtn');
    const audio = document.getElementById('myAudio');
    playBtn.addEventListener('click', function () {
        audio.play();
    });
});