import sqlite3
import pandas as pd

conn = sqlite3.connect("backend/db/healthcare.db")

print("\n=== MEMBER ELIGIBILITY ===")
members = pd.read_sql(
    "SELECT * FROM member_eligibility",
    conn
)
print(members)

print("\n=== CLAIMS ===")
claims = pd.read_sql(
    "SELECT * FROM claims",
    conn
)
print(claims)

conn.close()