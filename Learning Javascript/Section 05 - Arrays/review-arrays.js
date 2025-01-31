// Retorne a soma do dobro de todos os pares
const numeros = [1, 2, 3, 4, 5];

const somaDobroPares = numeros.reduce(function (acumulador, valor) {
    if (valor % 2 === 0) acumulador += (valor * 2);
    return acumulador;
}, 0);

const versaoDois = numeros
    .filter(valor => valor % 2 === 0)
    .map(valor => valor*2)
    .reduce((soma,valor) => soma+valor);

console.log(somaDobroPares);
console.log(versaoDois);
