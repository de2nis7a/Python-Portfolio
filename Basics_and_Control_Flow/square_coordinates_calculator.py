# FILE: square_coordinates_calculator.py
# CONCEPT: Basic I/O and Coordinate Range Calculation
# DEMONSTRATES: Taking user input for the top-left corner and defining the X and Y 
# boundaries (range) of a fixed-size shape (100x100 units).

def rectangle_boundaries():
    x = int(input("Top-left x: "))
    y = int(input("Top-left y: "))
    
    # Print the boundary ranges based on the starting point (x, y)
    print("X range:", x , "to" , x + 100)
    print("Y range:", y , "to" , y + 100)
