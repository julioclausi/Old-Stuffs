function CPFValidator(cpf) {
    Object.defineProperty(this, 'cpfClean', {
        enumerable: true,
        get: function () {
            return cpf.replace(/\D+/g, '');
        }
    });
}

CPFValidator.prototype.CPFVerify = function () {
    const cpfParcial = this.cpfClean.slice(0, -2);
    const digit1 = this.verifyDigit(cpfParcial);
    const digit2 = this.verifyDigit(cpfParcial + digit1);

    const newCpf = cpfParcial + digit1 + digit2;
    return newCpf;
}

CPFValidator.prototype.verifyDigit = function (cpfPart) {
    const cpfArray = Array.from(cpfPart);
    const tamanho = cpfArray.length;
    const total = cpfArray.reduce((ac, val, index) => {
        ac += (Number(val) * (tamanho - index + 1));
        return ac;
    }, 0);
    const digit = 11 - (total % 11);
    return digit > 9 ? '0' : String(digit);
}

const cpf = new CPFValidator('705.484.450-52');
if (cpf.cpfClean === cpf.CPFVerify()) {
    console.log('CPF OK');
} else {
    console.log('CPF invalid');
}
