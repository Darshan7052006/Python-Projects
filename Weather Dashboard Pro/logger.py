import logging

from config import DATA_DIR, LOG_FILE


def get_logger():
    DATA_DIR.mkdir(exist_ok=True)
    logger = logging.getLogger("weather_dashboard")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(handler)
    return logger


logger = get_logger()
