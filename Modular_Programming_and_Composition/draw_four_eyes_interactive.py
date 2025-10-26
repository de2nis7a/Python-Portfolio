# FILE: draw_four_eyes_interactive.py
# CONCEPT: Modular Programming and Repetitive Graphics
# DEMONSTRATES: Using a loop to repeatedly prompt the user for input and calling a modular
# eye-drawing function to create a complex scene with multiple pairs of eyes.
# NOTE: Requires the draw_brown_eye function to be available (e.g., from draw_brown_eye_module.py).

from graphix import Window, Point
# Assuming draw_brown_eye is available
# from draw_brown_eye_module import draw_brown_eye, distance_between_points 
# ... and distance_between_points is available

# Define required helper functions inline for independence (draw_coloured_eye)
def draw_coloured_eye(win, centre, radius, colour):
    circle_one = Circle(centre, radius)
    circle_two = Circle(centre, radius // 2)
    circle_three = Circle(centre, radius //3)
    circle_one.fill_colour = "white"
    circle_two.fill_colour = colour
    circle_three.fill_colour = "black"
    circle_one.draw(win)
    circle_two.draw(win)
    circle_three.draw(win)

# Define the eye module function that uses the helper
def draw_brown_eye(win, centre, radius):
    draw_coloured_eye(win, centre, radius, "brown")

# Define the necessary math function (distance_between_points)
import math
def distance_between_points(p1,p2):
    return math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)


def draw_four_pairs_of_brown_eyes():
    """Draws four pairs of eyes where the size is determined by user clicks."""
    win = Window("Four Interactive Eyes", 800, 800)
    
    print("Click center, then circumference for the first eye in each pair.")
    
    for i in range(4):
       centre = win.get_mouse()
       circumference = win.get_mouse()
       
       # Calculate radius based on the distance between the two clicks
       radius = int(distance_between_points(centre, circumference))
       
       # Calculate the center for the second eye (placed to the right)
       right_eye_center = Point(int(centre.x + radius * 3.5), centre.y)
       
       draw_brown_eye(win, centre, radius)
       draw_brown_eye(win, right_eye_center, radius)
       
    win.get_mouse()
    win.close()

# draw_four_pairs_of_brown_eyes()
