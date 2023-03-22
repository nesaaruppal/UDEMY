from art import logo
import os
os.system('cls')


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


# Place into another function for RECURSION
def calculator():
    print(logo)
    first_num = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    # While Flag

    while should_continue:
        operation_choice = input("Pick an operation: ")
        second_num = float(input("What is the next number? "))
        calculation_function = operations[operation_choice]
        answer = calculation_function(first_num, second_num)

        print(f"{first_num} {operation_choice} {second_num} = {answer}  ")

        repeat = input(
            f"Would you like to continue calculation with {answer}? Type 'Y' for yes and 'N' if you would like to start a new calculation. Type 'Exit' to leave the calculation: ")
        if repeat == "Y":
            first_num = answer
        elif repeat == "N":
            should_continue = False
            os.system('cls')
            calculator()
        else:
            should_continue = False


calculator()
