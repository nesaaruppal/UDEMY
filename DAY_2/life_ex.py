print("Find out how much life you have left!")

age = input("Enter your age:\n")

age_as_int = int(age)

years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(
    f"You have {days_left} days, {weeks_left} weeks and {months_left} months remaining!")
