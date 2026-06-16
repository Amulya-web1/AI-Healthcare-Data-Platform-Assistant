import os
import sqlite3
import pandas as pd
from backend.config import DATABASE_PATH

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "db")
DB_PATH = os.path.join(DB_DIR, "healthcare.db")

os.makedirs(DB_DIR, exist_ok=True)

members_path = os.path.join(DATA_DIR, "member_eligibility.csv")
claims_path = os.path.join(DATA_DIR, "claims.csv")

members_df = pd.read_csv(members_path)
claims_df = pd.read_csv(claims_path)

conn = sqlite3.connect(DATABASE_PATH)

members_df.to_sql(
    "member_eligibility",
    conn,
    if_exists="replace",
    index=False
)

claims_df.to_sql(
    "claims",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Healthcare database created successfully.")
print(f"Database path: {DB_PATH}")
print(f"Member records loaded: {len(members_df)}")
print(f"Claims records loaded: {len(claims_df)}")