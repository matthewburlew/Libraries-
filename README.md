# data4000-assignment5

## Installation
pip install requests

## Exercise 1 - pos_checkout.py

### Description:
This program simulates a point-of-sale checkout system for a campus retail store. It allows cashiers to enter items, calculates the subtotal, applies discounts, and applies a seed-based member perk.

### How to run:
python pos_checkout.py

### Example run:
Student key: abc
Enter item name (or DONE to finish): apple
Enter unit price for apple: 2.50
Enter quantity for apple: 3
Enter item name (or DONE to finish): DONE
Seed: 294
Units: 3
Subtotal: $7.50
Discount: 0%
Perk applied: NO
Total: $7.50

## Exercise 2 - inventory_spotcheck.py

### Description:
This program allows operations staff to enter inventory counts for products and determines which items need to be reordered. It also performs an API spot check using the iTunes Search API to retrieve song data based on the user's seed value.

### How to run:
python inventory_spotcheck.py

### Example run:
Student key: abc
SKU: ITEM001
On hand: 5
SKU: ITEM002
On hand: 20
SKU: DONE
Seed: 294
Threshold: 15
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
