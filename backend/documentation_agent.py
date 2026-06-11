import ollama

def generate_documentation(component_name: str):

    prompt = f"""
You are a healthcare data engineer.

Generate concise technical documentation using only the details below.

Rules:
- Do not invent tools or platforms.
- If a detail is missing, write "Not specified".
- Keep the response under 250 words.

Component Details:
{component_name}

Format:
1. Purpose
2. Inputs
3. Processing Logic
4. Outputs
5. Data Quality Rules
6. Dependencies
7. Monitoring
8. Owner
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()