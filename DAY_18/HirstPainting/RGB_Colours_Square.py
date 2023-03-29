import colorgram
from turtle import Screen
import turtle as turtle_module
import random

colours_list = [(237, 234, 226), (223, 159, 79), (37, 109, 152), (118, 163, 192), (153, 62, 85), (206, 133,
                                                                                                  157), (179, 160, 34), (28, 132, 96), (121, 180, 152), (215, 86, 59), (200, 84, 111), (163, 81, 50), (213,
                                                                                                                                                                                                       227, 218), (142, 33, 42), (54, 167, 135), (232, 197, 107), (228, 208, 218), (7, 106, 82), (42, 159, 184), (203, 218, 226), (118, 113, 163), (236, 160, 178), (32, 62, 112), (237, 170, 156), (155, 210, 197), (125, 38, 36), (67, 44, 42), (37, 57, 75), (28, 65, 58), (78, 36, 45)]


def turn_left():
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward(50)


def turn_right():
    tim.right(90)
    tim.penup()
    tim.forward(50)
    tim.right(90)
    tim.forward(50)


def draw_dots():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colours_list))
        tim.penup()
        tim.forward(50)


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()
tim.setposition(-300, -300)


for _ in range(5):
    draw_dots()
    turn_left()
    draw_dots()
    turn_right()


my_screen = Screen()
my_screen.exitonclick()
