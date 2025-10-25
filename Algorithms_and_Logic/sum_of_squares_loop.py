# FILE: sum_of_squares_loop.py
# CONCEPT: Iterative Algorithm (Loop)
# DEMONSTRATES: Using a 'for' loop to iterate and accumulate the sum of squares up to 'n'.

def sum_of_squares():
    n = int(input("The integer is: "))
    sum_of_squares_value = 0
    for i in range(1, n + 1):
      sum_of_squares_value = sum_of_squares_value + i ** 2
    print(f"The sum is: {sum_of_squares_value}")
