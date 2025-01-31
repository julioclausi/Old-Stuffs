function dateToSeconds(segundos) {
    const data = new Date(segundos * 1000);
    return data.toLocaleTimeString('pt-BR', {
        hour12: false,
        timeZone: 'GMT'
    });
}

function iniciar() {
    clearInterval(timer);
    localCronometro.style.color = 'green';
    timer = setInterval(function () {
        contador++;
        localCronometro.innerHTML = dateToSeconds(contador);
    }, 1000);
}

function parar() {
    localCronometro.style.color = 'red';
    clearInterval(timer);
}

function zerar() {
    parar();
    localCronometro.style.color = 'black';
    localCronometro.innerHTML = '00:00:00';
    hist.innerHTML += dateToSeconds(contador) + '<br>';
    contador = 0;
}

const botaoIniciar = document.getElementById('iniciar');
const botaoParar = document.getElementById('parar');
const botaoZerar = document.getElementById('zerar');
const localCronometro = document.getElementById('tempo');
const hist = document.getElementById('hist');
let contador = 0;
let timer;

botaoIniciar.addEventListener("click", iniciar);
botaoParar.addEventListener("click", parar);
botaoZerar.addEventListener("click", zerar);

/*
document.addEventListener('click', function(e) {
    console.log(e.target);
    const el = e.target;
    if (el.classList.contains('zerar')) {
        ...
    } else if (el.classList.contains('iniciar')) {
        ...
    }
// Dessa forma não precisa do document.getElement...
})

-=-=-=-=-=-=-=-=
Poderia ter feito no CSS
classe

.pausado {
    color: red;
}

E usar:
-localCronometro.classList.remove('pausado');
-localCronometro.classList.add('pausado');

*/