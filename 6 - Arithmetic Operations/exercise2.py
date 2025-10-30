import math

# Exercise 2 - Calculate area of a circle

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area)}cm²")