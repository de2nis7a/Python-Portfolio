# FILE: average_speed_calculator.py
# CONCEPT: Unit Conversion Logic
# DEMONSTRATES: Converting composite units (km+m and hours+min) into a single base unit 
#               before calculating speed (distance/time).

def speed_calculator():
    kilometers = int(input("The distance travelled in kilometers: "))
    meters = int(input("The additional distance in meters: "))
    total_distance = kilometers + (meters / 1000)
    
    hours = int(input("The duration of the journey in hours: "))
    minutes = int(input("The additional minutes of the journey: "))
    total_duration = hours + (minutes / 60)
    
    average_speed = total_distance / total_duration
    print(f"The average speed is {average_speed:.2f} km/h")
