# NO BLOCK SCOPE IN PYTHON

enemies = 1


def increase_enemies():
    global enemies
    # Accessing a global scope created outside of a function
    enemies += 1
    print(f"Enemies inside the function: {enemies}")


increase_enemies()
print(f"Enemies outside the function: {enemies}")


# Constants use CAPITALS
PI_NUMBER = 3.14159
URL = "http://www.google.com"
# Capitals remind you that these are GLOBAL SCOPES
