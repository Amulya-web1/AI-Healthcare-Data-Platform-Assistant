from rag_agent import ask_rag_agent

question = "Why did claims ingestion fail?"

answer = ask_rag_agent(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)