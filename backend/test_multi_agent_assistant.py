from multi_agent_assistant import answer_question

questions = [
    "How many active members are in Texas?",
    "Why did claims ingestion fail?",
    "Check data quality for member_eligibility",
    "Generate documentation for Claims Ingestion Pipeline"
]

for question in questions:
    print("\n" + "=" * 80)
    print("Question:")
    print(question)

    response = answer_question(question)

    print("\nAgent Used:")
    print(response["agent"])

    print("\nResponse:")
    for key, value in response.items():
        if key not in ["agent", "question"]:
            print(f"\n{key}:")
            print(value)