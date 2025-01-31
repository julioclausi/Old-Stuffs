const pessoa = {
    nome: 'Julio',
    sobrenome: 'Roberto',
    genero: 'Masculino',
    algumMetodo: function () { }
};

console.log(pessoa);
console.log(pessoa.nome);
console.log(pessoa['sobrenome']);

const chave = 'genero';
console.log(pessoa[chave]);

delete pessoa.genero;
delete pessoa.algumMetodo;
console.log(pessoa);

pessoa.falaOi = function () {
    console.log(`Oi, meu nome é ${this.nome}.`);
}
pessoa.falaOi();

//Factory Function
function criaPessoa(nome, sobrenome) {
    return {
        nome,
        sobrenome,
        get nomeCompleto() {
            return `${this.nome} ${this.sobrenome}`
        }
    };
}
const p1 = criaPessoa('Silvio', 'Santos');
console.log(p1.nomeCompleto); //com o get na declaração do método não há necessidade de usar ()

//Constructor Function
function Pessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    this.nomeCompleto = function () {
        return `${this.nome} ${this.sobrenome}`;
    };
}
const p2 = new Pessoa('Ayrton', 'Senna');
console.log(p2, p2.nomeCompleto());
