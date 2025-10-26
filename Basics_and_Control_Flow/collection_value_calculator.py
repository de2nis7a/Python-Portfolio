# FILE: collection_value_calculator.py
# CONCEPT: Control Flow (Loop for Financial Simulation)
# DEMONSTRATES: Using a 'for' loop to simulate compound growth (appreciation) over a fixed number of years 
# and performing basic arithmetic on floating-point numbers.

def collection_value_calculator():
    print("\nYear\tValue")
    value = int(input("The initial value is: "))
    annual_appreciation_rate = int(input("Annual appreciation rate: "))
    annual_rate = annual_appreciation_rate / 100
    for year in range(1, 11):
        value += value * annual_rate
        #value *= (1 + annual_rate) # Alternative, cleaner calculation
        print(year, "\t$", round(value, 2))
    # Calculate what the final value can buy, demonstrating final output formatting
    print("\nAfter 10 years, your collection could buy", int(value / 60), "new releases at $60 each!")
