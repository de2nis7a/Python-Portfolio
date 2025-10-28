# FILE: draw_stick_figure.py
# CONCEPT: External Library Usage - Basic Graphics Programming (graphix)
# DEMONSTRATES: Using the 'graphix' library to draw multiple basic shapes (Circle and Line) 
#               to create a composite figure.

from graphix import Window, Circle, Point , Line

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arms = Line(Point(120,180), Point(280,180))
    arms.draw(win)
    leg_1 = Line(Point(200,240),Point(120,280))
    leg_1.draw(win)
    leg_2 = Line(Point(200,240),Point(280,280))
    leg_2.draw(win)
