# for number in range(a, b):
# print number

for number in range(1, 10):
    print(number)

# NOT PRINTING 10
for number in range(1, 11):
    print(number)

# Change the step-size
for number in range(1, 11, 3):
    print(number)


total = 0
for number in range(1, 101):
    total += number
print(total)
