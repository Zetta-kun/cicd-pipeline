from fastapi import FastAPI
import sys
sys.path.append(".")

from app import app
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code ==200
    assert "message" in response.json()
    assert response.json()["message"] == "Hello from CI/CD Pipeline!"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json()["app"] == "cicd-pipeline"
    assert response.json()["version"] == "1.0.0"