print("Welcome to the tip calculator!")

bill = input("What was the total bill?\n$")
bill_as_float = float(bill)

tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
tip_as_int = int(tip)
tip_added = (bill_as_float/100) * tip_as_int

split = input("How many people are splitting the bill?\n")
num_people = int(split)

bill_with_tip = bill_as_float + tip_added

final_bill = bill_with_tip / num_people
round_bill = round(final_bill, 2)

print(f"Each person should pay: ${round_bill}.")
