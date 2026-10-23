
import pandas as pd

# Sample data with an invalid quantity
test_df = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "quantity": [2, 5, -1],
    "unit_price": [45000, 500, 1200]
})

print("TESTING INVALID DATA")

# Check for invalid quantities
invalid_quantity = (test_df["quantity"] <= 0).any()

if invalid_quantity:
    print("PASS: Invalid quantity was detected.")
else:
    print("FAIL: Invalid quantity was not detected.")

# Check for invalid prices
invalid_price = (test_df["unit_price"] <= 0).any()

if invalid_price:
    print("PASS: Invalid price was detected.")
else:
    print("FAIL: Invalid price was not detected.")
