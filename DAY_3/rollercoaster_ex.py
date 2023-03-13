print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
age = int(input("How old are you?\n"))

if height >= 120:
    print("Yay you can ride the rollercoaster!")
    if age < 12:
        print("The ticket price is $5.")
    elif age <= 18:
        print("The ticket price is $7")
    else:
        print("The ticket price is $12.")
else:
    print("Unlucky! You're too short!")
