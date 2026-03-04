
import requests

# Step 1 - Student Key & Seed
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

# Step 4 - Threshold Logic
if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

# Step 6 - Select API Term
if seed % 2 == 0:
    chosen_term = "weezer"
else:
    chosen_term = "drake"

# Part A - Inventory Entry
total_skus = 0
reorder_count = 0

# Step 2 - SKU Entry Loop
while True:
    sku_input = input("SKU: ").strip()
    if sku_input.upper() == "DONE":
        break
    if sku_input == "":
        print("Blank SKUs are not allowed. Please enter a valid SKU.")
        continue

    # Step 3 - On-Hand Quantity
    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("Quantity must be 0 or greater. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Step 5 - Reorder Decision
    total_skus += 1
    if on_hand < threshold:
        reorder_count += 1

# Part B - API Spot Check
songs_returned = "N/A"
api_status = ""

# Step 7 - API Request
try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={"entity": "song", "limit": 5, "term": chosen_term}
    )

    # Step 8 - Check HTTP Status Code
    if response.status_code != 200:
        api_status = "FAILED"
        songs_returned = "N/A"
    else:
        # Step 9 - JSON Processing
        try:
            data = response.json()
            results = data["results"]
            songs_returned = len(results)  # Fixed: count all results reliably
            api_status = "OK"
        except (KeyError, TypeError, ValueError):
            api_status = "INVALID_RESPONSE"
            songs_returned = "N/A"

except Exception:
    api_status = "FAILED"
    songs_returned = "N/A"

# Step 10 - Output Format
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {chosen_term}")
print(f"Songs returned: {songs_returned}")
print(f"API status: {api_status}")
