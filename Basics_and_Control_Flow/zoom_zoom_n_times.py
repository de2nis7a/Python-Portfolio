# FILE: zoom_zoom_n_times.py
# CONCEPT: Control Flow (Dynamic Loop)
# DEMONSTRATES: Taking integer input and using it to define the range of a 'for' loop.

def zoom_zoom():
    num=int(input("Enter a number:"))
    for i in range(num):
      print("zoom", i+1)