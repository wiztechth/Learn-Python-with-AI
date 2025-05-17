# Restaurant System
item_names = ["Book", "Pen", "Notebook", "Eraser"]
item_prices = [10, 5, 20, 2]

# Use List Comprehension
item_prices = [round(price * 1.1, 2) for price in item_prices]
print("Updated Prices after add more 10%:", item_prices)
