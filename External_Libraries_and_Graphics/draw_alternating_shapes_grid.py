# FILE: draw_alternating_shapes_grid.py
# CONCEPT: Advanced Conditional Grid Drawing (Composition and Checkerboard Logic)
# DEMONSTRATES: Using a single pair of nested loops to draw two different shapes 
# (Rectangle and Circle) and two different colors based on the checkerboard logic (i+j)%2.
from graphix import Window, Circle, Point, Rectangle

# Constants (Assumed based on previous code)
WIN_SIZE = 500
WIDTH = 100
HEIGHT = 100
RADIUS = 50

# --- Helper Functions ---
def draw_rectangle(win, p1, p2, colour):
    rect = Rectangle(p1,p2)
    rect.fill_colour = colour
    rect.draw(win)

def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
# --- Main Drawing Logic ---
def draw_alternating_shapes(win, colour1, colour2):
    for i in range(5):
        for j in range(5):
            # Coordinates for Rectangle
            p1 = Point(j * WIDTH, i * HEIGHT)
            p2 = Point((j + 1) * WIDTH, (i + 1) * HEIGHT)
            
            # Center for Circle
            center = Point(j * WIDTH + RADIUS, i * HEIGHT + RADIUS)
            
            # Checkerboard logic: Alternating between Rectangle (color1) and Circle (color2)
            if (i + j) % 2 == 0:
                draw_rectangle(win, p1, p2, colour1)
            else:
                draw_circle(win, center, RADIUS, colour2)

def main():
    colour1 = input("Enter the color for rectangles: ")
    colour2 = input("Enter the color for circles: ")
    win = Window("Alternating Shapes", WIN_SIZE, WIN_SIZE)
    draw_alternating_shapes(win, colour1, colour2)
    win.get_mouse() 
    win.close()
