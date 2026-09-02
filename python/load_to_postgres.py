import pandas as pd
from getpass import getpass
from sqlalchemy import create_engine, text

CSV_PATH = "data/clean_transactions.csv"

DB_HOST = "10.0.2.67"
DB_PORT = "5432"
DB_NAME = "investment_analytics"
DB_USER = "powerbi_reader"

password = getpass("Enter PostgreSQL password: ")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Loading transactions...")

df = pd.read_csv(CSV_PATH)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df.to_sql(
    "transactions",
    engine,
    if_exists="replace",
    index=False
)

with engine.connect() as conn:
    count = conn.execute(
        text("SELECT COUNT(*) FROM transactions")
    ).scalar()

print(f"Transactions loaded: {count}")
