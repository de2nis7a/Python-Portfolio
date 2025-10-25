# FILE: distance_between_points.py
# CONCEPT: Geometry and Math Functions
# DEMONSTRATES: Implementing the distance formula using 'math.sqrt' and exponentiation.

import math

def distance_between_points():
    x_1 = int(input("First point's first coordinate is: "))
    y_1 = int(input("First point's second coordinate is: "))
    x_2 = int(input("Second point's first coordinate is: "))
    y_2 = int(input("Second point's second coordinate is: "))
    
    # Distance formula: sqrt((y2 - y1)^2 + (x2 - x1)^2)
    distance = math.sqrt((y_2 - y_1) ** 2 + (x_2 - x_1) ** 2)
    print(f"The distance between the points is: {distance}")
