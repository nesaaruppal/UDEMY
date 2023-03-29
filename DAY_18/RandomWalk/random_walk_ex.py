from turtle import Turtle, Screen
import random

colours = ["White", "LightSteelBlue",
           "SkyBlue",
           "DarkCyan",
           "MediumSpringGreen", "Beige",
           "Gold", "Moccasin",
           "Bisque", "RosyBrown",
           "MediumVioletRed",
           "MediumPurple", "Silver",
           "MediumBlue", "LightCyan",
           "Aquamarine",
           "ForestGreen",
           "PaleGoldenrod", "Tan",
           "DarkOrange", "Chocolate",
           "DarkRed",
           "Magenta", "Yellow", "Red",
           "Indigo",
           "DarkSlateBlue", "Brown",
           "GreenYellow",
           "SandyBrown",
           "AntiqueWhite", ]

directions = [0, 90, 180, 270]


tim = Turtle()
tim.shapesize(2, 2, 2)
tim.pensize(10)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

my_screen = Screen()
my_screen.exitonclick()
