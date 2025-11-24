# iterables = an object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5] # a list is iterable

for number in numbers:
    print(number)

fruits = {"apple", "orange", "banana", "coconut"} # a set is iterable, but not reversible

for fruit in fruits:
    print(fruit)

name = "Spongebob Squarepants"

for character in name:
    print(character, end=" ")

print()

my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")