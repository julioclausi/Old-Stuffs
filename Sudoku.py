class Sudoku ():
    def __init__ (self,game):
        self.matrix = []
        for i in range(0,9):
            line = []
            for j in range(0,9):
                line.append(game[i][j])
            self.matrix.append(line)
    
    def print (self):
        for i in range(0,9):
            for j in range(0,9):
                print(self.matrix[i][j],end=' ')
                if j in [2,5]:
                    print('|',end=' ')
            print()
            if i in [2,5]:
                print('──────+───────+──────')

def read_the_game():
    with open('Game.txt') as tex:
        list_of_strings = tex.readlines()
    return list_of_strings

game = read_the_game()
jogo = Sudoku(game)
jogo.print()