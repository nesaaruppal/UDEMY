from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

first_num = int(input("What is the first number?: "))

for symbol in operations:
    print(symbol)
operation_choice = input("Pick an operation: ")

second_num = int(input("What is the next number?"))

calculation_function = operations[operation_choice]
answer = calculation_function(first_num, second_num)

print(f"{first_num} {operation_choice} {second_num} = {answer}")

operation_choice = input("Pick another operation: ")
num3 = int(input("What is the next number?: "))
calculation_function = operations[operation_choice]
answer = calculation_function(answer, num3)
# The return function means that you can use the output of a function ("answer") as an input into the same function so that it can be re-used for further calculations.
