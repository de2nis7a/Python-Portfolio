# FILE: interactive_distance_calculator_v2.py
# CONCEPT: Modular Programming and External I/O
# DEMONSTRATES: Integration of a mathematical function (distance_between_points)
# with an external I/O system (graphix Window) to create an interactive tool.
# NOTE: This file requires the distance_between_points function to be available 
# (e.g., from Math_and_Geometric_Calculations/distance_calculator_module.py).

from graphix import Window, Point, Text
import math

def distance_between_points(p1,p2):
    """Calculates the distance between two points (p1 and p2) using the distance formula."""
    return math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)

def distance_calculator():
    """Allows user to click two points and displays the calculated distance."""
    win = Window("Distance Calculator", 500, 500)
    question = Text(Point(250, 50) , "Click on two locations of the window")
    question.draw(win)
    
    p1 = win.get_mouse()
    p2 = win.get_mouse()
    
    distance = distance_between_points(p1, p2)
    distance = f"Distance: {distance:.2f}"
    
    question.text = distance
    
    win.get_mouse()
    win.close()
    
# distance_calculator()
