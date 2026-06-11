from data_quality_agent import run_data_quality_checks

table_name = "member_eligibility"

response = run_data_quality_checks(table_name)

print("\nRaw Data Quality Results:")
print(response["raw_results"])

print("\nAI Summary:")
print(response["summary"])
print(response["raw_results"])