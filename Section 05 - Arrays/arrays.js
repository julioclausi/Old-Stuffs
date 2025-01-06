const nomes = ['Abacaxi','Banana','Carambola'];

//valor por referência
const outrosNomes = nomes;

//cópia
const maisNomes = [...nomes];

const removidoDoFinal = outrosNomes.pop(); //método
const removidoDoComeco = outrosNomes.shift();

maisNomes.push('Damasco'); //adiciona no final
maisNomes.unshift('Abacate'); //adiciona no começo

console.log(nomes);
console.log(outrosNomes);
console.log(maisNomes);
console.log(maisNomes.length); //atributo
console.log(removidoDoComeco);
console.log(removidoDoFinal);

const frase = 'Uma frase bem longa';
const letras = [...frase];
const palavras = frase.split(' ');
console.log(letras);
console.log(palavras);
const outraFrase = palavras.join(' ');
console.log(outraFrase);
