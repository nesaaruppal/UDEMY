from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("Red")


# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

for _ in range(4):
    tim.forward(100)
    tim.right(90)

my_screen = Screen()
my_screen.exitonclick()
