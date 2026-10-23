import logging
import sqlite3
from pathlib import Path

import pandas as pd


# 1. PROJECT PATHS

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

CSV_PATH = DATA_DIR / "cleaned_retail_sales.csv"
DB_PATH = DATA_DIR / "retail_sales.db"
LOG_PATH = BASE_DIR / "pipeline.log"


# 2. LOGGING CONFIGURATION

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


# 3. EXTRACT DATA

def extract_data():

    logging.info("Data extraction started")

    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"CSV file not found: {CSV_PATH}"
        )

    df = pd.read_csv(CSV_PATH)

    if df.empty:
        raise ValueError("Input CSV contains no records")

    print("\nDATA EXTRACTION")
    print("----------------")
    print(f"Total records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    logging.info("Extracted %s records", len(df))

    return df


# 4. VALIDATE DATA

def validate_data(df):

    required_columns = [
        "order_id",
        "category",
        "quantity",
        "unit_price"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    quantity = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    unit_price = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    missing_ids = int(df["order_id"].isna().sum())
    duplicate_ids = int(df["order_id"].duplicated().sum())
    invalid_quantities = int(
        (quantity.isna() | (quantity <= 0)).sum()
    )
    invalid_prices = int(
        (unit_price.isna() | (unit_price <= 0)).sum()
    )
    missing_categories = int(df["category"].isna().sum())

    print("\nDATA QUALITY CHECKS")
    print("-------------------")
    print(f"Missing order IDs: {missing_ids}")
    print(f"Duplicate order IDs: {duplicate_ids}")
    print(f"Invalid quantities: {invalid_quantities}")
    print(f"Invalid prices: {invalid_prices}")
    print(f"Missing categories: {missing_categories}")

    # Duplicate order IDs are reported separately because
    # an order can contain multiple product rows.

    if (
        missing_ids > 0
        or invalid_quantities > 0
        or invalid_prices > 0
        or missing_categories > 0
    ):
        logging.error("Data quality checks failed")
        return False

    logging.info("Data quality checks passed")
    print("Data quality checks passed!")

    return True


# 5. LOAD DATA INTO SQLITE

def load_data(df):

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    logging.info("Loading data into SQLite")

    with sqlite3.connect(DB_PATH) as connection:
        df.to_sql(
            "retail_sales",
            connection,
            if_exists="replace",
            index=False
        )

    print("\nDATABASE LOADING")
    print("----------------")
    print("Data loaded successfully!")
    print(f"Database: {DB_PATH}")

    logging.info("SQLite loading completed")


# 6. GENERATE REPORTS AND EXPORT CSV FILES

def generate_report():

    logging.info("Report generation started")

    with sqlite3.connect(DB_PATH) as connection:

        # Total record count
        record_report = pd.read_sql_query(
            """
            SELECT COUNT(*) AS total_records
            FROM retail_sales;
            """,
            connection
        )