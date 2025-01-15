const numeros = [1, 2, 3, 4, 5];
const somaTotal = numeros.reduce(
    function (acumulador, valor) {
        acumulador += valor;
        return acumulador;
    }, 0);

console.log(somaTotal);

const pessoas = [
    { nome: 'Luiz', idade: 62 },
    { nome: 'Maria', idade: 23 },
    { nome: 'Eduardo', idade: 55 },
    { nome: 'Wallace', idade: 47 }
]

const maisVelho = pessoas.reduce(function (velho, valor) {
    if (velho === 0) {
        velho = valor;
    } else {
        if (velho.idade < valor.idade) {
            velho = valor;
        }
    }
    return velho;
}, 0);

const maisNovo = pessoas.reduce(function (novo, valor) {
    if (valor.idade < novo.idade) return valor;
    return novo;
});

console.log(maisVelho);
console.log(maisNovo);

//Da pra fazer map e filter com reduce!