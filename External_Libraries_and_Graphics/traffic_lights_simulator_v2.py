# FILE: traffic_lights_simulator_v2.py
# CONCEPT: Graphics, While Loop, and Time Control
# DEMONSTRATES: Using a while True loop with time.sleep() to create a simple, sequential 
# animation (traffic light cycle) by redrawing and changing colors.
# NOTE: This file depends on the 'graphix' library.

from graphix import Window, Circle, Point, Text
import time

def traffic_lights():
    """Simulates a basic sequence of traffic lights (Red-Amber, Green, Amber, Red)."""
    win = Window("Traffic Lights", 200, 200)
    
    # Initialize light positions
    red = Circle(Point(100, 50), 20)
    amber = Circle(Point(100, 100), 20)
    green = Circle(Point(100, 150), 20)
    
    # Draw initial state (Red On)
    red.fill_colour = "red"
    amber.fill_colour = "black"
    green.fill_colour = "black"
    
    red.draw(win)
    amber.draw(win)
    green.draw(win)
    
    while True:
        # 1. Red + Amber (Prepare to go)
        red.fill_colour = "red"
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1.00)
        
        # 2. Green
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(1.00)
        
        # 3. Amber (Prepare to stop)
        red.fill_colour = "black"
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1.00)
        
        # 4. Red (Stop)
        red.fill_colour = "red"
        amber.fill_colour = "black"
        green.fill_colour = "black"
        time.sleep(1.00)
        
    win.get_mouse() # Keep window open after loop (unreachable in while True)
    win.close()
