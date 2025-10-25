# FILE: pizza_cost_calculator.py
# CONCEPT: Area Calculation and Unit Cost
# DEMONSTRATES: Calculating the cost of an item based on its area, using unit price 
#               conversion (pence to pounds).

import math

def cost_of_pizza():
    # Cost is calculated based on area, at 3.5 pence per unit area.
    diameter = int(input("The diameter of pizza is: "))
    radius = diameter / 2
    area = radius ** 2 * math.pi
    
    # Cost per unit area: 3.5 pence = 0.035 pounds
    cost_in_pounds = area * (3.5 / 100)
    print(f"The cost of pizza is: £ {cost_in_pounds:.2f}")
