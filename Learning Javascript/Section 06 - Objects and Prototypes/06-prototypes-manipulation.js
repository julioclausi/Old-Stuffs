// new Object -> Object.prototype
const objA = {
    chaveA: 'A'
    // __proto__
};

const objB = {
    chaveB: 'B'
    // __proto__ : objA
};

const objC = new Object;
objC.chaveC = 'C';

Object.setPrototypeOf(objB, objA);
Object.setPrototypeOf(objC, objB);

console.log(objA.__proto__ === Object.prototype); //true
console.log(objB); //{ chaveB: 'B' }
console.log(objB.__proto__); //{ chaveA: 'A' }

//objB -> objA -> prototype
console.log(Object.prototype === objB.__proto__.__proto__); //true
console.log(Object.prototype === objC.__proto__.__proto__.__proto__); //true
console.log(objC.chaveB); //B
console.log(objC.chaveA); //A

function Produto(nome, preco) {
    this.nome = nome;
    this.preco = preco;
}

Produto.prototype.desconto = function (valor) {
    this.preco = this.preco * (1 - (valor / 100));
}

const p1 = new Produto('Camiseta', 50);

console.log(p1) //Produto { nome: 'Camiseta', preco: 50 }
p1.desconto(50);
console.log(p1); //Produto { nome: 'Camiseta', preco: 25 }

// criar um objeto diferente e reaproveitar o metodo desconto
const p2 = {
    nome: 'Outra camiseta',
    preco: '100',
};

console.log(p2); //{ nome: 'Outra camiseta', preco: '100' }
Object.setPrototypeOf(p2, Produto.prototype);
p2.desconto(50);
console.log(p2); //Produto { nome: 'Outra camiseta', preco: 50 }
console.log(p1.__proto__ === p2.__proto__); //true

const p3 = Object.create(Produto.prototype);
p3.preco = 1000;
p3.desconto(50);
console.log(p3); //Produto { preco: 500 }
