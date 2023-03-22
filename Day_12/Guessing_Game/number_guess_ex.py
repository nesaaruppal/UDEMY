# Number Guessing Game Objectives:

# Include an ASCII art logo. /////
# Allow the player to submit a guess for a number between 1 and 100. ///////
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


def check_answer(random_number, user_guess):
    """Checks the random number against the user's guess"""
    user_guess = int(
        input("I'm thinking of a number between 1 and 100, have a guess: "))
    lives = 10
    if random_number == user_guess:
        lives = 10
        return(
            "You got the right answer: {random_number}! YOU WIN! You had {lives_remaining} lives left!")
    if random_number > user_guess:
        lives -= 1
        print(f"You have {lives_remaining} lives left!")
        print("Your guess was too low!\nGuess again:")
    elif random_number < user_guess:
        lives -= 1
        print(f"You have {lives_remaining} lives left!")
        print("Your guess was too high!\nGuess again: ")
    else:
        print("Please make sure you enter a number between 1 and 100!")


print(logo)
print("Welcome to the Number Guessing Game!")

random_number = (random.randint(1, 100))

user_guess = int(
    input("I'm thinking of a number between 1 and 100, have a guess: "))
print(user_guess)
check_answer(random_number, user_guess)


should_continue = True

while not should_continue:
    game()
    lives_remaining = 10
    random_number = (random.randint(1, 100))
    user_guess = int(
        input("I'm thinking of a number between 1 and 100, have a guess: "))
    check_answer(random_number, user_guess)
