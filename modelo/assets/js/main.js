function getDiaDaSemana(diaDaSemana) {
    switch (diaDaSemana) {
        case 0:
            return 'Domingo';
        case 1:
            return 'Segunda-feira';
        case 2:
            return 'Terça-feira';
        case 3:
            return 'Quarta-feira';
        case 4:
            return 'Quinta-feira';
        case 5:
            return 'Sexta-feira';
        case 6:
            return 'Sábado';
    }
}

function getMes(mes) {
    switch (mes) {
        case 0:
            return 'Janeiro';
        case 1:
            return 'Fevereiro';
        case 2:
            return 'Março';
        case 3:
            return 'Abril';
        case 4:
            return 'Maio';
        case 5:
            return 'Junho';
        case 6:
            return 'Julho';
        case 7:
            return 'Agosto';
        case 8:
            return 'Setembro';
        case 9:
            return 'Outubro';
        case 10:
            return 'Novembro';
        case 11:
            return 'Dezembro';
    }
}

function functionDataBrasil() {
    const data = new Date();
    const dia = data.getDate();
    const mes = data.getMonth();
    const ano = data.getFullYear();
    const diaDaSemana = data.getDay();
    const hora = data.getHours();
    const minuto = data.getMinutes();
    let texto = '';
    texto += `${getDiaDaSemana(diaDaSemana)}, ${dia} de ${getMes(mes)} de ${ano}, ${hora}:${minuto>=10 ? minuto : '0' + minuto}`;
    return texto;
}

const dataBrasil = functionDataBrasil()
const data = document.querySelector('.data');
const p = document.createElement('p');
data.innerHTML = '';
p.classList.add('classe-paragrafo');
p.innerHTML = dataBrasil;
data.appendChild(p);

function jeitoFacil() {
    const h1 = document.querySelector('.container h1');
    const data = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        timeStyle: 'short'
    };
    h1.innerHTML = data.toLocaleDateString('pt-BR', options);
}

jeitoFacil();