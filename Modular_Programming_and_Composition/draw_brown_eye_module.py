# FILE: draw_brown_eye_module.py
# CONCEPT: Modular Programming and Function Composition (Graphics)
# DEMONSTRATES: Breaking down a complex shape (an eye) into multiple modular functions 
# that can be reused and composed into larger scenes (a pair of eyes, or four pairs).
# NOTE: This file depends on a graphics library (graphix).

from graphix import Window, Circle, Point

# Helper function to draw a single circle with color
def draw_circle(centre, radius, colour, win):
    """Draws a single circle with specified parameters."""
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
def draw_brown_eye_in_centre():
    """Draws a single brown eye in the center of the window."""
    win = Window()
    draw_circle(Point(200, 200), 120, "white" , win)
    draw_circle(Point(200, 200), 60, "brown" , win)
    draw_circle(Point(200, 200), 30, "black", win)
    win.get_mouse()
    win.close()
    
def draw_brown_eye(win, centre, radius):
    """Draws a complete brown eye composed of three circles."""
    # Sclera (White) - Full size
    draw_circle(centre, radius, "white", win)
    # Iris (Brown) - Half size
    draw_circle(centre, radius //2, "brown", win)
    # Pupil (Black) - Quarter size
    draw_circle(centre, radius // 4, "black", win)
    

def draw_pair_of_brown_eyes():
    """Composes two calls to draw_brown_eye to create a pair."""
    win = Window("Pair of Eyes", 800, 400)
    left_eye = Point(250,200)
    right_eye = Point (550,200)
    radius = 120
    draw_brown_eye(win, left_eye, radius)
    draw_brown_eye(win, right_eye, radius)
    win.get_mouse()
    win.close()

# Calls for drawing four pairs of eyes (Task 9)
def draw_four_pairs_of_brown_eyes():
    """Draws four pairs of eyes based on user clicks, demonstrating reuse."""
    # Requires distance_between_points from Math_and_Geometric_Calculations/distance_calculator_module.py
    # For now, this function is included here for context, assuming the distance function is available.
    print("Click on 4 pairs of eyes, defining the center and circumference of the first eye in the pair.")
    win = Window("Four pairs of eyes", 800, 800)
    
    for i in range(4):
       print(f"Pair {i+1}: Click center, then circumference for the first eye.")
       centre = win.get_mouse()
       circumference = win.get_mouse()
       
       # This is where the distance_between_points module is needed. 
       # For local run, you'd need to import it or define it here.
       # For portfolio, we document the dependency.
       # distance = distance_between_points(centre, circumference) 
       
       # For demonstration, we'll use a fixed radius calculation based on X coordinates
       radius = abs(circumference.x - centre.x) // 2 
       
       right_eye_center = Point(int(centre.x + radius * 3.5), centre.y) # Spacing logic
       draw_brown_eye(win, centre, radius)
       draw_brown_eye(win, right_eye_center, radius)
       
    win.get_mouse()
    win.close()
