from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import datetime
import time
import logging
from .cache import get_cache, set_cache, delete_cache

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="CICD app",
    description="Learning CICD",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

START_TIME = datetime.datetime.now()
APP_VERSION = "1.0.0"

@app.get("/", response_model=dict)
def read_root():
    uptime = datetime.datetime.now() - START_TIME
    return {
        "message": "Welcome to the CICD app!",
        "version": APP_VERSION,
        "docs": "/docs"
    }

@app.get("/datetime", response_model=dict)
def get_datetime():
    cached = get_cache("current_datetime")
    if cached:
        return cached
    
    now = datetime.datetime.now()
    response = {
        "datetime": now.isoformat(),
        "timestamp": int(time.time()),
        "timezone": str(now.tzinfo)
    }
    set_cache("current_datetime", response, expire=10)
    return response

@app.get("/health", response_model=dict)
def health_check():
    return {
        "status": "healthy",
        "uptime_seconds": (datetime.datetime.now() - START_TIME).total_seconds(),
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/version", response_model=dict)
def get_version():
    return {
        "app": "CICD app",
        "version": APP_VERSION,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/stats", response_model=dict)
def get_stats():
    cache_info ={}
    try:
        from .cache import redis_client
        cache_info = redis_client.info(section='stats')
    except Exception as e:
        cache_info = {"error": "Redis client not available"}
    
    return {
        "start_time": START_TIME.isoformat(),
        "uptime_seconds": (datetime.datetime.now() - START_TIME).total_seconds(),
        "cache_info": cache_info,
        "timestamp": datetime.datetime.now().isoformat()
    }