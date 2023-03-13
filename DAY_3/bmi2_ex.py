print("Welcome to the BMI calculator!")

height = float(input("How tall are you in metres?\n"))
weight = float(input("What is your weight in kg?\n"))

bmi = round(weight / (height**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}.You are obese.")
else:
    print(f"Your BMI is {bmi}.You are clinically obese.")
