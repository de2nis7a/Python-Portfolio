# FILE: compound_interest_calculator.py
# CONCEPT: Control Flow (Loop for Simulation)
# DEMONSTRATES: Using a 'for' loop to simulate a process (compound interest calculation) over multiple iterations.

def future_value():
    initial_amount=float(input("Initial amount is:"))
    years=int(input("Number of years:"))
    # Assuming a fixed 3.5% interest rate applied annually
    for i in range(1 , years+1):
        initial_amount = initial_amount + (3.5 * initial_amount) / 100
    print(initial_amount)