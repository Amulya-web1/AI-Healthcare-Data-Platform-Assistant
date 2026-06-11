def route_question(question: str):

    question = question.lower()

    if any(word in question for word in [
        "how many",
        "count",
        "show",
        "list",
        "total",
        "average"
    ]):
        return "sql"

    elif any(word in question for word in [
        "why",
        "troubleshoot",
        "failure",
        "failed",
        "issue",
        "error"
    ]):
        return "rag"

    elif any(word in question for word in [
        "quality",
        "duplicate",
        "null",
        "validate",
        "validation"
    ]):
        return "data_quality"

    elif any(word in question for word in [
        "documentation",
        "document",
        "pipeline doc",
        "generate doc"
    ]):
        return "documentation"

    return "unknown"