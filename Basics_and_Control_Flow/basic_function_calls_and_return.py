# FILE: basic_function_calls_and_return.py
# CONCEPT: Function Definition and Composition
# DEMONSTRATES: Defining functions with clear inputs and outputs, and having one function 
# call multiple other simple functions to compose a result.

def greet(name):
    """Returns a simple greeting message."""
    return f"Hello, {name}!"

def product(a, b):
    """Calculates the product of two numbers."""
    return a * b

def divide(a, b):
    """Calculates the division of two numbers."""
    # Note: Requires error handling for division by zero in a production environment
    return a / b

def divide_and_product(a, b):
    """Calls product and divide functions and returns both results."""
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result

def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    # Example of unpacking multiple return values
    product_result, divide_result = divide_and_product(num1, num2)
    
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")
    
# main()
