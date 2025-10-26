# FILE: distance_calculator_module.py
# CONCEPT: Geometric Formula Implementation (Distance)
# DEMONSTRATES: Implementing the mathematical formula for calculating the distance 
# between two points. This function is designed to be reusable (modular).

import math

# Requires Point object from a graphics library or defined class, 
# but uses mathematical logic.
# Assume p1 and p2 have attributes .x and .y
def distance_between_points(p1,p2):
    """Calculates the distance between two points (p1 and p2) using the distance formula."""
    distance = math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)
    return distance

# Note: The distance_calculator and draw_four_pairs_of_brown_eyes functions 
# which use this are placed in a different folder (Modular_Programming) as they involve graphics.
