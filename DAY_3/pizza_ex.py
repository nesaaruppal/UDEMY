print("Welcome to your Pizza Order App!")
size = input("What size pizza would you like? Type 'S' for small which is £15, 'M' for medium which is £20 and 'L' for large which is £25:\n")
add_pepperoni = input(
    "Would you like to add pepperoni to your pizza? For Small pizza's this is £3 and for Medium or Large this is £3. Type 'Y' for yes and 'N' for no:\n")
extra_cheese = input(
    "Would you like extra cheese for £1? Type 'Y' for yes and 'N' for no:\n")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
            if extra_cheese == "Y":
                bill += 1
            else:
                bill == bill

print(f"Your final bill is: £{bill}")
