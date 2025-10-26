# FILE: draw_interactive_circles.py
# CONCEPT: Infinite Loop and Mouse Interaction
# DEMONSTRATES: Using a 'while True' loop to continuously check for mouse clicks (get_mouse) 
# and drawing a new shape (Circle) at the clicked location.
from graphix import Window, Circle, Point

def interactive_circle_drawing():
    win = Window("Draw Circles on Click", 400, 400)
    
    # Loop continuously until the window is manually closed
    while True:
        click = win.get_mouse()  # Pauses execution, waits for a click, and returns the Point object
        
        # Create a circle centered at the click point
        circle = Circle(click, 20)  
        circle.fill_colour = "purple"   
        circle.draw(win) 
