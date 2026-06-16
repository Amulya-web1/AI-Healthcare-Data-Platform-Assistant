import sqlite3
import pandas as pd
import os
import ollama
from backend.config import (
    OLLAMA_HOST,
    OLLAMA_MODEL
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

client = ollama.Client(
    host=OLLAMA_HOST
)
from backend.config import DATABASE_PATH

DB_PATH = DATABASE_PATH

def run_data_quality_checks(table_name: str):
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        f"SELECT * FROM {table_name}",
        conn
    )

    conn.close()

    results = {
        "table": table_name,
        "row_count": len(df),
        "null_counts": df.isnull().sum().to_dict(),
        "duplicate_count": int(df.duplicated().sum())
    }

    #Business Rule Validation
    inactive_missing_termination = df[
        (df["status"] == "Inactive") &
        (df["termination_date"].isnull())
    ]

    results["inactive_members_missing_termination_date"] = len(
        inactive_missing_termination
    )


    prompt = f"""
You are a healthcare data quality analyst.

Review the following data quality results and provide a short summary.

Business rules:
- termination_date is expected to be null for Active members.
- termination_date should be populated for Inactive members.
- inactive_members_missing_termination_date is the most important rule check.
- If inactive_members_missing_termination_date is 0, do not call this high-risk or critical.
- Column-level null counts alone should not be treated as a defect when the row-level rule check passes.

Results:
{results}

Return:
1. Overall status
2. Key findings
3. Recommended next steps
"""

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "raw_results": results,
        "summary": response["message"]["content"].strip()
    }