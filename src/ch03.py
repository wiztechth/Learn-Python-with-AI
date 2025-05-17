# Restaurang Management System
# String Bacics

# resturant_name = "The Food Palace"
# menu_item = "Pad Thai with Shimp"
# address = "1234 Food St, Flavor Town, USA"

# print(resturant_name)

# # Indexing and Slicing
# dish = "Spaghetti Bolognese"
# first_char = dish[0]  # First character
# last_char = dish[-1]  # Last character  
# print(f"First character: {first_char}")
# print(f"Last character: {last_char}")

# # Slicing
# price = "250THB"
# amount = price[0:3]  # First three characters
# currency = price[3:]  # Remaining characters
# print(f"Amount: {amount}")  
# print(f"Currency: {currency}")

# String format & f-string
# customer = "John Doe"
# total = 150.75
# message = f"Thank you, {customer}, for dining with us! Your total is ${total:.2f}."
# print(message)

# # String Methods
# ingredients = "chicken, rice, vegetables"
# listed_ingredients = ingredients.split(", ") 
# print(listed_ingredients)

# joined_ingredients = "-".join(listed_ingredients)
# print(joined_ingredients)

# old_menu = "Pasta, Salad, Soup"
# new_menu = old_menu.replace("Salad", "Pizza")
# print(new_menu)

# Escape characters & Raw strings
menu_description = "Today's Spicy Noodele' is very hot!\\nAvoid if sensitive to spice."
print(menu_description)

raw_string = r"Today's Spicy Noodele' is very hot!\nAvoid if sensitive to spice."
print(raw_string)

# multi-line 
welcome_message = """Welcome to The Food Palace!
We are delighted to serve you a variety of delicious dishes.
We hope you enjoy your dining experience with us!"""
print(welcome_message)
