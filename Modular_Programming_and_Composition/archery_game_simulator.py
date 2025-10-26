# FILE: archery_game_simulator.py
# CONCEPT: Modular Programming, Game Logic, and Graphics Integration
# DEMONSTRATES: Using geometry and conditional logic (if/elif) to calculate score 
# based on distance from the center (bullseye).

from graphix import Window, Circle, Point, Text
import random
import math

# Define required helper functions inline for independence (draw_circle)
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)

# Define the necessary math function (distance_between_points)
def distance_between_points(p1,p2):
    return math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)

def archery_game():
    """Simulates a target shooting game, calculating score based on mouse clicks."""
    win = Window("Archery Game", 400, 400)
    
    # Draw Target Rings (Center: 200, 200)
    draw_circle(win, Point(200, 200), 200, "blue")    # Outer ring (200 radius)
    draw_circle(win, Point(200, 200), 100, "red")     # Middle ring (100 radius)
    draw_circle(win, Point(200, 200), 50, "yellow")    # Bullseye (50 radius)
    
    target_center = Point(200, 200)
    total_score = 0
    
    print("Click 5 times on the target to shoot.")
    
    for i in range(5):
        firing_point = win.get_mouse()
        
        # Draw the hit mark
        hit_mark = Circle(firing_point, 3)
        hit_mark.fill_colour = "black"
        hit_mark.draw(win)
        
        # Calculate distance from the center
        dist = distance_between_points(firing_point, target_center)
        
        # Scoring logic
        if dist <= 50:
            total_score += 10
        elif dist <= 100:
            total_score += 5
        elif dist <= 200: # Max radius is 200
            total_score += 2
            
    # Display final score
    score_message = Text(Point(200, 50), f"Final Score: {total_score}")
    score_message.size = 20
    score_message.draw(win)
    
    win.get_mouse()
    win.close()
    
# archery_game()
