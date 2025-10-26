# FILE: temp_converter_loop.py
# CONCEPT: Modular Conversion Loop and Flag Control
# DEMONSTRATES: Creating a reusable loop for continuous temperature conversions, 
# controlled by a user input flag, and calling external conversion functions.

# Helper functions are defined internally for file independence.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def temperature_converter():
    """Allows user to perform multiple temperature conversions until they choose to stop."""
    flag = True
    while flag:
        temperature = float(input("The temperature is: "))
        way = input("Which way?(f-c / c-f)")
        
        if way == "f-c":
            d = fahrenheit_to_celsius(temperature)
        elif way == "c-f":
            d = celsius_to_fahrenheit(temperature)
            
        print(f"The converted temperature is: {d:.2f}")
        
        new = input("Convert a new one? (y/n) ")
        if new == "n":
           flag = False
           
# temperature_converter()
