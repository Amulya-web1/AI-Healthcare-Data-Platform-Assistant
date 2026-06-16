import sqlite3
import pandas as pd
from backend.config import DATABASE_PATH

DB_PATH = DATABASE_PATH

def execute_sql(sql_query):

    conn = sqlite3.connect(DB_PATH)

    try:
        result = pd.read_sql_query(
            sql_query,
            conn
        )

        conn.close()

        return result

    except Exception as e:

        conn.close()

        return f"Error: {str(e)}"