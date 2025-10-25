# FILE: sine_and_cosine_calculator.py
# CONCEPT: Trigonometric Functions
# DEMONSTRATES: Using 'math.radians', 'math.sin', and 'math.cos' to calculate trigonometric 
#               values from user input in degrees.

import math

def sine_and_cosine():
    angle = float(input("Enter an angle in degrees: "))
    angle_in_radians = math.radians(angle)  # converts degrees to radians
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    print("Sine of the angle:", round(sine_value, 2))
    print("Cosine of the angle:", round(cosine_value, 2))
