user_cart = [
    {"name": "apple", "price": 5},
    {"name": "sugar", "price": 4},
    {"name": "bananas", "price": 3}
]

user_cart_quantity = [
    {"name": "apple", "quantity": 5},
    {"name": "sugar", "quantity": 8},
    {"name": "bananas", "quantity": 6}
]

# Create a lookup dictionary for quantities
quantity_lookup = {item["name"]: item["quantity"] for item in user_cart_quantity}
print(quantity_lookup)

# Use list comprehension to calculate total price per item
price_list = [item["price"] * quantity_lookup[item["name"]] for item in user_cart]

print(price_list)       # [25, 32, 18]

# Optional: dictionary with item-wise totals
cart_totals = {item["name"]: item["price"] * quantity_lookup[item["name"]] for item in user_cart}
print(cart_totals)      # {'apple': 25, 'sugar': 32, 'bananas': 18}

# Optional: grand total
total_bill = sum(price_list)
print(total_bill)       # 75



