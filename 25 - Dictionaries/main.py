# dictionary = collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Bejing",
            "Russia": "Moscow"}

# print(dir(capitals)) # attributes and methods of a dictionary
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"}) # insert new key:value pair or update current one
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") # removes key:value pair
# capitals.popitem() # removes most recent key:value pair
# capitals.clear() # clears dictionary

# keys = capitals.keys()
# for key in keys:
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)

items = capitals.items() # returns a 2d list
for key, value in items:
    print(f"{key}: {value}")