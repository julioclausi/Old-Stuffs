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

#Printhing the map
def print_the_map():
    os.system('cls')
    for line in my_maze:
        for row in line:
            print(row,end='')
        print()

#Finding the player
def find_the_player():
    for i in range (0,len(my_maze)):
        for j in range (0, len(my_maze[i])):
            if my_maze[i][j] == 'X':
                player_pos=(i,j)
                print (player_pos)
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

my_maze = convert_the_map(read_the_map())
player_pos = find_the_player()
input('Press Enter to start')

while True:
    print_the_map()
    entry = input('\n W A S D? ')
    if entry.upper() == 'W':
        moving(-1,0,my_maze)
    elif entry.upper() == 'A':
        moving(0,-1,my_maze)
    elif entry.upper() == 'S':
        moving(1,0,my_maze)
    elif entry.upper() == 'D':
        moving(0,+1,my_maze)
    elif entry.upper() == 'Q':
        break
