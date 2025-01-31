const btnNovoJogo = document.querySelector('.novojogo');
const vencedor = document.querySelector('.winner');
btnNovoJogo.addEventListener('click', novoJogo);
const campos = document.getElementsByClassName('campo');
const jogadorAtivo = document.querySelector('.player');
let jogador = 'X';
let temVencedor = false;

function fazJogada(campo) {
    campo.innerText = jogador;
    if (jogador === 'X') {
        campo.style.color = 'red';
    } else campo.style.color = 'blue';
    console.log(campo);
    jogador = jogador === 'X' ? 'O' : 'X';
    verificaVencedor();
    if (temVencedor) {
        vencedor.innerText += '! Clique em "Novo Jogo" para reiniciar.'
    }
}

function click() {
    addEventListener('click', e => {
        const el = e.target;
        if (el.classList.contains('campo')) {
            if (!temVencedor) {
                if (el.innerText === '') {
                    fazJogada(el);
                }
            }
        }
        jogadorAtivo.innerText = jogadorAtivo.innerText.slice(0, -1) + jogador;
    });
}

function novoJogo() {
    // deixar os campos limpos
    for (let campo of campos) {
        campo.innerText = '';
        temVencedor = false;
        campo.bgColor = '#ffffff';
        vencedor.innerText = '';
    }
}

function verificaVencedor() {
    if (campos[0].innerText == campos[1].innerText && campos[0].innerText == campos[2].innerText && campos[0].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[0].innerText;
        campos[0].bgColor = 'lightgreen';
        campos[1].bgColor = 'lightgreen';
        campos[2].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[3].innerText == campos[4].innerText && campos[3].innerText == campos[5].innerText && campos[3].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[3].innerText;
        campos[3].bgColor = 'lightgreen';
        campos[4].bgColor = 'lightgreen';
        campos[5].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[6].innerText == campos[7].innerText && campos[6].innerText == campos[8].innerText && campos[6].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[6].innerText;
        campos[6].bgColor = 'lightgreen';
        campos[7].bgColor = 'lightgreen';
        campos[8].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[0].innerText == campos[3].innerText && campos[0].innerText == campos[6].innerText && campos[0].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[0].innerText;
        campos[0].bgColor = 'lightgreen';
        campos[3].bgColor = 'lightgreen';
        campos[6].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[1].innerText == campos[4].innerText && campos[1].innerText == campos[7].innerText && campos[1].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[1].innerText;
        campos[1].bgColor = 'lightgreen';
        campos[4].bgColor = 'lightgreen';
        campos[7].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[2].innerText == campos[5].innerText && campos[2].innerText == campos[8].innerText && campos[2].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[2].innerText;
        campos[2].bgColor = 'lightgreen';
        campos[5].bgColor = 'lightgreen';
        campos[8].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[0].innerText == campos[4].innerText && campos[0].innerText == campos[8].innerText && campos[0].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[0].innerText;
        campos[0].bgColor = 'lightgreen';
        campos[4].bgColor = 'lightgreen';
        campos[8].bgColor = 'lightgreen';
        temVencedor = true;
    }
    if (campos[2].innerText == campos[4].innerText && campos[2].innerText == campos[6].innerText && campos[2].innerText != '') {
        vencedor.innerText = 'Vencedor é ' + campos[2].innerText;
        campos[2].bgColor = 'lightgreen';
        campos[4].bgColor = 'lightgreen';
        campos[6].bgColor = 'lightgreen';
        temVencedor = true;
    }
}

click();
