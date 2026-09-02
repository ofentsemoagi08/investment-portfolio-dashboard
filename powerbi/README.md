# Power BI Dashboard

## Data Source

The dashboard connects to a PostgreSQL database containing the cleaned
financial transaction dataset.

- Database: PostgreSQL
- Connection mode: Import
- Source table: `transactions`
- Tool: Microsoft Power BI Desktop

## Data Model

The Power BI model uses a star-schema approach.

### Fact Table

- `transactions`

### Dimension Tables

- `DimCustomer`
- `DimCategory`
- `DimChannel`
- `DimDate`

The dimension tables have one-to-many relationships with the transaction
fact table and provide filtering for the report.

## DAX Measures

The dashboard uses DAX measures for the main KPIs:

- Total Transaction Value
- Total Transactions
- Average Transaction Value
- Active Customers

Example measures:

    Total Transaction Value =
    SUM('transactions'[amount])

    Total Transactions =
    COUNTROWS('transactions')

    Average Transaction Value =
    AVERAGE('transactions'[amount])

    Active Customers =
    DISTINCTCOUNT('transactions'[customer_id])

## Dashboard Pages

### 1. Executive Overview

Provides a high-level view of financial transaction activity.

Key visuals:

- Total transaction value
- Total transaction volume
- Average transaction value
- Active customers
- Monthly transaction value
- Transaction value by category
- Transaction value by customer segment

### 2. Customer Behaviour

Focuses on customer-level transaction activity.

Key visuals:

- Top 10 customers by transaction volume
- Transaction value by customer segment
- Average transaction value by segment
- Customer-level transaction summary

### 3. Transaction Analysis

Provides deeper analysis of transaction channels and category trends.

Key visuals:

- Transaction value by channel
- Transaction volume by channel
- Monthly transaction value by category
- Transaction volume vs transaction value by channel

## Interactivity

The dashboard includes slicers for:

- Customer segment
- Channel
- Category
- Year

Slicers are synchronised across relevant report pages.

## Key Results

Based on the synthetic dataset:

- Total transaction value: approximately R4.37 million
- Total transactions: 12,000
- Average transaction value: approximately R363.81
- Active customers: 500
- Premium customers have the highest average transaction value among the
  customer segments.
- Mass Market customers generate the highest overall transaction value due
  to their larger customer base.
- Online transactions generate the highest transaction value among channels.
- July records the highest monthly transaction value.

## Screenshots

Dashboard screenshots can be added to the `screenshots/` directory.

Suggested filenames:

- `executive_overview.png`
- `customer_behaviour.png`
- `transaction_analysis.png`
