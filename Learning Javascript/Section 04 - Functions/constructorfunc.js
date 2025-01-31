function Pessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    // não precisa do return this;

    const metodoInterno = function() {
        console.log('interno..');
    }

    this.metodo = function() {
        console.log(this.nome + ': olá!');
        metodoInterno();
    }
}

//com this é publico
//sem this é privado

const pessoa = new Pessoa('Julio', 'Roberto');
console.log(pessoa);
console.log(pessoa.nome);
console.log(pessoa.sobrenome);
pessoa.metodo();
