import time
from backend.agent_router import route_question
from backend.sql_agent import generate_sql
from backend.sql_executor import execute_sql
from backend.rag_agent import ask_rag_agent
from backend.data_quality_agent import run_data_quality_checks
from backend.documentation_agent import generate_documentation
try:
    from backend.logger import logger
except ModuleNotFoundError:
    from logger import logger


def extract_table_name(question: str) -> str:
    question_lower = question.lower()

    if "claims" in question_lower:
        return "claims"

    if "member" in question_lower or "eligibility" in question_lower:
        return "member_eligibility"

    return "member_eligibility"


def answer_question(question: str):
    start_time = time.time()

    logger.info(f"QUESTION_RECEIVED | {question}")
    
    route = route_question(question)

    if route == "sql":
        sql = generate_sql(question)
        result = execute_sql(sql)

        execution_time = round(
            time.time() - start_time,
            2
        )

        logger.info(
            f"SQL_AGENT | SUCCESS | {execution_time}s | {question}"
        )

        return {
            "agent": "SQL Agent",
            "question": question,
            "generated_sql": sql,
            "result": result.to_string(index=False) if hasattr(result, "to_string") else result
        }

    if route == "rag":
        answer = ask_rag_agent(question)

        execution_time = round(
            time.time() - start_time,
            2
        )

        logger.info(
            f"RAG_AGENT | SUCCESS | {execution_time}s | {question}"
        )

        return {
            "agent": "RAG Assistant",
            "question": question,
            "answer": answer
        }

    if route == "data_quality":
        table_name = extract_table_name(question)
        dq_result = run_data_quality_checks(table_name)

        execution_time = round(
            time.time() - start_time,
            2
        )

        logger.info(
            f"DQ_AGENT | SUCCESS | {execution_time}s | {question}"
        )

        return {
            "agent": "Data Quality Agent",
            "question": question,
            "table": table_name,
            "raw_results": dq_result["raw_results"],
            "summary": dq_result["summary"]
        }

    if route == "documentation":
        component_details = """
    Claims Ingestion Pipeline

    Source:
    claims.csv

    Target:
    SQLite claims table in healthcare.db

    Processing:
    Loads claims CSV data into the local healthcare SQLite database.

    Validation:
    member_id must exist
    claim_amount should not be null
    claim_status should be Approved, Denied, or Pending

    Frequency:
    On demand for local demo

    Dependencies:
    Python, pandas, SQLite

    Monitoring:
    Manual validation through test scripts and data quality checks

    Owner:
    Healthcare Data Engineering Team
    """

    documentation = generate_documentation(component_details)

    execution_time = round(
        time.time() - start_time,
        2
    )

    logger.info(
        f"DOC_AGENT | SUCCESS | {execution_time}s | {question}"
    )

    return {
        "agent": "Documentation Agent",
        "question": question,
        "documentation": documentation
    }

    return {
        "agent": "Unknown",
        "question": question,
        "answer": "I could not determine which agent should handle this question."
    }
