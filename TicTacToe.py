class Jogo ():
    def __init__ (self):
        self.tabuleiro = [' '] * 9

    def show (self):
        print (f'{self.tabuleiro[0]}|{self.tabuleiro[1]}|{self.tabuleiro[2]}')
        print (f'-----')
        print (f'{self.tabuleiro[3]}|{self.tabuleiro[4]}|{self.tabuleiro[5]}')
        print (f'-----')
        print (f'{self.tabuleiro[6]}|{self.tabuleiro[7]}|{self.tabuleiro[8]}')

    def jogadas_possiveis (self):
        jogadas = []
        for i in range (0,9):
            if self.tabuleiro[i] == ' ':
                jogadas.append(i)
        return jogadas

    def vitoria (self):
        if self.tabuleiro[0] == self.tabuleiro[1] and self.tabuleiro[0] == self.tabuleiro[2] and self.tabuleiro[0] != ' ':
            return True
        elif self.tabuleiro[3] == self.tabuleiro[4] and self.tabuleiro[3] == self.tabuleiro[5] and self.tabuleiro[3] != ' ':
            return True
        elif self.tabuleiro[6] == self.tabuleiro[7] and self.tabuleiro[6] == self.tabuleiro[8] and self.tabuleiro[6] != ' ':
            return True
        elif self.tabuleiro[0] == self.tabuleiro[3] and self.tabuleiro[0] == self.tabuleiro[6] and self.tabuleiro[0] != ' ':
            return True
        elif self.tabuleiro[1] == self.tabuleiro[4] and self.tabuleiro[1] == self.tabuleiro[7] and self.tabuleiro[1] != ' ':
            return True
        elif self.tabuleiro[2] == self.tabuleiro[5] and self.tabuleiro[2] == self.tabuleiro[8] and self.tabuleiro[2] != ' ':
            return True
        elif self.tabuleiro[0] == self.tabuleiro[4] and self.tabuleiro[0] == self.tabuleiro[8] and self.tabuleiro[0] != ' ':
            return True
        elif self.tabuleiro[2] == self.tabuleiro[4] and self.tabuleiro[2] == self.tabuleiro[6] and self.tabuleiro[2] != ' ':
            return True

    def jogada (self,player):
        if player == 1:
            # XXXXX
            print (self.jogadas_possiveis())
            play = int (input ('Jogador X entre com uma opção acima: '))
            self.tabuleiro[play] = 'X'
        else:
            # OOOOO
            print (self.jogadas_possiveis())
            play = int (input ('Jogador O entre com uma opção acima: '))
            self.tabuleiro[play] = 'O'

    def teste1 (self):
        """
        X|0|X
         |0|X
        X| |0
        """
        self.tabuleiro[0] = 'X'
        self.tabuleiro[2] = 'X'
        self.tabuleiro[5] = 'X'
        self.tabuleiro[6] = 'X'
        self.tabuleiro[1] = 'O'
        self.tabuleiro[4] = 'O'
        self.tabuleiro[8] = 'O'





player = -1
novo_jogo = Jogo()
novo_jogo.teste1()

while True:
    novo_jogo.show()
    novo_jogo.jogada(player)
    novo_jogo.show()
    if novo_jogo.vitoria():
        print ('Vitoria')
        if player == 1:
            print ('Jogador X venceu')
        else:
            print ('Jogador O venceu')
        break
    else:
        if len(novo_jogo.jogadas_possiveis()) <1:
            print ('Empate')
            break
    player *= -1