# Retail Sales ETL Pipeline

## Project Overview
This project implements a retail sales ETL pipeline using Python, Pandas, SQLite, and SQL. It extracts sales data from CSV files, validates data quality, loads the data into a SQLite database, and generates sales reports.

## Project Objectives
- Extract retail sales data from CSV files.
- Validate data quality.
- Load data into a SQLite database.
- Generate category-wise sales reports.
- Identify the top five products by revenue when product information is available.
- Export reports as CSV files.
- Maintain execution logs for troubleshooting.

## Technologies Used
- Python
- Pandas
- SQLite
- SQL
- CSV
- Logging
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
retail-sales-etl/
├── data/
│   ├── retail_sales.csv
│   ├── cleaned_retail_sales.csv
│   ├── category_sales_report.csv
│   └── retail_sales.db
├── main.py
├── sqlite_pipeline.py
├── test_data_quality.py
├── pipeline.log
├── .gitignore
└── README.md
```

## ETL Workflow

### 1. Extract
Reads cleaned retail sales data from a CSV file using Pandas.

### 2. Transform and Validate
Checks required columns, missing order IDs, duplicate order IDs, invalid quantities, invalid prices, and missing categories.

### 3. Load
Loads validated data into a SQLite database table named `retail_sales`.

### 4. Analyze
Uses SQL queries to calculate:
- Total number of records.
- Total sales by category.
- Top five products by revenue, when the product column is available.

### 5. Export
Saves the category-wise sales report and, when possible, the top-products report as CSV files.

### 6. Logging
Records pipeline execution and errors in `pipeline.log`.

## Requirements
- Python 3
- Pandas

Install Pandas using:

```bash
pip install pandas
```

## How to Run

1. Open the project folder in Visual Studio Code.
2. Ensure the input file exists at `data/cleaned_retail_sales.csv`.
3. Open the terminal.
4. Run:

```bash
python sqlite_pipeline.py
```

## Output Files
- `data/retail_sales.db` — SQLite database.
- `data/category_sales_report.csv` — Category-wise sales report.
- `data/top_5_products_report.csv` — Top five products report, if product information is available.
- `pipeline.log` — Pipeline execution log.

## Learning Outcomes
- Building a basic ETL pipeline.
- Reading and validating CSV data with Pandas.
- Using SQL for sales analysis.
- Loading data into SQLite.
- Exporting analytical reports.
- Implementing logging and error handling.

## Future Improvements
- Add automated unit tests.
- Schedule pipeline execution.
- Add more business reports.
- Integrate a cloud data platform such as Azure.
- Implement a larger-scale pipeline using Apache Spark.

## Project Status
Core ETL functionality, SQLite loading, data quality checks, logging, and CSV report generation have been implemented. Final validation and repository setup are pending.