# FILE: kilos_to_ounces.py
# CONCEPT: Input/Output and Float Conversion
# DEMONSTRATES: Taking user input (kilos), converting to float, and performing a unit conversion.

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)