########## TUPLES ########

# Data Type
# (1, 3, 8)

# You cannot change things within a Tuple
# Cannot remove
# Once created it is IMMUTABLE


import random
import turtle as t
my_tuple = (1, 3, 8)
print(my_tuple[1])


tim = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour
