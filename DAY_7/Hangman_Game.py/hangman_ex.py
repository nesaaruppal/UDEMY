import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print("Let's play Hangman!")
print(logo)

chosen_word = random.choice(word_list)
lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    print(f"You have {lives} lives!")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed {guess}!!")

    # Position will be = to 0
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word!")
        lives -= 1
        print(f"You have {lives} lives left!")
        if lives == 0:
            print("YOU LOSE!")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
