###### Create your own Class ######

class User:
    # CONSTRUCTOR
    def __init__(self):
        print("Nesaar Uppal")


user_1 = User()
user_1.id = "001"
user_1.username = "Nesaar"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Uppal"

print(user_2.id)


class Car:
    def __init__(self, seats):
        self.seats = seats


# Means that the car has 5 seats because of the data passed through
# Same as creating the object first
# Then doing my_car.seats = 5
my_car = Car(5)
