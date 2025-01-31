class ControleRemoto {
    constructor(tv) {
        this.tv = tv;
        this.volume = 0;
    }

    aumentarVolume() {
        this.volume += 2;
    }

    // Static method
    static fazAlgo() {
        console.log('Fiz!');
    }
}

const controle = new ControleRemoto('TV');
controle.aumentarVolume();
controle.aumentarVolume();
controle.aumentarVolume();
console.log(controle);
//controle.fazAlgo();
ControleRemoto.fazAlgo();
