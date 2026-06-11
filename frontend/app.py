import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="AI Healthcare Data Platform Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AI Healthcare Data Platform Assistant")

st.write(
    "Ask questions about healthcare claims, member eligibility, data quality, troubleshooting, and documentation."
)

sample_questions = [
    "How many active members are in Texas?",
    "Why did claims ingestion fail?",
    "Check data quality for member_eligibility",
    "Generate documentation for Claims Ingestion Pipeline"
]

question = st.selectbox(
    "Choose a sample question or type your own below:",
    sample_questions
)

custom_question = st.text_input("Custom question:")

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

                st.subheader("Question")
                st.write(final_question)

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
                    st.write(result["answer"])

                if "summary" in result:
                    st.write("Data Quality Summary:")
                    st.markdown(result["summary"])

                if "raw_results" in result:
                    st.write("Raw Data Quality Results:")
                    st.json(result["raw_results"])

                if "documentation" in result:
                    st.markdown(result["documentation"])

            except Exception as e:
                st.error(f"Error connecting to API: {e}")
    else:
        st.warning("Please enter a question.")