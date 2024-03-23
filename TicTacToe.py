class Jogo:
    def __init__ (self):
        self.tabuleiro = [' '] * 10

    def show (self):
        for i in range (0,3):
            print (f'{self.tabuleiro[1+(i*3)]}|{self.tabuleiro[2+(i*3)]}|{self.tabuleiro[3+(i*3)]}')
            if i == 2:
                return
            print ('------')

    def jogadaspossiveis (self):
        possiveis = []
        for i in range (1,10):
            if self.tabuleiro[i] == 'X' or self.tabuleiro[i] == 'O':
                ...
            else:
                possiveis.append(i)
        print (f'Jogadas possiveis: {possiveis}')
        if len(possiveis) < 1:
            return True
        return False

    def joga (self, jogador):
        self.jogadaspossiveis()
        jogada = int (input ('Escolha uma: '))
        self.tabuleiro[jogada] = jogador

    def verificavitoria (self):
        if self.tabuleiro[1] == self.tabuleiro[2] and self.tabuleiro[1] == self.tabuleiro[3] and self.tabuleiro[1] != ' ':
            return True
        elif self.tabuleiro[4] == self.tabuleiro[5] and self.tabuleiro[4] == self.tabuleiro[6] and self.tabuleiro[4] != ' ':
            return True
        elif self.tabuleiro[7] == self.tabuleiro[8] and self.tabuleiro[7] == self.tabuleiro[9] and self.tabuleiro[7] != ' ':
            return True
        elif self.tabuleiro[1] == self.tabuleiro[4] and self.tabuleiro[1] == self.tabuleiro[7] and self.tabuleiro[1] != ' ':
            return True
        elif self.tabuleiro[2] == self.tabuleiro[5] and self.tabuleiro[2] == self.tabuleiro[8] and self.tabuleiro[2] != ' ':
            return True
        elif self.tabuleiro[3] == self.tabuleiro[6] and self.tabuleiro[3] == self.tabuleiro[9] and self.tabuleiro[3] != ' ':
            return True
        elif self.tabuleiro[1] == self.tabuleiro[5] and self.tabuleiro[1] == self.tabuleiro[9] and self.tabuleiro[1] != ' ':
            return True
        elif self.tabuleiro[3] == self.tabuleiro[5] and self.tabuleiro[3] == self.tabuleiro[7] and self.tabuleiro[3] != ' ':
            return True
        else:
            return False

jogo = Jogo()

jogador = 'X'
jogo.show()

while True:
    jogo.joga(jogador)
    jogo.show()
    if jogo.verificavitoria() or jogo.jogadaspossiveis():
        break
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

if jogo.verificavitoria():
    if jogador == 'X':
        print ('X VENCEU')
    if jogador == 'O':
        print ('O VENCEU')
else:
    print ('EMPATE!')