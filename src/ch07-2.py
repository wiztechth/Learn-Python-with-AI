# E-Commerce platform
# Introdduction to List
products = [ "Laptop", "Smartphone", "Tablet", "Headphones" ]

# shopping cart
cart = ["Laptop", "Smartphone", "Tablet" ]

# print item 2 & 3 from the list
print(products[1:3]) # prints ['Smartphone', 'Tablet']

# append Headphones to the cart
cart.append("Headphones")
print(cart) 

# count the number of items in the cart
print(f"มีสินค้าในตะกร้าจำนวน {len(cart)} รายการ") # prints 4