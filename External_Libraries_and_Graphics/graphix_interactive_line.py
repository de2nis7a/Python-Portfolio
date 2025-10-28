# FILE: graphix_interactive_line.py
# CONCEPT: External Library Usage - User Interaction (Mouse Input)
# DEMONSTRATES: Capturing mouse clicks (I/O) to define the coordinates of points and dynamically drawing a line between them.
from graphix import Window, Point, Text, Line

def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    
    p1 = win.get_mouse() # Captures first click
    
    message.text = "click on second point"
    p2 = win.get_mouse() # Captures second click
    
    line = Line(p1, p2)
    line.draw(win)
    
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()
