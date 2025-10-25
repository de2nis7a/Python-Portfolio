# FILE: travel_statistics.py
# CONCEPT: Simple Arithmetic Simulation
# DEMONSTRATES: Calculating derived metrics (distance and fuel consumption) from base inputs.

def travel_statistics():
    average_speed = int(input("The average speed is: "))
    duration = int(input("The duration is: "))
    
    distance = average_speed * duration
    # Assuming 5 units of distance per 1 unit of fuel (e.g., 5 km/liter)
    fuel = distance / 5
    
    print(f"The distance is {distance} and the amount of fuel is {fuel}")
