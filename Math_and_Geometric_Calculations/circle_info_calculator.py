# FILE: circle_info_calculator.py
# CONCEPT: Geometric Calculation and Math Library Usage
# DEMONSTRATES: Calculating both circumference and area of a circle with a fixed radius 
# by using the 'math.pi' constant.
import math

def circle_circumference_and_area():
    # Note: The x and y inputs are not used in the calculation, only the radius is relevant.
    # We keep them here for input demonstration purposes.
    x = int(input("X coordinate of circle: "))
    y = int(input("Y coordinate of circle: "))
    radius = 50
    
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    
    print(f"The circumference is: {circumference:.2f}")
    print(f"The area is: {area:.2f}")
