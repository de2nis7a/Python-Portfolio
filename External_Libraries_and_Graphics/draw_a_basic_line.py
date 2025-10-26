# FILE: draw_a_basic_line.py
# CONCEPT: Basic Shape Drawing
# DEMONSTRATES: Setting up a graphics window and drawing a static line segment 
# between two predefined coordinates (Points). Waits for user input before closing.
from graphix import Window, Point, Line

def draw_line():
    win = Window("Draw a Line", 400, 400)
    
    # Create and draw the line object
    line = Line(Point(50, 50), Point(350, 350))
    line.draw(win)
    
    win.get_mouse() # Wait for user interaction
    win.close()
