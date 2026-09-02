# Dataset

This project uses a synthetic financial transaction dataset created specifically
for portfolio and demonstration purposes.

## Dataset Summary

- 500 customers
- 12,000 cleaned transactions
- Transaction period: January 2025 to December 2025
- South African cities
- Transaction categories including Groceries, Transport, Dining, Shopping,
  Healthcare, Travel, Education and Subscriptions
- Customer segments: Mass Market, Affluent and Premium
- Account types: Current, Savings and Credit
- Channels: Card, Online, ATM, Mobile and Branch
## Data Quality

The raw dataset intentionally contains common data-quality issues to
demonstrate an ETL and validation workflow:

- 10 duplicate rows
- 15 missing category values
- 15 missing channel values

The Python cleaning process removes duplicate records and replaces missing
categorical values with "Unknown".

The resulting dataset contains 12,000 clean transactions with no remaining
missing values.

## Data Generation

The synthetic dataset can be regenerated using:

    python python/generate_data.py

The cleaning process can then be run using:

    python python/clean_transactions.py

## Disclaimer

This dataset contains no real customer, banking, financial-account or
personally identifiable information. All data is synthetic and intended only
for learning, portfolio demonstration and technical assessment purposes.
