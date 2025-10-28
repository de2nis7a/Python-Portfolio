# FILE: draw_centered_rectangle.py
# CONCEPT: Centering and Dynamic Coordinate Calculation
# DEMONSTRATES: Calculating the top-left starting point of a shape based on the 
# window size (400x400) and user-defined width/height to ensure the shape is centered.

from graphix import Window, Rectangle, Point

def draw_rectangle():
    win = Window("Centered Rectangle", 400, 400)
    
    # Get dynamic input for dimensions
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    
    # Calculate starting coordinates to center the rectangle in a 400x400 window
    x_left = (400 - width) // 2
    y_top = (400 - height) // 2
    
    # Define the rectangle using the calculated top-left point and the bottom-right point
    rect = Rectangle(Point(x_left, y_top), Point(x_left + width, y_top + height))
    rect.draw(win)
    
    win.get_mouse()
    win.close()
