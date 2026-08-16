from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["version"] == "2.0.0"
    assert "/docs" in data["docs"]

def test_datetime():
    response = client.get("/datetime")
    assert response.status_code == 200
    data = response.json()
    assert "datetime" in data
    assert "timestamp" in data

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "uptime_seconds" in data

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "cicd-pipeline"
    assert data["version"] == "2.0.0"
    assert "python_version" in data
    assert "environment" in data

def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "start_time" in data
    assert "environment" in data

def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["info"]["title"] == "CICD Pipeline App"