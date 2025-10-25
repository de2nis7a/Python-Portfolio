# FILE: slope_of_line.py
# CONCEPT: Geometry and Error Handling
# DEMONSTRATES: Implementing the slope formula and conditional logic (if/else) to prevent 
#               division by zero (vertical line).

def slope_of_line():
    x_1 = int(input("First point's first coordinate is: "))
    y_1 = int(input("First point's second coordinate is: "))
    x_2 = int(input("Second point's first coordinate is: "))
    y_2 = int(input("Second point's second coordinate is: "))
    
    delta_x = x_2 - x_1
    
    if delta_x == 0:
        print("The slope is undefined (vertical line).")
    else:
        slope = (y_2 - y_1) / delta_x
        print(f"The slope is: {slope}")
