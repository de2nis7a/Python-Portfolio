# FILE: draw_user_defined_circle.py
# CONCEPT: External Library Usage - Simple Graphics and User Input
# DEMONSTRATES: Drawing a circle whose radius is determined by user input. 
# NOTE: Requires the 'graphix' library to be installed and run in a compatible environment.

from graphix import Window, Circle, Point

def draw_circle():
    win = Window()
    radius = int(input("The radius is:"))
    centre = Point(200,200)
    circle = Circle(centre, radius)
    circle.draw(win)
