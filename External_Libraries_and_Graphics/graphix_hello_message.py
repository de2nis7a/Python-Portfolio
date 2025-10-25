# FILE: graphix_hello_message.py
# CONCEPT: External Library Usage - Simple Display
# DEMONSTRATES: Basic initialization of the graphical environment (Window) and displaying static text.
# NOTE: Requires the 'graphix' library to be installed.

from graphix import Window, Point, Text

def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)
