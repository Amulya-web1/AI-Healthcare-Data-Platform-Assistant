from fastapi import FastAPI
from pydantic import BaseModel

from backend.multi_agent_assistant import answer_question

app = FastAPI(
    title="AI Healthcare Data Platform Assistant",
    version="1.0"
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "AI Healthcare Data Platform Assistant"
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = answer_question(
        request.question
    )

    return response