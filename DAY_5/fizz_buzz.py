print("Let's play FIZZ BUZZ!")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZ BUZZ!")
    elif number % 5 == 0:
        print("FIZZ!")
    elif number % 3 == 0:
        print("BUZZ!")
    else:
        print(number)
