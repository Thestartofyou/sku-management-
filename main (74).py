class SKU:
    def __init__(self, product_type, size, color, sku_number):
        self.product_type = product_type
        self.size = size
        self.color = color
        self.sku_number = sku_number
        self.stock = 0
        
    def __str__(self):
        return f"{self.product_type} {self.size} {self.color} ({self.sku_number})"
    
    def add_stock(self, quantity):
        self.stock += quantity
        
    def remove_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock")
        self.stock -= quantity
        
class Inventory:
    def __init__(self):
        self.skus = {}
        
    def add_sku(self, sku):
        self.skus[sku.sku_number] = sku
        
    def remove_sku(self, sku_number):
        del self.skus[sku_number]
        
    def get_sku(self, sku_number):
        return self.skus[sku_number]
    
    def get_sku_list(self):
        return list(self.skus.values())
    
    def restock(self, sku_number, quantity):
        self.get_sku(sku_number).add_stock(quantity)
        
    def sell(self, sku_number, quantity):
        self.get_sku(sku_number).remove_stock(quantity)

# Example usage:
inventory = Inventory()

# Add some SKUs
sku1 = SKU("T-shirt", "L", "Red", "12345")
sku2 = SKU("T-shirt", "M", "Blue", "67890")
inventory.add_sku(sku1)
inventory.add_sku(sku2)

# View the list of SKUs
print("Inventory:")
for sku in inventory.get_sku_list():
    print(f"- {sku} ({sku.stock} in stock)")

# Restock some SKUs
inventory.restock("12345", 10)
inventory.restock("67890", 5)

# Sell some SKUs
inventory.sell("12345", 3)
inventory.sell("67890", 2)

# View the updated inventory
print("\nUpdated inventory:")
for sku in inventory.get_sku_list():
    print(f"- {sku} ({sku.stock} in stock)")
