# FILE: rainfall_unit_converter.py
# CONCEPT: File I/O and Unit Conversion
# DEMONSTRATES: Reading and splitting structured data, performing a unit conversion (mm to inches, 1 inch = 25.4 mm), 
#               and controlling output precision.

def rainfall_in_inches():
    
    try:
        with open("rainfall.txt", "r") as input_file:
            lines = input_file.readlines()
            for line in lines:
                city, rainfall = line.split()
                rainfall = int(rainfall)
                # Conversion formula (mm to inches)
                rainfall_inches = rainfall / 25.4 
                print(f"{city:<15} {rainfall_inches:.2f} inches")
                
    except FileNotFoundError:
        print("Error: rainfall.txt not found.")
