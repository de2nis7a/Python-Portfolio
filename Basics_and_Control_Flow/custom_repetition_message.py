# FILE: custom_repetition_message.py
# CONCEPT: Control Flow (Dynamic Loop)
# DEMONSTRATES: Taking user input to determine the number of iterations (repeat_count) 
# and using a 'for' loop to repeat the action that specific number of times.

def custom_repeat_message():
    print("Welcome to The Media Hub!")
    repeat_count = int(input("How many times should we say 'Media is great!'? "))
    for i in range(repeat_count):
        print("Media is great!")
