# FILE: order_price_calculator.py
# CONCEPT: Iterative Calculation with Flag Control
# DEMONSTRATES: Calculating a running total price using a flag variable to control 
# the loop and validate positive input values.

def order_price():
    """Calculates the total price of an order iteratively until stopped by user input."""
    flag = True
    price = 0
    while flag:
        unit_price = float(input("Enter the unit price: "))
        quantity = int(input("The quantity is: "))
        
        # Validation
        if unit_price > 0 and quantity > 0:
            price = price + unit_price * quantity
            
        completed = input("Is it completed? (y/n) ")
        if completed == "y":
           flag = False
           
    print(f"The price is {price:.2f}")
