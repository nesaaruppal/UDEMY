import random
print("Let's play Rock, Paper, Scissors!")

rock = print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]


player_choice = int(input(
    "What would you like to choose? Type '0' for Rock, '1' for Paper and '2' for Scissors:\n"))

computer_choice = random.randint(0, 2)

if computer_choice == player_choice:
    print("DRAW!")

elif computer_choice == 0 and player_choice == 1:
    print("The computer chose ROCK. You chose paper. YOU WIN!")
    print(game_images[computer_choice])
elif computer_choice == 0 and player_choice == 2:
    print("The computer chose ROCK. You chose scissors. YOU LOSE!")
    print(game_images[0])

elif computer_choice == 1 and player_choice == 0:
    print("The computer chose PAPER. You chose rock. YOU LOSE!")
    print(game_images[1])
elif computer_choice == 1 and player_choice == 2:
    print("The computer chose PAPER. You chose scissors. YOU WIN!")
    print(game_images[2])

elif computer_choice == 2 and player_choice == 0:
    print("The computer chose SCISSORS. You chose Rock. YOU WIN!")
    print(game_images[0])
elif computer_choice == 2 and player_choice == 1:
    print("The computer chose SCISSORS. You chose paper. YOU LOSE!")
    print(game_images[2])
else:
    print("Please enter a valid number to play!")
