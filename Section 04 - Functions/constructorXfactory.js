function ConstructorPessoa(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    this.falaNomeCompleto = function () {
        console.log(this.nome + ' ' + this.sobrenome);
    }
}

function factoryPessoa(nome, sobrenome) {
    return {
        nome,
        sobrenome,
        falaNomeCompleto: function () {
            console.log(nome + ' ' + sobrenome);
        }
    };
}

const pessoa1 = new ConstructorPessoa('Julio', 'Roberto');
const pessoa2 = factoryPessoa('Jéssica', 'Rocha');

pessoa1.falaNomeCompleto();
pessoa2.falaNomeCompleto();
console.log(pessoa1.nome);
console.log(pessoa2.nome);
