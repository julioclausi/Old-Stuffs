const elementos = [
    {tag: 'p', texto: 'Isto é um p'},
    {tag: 'div', texto: 'Isto é um div'},
    {tag: 'footer', texto: 'Isto é um footer'},
    {tag: 'section', texto: 'Isto é um section'}
];

const ondeAdicionar = document.querySelector('.container');

for (let i=0; i < elementos.length; i++){
    const elemento = document.createElement(elementos[i].tag);
    elemento.innerHTML = elementos[i].texto;
    ondeAdicionar.appendChild(elemento);
}