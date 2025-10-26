# FILE: draw_colorful_spiral.py
# CONCEPT: Loops and Dynamic Drawing
# DEMONSTRATES: Using a 'for' loop to iterate and change the properties (position, 
# radius, and color) of a shape (Circle), creating a dynamic visual pattern.
from graphix import Window, Circle, Point

def draw_spiral():
    win = Window("Colorful Spirals", 400, 400)
    
    # Iterate to draw 10 circles, changing radius and position slightly each time
    for i in range(10):
        # Position is offset by 'i * 10' on the x-axis
        circle = Circle(Point(200 + (i * 10), 200), 10 + (i * 5))
        
        # Change color based on whether 'i' is even or odd
        if i % 2 == 0:
            circle.fill_colour = "blue"        
        else:
            circle.fill_colour = "green"
            
        circle.draw(win)
        
    win.get_mouse()
    win.close()
