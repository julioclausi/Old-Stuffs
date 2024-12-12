function mostraHora () {
    let data = new Date()
    return data.toLocaleTimeString('pt-BR', {
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    })
}

const timer = setInterval(function() {
    console.log(mostraHora());
}, 1000);

setTimeout(function(){
    clearInterval(timer);
}, 3000);

setTimeout(function(){
    console.log('Fim do código.');
}, 5000);
