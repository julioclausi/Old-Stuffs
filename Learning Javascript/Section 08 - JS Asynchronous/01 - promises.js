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
        setTimeout(() => {
            if (typeof msg !== 'string') {
                reject('Bad value');
                return;
            }
            resolve(msg.toUpperCase() + ' - passei na promise');
        }, tempo);
    });
}

// esperaAi('[1] Conectando ao BD', aleatorio(1, 3))
//     .then(mensagem => {
//         console.log(mensagem);
//         return esperaAi('[2] Buscando dados do BD', aleatorio(1, 3));
//     }).then(mensagem => {
//         console.log(mensagem);
//         return esperaAi('[3] Tratando os dados', aleatorio(1, 3))
//     }).then(mensagem => {
//         console.log(mensagem);
//     }).then(() => {
//         console.log('[4] Exibindo os dados');
//     }).catch(e => {
//         console.log(e);
//     });

// const promises = [
//     //'Primeiro valor',
//     esperaAi('Promise 1', 2000),
//     esperaAi('Promise 2', 500),
//     esperaAi('Promise 3', 1000),
//     esperaAi(5, 5000),
//     //'Último valor'
// ];

// Promise.all(promises)
//     .then(function (valor) {
//         console.log('Retorna uma lista com tudo pronto:', valor);
//     })
//     .catch(e => {
//         console.log('Caiu no erro e não retorna nenhuma');
//     }
//     );

// entrega o valor da primeira que resolver, mas faz todas
// Promise.race(promises)
//     .then(function (valor) {
//         console.log('Retorna a mais rápida:', valor);
//     })
//     .catch(e => {
//         console.log('Caiu no erro e não retorna nenhuma');
//     }
//     );

function baixaPagina() {
    const emCache = false;
    if (emCache) {
        return Promise.resolve('Página em cache');
    } else {
        return esperaAi('Baixei a página', 3000);
    }
}

baixaPagina()
    .then(dadosPagina => {
        console.log(dadosPagina);
    })
    .catch(e => console.log('ERRO', e));
