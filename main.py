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
def print_the_map(my_maze):
    for line in my_maze:
        for row in line:
            print(row,end='')
        print()

my_maze = convert_the_map(read_the_map())

print_the_map (my_maze)
