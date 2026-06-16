import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1"
)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "backend/db/healthcare.db"
)

VECTORSTORE_PATH = os.getenv(
    "VECTORSTORE_PATH",
    "backend/vectorstore"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)