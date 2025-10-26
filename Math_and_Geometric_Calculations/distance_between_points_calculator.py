# FILE: distance_between_points_calculator.py
# CONCEPT: Geometric Calculation (Distance Formula)
# DEMONSTRATES: Using the 'math.sqrt' function to calculate the distance between 
# two points in a 2D Cartesian coordinate system based on user input.
import math

def distance_between_points():
     x = int(input("First point x: "))
     y = int(input("First point y: "))
     x_two = int(input("Second point x: "))
     y_two = int(input("Second point y: "))
     
     # Calculate distance using the distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
     distance = math.sqrt((x_two - x) ** 2 + (y_two - y) ** 2)
     
     print(f"The distance is {distance:.2f}")
