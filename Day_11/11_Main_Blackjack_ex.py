from art import logo
import random
import os
os.system('cls')


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOSE! The computer has blackjack!"
    elif user_score == 0:
        return "WIN! You have blackjack!"
    elif user_score > 21:
        return "LOSE! You went over 21 and lost!"
    elif computer_score > 21:
        return "WIN! The computer went over 21 and lost!"
    elif user_score > computer_score:
        return "WIN! Your score was higher than the computers'!"
    else:
        return "LOSE! The computer's score was higher than yours!"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        #new_card = deal_card()
        # user_cards.append(new_card)
        # Not "EXTEND" because that adds a list to a list. Append   just adds to the list.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score:    {user_score}")
        print(f"The Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'Y' for yes and 'N' for no:  ")
            if another_card == "Y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score:     {user_score}!")
    print(
        f"The computer's final hand: {computer_cards}, their final  score was {computer_score}!")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ") == "y":
    os.system('cls')
    play_game()
