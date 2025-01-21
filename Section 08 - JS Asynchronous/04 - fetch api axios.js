// fetch('pessoas.json')
//     .then(resposta => resposta.json())
//     .then(json => carregaDados(json))
//     .catch(e => console.warn(e));

//<script src="https://unpkg.com/axios@1.6.7/dist/axios.min.js"></script>
axios('pessoas.json')
    .then(resposta => carregaDados(resposta.data));

function carregaDados(json) {
    const table = document.createElement('table');
    const cabecalho = document.createElement('tr');
    let th = document.createElement('th');
    th.innerHTML = 'NOME';
    cabecalho.appendChild(th);
    th = document.createElement('th');
    th.innerHTML = 'IDADE';
    cabecalho.appendChild(th);
    th = document.createElement('th');
    th.innerHTML = 'EMAIL';
    cabecalho.appendChild(th);
    table.appendChild(cabecalho);
    for (let pessoa of json) {
        const tr = document.createElement('tr');
        let td = document.createElement('td');
        td.innerHTML = pessoa.nome;
        tr.appendChild(td);
        td = document.createElement('td');
        td.innerHTML = pessoa.idade;
        tr.appendChild(td);
        td = document.createElement('td');
        td.innerHTML = pessoa.email;
        tr.appendChild(td);
        table.appendChild(tr);
    }
    const resultado = document.querySelector('.container');
    resultado.appendChild(table);
}
