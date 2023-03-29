import colorgram
from turtle import Turtle, Screen
import random

#rgb_colours = []


#colours = colorgram.extract("image.jpg", 30)
# print(colours)

# for colour in colours:
#    r = colour.rgb.r
#    b = colour.rgb.b
#    g = colour.rgb.g
#    new_colour = (r, g, b)
#    rgb_colours.append(new_colour)

# print(rgb_colours)

colours_list = [(237, 234, 226), (223, 159, 79), (37, 109, 152), (118, 163, 192), (153, 62, 85), (206, 133, 157), (179, 160, 34), (28, 132, 96), (121, 180, 152), (215, 86, 59), (200, 84, 111), (163, 81, 50), (213, 227, 218), (142, 33, 42), (54,
                                                                                                                                                                                                                                                 167, 135), (232, 197, 107), (228, 208, 218), (7, 106, 82), (42, 159, 184), (203, 218, 226), (118, 113, 163), (236, 160, 178), (32, 62, 112), (237, 170, 156), (155, 210, 197), (125, 38, 36), (67, 44, 42), (37, 57, 75), (28, 65, 58), (78, 36, 45)]

# Spot painting

# 10 x 10 rows
# Dots 20 space 50

tim = Turtle()
tim.shape("arrow")


for _ in range(10):
    tim.pendown()
    tim.dot(20, choice[colours_list])
    tim.penup(50)
    tim.pendown()
    tim.dot(20, choice(colours_list))

my_screen = Screen()
my_screen = exitonclick()
