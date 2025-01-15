const numeros = [1, 2, 3, 4, 5];
const somaTotal = numeros.reduce(
    function (acumulador, valor) {
        acumulador += valor;
        return acumulador;
    }, 0);

console.log(somaTotal);
