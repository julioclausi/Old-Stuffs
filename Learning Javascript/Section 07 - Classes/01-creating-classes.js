class Pessoa {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    falar() {
        console.log(`${this.nome} está falando.`);
    }

    comer() {
        console.log(`${this.nome} está comendo.`);
    }
}

const p1 = new Pessoa('Julio', 'Roberto');
console.log(p1);
p1.falar();
p1.comer();
// Não precisa de prototype
