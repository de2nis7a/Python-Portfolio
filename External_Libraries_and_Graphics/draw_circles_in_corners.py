# FILE: draw_circles_in_corners.py
# CONCEPT: Conditional Drawing and Data Structures (Tuples and Lists)
# DEMONSTRATES: Using a list of specific coordinates (tuples) to conditionally draw 
# a shape (Circle) only at predefined locations within a nested loop grid.
from graphix import Window, Circle, Point, Rectangle

# Constants (Assumed based on previous code and context)
SCREEN = 500
TILE = 100
RADIUS = 50

# Helper function definition (Required for standalone functionality)
def draw_rectangle(win, p1, p2, colour):
    rect = Rectangle(p1,p2)
    rect.fill_colour = colour
    rect.draw(win)

def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)

def draw_circles_in_corners():
    win = Window("Circles in Corners", SCREEN, SCREEN)
    
    # Define the coordinates where circles should be drawn (The corners of the grid)
    circle_list = [(0,0), (0, SCREEN - TILE), (SCREEN - TILE, 0), (SCREEN - TILE, SCREEN - TILE)]

    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            p1 = Point(X, Y)
            p2 = Point(X + TILE, Y + TILE)
            # Draw the background grid
            draw_rectangle(win, p1, p2, "blue")
            
            # Conditional Logic: Check if current cell (X, Y) is in the list of corners
            if (X, Y) in circle_list:
                center = Point(X + RADIUS, Y + RADIUS) # Center the circle in the tile
                draw_circle(win, center, RADIUS, "red")
    
    win.get_mouse()
    win.close()
