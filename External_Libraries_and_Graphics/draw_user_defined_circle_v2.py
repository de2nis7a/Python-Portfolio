# FILE: draw_user_defined_circle_v2.py
# CONCEPT: I/O Applied to Graphics
# DEMONSTRATES: Reading an integer input from the user (radius) and using that 
# value to dynamically define the dimensions of a drawn shape (Circle).
from graphix import Window, Circle, Point

def draw_circle():
    win = Window("Circle Drawer", 400, 400)
    
    # Get dynamic input for the radius
    radius = int(input("Enter the radius of the circle: "))
    
    # Create and draw the circle based on user input
    circle = Circle(Point(200, 200), radius)
    circle.draw(win)
    
    win.get_mouse() # Wait for user interaction
    win.close()
