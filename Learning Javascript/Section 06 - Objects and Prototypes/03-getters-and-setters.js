function Produto(nome, preco, estoque) {
    this.nome = nome;
    this.preco = preco;

    Object.defineProperty(this, 'estoque', {
        enumerable: true,
        // value: estoque,
        // writable: true,
        configurable: true,
        get: function () {
            return estoque;
        },
        set: function (valor) {
            estoque = valor;
        }
    });
}

const p1 = new Produto('Camiseta', 50, 3);
console.log(p1);
console.log(p1.estoque);
p1.estoque = 40;
console.log(p1.estoque);

function pessoa(nome) {
    return {
        get nome() {
            return nome;
        },
        set nome(valor) {
            nome = valor;
        }
    };
}

const p2 = pessoa('Silvio');
console.log(p2);
console.log(p2.nome);
p2.nome = 'Silvio Santos';
console.log(p2.nome);
