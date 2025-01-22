const mod = require('./mod');
const fala = mod.falaNome;

console.log(mod.nome);
console.log(fala());
console.log(__filename);
console.log(__dirname);

const path = require('path');
console.log(path.resolve(__dirname, '..', '..', 'modelo'));

// npm init -y
// npm u axios
// const axios = require('axios');
// axios('link')
//     .then(response => console.log(response.data))
//     .catch(e => console.log(e));
