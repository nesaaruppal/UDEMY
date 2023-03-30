####### CLASS INHERITANCE ######

# Normal Class
# class Fish:
# def __init__(self):

# Inheritance
# class Fish(Animal):
# def __init__(self):
# super().__init__()

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish:
    def swim(self):
        print("Moving in Water")


nemo = Fish()
nemo.swim()


######## CLASS INHERITANCE #######
# SUPER().

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Inhale, Exhale!")

    def breathe(self):
        super().breathe()
        print("Under water!")


nemo_2 = Fish()
nemo_2.swim()
nemo_2.breathe()
print(nemo_2.num_eyes)
