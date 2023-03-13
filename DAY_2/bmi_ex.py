print("Welcome to your BMI calculator!")

weight = input("Please enter your weight in kg:\n")
height = input("Please enter your height in m:\n")

num_weight = float(weight)
num_height = float(height)

bmi = round(num_weight / (num_height**2))

print(f"Your BMI is {bmi}!")
