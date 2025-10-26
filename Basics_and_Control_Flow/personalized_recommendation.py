# FILE: personalized_recommendation.py
# CONCEPT: Input/Output and String Formatting
# DEMONSTRATES: Collecting multiple inputs (name, age, media type) from the user
# and using string concatenation and printing to generate a personalized message.

def personalized_recommendation():
    print("Welcome to The Media Hub!")
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    media_type = input("What's your favorite media type (film, music, or game)? ")
    
    print("Hi", name, "! We love", media_type, "too!")
    # Note: Assumes discount logic is handled elsewhere, focuses only on the message.
    print("As you're", age, ", you might enjoy our", age, "% birthday discount!")
    print("Check out our", media_type, "section for great deals!")
