# FILE: average_of_n_numbers.py
# CONCEPT: Iterative Aggregation and User Input
# DEMONSTRATES: Using a loop to repeatedly prompt the user for input and calculate the average 
#               of a user-defined quantity of numbers.

def average_of_numbers():
    numbers_count = int(input("The number of numbers is: "))
    total_sum = 0
    
    for i in range (numbers_count):
       number = int(input(f"Enter number {i+1} for average: "))
       total_sum = total_sum + number
       
    # Check to prevent division by zero in case user enters 0
    if numbers_count > 0:
        print(f"The average is : {total_sum / numbers_count}")
    else:
        print("Cannot calculate average for zero numbers.")
