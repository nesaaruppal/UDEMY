from turtle import Turtle, Screen

tim = Turtle()

num_sides = 10


def draw_shape(num_sides):
    for _ in range(num_sides, ):
        num_sides += 1
        angle = 360/num_sides
        tim.forward(100)
        tim.right(angle=angle)


my_screen = Screen()
my_screen.exitonclick()
