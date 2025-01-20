function aleatorio(min, max) {
    min *= 1000;
    max *= 1000;
    return Math.floor(Math.random() * ((max - min) + min));
}

// function esperaAi(msg, tempo, cb) {
//     setTimeout(() => {
//         console.log(msg);
//         if (cb) cb();
//     }, tempo)
// }

// esperaAi('Frase 1', aleatorio(1, 3), function () {
//     esperaAi('Frase 2', aleatorio(1, 3), function () {
//         esperaAi('Frase 3', aleatorio(1, 3));
//     });
// });

function esperaAi(msg, tempo) {
    return new Promise((resolve, reject) => {
        if(typeof msg!== 'string') reject('Bad value');
        setTimeout(() => {
            resolve(msg);
        }, tempo);
    });
}

esperaAi('[1] Conectando ao BD', aleatorio(1, 3))
    .then(mensagem => {
        console.log(mensagem);
        return esperaAi('[2] Buscando dados do BD', aleatorio(1, 3));
    }).then(mensagem => {
        console.log(mensagem);
        return esperaAi('[3] Tratando os dados', aleatorio(1, 3))
    }).then(mensagem => {
        console.log(mensagem);
    }).then(() => {
        console.log('[4] Exibindo os dados');
    }).catch(e => {
        console.log(e);
    });
