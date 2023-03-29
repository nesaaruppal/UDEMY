from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color("red")
tim.shape("turtle")
tim.pencolor("blue")
tim.pensize(10)
tim.shapesize(3)


def move_forward():
    tim.forward(25)


def move_backwards():
    tim.back(25)


def turn_left():
    tim.left(45)


def turn_right():
    tim.right(45)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen = Screen()
my_screen.listen()

my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=turn_left, key="d")
my_screen.onkey(fun=turn_right, key="a")
my_screen.onkey(fun=clear_screen, key="c")


my_screen.exitonclick()
