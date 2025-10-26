# FILE: ticket_price_calculator.py
# CONCEPT: Calculation Logic and Conditional Discount
# DEMONSTRATES: Calculating a variable price based on distance and applying a percentage 
# discount based on age thresholds (seniors and minors).

def ticket_price(journey_distance, age):
    """Calculates a discounted ticket price based on distance and age."""
    price_km = 0.15
    # Base price calculation
    price = 10 + price_km * journey_distance
    
    # Conditional discount
    if age >= 60 or age <=15:
        price -= 0.40 * price  # 40% discount
    return price
