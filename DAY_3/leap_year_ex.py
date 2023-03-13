print("Work out which years are Leap Years!")

year = int(input("Which year would you like to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year!")
        else:
            print("NOT a Leap Year!")
    else:
        print("Leap Year!")
else:
    print("NOT a Leap Year!")
