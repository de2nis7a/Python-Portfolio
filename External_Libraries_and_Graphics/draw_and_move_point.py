# FILE: draw_and_move_point.py
# CONCEPT: Point Object Manipulation
# DEMONSTRATES: Creating a Point object, drawing it to the window (implicitly in graphix), 
# reading user input to pause, and moving the point using the 'move' method.
from graphix import Window, Point

def draw_point():
    win = Window("Draw and Move Point", 400, 400)
    
    # Create the point object
    p = Point(200, 200)  
    
    # Draw implicitly draws the point (or shape created from it)
    # We will use a small circle to make the point visible
    small_circle = Circle(p, 5) # Assuming Circle is available or defined elsewhere
    small_circle.fill_colour = "blue"
    small_circle.draw(win) 
       
    win.get_mouse() # Wait for first click
    
    # Move the point and redraw the circle
    p.move(50, -50)  
    small_circle.undraw()
    small_circle = Circle(p, 5)
    small_circle.fill_colour = "red"
    small_circle.draw(win) 
    
    win.get_mouse() # Wait for second click
    win.close()

# Note: Since the exact 'Point' drawing behavior isn't defined without a shape like Circle, 
# this implementation uses a small Circle to demonstrate drawing and movement accurately.
