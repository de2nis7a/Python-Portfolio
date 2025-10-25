# FILE: circumference_of_circle.py
# CONCEPT: Geometry and Math Constants
# DEMONSTRATES: Basic formula calculation using the 'math.pi' constant.

import math

def circumference_of_circle():
    radius = int(input("The radius of circle is: "))
    # Circumference = 2 * pi * radius
    print(f"Circles's circumference is: {radius * math.pi * 2}")
