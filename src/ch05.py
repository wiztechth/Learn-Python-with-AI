# Restaurant Management System
# Arithmetic operators
price_pizza = 10.99
price_burger = 8.99 
total = price_pizza + price_burger
print("Total price of pizza and burger: $", total)

# Discount 10%
discount = 0.10 * total
new_total = total - discount

# calculate changes
payment = 50
change = payment - new_total
print("Change to be returned: $", change)

# calculate extra discount
price = 550
minimum_spend = 500

if price >= minimum_spend:
    print("You are eligible for an extra discount!")
else:
    print("You have to order another", minimum_spend - price, "to be eligible for an extra discount!")
    