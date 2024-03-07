class Sudoku ():
    def __init__ (self,game):
        self.steps = 0
        self.matrix = []
        for i in range(0,9):
            line = []
            for j in range(0,9):
                line.append(int(game[i][j]))
            self.matrix.append(line)
    
    def print (self):
        for i in range(0,9):
            for j in range(0,9):
                if self.matrix[i][j]:
                    print(self.matrix[i][j],end=' ')
                else:
                    print('_',end=' ')
                if j in [2,5]:
                    print('|',end=' ')
            print()
            if i in [2,5]:
                print('──────+───────+──────')

def read_the_game ():
    with open('Game2.txt') as tex:
        list_of_strings = tex.readlines()
    return list_of_strings

def return_line (matrix,num):
    return matrix[num]

def return_column (matrix, num):
    column = []
    for i in range(0,9):
        column.append(matrix[i][num])
    return column

def return_block (matrix,num):
    block = []
    if num == 1:
        for i in range (0,3):
            for j in range (0,3):
                block.append(matrix[i][j])
    elif num == 2:
        for i in range (0,3):
            for j in range (3,6):
                block.append(matrix[i][j])
    elif num == 3:
        for i in range (0,3):
            for j in range (6,9):
                block.append(matrix[i][j])
    elif num == 4:
        for i in range (3,6):
            for j in range (0,3):
                block.append(matrix[i][j])
    elif num == 5:
        for i in range (3,6):
            for j in range (3,6):
                block.append(matrix[i][j])
    elif num == 6:
        for i in range (3,6):
            for j in range (6,9):
                block.append(matrix[i][j])
    elif num == 7:
        for i in range (6,9):
            for j in range (0,3):
                block.append(matrix[i][j])
    elif num == 8:
        for i in range (6,9):
            for j in range (3,6):
                block.append(matrix[i][j])
    elif num == 9:
        for i in range (6,9):
            for j in range (6,9):
                block.append(matrix[i][j])
    return block

def finder_line (matrix):
    for i in range (0,9):
        attempt = [0,0,0,0,0,0,0,0,0]
        attempts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        line = return_line(matrix,i)
        for j in range (0,9):
            column = return_column(matrix,j)
            block_num = int(i/3)*3 + 1 + int(j/3)
            block = return_block(matrix, block_num)
            if matrix[i][j] == 0:
                for num in range (1,10):
                    if num in line:
                        ...
                    else:
                        if num in column:
                            ...
                        else:
                            if num in block:
                                ...
                            else:
                                attempt[num-1] += 1
                                attempts[num-1] = (i,j)

        for k in range (1,10):
            if attempt[k-1] == 1:
                x,y = attempts[k-1]
                print (f'The {k} is in line {x} column {y}')
                matrix[x][y] = k
                jogo.print()
                jogo.steps +=1
                return

def finder_column (matrix):
    for j in range (0,9):
        attempt = [0,0,0,0,0,0,0,0,0]
        attempts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        column = return_column(matrix,j)
        for i in range (0,9):
            line = return_line(matrix,i)
            block_num = int(i/3)*3 + 1 + int(j/3)
            block = return_block(matrix, block_num)
            if matrix[i][j] == 0:
                for num in range (1,10):
                    if num in line:
                        ...
                    else:
                        if num in column:
                            ...
                        else:
                            if num in block:
                                ...
                            else:
                                attempt[num-1] += 1
                                attempts[num-1] = (i,j)

        for k in range (1,10):
            if attempt[k-1] == 1:
                x,y = attempts[k-1]
                print (f'The {k} is in line {x} column {y}')
                matrix[x][y] = k
                jogo.print()
                jogo.steps +=1
                return

def finder_block (matrix):
    block = []
    for num in range (1,10):
        attempt = [0,0,0,0,0,0,0,0,0]
        attempts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        block = return_block(matrix,num)
        if num == 1:
            for i in range (0,3):
                for j in range (0,3):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 2:
            for i in range (0,3):
                for j in range (3,6):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 3:
            for i in range (0,3):
                for j in range (6,9):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 4:
            for i in range (3,6):
                for j in range (0,3):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 5:
            for i in range (3,6):
                for j in range (3,6):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 6:
            for i in range (3,6):
                for j in range (6,9):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 7:
            for i in range (6,9):
                for j in range (0,3):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 8:
            for i in range (6,9):
                for j in range (3,6):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        elif num == 9:
            for i in range (6,9):
                for j in range (6,9):
                    line = return_line(matrix,i)
                    column = return_column(matrix,j)
                    if matrix[i][j] == 0:
                        for k in range (1,10):
                            if k in line:
                                ...
                            else:
                                if k in block:
                                    ...
                                else:
                                    if k in column:
                                        ...
                                    else:
                                        attempt[k-1] +=1
                                        attempts[k-1] = (i,j)
        for k in range (1,10):
            if attempt[k-1] == 1:
                x,y = attempts[k-1]
                print (f'The {k} is in line {x} column {y}')
                matrix[x][y] = k
                jogo.print()
                jogo.steps +=1
                return

def end_game(matrix):
    gameover=True
    for i in range(0,9):
        for j in range(0,9):
            if matrix[i][j]:
                ...
            else:
                gameover=False
    return gameover
                

game = read_the_game()
jogo = Sudoku(game)
jogo.print()

while not end_game(jogo.matrix):
    finder_line (jogo.matrix)
    finder_column (jogo.matrix)
    finder_block (jogo.matrix)

print (f"PUZZLE SOLVED! Steps: {jogo.steps}")