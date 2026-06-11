from documentation_agent import generate_documentation

component = """
Claims Ingestion Pipeline

Source:
claims.csv

Target:
SQLite claims table

Processing:
Loads claims CSV data into healthcare.db

Validation:
member_id must exist
claim_amount should not be null
claim_status should be Approved, Denied, or Pending

Frequency:
On demand for local demo

Owner:
Healthcare Data Engineering Team
"""

documentation = generate_documentation(component)

print("\nGenerated Documentation:\n")
print(documentation)