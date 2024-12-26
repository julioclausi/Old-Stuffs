function Pessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    return this;
}

const pessoa = new Pessoa('Julio', 'Roberto');
console.log(pessoa);
console.log(pessoa.nome);
console.log(pessoa.sobrenome);
