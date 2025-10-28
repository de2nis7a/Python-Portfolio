# FILE: circle_info_calculator.py
# CONCEPT: Geometric Calculation and Math Library Usage
# DEMONSTRATES: Calculating both circumference and area of a circle with a fixed radius 
# by using the 'math.pi' constant.

import math

def circle_circumference_and_area():
    
    x = int(input("X coordinate of circle: "))
    y = int(input("Y coordinate of circle: "))
    radius = 50
    
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    print(f"The circumference is: {circumference:.2f}")
    print(f"The area is: {area:.2f}")
