print("Welcome to your rollercoaster ride!")
height = int(input("What is your height in cm?\n"))

bill = 0

if height >= 120:
    print("YAY! You can ride the rollercoaster!")
    age = int(input("How old are you?\n"))
    if age < 12:
        print("The children's ticket price is £5.")
        bill = 5
    elif age <= 18:
        print("The teenager's ticket price is £7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everythig's going to be okay. Have a free ride on us!")
    else:
        print("The adult's ticket price is £12.")
        bill = 12

    wants_photo = input(
        "Would you like to purchase a picture for £3? Type 'Y' for yes and 'N' for no.")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final total ticket price is £{bill}.")
    else:
        print(f"Okay! Your final bill is £{bill}")

else:
    print("UNLUCKY! You are too short to ride the rollercoaster!")
