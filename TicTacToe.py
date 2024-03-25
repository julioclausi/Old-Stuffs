class Jogo ():
    def __init__ (self):
        self.tabuleiro = [' '] * 9
        self.turno = 0

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
            print ('Jogada do computador')
            jogada = melhor_jogada(self)
            self.tabuleiro[jogada] = 'O'

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

    def empate (self):
        jogadas = self.jogadas_possiveis()
        if len(jogadas)<1:
            return True
        return False

    def calcula (self,player):
        if self.vitoria():
            if self.turno == player:
                return -1
            else:
                return 1
        else:
            return 0

def minimax (jogo_teste: Jogo,player,maximizing):

    if jogo_teste.vitoria() or jogo_teste.empate():
        return jogo_teste.calcula(player)
    
    if maximizing:
        melhor_valor = -10
        jogadas = jogo_teste.jogadas_possiveis()
        for jogada in jogadas:
            if player == 1:
                jogo_teste.tabuleiro[jogada] = 'X'
            else:
                jogo_teste.tabuleiro[jogada] = 'O'
            resultado = minimax(jogo_teste,player*-1,False)
            jogo_teste.tabuleiro[jogada] = ' '
            melhor_valor = max(melhor_valor,resultado)
        return melhor_valor

    else:
        pior_valor = 10
        jogadas = jogo_teste.jogadas_possiveis()
        for jogada in jogadas:
            if player == 1:
                jogo_teste.tabuleiro[jogada] = 'X'
            else:
                jogo_teste.tabuleiro[jogada] = 'O'
            resultado = minimax(jogo_teste,player*-1,True)
            jogo_teste.tabuleiro[jogada] = ' '
            pior_valor = min (pior_valor,resultado)
        return pior_valor

def melhor_jogada (jogo_teste: Jogo):
    jogada_correta = -1
    melhor_resultado = -10
    jogadas = jogo_teste.jogadas_possiveis()
    for jogada in jogadas:
        if jogo_teste.turno == 1:
            jogo_teste.tabuleiro[jogada] = 'X'
        else:
            jogo_teste.tabuleiro[jogada] = 'O'
        resultado = minimax(jogo_teste,jogo_teste.turno*-1,False)
        jogo_teste.tabuleiro[jogada] = ' '
        if resultado > melhor_resultado:
            melhor_resultado = resultado
            jogada_correta = jogada
    return jogada_correta

jogo = Jogo()
# jogo.teste1()
jogo.show()
jogo.turno = 1

while True:
    jogo.jogada(jogo.turno)
    jogo.show()
    if jogo.vitoria():
        if jogo.turno == -1:
            print ('Computador venceu')
        else:
            print ('Jogador venceu')
        break
    else:
        if jogo.empate():
            print ('Empate')
            break
    jogo.turno *= -1