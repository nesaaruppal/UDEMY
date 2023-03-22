from random import randint


def check_answer(guess, answer):
    if guess > answer:
        print("Too High!")
    elif guess < answer:
        print("Too Low!")
    else:
        print(f"You got it! The answer is {answer}.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

answer = randint(1, 100)

guess = int(input("Make a guess: "))
