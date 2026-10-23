import pandas as pd


def validate_data(df):
    """Validate quantity and unit price values."""

    required_columns = ["quantity", "unit_price"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    quantity = pd.to_numeric(df["quantity"], errors="coerce")
    unit_price = pd.to_numeric(df["unit_price"], errors="coerce")

    invalid_quantity = (
        quantity.isna() | (quantity <= 0)
    ).any()

    invalid_price = (
        unit_price.isna() | (unit_price <= 0)
    ).any()

    return {
        "invalid_quantity": invalid_quantity,
        "invalid_price": invalid_price,
    }


def test_invalid_quantity():
    df = pd.DataFrame({
        "quantity": [2, -1, 5],
        "unit_price": [100, 200, 300],
    })

    result = validate_data(df)

    assert result["invalid_quantity"], (
        "Invalid quantity was not detected"
    )

    print("PASS: Invalid quantity was detected.")


def test_invalid_price():
    df = pd.DataFrame({
        "quantity": [2, 3, 5],
        "unit_price": [100, -50, 300],
    })

    result = validate_data(df)

    assert result["invalid_price"], (
        "Invalid price was not detected"
    )

    print("PASS: Invalid price was detected.")


if __name__ == "__main__":
    print("TESTING INVALID DATA")

    test_invalid_quantity()
    test_invalid_price()

    print("\nALL DATA QUALITY TESTS PASSED!")

