from data import data
from art import logo, vs
import random
import os
def clear(): return os.system('cls')


# Format Data into a printable format
# Moved up to make a separate function
# Changed account_a to "account" to make it more reusable


def format_data(account):
    """Formats the random data selection into a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}!"

# Use if statement to check if user is correct
# Moved up to make a separate function


def check_answer(guess, a_followers, b_followers):
    """Uses an if statement to check the user's guess"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display logo Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    # Use the format_data function to make a printable version
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Keep track of score
    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"Yay! You're right! You're current score is {score}!")
    else:
        game_should_continue = False
        print(f"Sorry! You got it wrong! Your final score is {score}!")
