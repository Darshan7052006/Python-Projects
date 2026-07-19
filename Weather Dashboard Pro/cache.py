import json
from datetime import datetime, timedelta, timezone

from config import CACHE_FILE, CACHE_TTL_SECONDS, DATA_DIR


def _load_cache():
    if not CACHE_FILE.exists():
        return {}

    try:
        with CACHE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def get_cached_data(key):
    entry = _load_cache().get(key)
    if not entry:
        return None

    try:
        saved_at = datetime.fromisoformat(entry["saved_at"])
    except (KeyError, TypeError, ValueError):
        return None

    if datetime.now(timezone.utc) - saved_at > timedelta(seconds=CACHE_TTL_SECONDS):
        return None
    return entry.get("data")


def save_cached_data(key, data):
    DATA_DIR.mkdir(exist_ok=True)
    cache = _load_cache()
    cache[key] = {
        "saved_at": datetime.now(timezone.utc).isoformat(),
        "data": data,
    }
    with CACHE_FILE.open("w", encoding="utf-8") as file:
        json.dump(cache, file, indent=2)
