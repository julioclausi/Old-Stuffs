function callbackFilter(valor, indice, array) {
    console.log(valor, indice);
    return (valor % 3 === 0);
}

const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 27, 28, 29, 30];
console.log(numeros);

// Filter -> sempre retornar um array com a mesma quantidade de elementos ou menos.
const multiplosDe3 = numeros.filter(callbackFilter);
console.log(multiplosDe3);

console.log(numeros.filter(valor => valor % 2 === 0));

const pessoas = [
    { nome: 'Luiz', idade: 62 },
    { nome: 'Maria', idade: 23 },
    { nome: 'Eduardo', idade: 55 },
    { nome: 'Wallace', idade: 47 }
]

console.log(pessoas);
console.log(pessoas.filter(valor => valor.idade > 50));
