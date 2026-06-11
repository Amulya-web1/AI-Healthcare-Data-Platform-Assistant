from sql_agent import generate_sql

question = "How many active members are in Texas?"

sql = generate_sql(question)

print("Question:")
print(question)

print("\nGenerated SQL:")
print(sql)