
import pandas as pd
import os


file_path = "data/retail_sales.csv"

try:
    # Check whether the dataset file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    # Load the dataset
    df = pd.read_csv(file_path)

    # Required columns
    required_columns = [
        "order_id",
        "order_date",
        "product",
        "category",
        "quantity",
        "unit_price"
    ]

    # Check for missing columns
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("Dataset loaded and validated successfully!")

except (
    FileNotFoundError,
    ValueError,
    pd.errors.ParserError
) as error:
    print("ERROR:", error)
    raise SystemExit(1)



print("BEFORE CLEANING")
print(df)

# 2. Remove extra spaces from text columns
df["product"] = df["product"].str.strip()
df["category"] = df["category"].str.strip()

# 3. Convert order_date into date format
df["order_date"] = pd.to_datetime(df["order_date"])

# 4. Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Create a new column for total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

print("\nCLEANED DATA")
print(df)

# 7. Display total sales
print("\nTOTAL SALES")
print(df["total_sales"].sum())

# 8. Save cleaned data into a new CSV file
output_path = "data/cleaned_retail_sales.csv"
df.to_csv(output_path, index=False)

print("\nCLEANED DATA SAVED SUCCESSFULLY!")
print("Output file:", output_path)

# 9. Data quality checks
print("\nDATA QUALITY CHECKS")

# Check whether order IDs are missing
print("Missing Order IDs:", df["order_id"].isnull().sum())

# Check duplicate order IDs
print("Duplicate Order IDs:", df["order_id"].duplicated().sum())

# Check invalid quantities
print("Invalid Quantities:", (df["quantity"] <= 0).sum())

# Check invalid prices
print("Invalid Prices:", (df["unit_price"] < 0).sum())

# Check total number of records
print("Total Records:", len(df))

# 10. Category-wise sales report
category_sales = df.groupby("category")["total_sales"].sum()

print("\nCATEGORY-WISE SALES REPORT")
print(category_sales)

# 11. Save category-wise report
category_sales.to_csv("data/category_sales_report.csv")

print("\nCATEGORY SALES REPORT SAVED SUCCESSFULLY!")

# 12. Test total sales calculation
expected_total = 222500
actual_total = df["total_sales"].sum()

print("\nSALES CALCULATION TEST")

if actual_total == expected_total:
    print("PASS: Total sales calculation is correct.")
else:
    print("FAIL: Total sales calculation needs checking.")

print("Expected total:", expected_total)
print("Actual total:", actual_total)

# Debug total sales calculation
print("\nSALES CALCULATION DEBUG")

print("Sales by order:")
print(df[["order_id", "quantity", "unit_price", "total_sales"]])

actual_total = df["total_sales"].sum()

print("\nActual total sales:", actual_total)
# Automatic sales calculation test
expected_total = 222500
actual_total = df["total_sales"].sum()

assert actual_total == expected_total, (
    f"Expected {expected_total}, but got {actual_total}"
)

print("PASS: Automatic sales test completed!")

# DAY 1: DATA QUALITY TESTS

print("\n--- DATA QUALITY TESTS ---")

# Test 1: Check whether the dataset is empty
assert not df.empty, "Dataset is empty!"
print("PASS: Dataset is not empty.")

# Test 2: Check for missing values
missing_values = df[
    ["order_id", "order_date", "product",
     "category", "quantity", "unit_price"]
].isnull().sum().sum()

assert missing_values == 0, (
    f"Dataset contains {missing_values} missing values."
)
print("PASS: No missing values found.")

# Test 3: Check duplicate order IDs
duplicate_orders = df["order_id"].duplicated().sum()

assert duplicate_orders == 0, (
    f"Found {duplicate_orders} duplicate order IDs."
)
print("PASS: No duplicate order IDs found.")

# Test 4: Check positive quantities
assert (df["quantity"] > 0).all(), (
    "Invalid quantity found."
)
print("PASS: All quantities are positive.")

# Test 5: Check positive unit prices
assert (df["unit_price"] > 0).all(), (
    "Invalid unit price found."
)
print("PASS: All unit prices are positive.")

print("\nALL DATA QUALITY TESTS PASSED!")





