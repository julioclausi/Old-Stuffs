#My version of Snake


from turtle import Screen,Turtle
from time import sleep
import random

SIZE = 20
STARTING_POS = [(0,0),(SIZE * (-1),0),(SIZE * (-2),0)]

def init_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('A Simple Snake Game')
    screen.tracer(0)
    return screen

class Snake():
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]
    
    def eat(self):
        self.body +=1
    
    def create(self):
        for position in STARTING_POS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for count in range(len(self.segments)-1,0,-1):
            coord_x = self.segments[count-1].xcor()
            coord_y = self.segments[count-1].ycor()
            self.segments[count].goto(coord_x,coord_y)
        self.head.forward(SIZE)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
 
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def ate(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        #self.shapesize(0.5,0.5)
        self.penup()
        self.create()
    
    def create(self):
        x = random.randint(-14,14)*20
        y = random.randint(-14,14)*20
        print(x,y)
        self.goto(x,y)

def eat(snake,food):
    for segment in snake.segments:
        if Turtle.distance(segment,food) < 14:
            food.create()
            snake.ate()
            score.increase()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.print_score()
    
    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center")
    
    def game_over(self):
        self.clear()
        self.goto(0,00)
        self.write(f"GAME OVER!\nScore: {self.score}",font=("Arial",30,"normal"), align="center")

    def increase(self):
        self.score+=1
        self.print_score()

game = init_game()

alive = True

snake = Snake()

food = Food()

score = Scoreboard()

while alive:
    game.update()
    sleep(0.1)
    snake.move()
    game.listen()
    game.onkey(snake.up,"Up")
    game.onkey(snake.down,"Down")
    game.onkey(snake.left,"Left")
    game.onkey(snake.right,"Right")
    eat(snake,food)

    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        break

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            alive = False

score.game_over()

game.exitonclick()