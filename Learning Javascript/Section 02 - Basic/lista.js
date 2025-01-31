function  criaPessoa (nome, sobrenome, idade) {
    return {
        nome,
        sobrenome,
        idade
    }
};

function init () {
    const form = document.querySelector('.formulario');
    const pessoas = document.querySelector('.pessoas');
    const lista = [];

    function recebeEvento (evento) {
        evento.preventDefault();
        const nome = form.querySelector('.nome');
        const sobrenome = form.querySelector('.sobrenome');
        const idade = form.querySelector('.idade');
        lista.push(criaPessoa(nome.value,sobrenome.value,idade.value));
        console.log(lista);
        pessoas.innerHTML += `<p>${nome.value} ${sobrenome.value} - ${idade.value}</p>`
    }

    form.addEventListener('submit', recebeEvento);
}

init();