const nomes = ['A','B','C'];

//valor por referência
const outrosNomes = nomes;

//cópia
const maisNomes = [...nomes];

outrosNomes.pop();

maisNomes.push('D');

console.log(nomes);
console.log(outrosNomes);
console.log(maisNomes);
console.log(maisNomes.length);
