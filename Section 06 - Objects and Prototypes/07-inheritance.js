function Produto(nome, preco) {
    this.nome = nome;
    this.preco = preco;
}

function Camiseta(nome, preco, cor) {
    Produto.call(this, nome, preco);
    this.cor = cor;
}

Produto.prototype.especificacao = function () {
    console.log(`${this.nome} custa ${this.preco}`);
};

Camiseta.prototype = Object.create(Produto.prototype);
Camiseta.prototype.constructor = Camiseta;

Camiseta.prototype.minhaCor = function () {
    this.especificacao();
    console.log(`Sou da cor ${this.cor}`);
};

const camiseta = new Camiseta('T-shirt', 50, 'Preta');
console.log(camiseta);
camiseta.especificacao();
camiseta.minhaCor();

function Caneca(nome, valor, material, estoque) {
    Produto.call(this, nome, valor);
    this.material = material;

    Object.defineProperty(this, 'estoque', {
        enumerable: true,
        configurable: false,
        get: function () {
            return estoque;
        },
        set: function (valor) {
            if (typeof valor !== 'number') return;
            estoque = valor;
        }
    });
}

Caneca.prototype = Object.create(Produto.prototype);
Caneca.prototype.constructor = Caneca;

Caneca.prototype.quemSouEu = function () {
    this.especificacao();
    console.log(`Sou feito de ${this.material}`);
    console.log(`Tem ${this.estoque} no estoque`);
};

const caneca = new Caneca('Star Wars', 80, 'Porcelana', 5);
console.log(caneca);
caneca.quemSouEu();
