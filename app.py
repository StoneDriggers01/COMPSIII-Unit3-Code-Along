class Product:
    # Define Constructor with name, price, and sku
    def __init__(self, name, price, sku):
        # set the params to properties
        self.name = name
        self.price = price
        self.sku = sku

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"

class ShoppingCart:
    #Define the constructor
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    
    # Method that takes the object, a product, and a quantity as an argument and adds it to the cart. 
    def add_items(self, product, quantity = 1):
        self.items.append({"product": product, "quantity": quantity})

    def get_total(self):
        #Initalize a total
        total = 0

        #Iterate through the shopping cart and sum up the values
        for item in self.items:
            total += item["product"].price * item["quantity"]

        #Return the total
        return total
    
    def display_cart(self):
        # Iterate through the items
        for item in self.items:
            print(f"{item["product"]} - Quantity: {item["quantity"]}")

        print(f"Total: ${self.get_total():.2f}")