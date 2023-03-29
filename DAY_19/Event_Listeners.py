##### EVENT LISTENERS ####

# Computer listens to the user's keystrokes to affect the screen
# .listen METHOD

from turtle import Turtle, Screen


def move_forward():
    tim.forward(10)


tim = Turtle()


# SCREEN.LISTEN
# ON KEY METHOD
my_screen = Screen()
my_screen.listen()
my_screen.onkey(fun=move_forward, key="space")
my_screen.exitonclick()


#### HIGHER ORDER FUNCTIONS ####
# A function which can work with other functions
