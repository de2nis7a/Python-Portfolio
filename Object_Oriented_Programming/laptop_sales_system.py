# FILE: laptop_sales_system.py
# CONCEPT: Object-Oriented Programming (OOP) - Inheritance, Properties, Composition
# DEMONSTRATES: Defining base class (Laptop) with property setters for validation, 
#               inheritance (GamingLaptop) to add new features, and composition (ShoppingCart).

class Laptop:
    
    # Static data for price lookup (Configuration options)
    available_ram = {
        4 : 0,
        8 : 50,
        16 : 100,
        32 : 200
    }
    
    available_ssd = {
        256 : 0,
        512 : 30,
        1024 : 100
    }
    
    def __init__(self, brand, base_price):
        self.brand = brand
        self.base_price = base_price
        self._ram = 4
        self._ssd = 256
        
    @property    
    def ram(self):
        return self._ram
             
    @ram.setter
    def ram(self, new_ram):
        if new_ram in self.available_ram:
            self._ram = new_ram
            
    @property
    def ssd(self):
        return self._ssd
    
    @ssd.setter
    def ssd(self, new_ssd):
        if new_ssd in self.available_ssd:
            self._ssd = new_ssd
            
    def calculate_price(self):
        # Calculate price based on base price plus upgrades
        ram_cost = self.available_ram.get(self._ram, 0)
        ssd_cost = self.available_ssd.get(self._ssd, 0)
        return self.base_price + ram_cost + ssd_cost

    def __str__(self):
        output = f"{self.brand} Laptop with {self._ram} GB RAM and {self._ssd} GB SSD"
        output += f" priced at £{self.calculate_price()}"
        return output

class ShoppingCart:
    
    def __init__(self):
        self.laptops = []
        self.total = 0
    
    def add_laptop(self, laptop):
        self.laptops.append(laptop)
        self.total += laptop.calculate_price()
    
    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"- {laptop}\n"
        output += f"\nTotal price is £{self.total}"
        return output
    
class GamingLaptop(Laptop):
    
    available_gpu = {
        "NVIDIA GTX 1650" : 0,
        "NVIDIA RTX 3070" : 250,
        "NVIDIA RTX 4080" : 350,
        "AMD RX 6800M" : 280
        }
    
    def __init__(self, brand, base_price):
        super().__init__(brand, base_price)
        self._gpu = "NVIDIA GTX 1650"
        
    @property
    def gpu(self):
        return self._gpu
    
    @gpu.setter
    def gpu(self, new_gpu):
        if new_gpu in self.available_gpu:
            self._gpu = new_gpu
        
    def calculate_price(self):
        # Calculate base price (from parent) and add GPU cost
        base_calc = super().calculate_price()
        gpu_cost = self.available_gpu.get(self._gpu, 0)
        return base_calc + gpu_cost
    
    def __str__(self):
        output = f"{self.brand} Gaming Laptop with {self._ram} GB RAM, {self.ssd} GB SSD "
        output += f"and {self._gpu} priced at £{self.calculate_price()}"
        return output
    
def test_sales_system():
    laptop = Laptop("Dell", 100)
    print(laptop)
    laptop.ram = 16
    print(laptop)
    
    laptop2 = Laptop("ASUS", 200)
    print(laptop2)
    laptop2.ssd = 1024
    print(laptop2)
    
    shop = ShoppingCart()
    shop.add_laptop(laptop)
    print(shop)
    
    shop.add_laptop(laptop2)
    print(shop)
    
    laptop3 = GamingLaptop("Samsung", 50)
    print(laptop3)
    
    laptop3.gpu = "NVIDIA RTX 3070"
    print(laptop3)
    
    shop.add_laptop(laptop3)
    print(shop)

if __name__ == "__main__":
    test_sales_system()
