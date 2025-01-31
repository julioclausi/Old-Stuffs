const objeto1 = { nome: 'ABC', valor: 123 };
const objeto2 = objeto1;
// dessa forma acima ambos objetos vão estar sendo setados para o mesmo lugar da memória
// por referência

const objeto3 = { ...objeto1 };
// com spread operator o objeto3 será cópia do objeto1
objeto1.valor = 5;
objeto3.nome = 'Outro';
console.log(objeto1);
console.log(objeto2);
console.log(objeto3);
const objeto4 = { ...objeto3, material: 'xyz' };
console.log(objeto4);

// usando object.assign para copiar
const objeto5 = Object.assign({}, objeto1, { tipo: 'qwerty' });
console.log(objeto5);
console.log(Object.getOwnPropertyDescriptor(objeto5, 'nome'));
// { value: 'ABC', writable: true, enumerable: true, configurable: true }
console.log(Object.keys(objeto5)); //[ 'nome', 'valor', 'tipo' ]
console.log(Object.values(objeto5)); //[ 'ABC', 5, 'qwerty' ]
console.log(Object.entries(objeto5)); //[ [ 'nome', 'ABC' ], [ 'valor', 5 ], [ 'tipo', 'qwerty' ] ]

for (let [chave, valor] of Object.entries(objeto5)) {
    console.log(chave, valor);
}
// nome ABC
// valor 5
// tipo qwerty
