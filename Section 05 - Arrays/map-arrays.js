// Maps -> sempre retorna com o mesmo tamanho do vetor original
const numeros = [1, 2, 3, 4, 5];
const doubleNumeros = numeros.map(valor => valor * 2);
console.log(numeros);
console.log(doubleNumeros);

const pessoas = [
    { nome: 'Luiz', idade: 62 },
    { nome: 'Maria', idade: 23 },
    { nome: 'Eduardo', idade: 55 },
    { nome: 'Wallace', idade: 47 }
]
const nomes = pessoas.map(obj => ({ nome: obj.nome }));
console.log(nomes);
const id = pessoas.map(
    function (obj, indice) {
        const newObj = { ...obj };
        newObj.id = indice + 1;
        return newObj;
    }
);

console.log(id);
console.log(pessoas);
