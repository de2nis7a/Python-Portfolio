# FILE: draw_diagonal_circles.py
# CONCEPT: Conditional Drawing and Diagonal Logic
# DEMONSTRATES: Using the geometric condition (X == Y) inside nested loops to draw 
# shapes (Circles) only along the main diagonal of a grid.

from graphix import Window, Circle, Point, Rectangle

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

def draw_diagonal_circles():
    win = Window("Diagonal Line of Circles", SCREEN, SCREEN)
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            p1 = Point(X, Y)
            p2 = Point(X + TILE, Y + TILE)
            # Draw the background grid
            draw_rectangle(win, p1, p2, "blue")
            
            # Conditional Logic: Draw a circle only if X coordinate equals Y coordinate (main diagonal)
            if X == Y:
                center = Point(X + RADIUS, Y + RADIUS)
                draw_circle(win, center, RADIUS, "red")
    
    win.get_mouse()
    win.close()
