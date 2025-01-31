function criaMultiplicador(multiplicador) {
    function multiplica(numero) {
        return numero * multiplicador;
    }
    return multiplica;
}

const duplica = criaMultiplicador(2);
const triplica = criaMultiplicador(3);
const quadriplica = criaMultiplicador(4);

console.log(duplica(5));
console.log(triplica(5));
console.log(quadriplica(5));

console.log(typeof duplica);
console.log(typeof criaMultiplicador);
console.log(duplica);
