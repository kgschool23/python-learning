# colleciton = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# ------ Lists ------

# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[2]) # prints banana
# print(dir(fruits)) # lists all methods
# print(help(fruits)) # lists what each method does
# print(len(fruits)) # 4
# print("pineapple" in fruits) # returns Boolean

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort() # sorts list in alphabetical order (strings)
# fruits.reverse() # reverses in order of which list elemetns are placed, not alphabetically, unless paired with sort()
# print(fruits.index("coconut")) # returns index number of specified element
# print(fruits.count("banana")) # returns number of occurrences of specified element

# for fruit in fruits:
#     print(fruit)

# print(fruits)

# ------ Sets ------

# fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple in fruits")

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() removes whatever element is first (random)
# fruits.clear()

# print(fruits) # DIFFERENT order every time


# ------ Tuples ------
# fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("coconut")))

# for fruit in fruits:
#     print(fruit)
