const nome = 'Julio';
const sobrenome = 'Roberto';

const falaNome = () => {
    return nome + ' ' + sobrenome;
};

//module.exports.nome = nome;

exports.nome = nome;
this.sobrenome = sobrenome;
this.falaNome = falaNome;

//console.log(module.exports);
