function fatorial (num) {
    if (num === 0 || num === 1) return 1;
    else {
        return fatorial(num-1) * num;
    }
}

console.log(fatorial(1));
console.log(fatorial(3));
console.log(fatorial(5));
