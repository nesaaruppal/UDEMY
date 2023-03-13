import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(",")

num_people = len(names)

random_choice = random.randint(0, num_people - 1)
person_pays = names[random_choice]

print(person_pays + " is going to buy the meal today.")

# random.choice(x)
# person_who_pays = random.choice(names)
