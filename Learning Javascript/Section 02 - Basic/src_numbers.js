const numero = Number(prompt('Digite um numero:'));
const numeroTitulo = document.getElementById('numero-titulo');
const raizQuadrada = document.getElementById('raiz-quadrada');
const isInteger = document.getElementById('isInteger');
const isNan = document.getElementById('isNan');
const roundDown = document.getElementById('roundDown');
const roundUp = document.getElementById('roundUp');
const duasCasas = document.getElementById('duas-casas');

numeroTitulo.innerHTML = numero;
raizQuadrada.innerHTML = numero**0.5;
isInteger.innerHTML = Number.isInteger(numero);
isNan.innerHTML = Number.isNaN(numero);
roundDown.innerHTML = Math.floor(numero);
roundUp.innerHTML = Math.ceil(numero);
duasCasas.innerHTML = numero.toFixed(2);