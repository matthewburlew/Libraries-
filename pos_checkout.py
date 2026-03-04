# pos_checkout.py
# DATA 4000 - Assignment 5
# Exercise 1: Point-of-Sale Checkout System

# Step 1 - Student Key & Seed
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

# Step 2 - Item Entry Loop
subtotal = 0.0
total_units = 0

while True:
    item_name_input = input("Enter item name (or DONE to finish): ")

    if item_name_input.strip().upper() == "DONE":
        break

    # Validate item name
    item_name = item_name_input.strip()
    if item_name == "":
        print("Invalid item name. Please enter a non-empty name.")
        continue

    # Validate unit price
    while True:
        try:
            price_input = input(f"Enter unit price for {item_name}: ")
            unit_price = float(price_input)
            if unit_price <= 0:
                print("Price must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a numeric value.")

    # Validate quantity
    while True:
        try:
            qty_input = input(f"Enter quantity for {item_name}: ")
            quantity = int(qty_input)
            if quantity < 1:
                print("Quantity must be at least 1. Try again.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    # Step 4 - Update running totals
    subtotal += unit_price * quantity
    total_units += quantity

# Step 5 - Discount Logic
if total_units >= 10 or subtotal >= 100:
    discount_percent = 10
else:
    discount_percent = 0

discounted_total = subtotal * (1 - discount_percent / 100)

# Step 6 - Seed-Based Member Perk
perk_applied = False
if seed % 2 != 0:
    discounted_total -= 3.00
    perk_applied = True
    if discounted_total < 0:
        discounted_total = 0.00

# Step 7 - Output
print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
print(f"Total: ${discounted_total:.2f}")
