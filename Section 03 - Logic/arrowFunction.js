// Retorna o maior de dois números

function maior (x, y) {
    if (x > y) return x;
    return y;
}

const maior2 = (x,y) => x>y ? x : y;

console.log(maior(5,10));
console.log(maior2(10,5));