from turtle import Turtle, Screen
import random

is_race_on = False
colours = ["red", "blue", "green", "yellow", "purple", "orange", "brown"]
y_positions = [-300, -200, -100, 0, 300, 200, 100]
all_turtles = []

for turtle in range(0, 7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colours[turtle])
    new_turtle.shapesize(5)
    new_turtle.penup()
    new_turtle.goto(x=-425, y=y_positions[turtle])
    new_turtle.pendown()
    new_turtle.pensize(5)
    all_turtles.append(new_turtle)


my_screen = Screen()
my_screen.screensize(500, 500, bg=None)
user_guess = my_screen.textinput(title="Make your bet: ",
                                 prompt="Which turtle will win? Enter a colour: ")


if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 425:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if user_guess == winning_colour:
                print(f"You've won! The {winning_colour} turtle won!")
            else:
                print(f"You've lost! The {winning_colour} turtle won!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()
