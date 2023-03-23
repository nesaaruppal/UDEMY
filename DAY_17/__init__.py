class User:

    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        # Default values --> set, but do not provide within the brackets
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("Nesaar Uppal", "001")
user_2 = User("James Bond", "007")
print(user_1.name)
print(user_2.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# class Car:
#    def enter_race_mode():
#        self.seats = 2
