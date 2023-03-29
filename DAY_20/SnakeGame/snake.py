from turtle import Turtle, Screen
import random

#is_game_on = False

my_screen = Screen()
my_screen.screensize(canvwidth=600, canvheight=600, bg="black")
my_screen.title("My Snake Game")
my_screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle()
    new_segment.penup()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.goto(position)


def snake_food():
    """Generates random positions for Snake Food"""
    # if is_game_on == True:
    y_cord = random.randint(0, 250)
    x_cord = random.randint(0, 250)
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.shapesize(1)
    snake.penup()
    snake.goto(x=x_cord, y=y_cord)


def move_forward():
    snake.forward(20)


def turn_left():
    snake.left(90)


def turn_right():
    snake.right(90)


def move_back():
    snake.back(20)


game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)
        my_screen.update()

my_screen.listen()
my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_back, key="s")
my_screen.onkey(fun=turn_left, key="a")
my_screen.onkey(fun=turn_right, key="d")


snake_food()


my_screen.exitonclick()
