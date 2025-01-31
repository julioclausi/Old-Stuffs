function Pessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    //this.nomeCompleto = () => this.nome + ' ' + this.sobrenome;
    //se eu fizer dessa forma todos os objetos vão ter esse método, usando recurso a mais
}

// usa referência para acessar os métodos
Pessoa.prototype.nomeCompleto = function () {
    return this.nome + ' ' + this.sobrenome;
}

const p1 = new Pessoa('Silvio', 'Santos');
const p2 = new Pessoa('Ayrton', 'Senna');

console.dir(p1);
console.dir(p2);
console.log(p1.nomeCompleto());
console.log(Pessoa.prototype === p1.__proto__);
