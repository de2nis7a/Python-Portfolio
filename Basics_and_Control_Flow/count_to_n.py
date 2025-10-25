# FILE: count_to_n.py
# CONCEPT: Control Flow (Basic Counting Loop)
# DEMONSTRATES: Iterating from 1 up to a user-specified number using 'range'.

def count_to():
    num=int(input("Enter a number:"))
    for i in range(num):
      print(i+1)