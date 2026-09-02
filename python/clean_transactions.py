import pandas as pd


# -----------------------------------
# Configuration
# -----------------------------------

INPUT_FILE = "data/raw_transactions.csv"
OUTPUT_FILE = "data/clean_transactions.csv"


# -----------------------------------
# Load raw data
# -----------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("RAW DATA PROFILE")
print("=" * 60)

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print("\nMissing values:")
print(df.isna().sum())


# -----------------------------------
# Standardise column names
# -----------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


# -----------------------------------
# Convert data types
# -----------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

df["amount"] = pd.to_numeric(
    df["amount"],
    errors="coerce"
)


# -----------------------------------
# Remove exact duplicate records
# -----------------------------------

before_duplicates = len(df)

df = df.drop_duplicates()

duplicates_removed = (
    before_duplicates - len(df)
)


# -----------------------------------
# Handle missing categorical values
# -----------------------------------

df["category"] = df["category"].fillna("Unknown")

df["channel"] = df["channel"].fillna("Unknown")


# -----------------------------------
# Validate transaction dates
# -----------------------------------

invalid_dates = df["transaction_date"].isna().sum()

if invalid_dates > 0:
    print(
        f"Warning: {invalid_dates} invalid transaction dates found."
    )

df = df.dropna(subset=["transaction_date"])


# -----------------------------------
# Validate transaction amounts
# -----------------------------------

invalid_amounts = (
    df["amount"].isna() |
    (df["amount"] <= 0)
).sum()

if invalid_amounts > 0:
    print(
        f"Warning: {invalid_amounts} invalid transaction amounts found."
    )

df = df[
    df["amount"].notna() &
    (df["amount"] > 0)
]


# -----------------------------------
# Validate required identifiers
# -----------------------------------

required_columns = [
    "transaction_id",
    "customer_id"
]

for column in required_columns:

    missing_ids = df[column].isna().sum()

    if missing_ids > 0:
        print(
            f"Warning: {missing_ids} missing values in {column}."
        )

df = df.dropna(
    subset=required_columns
)


# -----------------------------------
# Add analytical date fields
# -----------------------------------

df["year"] = df["transaction_date"].dt.year

df["month"] = df["transaction_date"].dt.month

df["month_name"] = (
    df["transaction_date"]
    .dt.strftime("%B")
)

df["year_month"] = (
    df["transaction_date"]
    .dt.to_period("M")
    .astype(str)
)


# -----------------------------------
# Final validation
# -----------------------------------

print("\n" + "=" * 60)
print("CLEAN DATA PROFILE")
print("=" * 60)

print(f"Rows after cleaning: {len(df):,}")

print(
    f"Duplicates removed: {duplicates_removed}"
)

print("\nRemaining missing values:")

print(
    df.isna().sum()
)

print("\nData types:")

print(
    df.dtypes
)


# -----------------------------------
# Save cleaned dataset
# -----------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n" + "=" * 60)

print(
    f"Clean dataset saved to: {OUTPUT_FILE}"
)

print("=" * 60)
