# FILE: draw_custom_polygon_shape.py
# CONCEPT: User Input to Create Complex Shapes (Polygons)
# DEMONSTRATES: Using a 'for' loop and user input to collect multiple Point objects, 
# storing them in a list, and then passing that list to the Polygon constructor.

from graphix import Window, Point, Polygon

def draw_custom_shape():
    win = Window("Custom Shape", 400, 400)
    points = []
    
    # Collect 5 points from user input
    for i in range(5):  
        x = int(input(f"Enter x-coordinate for point {i + 1}: "))
        y = int(input(f"Enter y-coordinate for point {i + 1}: "))
        points.append(Point(x, y))  # Store the points in a list

    # Create the Polygon from the list of points
    custom_shape = Polygon(points)
    custom_shape.fill_colour = "orange"  
    custom_shape.draw(win)  
    
    win.get_mouse()  
    win.close()
