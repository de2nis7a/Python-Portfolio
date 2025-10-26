# FILE: count_up_to_n.py
# CONCEPT: Control Flow (Dynamic Loop and Range)
# DEMONSTRATES: Taking user input to define the upper limit of a counting loop 
# and using 'range(start, stop)' to iterate from 1 up to that number, inclusive.

def count_up():
    print("Welcome to The Media Hub!")
    number = int(input("Enter a number: "))
    print("Counting up to", number, ":")
    # range(1, number + 1) ensures the loop counts from 1 up to and including 'number'
    for i in range(1, number + 1):
        print(i)
