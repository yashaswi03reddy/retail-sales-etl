
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


