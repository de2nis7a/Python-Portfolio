# FILE: area_of_circle.py
# CONCEPT: Geometry and Math Constants
# DEMONSTRATES: Calculating the area of a circle using exponentiation and 'math.pi'.

import math

def area_of_circle():
    radius = int(input("The radius of circle is: "))
    # Area = pi * radius^2
    print(f"The circle's area is: {math.pi * radius ** 2}")
