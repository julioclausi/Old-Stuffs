const _velocidade = Symbol('velocidade');
class Carro {
    constructor(nome) {
        this.nome = nome;
        this[_velocidade] = 0;
    }

    acelerar() {
        if (this[_velocidade] >= 100) return;
        this[_velocidade]++;
    }

    frear() {
        if (this[_velocidade] <= 0) return;
        this[_velocidade]--;
    }

    get velocidade () {
        return this[_velocidade];
    }
}

const toyota = new Carro('Toyota');
console.log(toyota);

for (let i = 0; i <= 120; i++) {
    toyota.acelerar();
    console.log(toyota);
}

console.log(toyota.velocidade);
