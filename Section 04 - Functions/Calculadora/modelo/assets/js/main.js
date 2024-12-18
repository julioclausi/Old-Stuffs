function criaCalculadora() {
    return {
        display: document.querySelector('.display'),

        inicia() {
            this.clicaBotoes();
            this.pressEnter();
        },

        pressEnter() {
            this.display.addEventListener('keyup', e => {
                if (e.keyCode === 13) {
                    this.fazConta();
                }
            });

        },

        clicaBotoes() {
            document.addEventListener('click', e => {
                const el = e.target;
                if (el.classList.contains('btn-num')) {
                    this.btnParaDisplay(el.innerText);
                }
                if (el.classList.contains('btn-clear')) {
                    this.display.value = '';
                }
                if (el.classList.contains('btn-del')) {
                    this.display.value = this.display.value.slice(0, -1);
                }
                if (el.classList.contains('btn-eq')) {
                    this.fazConta();
                }
                this.display.focus();
            });

        },

        btnParaDisplay(valor) {
            this.display.value += valor;
        },

        fazConta() {
            let conta = this.display.value;

            try {
                conta = eval(conta);

                if (!conta) {
                    alert('Conta inválida');
                    return;
                }

                this.display.value = String(conta);
            } catch (e) {
                alert('Conta inválida');
                return;
            }
        }
    }
}

const calculadora = criaCalculadora();
calculadora.inicia();
