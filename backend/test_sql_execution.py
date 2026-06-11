from sql_agent import generate_sql
from sql_executor import execute_sql

question = "How many active members are in Texas?"

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

result = execute_sql(sql)

print("\nResult:")
print(result)