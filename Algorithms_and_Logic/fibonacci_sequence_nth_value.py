# FILE: fibonacci_sequence_nth_value.py
# CONCEPT: Classic Iterative Algorithm
# DEMONSTRATES: Calculating the nth value of the Fibonacci sequence using an iterative approach 
#               and temporary variables to swap values (previous, current).

def fibonacci():
    n = int(input("Enter the index N for the Fibonacci sequence (N > 2): "))
    
    if n <= 0:
        print("N must be a positive integer.")
        return
    if n == 1 or n == 2:
        print(f"The {n}th value in the Fibonacci sequence is: 1")
        return

    previous = 1
    current = 1
    
    # We start the loop from the 3rd term (i.e., n-2 iterations)
    for i in range(n - 2):
        temp = current
        current = previous + current
        previous = temp
        
    print(f"The {n}th value in the Fibonacci sequence is: {current}")
