import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_colour():
    """Takes random RGB numbers and returns a random RGB Colour code"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.pensize(10)
        tim.color(random_colour())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)


draw_spirograph(5)

my_screen = Screen()
my_screen = screen.exitonclick()
