import os
import json
import redis
from typing import Optional, Any
import logging

logger = logging.getLogger(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

try:
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True,
        socket_connect_timeout=2
    )
    redis_client.ping()
    REDIS_AVAILABLE = True
    logger.info("connected to Redis successfully")
except Exception as e:
    REDIS_AVAILABLE = False
    logger.warning(f"cant connect to Redis: {e}")

def get_cache(key: str) -> Optional[Any]:
    if not REDIS_AVAILABLE:
        return None
    try:
        data = redis_client.get(key)
        if data:
            return json.loads(data)
    except Exception as e:
        logger.error(f"read error: {e}")
    return None

def set_cache(key: str, value: Any, expire: int = 60) -> bool:
    if not REDIS_AVAILABLE:
        return False
    try:
        redis_client.setex(key, expire, json.dumps(value, default=str))
        return True
    except Exception as e:
        logger.error(f"write error: {e}")
        return False

def delete_cache(pattern: str = "*") -> bool:
    if not REDIS_AVAILABLE:
        return False
    try:
        keys = redis_client.keys(pattern)
        if keys:
            redis_client.delete(*keys)
        return True
    except Exception as e:
        logger.error(f"delete error: {e}")
        return False

def ping() -> bool:
    if not REDIS_AVAILABLE:
        return False
    try:
        return redis_client.ping()
    except:
        return False