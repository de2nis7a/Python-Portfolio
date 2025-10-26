# FILE: graphix_hello_message_v2.py
# CONCEPT: External Library Initialization and Text Output
# DEMONSTRATES: Setting up a graphics window, drawing text at a specific coordinate, 
# and waiting for mouse input before closing.
from graphix import Window, Point, Text

def hello_graphix():
    win = Window("Hello Graphix", 400, 400)  # Creates a 400x400 window with a title
    message = Text(Point(200, 200), "Hello, Graphix!") # Centers the text
    message.draw(win)
    win.get_mouse()  # Waits for user interaction
    win.close()
