const teclas = document.querySelectorAll("td");

document.addEventListener('keydown', e => {
    if (e.keyCode === 38) {
        teclas[1].bgColor = 'green';
    } else if (e.keyCode === 37) {
        teclas[3].bgColor = 'green';
    } else if (e.keyCode === 40) {
        teclas[4].bgColor = 'green';
    } else if (e.keyCode === 39) {
        teclas[5].bgColor = 'green';
    }
});

document.addEventListener('keyup', e => {
    if (e.keyCode === 38) {
        teclas[1].bgColor = 'white';
    } else if (e.keyCode === 37) {
        teclas[3].bgColor = 'white';
    } else if (e.keyCode === 40) {
        teclas[4].bgColor = 'white';
    } else if (e.keyCode === 39) {
        teclas[5].bgColor = 'white';
    }
});
