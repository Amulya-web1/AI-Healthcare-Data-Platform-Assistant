import streamlit as st
import requests
import os

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/ask"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(
    page_title="AI Healthcare Data Platform Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Healthcare Data Platform Assistant")

st.write(
    "Ask questions about healthcare claims, member eligibility, data quality, troubleshooting, and documentation."
)

if st.button("Clear Conversation History"):
    st.session_state.chat_history = []
    st.rerun()

sample_questions = [
    "How many active members are in Texas?",
    "Why did claims ingestion fail?",
    "Check data quality for member_eligibility",
    "Generate documentation for Claims Ingestion Pipeline"
]

question = st.selectbox(
    "Choose a sample question:",
    sample_questions
)

custom_question = st.text_input("Or type your own question:")

final_question = custom_question if custom_question else question

if st.button("Submit"):
    if final_question:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": final_question}
                )

                result = response.json()

                st.session_state.chat_history.append(
                    {
                        "question": final_question,
                        "response": result
                    }
                )

            except Exception as e:
                st.error(f"Error connecting to API: {e}")
    else:
        st.warning("Please enter a question.")

st.divider()

st.header("Latest Response")

if len(st.session_state.chat_history) > 0:
    latest = st.session_state.chat_history[-1]
    result = latest["response"]

    st.subheader("Question")
    st.write(latest["question"])

    st.subheader("Agent Used")
    st.success(result.get("agent", "Unknown"))

    st.subheader("Response")

    if "generated_sql" in result:
        st.write("Generated SQL:")
        st.code(result["generated_sql"], language="sql")

    if "result" in result:
        st.write("Query Result:")
        st.text(result["result"])

    if "answer" in result:
        st.markdown(result["answer"])

    if "summary" in result:
        st.write("Data Quality Summary:")
        st.markdown(result["summary"])

    if "raw_results" in result:
        st.write("Raw Data Quality Results:")
        st.json(result["raw_results"])

    if "documentation" in result:
        st.markdown(result["documentation"])

else:
    st.info("No response yet. Ask a question to get started.")

st.divider()

st.header("Conversation History")

if len(st.session_state.chat_history) == 0:
    st.info("No conversations yet.")
else:
    for idx, item in enumerate(
        reversed(st.session_state.chat_history),
        start=1
    ):
        response = item["response"]

        with st.expander(f"Conversation {idx}: {item['question']}"):
            st.write("Agent Used:")
            st.success(response.get("agent", "Unknown"))

            if "generated_sql" in response:
                st.write("Generated SQL:")
                st.code(response["generated_sql"], language="sql")

            if "result" in response:
                st.write("Query Result:")
                st.text(response["result"])

            if "answer" in response:
                st.markdown(response["answer"])

            if "summary" in response:
                st.write("Data Quality Summary:")
                st.markdown(response["summary"])

            if "raw_results" in response:
                st.write("Raw Data Quality Results:")
                st.json(response["raw_results"])

            if "documentation" in response:
                st.markdown(response["documentation"])