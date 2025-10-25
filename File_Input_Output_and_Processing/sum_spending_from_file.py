# FILE: sum_spending_from_file.py
# CONCEPT: File I/O and Data Aggregation
# DEMONSTRATES: Reading numerical data line by line from a file, converting strings to floats, 
#               and calculating the total sum.

def total_spending():
    # NOTE: Assumes 'spending.txt' contains one float number per line.
    total_sum = 0
    try:
        with open("spending.txt", "r") as input_file:
            lines = input_file.readlines()
            for line in lines:
                # strip() removes potential whitespace/newlines, float() converts to number
                total_sum = total_sum + float(line.strip())
        print(f"Total spending: {total_sum:.2f}")
        
    except FileNotFoundError:
        print("Error: spending.txt not found.")
    except ValueError:
        print("Error: spending.txt contains non-numerical data.")
