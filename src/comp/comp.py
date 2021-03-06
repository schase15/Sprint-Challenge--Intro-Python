# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]


# for ease of working, put list of names and ages into seperate lists

# List of names
names = []

for i in range(len(humans)):
    names.append(humans[i].name)

# List of ages
ages = []

for i in range(len(humans)):
    ages.append(humans[i].age)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")

a = [name for name in names if name.startswith("D")]
print(a)


# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")

b = [name for name in names if name.endswith('e')]
print(b)


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")

c = [name for name in names if name.startswith("C") or name.startswith("D") or name.startswith("E") or name.startswith("F") or name.startswith("G")]
print(c)


# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")

d = [age + 10 for age in ages]
print(d)


# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")

e = [f"{human.name}-{human.age}" for human in humans]
print(e)


# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if 26 < human.age < 33 ]
print(f)


# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(old_human.name.upper(), old_human.age +5) for old_human in humans]
print(g)


# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(age) for age in ages]
print(h)
