import logging
import os

os.makedirs("logs", exist_ok=True)

log_path = os.path.join(
    os.getcwd(),
    "logs",
    "agent_audit.log"
)

logger = logging.getLogger("healthcare_ai")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)