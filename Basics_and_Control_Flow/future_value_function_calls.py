# FILE: future_value_function_calls.py
# CONCEPT: Function Calls and Formatting
# DEMONSTRATES: Splitting a complex task (compound interest) into smaller functions 
# and formatting the final currency output.

def calc_future_value(amount, years):
    """Calculates the future value of an investment using a fixed interest rate."""
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount

def future_value():
    """Handles user input and displays the calculated future value."""
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)
    
# future_value()
