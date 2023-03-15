print("Welcome to the prime number checker!")


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print("NOT A PRIME NUMBER!")
