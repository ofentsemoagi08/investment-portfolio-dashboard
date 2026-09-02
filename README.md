# Investment Portfolio Analytics Dashboard

An end-to-end financial transaction analytics project demonstrating data
generation, data cleaning, SQL analysis, data modelling and interactive
visualisation using Python, PostgreSQL and Power BI.

## Project Overview

This project simulates a financial transaction analytics environment using
synthetic banking transaction data.

The objective is to transform raw transaction data into an analytical
dataset and dashboard that can be used to understand transaction behaviour,
customer segments, spending categories and transaction channels.

## Architecture

Raw CSV
   ↓
Python Data Generation
   ↓
Python Data Cleaning & Validation
   ↓
PostgreSQL
   ↓
SQL Analysis Views
   ↓
Power BI Star Schema
   ↓
DAX Measures
   ↓
Interactive Dashboard

## Technologies

- Python
- Pandas
- NumPy
- Faker
- PostgreSQL
- SQL
- Power BI
- DAX
- Git/GitHub

## Dataset

The dataset is completely synthetic and contains:

- 500 customers
- 12,000 cleaned transactions
- Transaction period: January 2025 to December 2025
- Customer segments: Mass Market, Affluent and Premium
- Account types: Current, Savings and Credit
- Multiple transaction categories
- Multiple transaction channels
- South African cities

The raw dataset intentionally contains data-quality issues including
duplicate records and missing categorical values.

## Data Engineering Workflow

### 1. Data Generation

Python is used to generate a realistic synthetic financial transaction
dataset.

The generated data includes customer attributes, transaction information,
categories, channels, dates and transaction amounts.

### 2. Data Cleaning

The cleaning pipeline:

- Standardises column names
- Converts dates and transaction amounts to appropriate data types
- Removes duplicate records
- Handles missing categorical values
- Validates transaction dates
- Validates transaction amounts
- Adds time-based analytical fields

After cleaning, the dataset contains 12,000 valid transactions.

### 3. PostgreSQL

The cleaned dataset is loaded into PostgreSQL for analytical querying.

SQL views were created for:

- Monthly transaction performance
- Category analysis
- Customer segment analysis
- Channel analysis
- Customer activity
- Monthly category trends

### 4. Power BI

Power BI connects to the PostgreSQL database and uses a star-schema model
consisting of:

- Fact table: transactions
- DimCustomer
- DimCategory
- DimChannel
- DimDate

The model uses one-to-many relationships from the dimension tables to the
transaction fact table.

### 5. DAX

DAX measures are used to calculate the core dashboard KPIs:

- Total Transaction Value
- Total Transactions
- Average Transaction Value
- Active Customers

## Dashboard

The Power BI report contains three analytical pages.

### Executive Overview

Provides a high-level view of transaction performance.

### Customer Behaviour

Analyses customer transaction activity and segment behaviour.

### Transaction Analysis

Analyses transaction channels and category trends over time.

The dashboard includes interactive slicers for customer segment, channel,
category and year.

## Key Insights

Based on the synthetic dataset:

- Total transaction value is approximately R4.37 million.
- 12,000 transactions were analysed.
- Average transaction value is approximately R363.81.
- 500 customers are represented in the dataset.
- Premium customers have the highest average transaction value.
- Mass Market customers generate the highest overall transaction value
  because of their larger customer base.
- Online transactions generate the highest transaction value among channels.
- July records the highest monthly transaction value.

## Project Structure

    investment-portfolio-dashboard/
    ├── data/
    │   ├── README.md
    │   ├── clean_transactions.csv
    │   └── raw_transactions.csv
    ├── python/
    │   ├── generate_data.py
    │   ├── clean_transactions.py
    │   └── load_to_postgres.py
    ├── sql/
    │   └── analysis_views.sql
    ├── powerbi/
    │   └── README.md
    ├── screenshots/
    ├── README.md
    └── .gitignore

## Reproducibility

The synthetic dataset can be regenerated with:

    python python/generate_data.py

The generated dataset can then be cleaned using:

    python python/clean_transactions.py

The cleaned dataset can be loaded into PostgreSQL using:

    python python/load_to_postgres.py

Database credentials are entered interactively and are not stored in the
repository.

## Disclaimer

This project uses entirely synthetic financial transaction data.

It contains no real customer information, banking records, financial
accounts or personally identifiable information.

The project is intended for portfolio demonstration, learning and technical
assessment purposes.
