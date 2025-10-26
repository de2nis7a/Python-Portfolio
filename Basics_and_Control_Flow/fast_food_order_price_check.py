# FILE: fast_food_order_price_check.py
# CONCEPT: Conditional Logic and Simple Arithmetic
# DEMONSTRATES: Applying a fixed delivery fee if the order price is below a threshold.

def fast_food_order_price():
    """Calculates final order price, adding a fee for orders under 20."""
    order_price = float(input("Enter the basic price of the order: "))
    if order_price < 20:
        order_price += 2.5
    print("The total price of your order is ", order_price)
