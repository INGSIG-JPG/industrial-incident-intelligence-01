from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_get_incidents():
    response = client.get("/api/v1/incidents?limit=5&offset=0")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_analytics_summary():
    response = client.get("/api/v1/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_incidents" in data
