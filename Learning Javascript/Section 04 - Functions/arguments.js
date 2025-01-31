function fazAlgumaCoisa(a = 0, b = 0, ...outros) {
    console.log(a,b,outros);
    console.log(arguments[10]);
    return arguments;
}

console.log(fazAlgumaCoisa(1, 2, 3, 4, 5, 6));