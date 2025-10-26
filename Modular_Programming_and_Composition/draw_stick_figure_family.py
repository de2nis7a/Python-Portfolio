# FILE: draw_stick_figure_family.py
# CONCEPT: Modular Programming and Function Composition (Graphics)
# DEMONSTRATES: Reusability of a drawing function (draw_stick_figure) with different 
# parameters (position and size) to create a complex scene (a family).
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Point, Line, Circle

def draw_stick_figure(win, position, size):
    """Draws a stick figure scaled by 'size' and positioned at 'position'."""
    head = Circle(position, size)
    head.draw(win)
    
    body_start = Point(position.x, position.y + size)
    body_end = Point(position.x, position.y + 3 * size)
    body = Line(body_start, body_end)
    body.draw(win)
    
    # Hands (simplified relative to size)
    hands = Line(Point(position.x - size , position.y + size + 10), Point(position.x + size, position.y + size + 10))
    hands.draw(win)
    
    # Legs
    leg_one = Line(body_end, Point(body_end.x - size, body_end.y + size))
    leg_two = Line(body_end, Point(body_end.x + size, body_end.y + size))
    leg_one.draw(win)
    leg_two.draw(win)


def draw_stick_figure_family():
    """Draws five stick figures of varying sizes to represent a family."""
    win = Window("Stick Figure Family", 800, 800)
    
    # Draw figures with decreasing size, showing scale modulation
    draw_stick_figure(win, Point(100, 300), 70)
    draw_stick_figure(win, Point(250, 300), 65)
    draw_stick_figure(win, Point(400, 300), 55)
    draw_stick_figure(win, Point(550, 300), 50)
    draw_stick_figure(win, Point(700, 300), 45)
    
    win.get_mouse()
    win.close()
    
# draw_stick_figure_family()
