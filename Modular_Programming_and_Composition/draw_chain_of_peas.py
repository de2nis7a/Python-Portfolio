# FILE: draw_chain_of_peas.py
# CONCEPT: Graphics Loop and Dynamic Window Sizing
# DEMONSTRATES: Using a 'for' loop to draw a sequence of objects and calculating 
# the required window size based on the user's input quantity.
# NOTE: This file depends on the 'graphix' library.

from graphix import Window, Circle, Point

def peas_in_a_pod():
    """Draws a horizontal chain of green circles based on user input."""
    number = int(input("The number of peas is: "))
    
    # Calculate window size based on number of peas (each circle is 100 wide)
    win = Window("Peas in a Pod", number * 100, 100)
    
    p = Point(50, 50)
    radius = 50
    
    for i in range(number):
        circle = Circle(p, radius)
        circle.fill_colour = "green"
        circle.draw(win)
        
        # Move the center point for the next pea
        p.move(100, 0)
        
    win.get_mouse()
    win.close()
    
# peas_in_a_pod()
