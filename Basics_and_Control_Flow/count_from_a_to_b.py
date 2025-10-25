# FILE: count_from_a_to_b.py
# CONCEPT: Control Flow (Ranged Loop)
# DEMONSTRATES: Using two inputs to set the start and stop boundaries of a 'for' loop.

def count_from_to():
    num_start=int(input("Enter the start number:"))
    num_stop=int(input("Enter the end number:"))
    for i in range(num_start, num_stop+1):
      print(i)