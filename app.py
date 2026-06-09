from FastAPI import FastAPI
import datetime
import os

app = FastAPI(title="CI/CD Pipeline Example, version 1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello, World!", "timestamp": datetime.datetime.now().isoformat(), "env": os.getenv("ENVIRONMENT", "development")}

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

