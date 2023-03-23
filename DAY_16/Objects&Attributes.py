#from turtle import Turtle

### Construct a new OBJECT ###
#   from turtle import Turtle, Screen
#   tim = Turtle()

### Identifies Object then retrieves Attribute ###
#   car.speed

### my_screen = Screen() ###
#   print(my_screen.canvheight)

### Identifies Object then retrieves Method ###
#   car.stop()

### my_screen.exitonclick() ###

### USING TURTLE GRAPHICS ###
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
