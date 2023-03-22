# SCOPE   Local vs Global


##### GLOBAL SCOPE #####
enemies = 1

####### LOCAL SCOPE #######


def increase_enemies():
    enemies = 2
    # Only valid within this particular function
    print(f"Enemies inside the function {enemies}.")


increase_enemies()
print(f"Enemies outside the function {enemies}")
