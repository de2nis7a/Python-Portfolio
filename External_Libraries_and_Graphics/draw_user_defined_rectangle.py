# FILE: draw_user_defined_rectangle.py
# CONCEPT: External Library Usage - Geometric Calculation and Drawing
# DEMONSTRATES: Calculating coordinates based on user input (height/width) 
#               to center a rectangle on the screen.
# NOTE: Requires the 'graphix' library to be installed and run in a compatible environment.

from graphix import Window, Point , Rectangle

def draw_rectangle():
    win=Window()
    height = int(input("The height is:"))
    width = int(input("The width is:"))
    
    # Assuming window size is 400x400 for centering calculation
    
    # Calculate top-left corner (p1) to center the rectangle
    center_x = 200
    center_y = 200
    
    x_start = center_x - (width / 2)
    y_start = center_y - (height / 2)
    
    p1 = Point(x_start, y_start)
    
    # Calculate bottom-right corner (p2)
    x_end = x_start + width
    y_end = y_start + height
    
    p2 = Point(x_end, y_end)
    
    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)
