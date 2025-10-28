# FILE: overlapping_shapes_demo.py
# CONCEPT: External Library Usage - Shape Overlap and Color
# DEMONSTRATES: Drawing and layering different geometric shapes (Rectangle and Circle) 
# and setting their fill colors to show rendering order.

from graphix import Window, Point, Circle, Rectangle

def mystery_1():
    win = Window()
    
    # Draw a blue rectangle first
    rectangle = Rectangle(Point(100, 100), Point(200,200))
    rectangle.fill_colour = "blue"
    rectangle.draw(win)
    
    # Draw a red circle, which will partially overlap the rectangle
    circle = Circle(Point(200, 200), 100)
    circle.fill_colour = "red"
    circle.draw(win)
    
# Call the function to run the demo (optional, can be called in a main block)
# mystery_1()
