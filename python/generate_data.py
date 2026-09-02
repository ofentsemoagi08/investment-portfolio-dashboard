import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker


fake = Faker()
random.seed(42)
np.random.seed(42)


# -----------------------------
# Configuration
# -----------------------------

NUM_CUSTOMERS = 500
NUM_TRANSACTIONS = 12000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)


# -----------------------------
# Reference data
# -----------------------------

segments = ["Mass Market", "Affluent", "Premium"]

account_types = [
    "Current",
    "Savings",
    "Credit",
]

transaction_types = [
    "Purchase",
    "Transfer",
    "Payment",
    "Withdrawal",
    "Deposit",
]

categories = [
    "Groceries",
    "Transport",
    "Dining",
    "Entertainment",
    "Utilities",
    "Shopping",
    "Healthcare",
    "Travel",
    "Education",
    "Subscriptions",
]

channels = [
    "Card",
    "Online",
    "ATM",
    "Mobile",
    "Branch",
]

cities = [
    "Cape Town",
    "Johannesburg",
    "Pretoria",
    "Durban",
    "Stellenbosch",
    "Port Elizabeth",
]


# -----------------------------
# Generate customers
# -----------------------------

customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    segment = random.choices(
        segments,
        weights=[60, 30, 10],
        k=1
    )[0]

    account_type = random.choices(
        account_types,
        weights=[50, 40, 10],
        k=1
    )[0]

    customers.append({
        "customer_id": f"CUST{i:04d}",
        "customer_name": fake.name(),
        "customer_segment": segment,
        "account_type": account_type,
        "city": random.choice(cities),
    })


customers_df = pd.DataFrame(customers)


# -----------------------------
# Generate transactions
# -----------------------------

transactions = []

date_range = (END_DATE - START_DATE).days


for i in range(1, NUM_TRANSACTIONS + 1):

    customer = customers_df.sample(1).iloc[0]

    transaction_date = (
        START_DATE +
        timedelta(days=random.randint(0, date_range))
    )

    transaction_type = random.choice(transaction_types)

    category = random.choice(categories)

    channel = random.choice(channels)

    # Generate realistic transaction amounts
    if transaction_type == "Purchase":
        amount = np.random.lognormal(mean=4.0, sigma=0.7)

    elif transaction_type == "Transfer":
        amount = np.random.lognormal(mean=6.0, sigma=0.8)

    elif transaction_type == "Payment":
        amount = np.random.lognormal(mean=5.0, sigma=0.6)

    elif transaction_type == "Withdrawal":
        amount = np.random.lognormal(mean=4.5, sigma=0.5)

    else:
        amount = np.random.lognormal(mean=6.5, sigma=0.8)

    transactions.append({
        "transaction_id": f"TXN{i:06d}",
        "transaction_date": transaction_date.date(),
        "customer_id": customer["customer_id"],
        "customer_segment": customer["customer_segment"],
        "account_type": customer["account_type"],
        "transaction_type": transaction_type,
        "category": category,
        "channel": channel,
        "amount": round(float(amount), 2),
        "city": customer["city"],
    })


transactions_df = pd.DataFrame(transactions)


# -----------------------------
# Introduce a small number of
# data-quality issues intentionally
# -----------------------------

missing_indices = np.random.choice(
    transactions_df.index,
    size=30,
    replace=False
)

transactions_df.loc[
    missing_indices[:15],
    "category"
] = None

transactions_df.loc[
    missing_indices[15:],
    "channel"
] = None


# Duplicate a few records
duplicates = transactions_df.sample(
    10,
    random_state=42
)

transactions_df = pd.concat(
    [transactions_df, duplicates],
    ignore_index=True
)


# -----------------------------
# Save data
# -----------------------------

output_path = "data/raw_transactions.csv"

transactions_df.to_csv(
    output_path,
    index=False
)

print("Dataset generated successfully.")
print(f"Rows generated: {len(transactions_df):,}")
print(f"Customers: {transactions_df['customer_id'].nunique():,}")
print(f"Date range: {transactions_df['transaction_date'].min()} "
      f"to {transactions_df['transaction_date'].max()}")
print(f"Output: {output_path}")
