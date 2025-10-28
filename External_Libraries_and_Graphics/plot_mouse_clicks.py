# FILE: plot_mouse_clicks.py
# CONCEPT: Mouse Interaction and Coordinate Display
# DEMONSTRATES: Using a fixed 'for' loop (10 iterations) to wait for mouse clicks (get_mouse), 
# and displaying the x,y coordinates of each click on the graphics window as a Text object.

from graphix import Window, Point, Text

def plot_clicks():
    win = Window("Plot Clicks", 400, 400)
    
    # Loop 10 times to capture 10 clicks
    for _ in range(10):  
        p = win.get_mouse() # Wait for user click
        
        # Create a text object at the click location showing the coordinates
        location = Text(Point(p.x, p.y), f"({p.x}, {p.y})")  
        location.draw(win)  
        
    win.get_mouse() # Wait for a final click before closing
    win.close()
