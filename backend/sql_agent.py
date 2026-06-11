import ollama

SCHEMA = """
Table: member_eligibility
Columns:
- member_id
- member_name
- state
- status
- plan_type
- effective_date
- termination_date

Table: claims
Columns:
- claim_id
- member_id
- provider_name
- claim_amount
- claim_status
- claim_date
- diagnosis_code
"""

REFERENCE_VALUES = """
Reference values:
- Texas is stored as TX
- Florida is stored as FL
- California is stored as CA
- New York is stored as NY
- New Jersey is stored as NJ
- Arizona is stored as AZ
- Georgia is stored as GA

Status values:
- Active
- Inactive

Rules:
- Use exact database values.
- For Texas, use 'TX', not 'Texas'.
- For active status, use 'Active', not 'active'.
"""

def generate_sql(question: str) -> str:
    prompt = f"""
You are a healthcare data engineer.

Convert the user question into SQLite SQL.

Rules:
- Return only SQL.
- Do not explain.
- Do not use markdown.
- Use only the tables and columns listed below.
- Use exact database values from the reference values.

Schema:
{SCHEMA}

{REFERENCE_VALUES}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()
