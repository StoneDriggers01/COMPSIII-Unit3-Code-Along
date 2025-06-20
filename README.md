# COMPS III: Unit 3 Code Along

## Overview

Object oriented programming is something that is utilized by nearly every business. To illustrate its utility, **we will be building an e-commerce application together using object oriented programming over the next three units**. 

This week, we’ll be implementing a `Product` class to represent the products in our store and a `ShoppingCart` class to store the `Product`(s) the user has selected.

![Product and ShoppingCart class](./E-Store.png)

## VS Code - `app.py` has syntax instructions
1. Define a `Product` class.
2. Define constructor with names (String), price (float), and sku (int).
3. Assign params to properties.
4. In the `tests` folder there is a test called `test_can_create_product` that tests that you can...create a product. You can set these up to run in your VS Code by doing the following:
    - Press the "Testing" flask icon in the left hand toolbar.
    - Press "Configure Python Tests"
    - Select "pytest"
    - Select the "root directory"
    - You can now run some or all of the tests in the left hand menu.

## VS Code - `main.py` has syntax instructions
5. Import the `Product` class into the file. 
6. Create `main()` function that will hold all of our program runs.  Call the function.
7. Create two instances of the `Product` class and print out the attributes. To see the output run `python3 main.py` in the command line.
8. Print out the object. You should see something like `<app.Product object at 0x1007e2e40>`. This is listing the memory address on our computer for the Product object, but that's not particularly useful. We can create a `__str__()` method to print out something more useful.

## VS Code - `app.py` has syntax instructions
9. Create a `__str__()` method  that takes the object as an argument and returns a string printing out the information about the object. This string should be in the format `"[NAME] (SKU: [SKU]) - $[PRICE]"`.
10. The `test_product_str` test should now be passing.

## Local Terminal - bash.sh has syntax instructions
11. Verify that the properties print out as expected using the command `python3 main.py`.

## VS Code - `app.py` has syntax information
12. Create a `ShoppingCart` class.
13. Define constructor with items (list) that will hold a list of `Product` objects.
14. Define a `__str()__` method that prints out information about the `ShoppingCart` object. This string should be in the format `"Shopping Cart with [NUMBER_OF_ITEMS] items.""`.
15. The `test_can_create_shoppingcart` and `test_shoppingcart_str` tests should now be passing.


## VS Code - `main.py` has syntax information
16. Import the `ShoppingCart` class into the file.
17. Inside `main()`, create an instance of the shopping cart and print it to the console.

# VS Code - `app.py` has syntax information
18.  Define a `add_items` method that takes the object, a product, and a quantity as an argument and does the following:
    - If no quantity is provided, it should be set to 1.
    - Add the item to the object's `items` list. It should be added as a dictionary in the format `{"product": [PRODUCT_OBJECT], "quantity": [QUANTITY]}`.
19. Define a `get_total` method that takes the object as an argument and does the following:
    - Initialize a variable called `total` with a value of zero.
    - Iterate through `items` and total up the cost of all the items in the cart
    - Return `total`
20. Define a `display_cart` method that takes the object as an argument and does the following:
    - Iterate through the `items` in the cart and print out a string in the format `"[PRODUCT_NAME] - Quantity: [QUANTITY]')"`
    - When the iteration is complete, print the total cost of all the items in the format `"Total: $[TOTAL]"`.
21. The `test_shoppingcart_add_items` should now be passing.

# VS Code - `main.py` has syntax information
22. Add each of the `Product` objects you created in step 9 to the `ShoppingCart` instance using the `add_items` method.
23. Display the cart contents using the `display_cart` method.
24. Call `get_total` to see the total cost of everything that you added to the cart.