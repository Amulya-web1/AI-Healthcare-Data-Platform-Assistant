from agent_router import route_question

questions = [
    "How many active members are in Texas?",
    "Why did claims ingestion fail?",
    "Check data quality for member_eligibility",
    "Generate documentation for claims pipeline"
]

for q in questions:

    print("\nQuestion:")
    print(q)

    print("Agent Selected:")

    print(route_question(q))