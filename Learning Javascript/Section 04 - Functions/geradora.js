function* geradora() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
    yield 5;
}

const g1 = geradora();

// console.log(g1);
// console.log(g1.next().value);
// console.log(g1.next().value);
// console.log(g1.next().value);
// console.log(g1.next().value);
// console.log(g1.next().value);
// console.log(g1.next().value);

for (let valor of g1) {
    console.log(valor);
}

function* contador () {
    let i = 0;
    while (true) {
        yield i;
        i++;
    }
}

console.log('-----');

const cont = contador();
console.log(cont.next().value);
console.log(cont.next().value);
console.log(cont.next().value);
console.log(cont.next().value);
console.log(cont.next().value);

console.log('-----');

function* gerador123 () {
    yield 1;
    yield 2;
    yield 3;
}

function* gerador123456() {
    yield* gerador123();
    yield 4;
    yield 5;
    yield 6;
}

const outroContador = gerador123456();
for (let valor of outroContador) {
    console.log(valor);
}
