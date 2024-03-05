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

# def find_missing_lines(jogo):
#     missing_numbers = []
#     for i in range(0,9):
#         line = [1,2,3,4,5,6,7,8,9]
#         print (line,end='--->')
#         for j in range(0,9):
#             try:
#                 num = int(jogo.matrix[i][j])
#                 if num in line:
#                     line.remove(num)
#             except:
#                 ...
#         print (line)
#     return missing_numbers

def find_missing_blocks (jogo):
    block = [1,2,3,4,5,6,7,8,9]
    for i in range (0,3):
        for j in range (0,3):
            try:
                num = int(jogo.matrix[i][j])
                block.remove(num)
            except:
                ...
    return block

def ismissing (block,num):
    if num in block:
        return True
    return False

game = read_the_game()
jogo = Sudoku(game)
jogo.print()

# There is a 9 at [0][1]

block = find_missing_blocks (jogo)

for num in block:
    print (f'{num} is missing')

# trying with #9

block2 = [4,9,5,3]
block3 = [9]

line = [1,1,1,1,1,1,1,1,1]
# if 9 in line1
if 9 in block2:
    line[3] = 0
    line[4] = 0
    line[5] = 0
if 9 in block3:
    line[6] = 0
    line[7] = 0
    line[8] = 0
for i in range (0,9):
    if line[i]:
        if jogo.matrix[0][i] != '_':
            line[i] = 0

print (line)