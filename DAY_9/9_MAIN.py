# DICTIONARIES
# Key : Value

# {"Bug": Value (description of what a bug is.)}

# Multiple values in your dictionary
# {"Bug" : Value,
# "Function" : Value,
# "Loop": Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# list[9]

# Index using the KEY
print(programming_dictionary["Bug"])
print(programming_dictionary)

# Add a new entry
programming_dictionary["Loop"] = "The definition of a loop!"
empty_dictionary = {}

# Wipe existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Editing Values
programming_dictionary["Bug"] = "An animal."
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
# You only get the Key and not the Value
