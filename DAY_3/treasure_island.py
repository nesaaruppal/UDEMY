print("Welcome to Treasure Island. Your mission is to find the treasure!")
print("Your mission is to find the treasure")

choice1 = input(
    "You are at a cross road. Would you like to turn left or right? Type 'L' for left and 'R' for right:\n")
if choice1 == "R":
    print("You fell into a hole! Game Over!")
else:
    print("Move forward!")

choice2 = input(
    "You have reached a river. Would you like to swim or wait? Type 'S' for swim and 'W' for wait:\n")
if choice2 == "S":
    print("You drowned! Game Over!")
else:
    print("Move Forward!")

choice3 = input(
    "Which door would you like to go through? Type 'R' for red, 'B' for blue and 'Y' for yellow:\n")
if choice3 == "R":
    print("Wrong door! Game Over!")
elif choice3 == "B":
    print("Wrong door! Game Over!")
else:
    print("YOU WIN!")
