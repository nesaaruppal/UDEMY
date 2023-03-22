from data import data
from art import logo, vs
import random


print(logo)
print("Welcome to the Higher or Lower game!")


def random_choice_A():
    """Selects a random set of data from the data set and formats it"""
    choice_A = random.choice(data)
    choice_A_name = choice_A.get("name")
    choice_A_description = choice_A.get("description")
    choice_A_country = choice_A.get("country")
    return f"Compare A: {choice_A_name}, a {choice_A_description} from {choice_A_country}"


def random_choice_B():
    """Selects a second random set of data from the data set and formats it"""
    choice_B = random.choice(data)
    choice_B_name = choice_B.get("name")
    choice_B_description = choice_B.get("description")
    choice_B_country = choice_B.get("country")
    return f"Against B: {choice_B_name}, a {choice_B_description} from {choice_B_country}"


def compare_score(random_choice_A, random_choice_B):
    guess = input("Who has more followers? Type 'A' or 'B': ")
    followers_A = int(random_choice_A.get("follower_count"))
    followers_B = int(random_choice_B.get("follower_count"))


def game(random_choice_A, random_choice_B):
    print(random_choice_A())
    print(logo)
    print(random_choice_B())
    compare_score()


game(random_choice_A, random_choice_B)
