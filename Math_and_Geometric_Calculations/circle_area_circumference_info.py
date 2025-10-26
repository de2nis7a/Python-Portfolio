# FILE: circle_area_circumference_info.py
# CONCEPT: Function Composition for Geometry
# DEMONSTRATES: Using separate helper functions for area and circumference and combining 
# the results in a main function for output.

import math

def area_of_circle(radius):
    """Calculates the area of a circle."""
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    """Calculates the circumference of a circle."""
    return math.pi * radius * 2

def circle_info():
    """Gets radius from user and prints calculated area and circumference."""
    radius = int(input("The radius is: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    # Output formatted to 3 decimal places
    print(f"The area is {area:.3f} and the circumference is {circumference:.3f}")

# circle_info()
