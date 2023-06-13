#Snake ASCII

from time import sleep
import os
import keyboard
import random

COLUMNS = 20
LINES = 20
STARTING_POSITIONS = [(5,5),(5,4),(5,3)]

class Snake():
    def __init__(self):
        self.segments = []
        self.direction = 'Right'
        self.create()
    
    def create(self):
        for segment in STARTING_POSITIONS:
            self.segments.append(segment)
    
    def print_segments(self):
        for segment in self.segments:
            print(segment)
    
    def eat(self):
        new_segment = self.segments[-1]
        self.segments.append(new_segment)
    
    def move(self):
        if self.direction == 'Right':
            for i in range(0,len(self.segments)):
                if i == 0:
                    head = self.segments[i]
                    self.segments[i] = (self.segments[i][0],self.segments[i][1]+1)
                else:
                    previous = self.segments[i]
                    self.segments[i] = head
                    head = previous
        if self.direction == 'Left':
            for i in range(0,len(self.segments)):
                if i == 0:
                    head = self.segments[i]
                    self.segments[i] = (self.segments[i][0],self.segments[i][1]-1)
                else:
                    previous = self.segments[i]
                    self.segments[i] = head
                    head = previous
        if self.direction == 'Up':
            for i in range(0,len(self.segments)):
                if i == 0:
                    head = self.segments[i]
                    self.segments[i] = (self.segments[i][0]-1,self.segments[i][1])
                else:
                    previous = self.segments[i]
                    self.segments[i] = head
                    head = previous
        if self.direction == 'Down':
            for i in range(0,len(self.segments)):
                if i == 0:
                    head = self.segments[i]
                    self.segments[i] = (self.segments[i][0]+1,self.segments[i][1])
                else:
                    previous = self.segments[i]
                    self.segments[i] = head
                    head = previous

class Food():
    def __init__(self):
        self.position = (0,0)
        self.create()

    def create(self):
        x = random.randint(0,LINES-1)
        y = random.randint(0,LINES-1)
        self.position = (x,y)
        if self.position in snake.segments:
            self.create()

class Scoreboard:
    def __init__(self):
        self.score = 0
    
    def increment(self):
        self.score += 1

    def __str__(self):
        return f'Score: {self.score}' 
    
def print_maze():
    os.system('cls')
    print ('#'*(COLUMNS+2))
    for i in range(0,LINES):
        print('#',end='')
        for j in range(0,COLUMNS):
            if (i,j) in snake.segments:
                print('s',end='')
            elif (i,j) == food.position:
                print('.',end='')
            else:
                print(maze[i][j],end='')
        print('#')
    print ('#'*(COLUMNS+2))
    print (score)

def create_maze():
    maze = []
    for i in range(0,LINES):
        maze.append([])
        for j in range(0,COLUMNS):
            maze[i].append(' ')
    return maze

def check_snake_food():
    if snake.segments[0] == food.position:
        snake.eat()
        food.create()
        score.increment()

def check_snake_wall():
    if snake.segments[0][0] == -1 or snake.segments[0][1] == -1 or snake.segments[0][0] == LINES or snake.segments[0][1] == COLUMNS:
        return False
    return True

maze = create_maze()
snake = Snake()
food = Food()
score = Scoreboard()
alive = True

while alive:
    print_maze()
    check_snake_food()
    snake.move()
    alive = check_snake_wall()
    try:
        if keyboard.is_pressed('left'):
            if snake.direction != 'Right':
                snake.direction='Left'
        if keyboard.is_pressed('right'):
            if snake.direction != 'Left':
                snake.direction='Right'
        if keyboard.is_pressed('Down'):
            if snake.direction != 'Up':
                snake.direction='Down'
        if keyboard.is_pressed('up'):
            if snake.direction != 'Down':
                snake.direction='Up'
        sleep(0.1)
    except:
        break

print('GAME OVER!')