# def greet():
#    print("Hello World!")
#    print("How are you?")
#    print("How is the weather?")

# greet()

# Functions with Inputs
# def my_function(variable)

def greet_with_name(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")


# greet_with_name("Nesaar")
# greet_with_name("James")

# Argument = Actual piece of data
# Parameter = Used inside the function to refer to

# Position Argument = Unspecified where the argument should be. Defaults to order.
# Keyword Arguments = Add the parameter sign to say what each argument should be attached to.
# Keyword arguments will have the specified

# KEYWORD ARGUMENTS
greet_with_name(name="Nesaar", location="London")
