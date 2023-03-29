from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shapesize(3, 3, 1)
tim.shape("turtle")
tim.color("Red")
tim.pensize(10)


colours = ["White", "LightSteelBlue", "SkyBlue",
           "DarkCyan", "MediumSpringGreen", "Beige", "Gold", "Moccasin", "Bisque", "RosyBrown", "MediumVioletRed", "MediumPurple", "Silver", "MediumBlue", "LightCyan", "Aquamarine", "ForestGreen", "PaleGoldenrod", "Tan", "DarkOrange", "Chocolate", "DarkRed", "Magenta", "Yellow", "Red", "Indigo", "DarkSlateBlue", "Browm", "GreenYellow", "SandyBrown", "AntiqueWhite", ]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle=angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


my_screen = Screen()
my_screen.exitonclick()
