from app import Product, ShoppingCart

laptop = Product("Macbook Pro", 1299.99, 123456)
headphones = Product("Airpods", 159.99, 78012)

#print(laptop)

cart = ShoppingCart()

cart.add_items(laptop)
cart.add_items(headphones, 2)

cart.display_cart()