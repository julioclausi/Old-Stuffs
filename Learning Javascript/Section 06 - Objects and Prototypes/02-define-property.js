function Produto(nome, preco, estoque, fornecedor) {
    //this.nome = nome;
    //this.preco = preco;
    Object.defineProperties(this, {
        nome: {
            enumerable: true,
            value: nome,
        },
        preco: {
            enumerable: true,
            value: preco,
        },
    });

    //Object.freeze(this);

    Object.defineProperty(this, 'fornecedor', {
        enumerable: false,
        value: fornecedor,
        configurable: false,
    });

    Object.defineProperty(this, 'estoque', {
        enumerable: true, // mostra a chave
        value: estoque, // valor
        writable: true, // pode alterar o valor
        configurable: true, // configurável
    });
}

const p1 = new Produto('Camiseta', 20, 3, 'ABC');
console.log(p1);
console.log(Object.keys(p1));
