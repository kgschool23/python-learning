import math

# Exercise 3 - Find hypotenuse of a right triangle. 

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse is: {round(c)}")