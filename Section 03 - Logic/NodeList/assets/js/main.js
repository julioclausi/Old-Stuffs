const paragrafos = document.querySelectorAll('p');

const estilosBody = getComputedStyle(document.body);
const bgColor = estilosBody.backgroundColor;

for (let paragrafo of paragrafos){
    paragrafo.style.backgroundColor = bgColor;
    paragrafo.style.color = '#fff';
}