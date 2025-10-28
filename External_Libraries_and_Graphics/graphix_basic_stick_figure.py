# FILE: graphix_basic_stick_figure.py
# CONCEPT: External Library Usage - Drawing Multiple Shapes
# DEMONSTRATES: Drawing two distinct shapes (Circle for head, Line for body) to create a simple composite figure.

from graphix import Window, Circle, Point , Line

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
