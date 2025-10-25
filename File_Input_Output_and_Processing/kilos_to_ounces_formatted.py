# FILE: kilos_to_ounces_formatted.py
# CONCEPT: Basic I/O and Output Formatting
# DEMONSTRATES: Unit conversion with controlled floating-point output precision (`.2f`).

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print(f" {kilos:.2f} kilos is equal to {ounces:.2f} ounces")
