class Product:
    def __init__(self, name, price, quantity):
        """Initialize product with name, price, and quantity"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        """Display product's name, price, and quantity"""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")

    def update_quantity(self, amount):
        """Update the quantity of the product (can be negative for sales)"""
        self.quantity += amount
        if self.quantity < 0:
            print("Error: Quantity cannot be negative.")
            self.quantity -= amount  # revert to previous value if invalid operation
        else:
            print(f"Updated Quantity of {self.name}: {self.quantity}")

    def calculate_total_value(self):
        """Calculate the total value of this product"""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        """Initialize inventory as an empty list"""
        self.products = []

    def add_product(self, name, price, quantity):
        """Add a new product to the inventory"""
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product {name} added to the inventory.")

    def display_inventory(self):
        """Display all products in the inventory"""
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                product.display_product_info()
                print("-" * 30)

    def calculate_inventory_value(self):
        """Calculate the total value of all products in the inventory"""
        total_value = sum(product.calculate_total_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}")

# Create an inventory instance
inventory = Inventory()

# Adding some products to the inventory
inventory.add_product("Laptop", 1200.00, 10)
inventory.add_product("Smartphone", 800.00, 25)
inventory.add_product("Headphones", 150.00, 50)

# Display inventory
inventory.display_inventory()

# Update quantities (for example, selling or restocking)
inventory.products[0].update_quantity(-3)  # Sold 3 laptops
inventory.products[1].update_quantity(10)  # Restocked 10 smartphones

# Display updated inventory
inventory.display_inventory()

# Calculate total inventory value
inventory.calculate_inventory_value()
