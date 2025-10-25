# FILE: pizza_order_system.py
# CONCEPT: Object-Oriented Programming (OOP) - Inheritance, Sets, and Type Checking
# DEMONSTRATES: Using sets for topping validation, inheritance (StuffedCrustPizza), and
#               type checking (isinstance) for complex business logic (upgrade_to_stuffed_crust).

class Pizza:

    valid_toppings = {'cheese', 'pepperoni', 'mushrooms', 'olives'}

    def __init__(self, size):
        self.size = size
        self._toppings = set() # Use a set for unique, unordered toppings

    @property
    def toppings(self):
        return self._toppings

    def add_topping(self, topping):
        if topping in self.valid_toppings:
            self._toppings.add(topping)

    def __str__(self):
        output = f"A {self.size} pizza with the following toppings:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        return output


class StuffedCrustPizza(Pizza):

    def __init__(self, size, crust):
        super().__init__(size)
        self._crust = crust

    @property
    def crust(self):
        return self._crust

    @crust.setter
    def crust(self, new_crust):
        if new_crust in {'mozzarella', 'hot dog'}:
            self._crust = new_crust

    def __str__(self):
        output = f"A {self.size} stuffed crust pizza"
        output += f" with {self.crust} crust and the following toppings:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        return output


class PizzaOrder:

    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, index):
        # Ensures index is within bounds
        if 0 <= index < len(self.pizzas):
            self.pizzas.pop(index)
        
    def upgrade_to_stuffed_crust(self, index, crust):
        if 0 <= index < len(self.pizzas):
            pizza = self.pizzas[index]
            # Check if it's a base Pizza class and NOT already a StuffedCrustPizza
            if isinstance(pizza, Pizza) and not isinstance(pizza, StuffedCrustPizza):
                upgraded_pizza = StuffedCrustPizza(pizza.size, crust)
                # Transfer existing toppings to the upgraded pizza
                upgraded_pizza._toppings = pizza.toppings
                self.pizzas[index] = upgraded_pizza
                

    def __str__(self):
        output = "Your order contains:"
        num_pizzas = len(self.pizzas)
        for i in range(num_pizzas):
            pizza = self.pizzas[i]
            index = i + 1
            # Recalculate toppings list for clean display
            output += f"\n{index}. {pizza}" 
        return output


def test_pizza():
    pizza = Pizza("large")
    pizza.add_topping("cheese")
    pizza.add_topping("pepperoni")
    print(pizza)

def test_stuffed_crust_pizza():
    pizza = StuffedCrustPizza("large", "mozzarella")
    pizza.add_topping("cheese")
    pizza.add_topping("pepperoni")
    pizza.crust = 'hot dog'
    pizza.crust = 'cheddar'  # should not change the crust

    print(pizza)


def test_pizza_order():
    order = PizzaOrder()

    pizza1 = Pizza("large")
    pizza1.add_topping("cheese")
    pizza1.add_topping("pepperoni")
    order.add_pizza(pizza1)

    pizza2 = StuffedCrustPizza("medium", "mozzarella")
    pizza2.add_topping("cheese")
    pizza2.add_topping("mushrooms")
    order.add_pizza(pizza2)

    print(order)
    print("--- Upgrading pizza 1 ---")

    # Upgrade pizza1 (index 0)
    order.upgrade_to_stuffed_crust(0, 'mozzarella')
    print(order)
    print("--- Removing pizza 2 ---")
    
    # Remove pizza2 (index 1)
    order.remove_pizza(1) 
    print(order)
    

if __name__ == "__main__":
    test_pizza_order()
