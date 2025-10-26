# FILE: rating_scale_generator.py
# CONCEPT: Control Flow (Dynamic Loop and String Manipulation)
# DEMONSTRATES: Taking user input to define the range of a loop and using 
# the string multiplication operator ('*') to dynamically create the output (stars).

def rating_scale():
    print("Welcome to The Media Hub!")
    max_rating = int(input("Maximum rating: "))
    print("Rating scale up to", max_rating, ":")
    for i in range (1, max_rating+1):
        star = "*" * i
        print(i, ":", star)
