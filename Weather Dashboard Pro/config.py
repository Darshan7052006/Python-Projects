from pathlib import Path

DATA_DIR = Path("data")
CACHE_FILE = DATA_DIR / "cache.json"
LOG_FILE = DATA_DIR / "logs.txt"
DEFAULT_UNITS = "metric"
REQUEST_TIMEOUT_SECONDS = 15
CACHE_TTL_SECONDS = 600
