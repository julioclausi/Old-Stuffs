function soma (a,b) {
    if (typeof a !== 'number' || typeof b !== 'number'){
        throw new TypeError('a e b precisam ser do tipo number')
    }
    return a+b;
}

console.log(soma(1,2));

try {
    console.log(soma('1',2));
} catch (e) {
    console.log(e);
} finally {
    console.log('finally...');
}