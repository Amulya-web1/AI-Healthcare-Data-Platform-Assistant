import ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTORSTORE_PATH = "backend/vectorstore"

def ask_rag_agent(question: str) -> str:
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a healthcare data platform support assistant.

Answer the question using only the context below.

If the context contains possible causes or troubleshooting steps, summarize them clearly.
If the exact root cause is not available, say that the exact root cause is not available, then list the possible causes and next troubleshooting steps from the context.


Context:
{context}

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