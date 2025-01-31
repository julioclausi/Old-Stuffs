const letras = ['A', 'B', 'C', 'D', 'E'];

// .splice(index,delete,elem1,elem2,elem3)

//Pop
const removidos = letras.splice(-1, 1);
console.log(letras);
console.log(removidos);

//Shift
console.log(letras.splice(0,1));
console.log(letras);

//Push
letras.splice(letras.length, 0, 'E voltou');
console.log(letras);

//Unshift
letras.splice(0, 0, 'A voltou');
console.log(letras);

console.log(letras.splice(1, 1, 'Troquei o B'));
console.log(letras);

