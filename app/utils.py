import hashlib
import re
from typing import Optional

def generate_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

def validate_version(version: str) -> bool:
    pattern = r"^\d+\.\d+\.\d+$"
    return bool(re.match(pattern, version))

def parse_datetime(dt_str: str) -> Optional[str]:
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(dt_str)
        return dt.isoformat()
    except:
        return None