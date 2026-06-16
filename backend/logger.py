import logging
import os

os.makedirs("logs", exist_ok=True)

log_path = os.path.join(
    os.getcwd(),
    "logs",
    "application.log"
)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("healthcare_ai")