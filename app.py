from fastapi import FastAPI
import datetime
import os

app = FastAPI(title="CI/CD Pipeline Example", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from CI/CD Pipeline!", "timestamp": datetime.datetime.now().isoformat(), "env": os.getenv("ENVIRONMENT", "development")}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/version")
def get_version():
    return {
        "app": "CI/CD Pipeline Example",
        "version": "1.0.0",
        "python_version": os.sys.version
    }

@app.get("/info")
def get_info():
    return {
        "app": "cicd-pipeline",
        "version": "1.0.0"
    }