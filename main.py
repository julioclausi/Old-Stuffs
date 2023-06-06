import os
from pynput import keyboard
from pynput.keyboard import Key

#Reading the map
def read_the_map():
    with open('maze.txt') as tex:
        list_of_strings = tex.readlines()
    return list_of_strings

#Converting the map
def convert_the_map(list_of_strings):
    my_maze = []
    for i in range(0,len(list_of_strings)):
        my_maze.append([])
        for j in range(0,len(list_of_strings[i])-1):
            my_maze[i].append(list_of_strings[i][j])
    return my_maze

#Printing the map
def print_the_map():
    os.system('cls')
    for i in range (0,len(my_maze)):
        for j in range (0, len(my_maze[i])):
            print (f'{my_maze[i][j]:^3}',end='')
        print()

#Printing the solution
def print_the_solution():
    os.system('cls')
    for i in range (0,len(new_maze)):
        for j in range (0, len(new_maze[i])):
            print (f'{new_maze[i][j]:^3}',end='')
        print()

#Finding the player
def find_the_player():
    for i in range (0,len(my_maze)):
        for j in range (0, len(my_maze[i])):
            if my_maze[i][j] == 'X':
                player_pos=(i,j)
                return player_pos
            
#Moving
def moving(x,y,my_maze):
    global player_pos 
    if my_maze[player_pos[0]+x][player_pos[1]+y] == '#':
        ...
    elif my_maze[player_pos[0]+x][player_pos[1]+y] == '@':
        print ("YOU WIN!!!")
        quit()
    else:
        my_maze[player_pos[0]+x][player_pos[1]+y] = 'X'
        my_maze[player_pos[0]][player_pos[1]] = '.'
        player_pos = (player_pos[0]+x,player_pos[1]+y)

#Finding the end
def find_the_end():
    for i in range (0,len(my_maze)):
        for j in range (0, len(my_maze[i])):
            if my_maze[i][j] == '@':
                end_pos=(i,j)
                return end_pos

def counting(i,j,counter):
    block = new_maze[i][j]
    if block.isdigit():
        if int(block) > int(counter):
            new_maze[i][j] = str(counter)
            counting(i,j+1,counter+1)
            counting(i+1,j,counter+1)
            counting(i,j-1,counter+1)
            counting(i-1,j,counter+1)
    else:
        if block == '@':
            new_maze[i][j] = str(counter)
            counting(i,j+1,counter+1)
            counting(i+1,j,counter+1)
            counting(i,j-1,counter+1)
            counting(i-1,j,counter+1)
        elif block == '.':
            new_maze[i][j] = str(counter)
            counting(i,j+1,counter+1)
            counting(i+1,j,counter+1)
            counting(i,j-1,counter+1)
            counting(i-1,j,counter+1)
        elif block == 'X':
            new_maze[i][j] = str(counter)

#Solving
def solve_the_map():
    end_pos = find_the_end()
    counting(end_pos[0],end_pos[1],0)
    print_the_solution()

def tracing_back(x,y,counter):
    if new_maze[x+1][y]!='#' and int(new_maze[x][y]) > int(new_maze[x+1][y]):
        my_maze[x][y] = counter
        tracing_back(x+1,y,counter+1)
    elif new_maze[x][y+1]!='#' and int(new_maze[x][y]) > int(new_maze[x][y+1]):
        my_maze[x][y] = counter
        tracing_back(x,y+1,counter+1)
    elif new_maze[x-1][y]!='#' and int(new_maze[x][y]) > int(new_maze[x-1][y]):
        my_maze[x][y] = counter
        tracing_back(x-1,y,counter+1)
    elif new_maze[x][y-1]!='#' and int(new_maze[x][y]) > int(new_maze[x][y-1]):
        my_maze[x][y] = counter
        tracing_back(x,y-1,counter+1)

my_maze = convert_the_map(read_the_map())
new_maze = convert_the_map(read_the_map())
player_pos = find_the_player()

input('Press Enter to view the backtesting')

solve_the_map()

input('Press Enter to view the map')

print_the_map()

tracing_back(player_pos[0],player_pos[1],0)

input('Press Enter to view the solution')

print_the_map()

# input('Press Enter to start')
# while True:
#     print_the_map()
#     entry = input('\n W A S D? ')
#     if entry.upper() == 'W':
#         moving(-1,0,my_maze)
#     elif entry.upper() == 'A':
#         moving(0,-1,my_maze)
#     elif entry.upper() == 'S':
#         moving(1,0,my_maze)
#     elif entry.upper() == 'D':
#         moving(0,+1,my_maze)
#     elif entry.upper() == 'Q':
#         break
