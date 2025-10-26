# FILE: birthday_discount_calculation.py
# CONCEPT: Conditional Logic, Input/Output, and Float Arithmetic
# DEMONSTRATES: Applying conditional logic using the built-in 'min' function to cap a discount 
# rate (ensuring it doesn't exceed 50%) and performing precise float arithmetic for price calculation.

def birthday_discount():
    print("Welcome to The Media Hub!")
    age = int(input("Please enter your age: "))
    item_price = float(input("Enter the price of your favorite film, album, or game: $"))
    
    # Cap discount at 50% using min()
    discount = min(age, 50)  
    discounted_price = item_price * (1 - discount/100)
    
    print("For your", age, "th birthday, we'll give you a", discount, "% discount!")
    print("Your item would cost: $", round(discounted_price, 2))
