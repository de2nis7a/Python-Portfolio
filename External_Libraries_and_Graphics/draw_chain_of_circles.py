# FILE: draw_chain_of_circles.py
# CONCEPT: External Library Usage - Graphics and Control Flow
# DEMONSTRATES: Using a 'for' loop to draw multiple geometric shapes (Circles) in a series,
# with centers calculated based on the loop counter (i) and user input (mouse click).

from graphix import Window, Point, Circle

def draw_chain_of_circles():
    win = Window ("Chain of Circles", 400, 600)
    radius= 20
    
    # Get the starting point of the chain
    print("Click to define the starting point of the circle chain.")
    click = win.get_mouse() 
    
    # Draw 10 circles vertically
    for i in range(10):   
       # Calculate the center point based on the initial click and the loop index (i)
       centre = Point(click.x, click.y + i * (radius * 2)) # Adjusted calculation for spacing
       circle = Circle(centre, radius)
       circle.draw(win)
       circle.outline_colour = "blue"
       
    # Keep the window open until the user clicks again
    print("Drawing complete. Click to close window.")
    win.get_mouse()
    win.close()
