# Import EVERYTHING
#import heroes
#from turtle import *

# More difficult to understand each module
# Should be checked

# Import MODULE AS
import turtle as t
from turtle import Screen
tim = t.Turtle()

for _ in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


my_screen = Screen()
my_screen.exitonclick()
