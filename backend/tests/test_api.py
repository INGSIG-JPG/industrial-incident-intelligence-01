"""
API Unit Tests
Tests the health check and endpoint responses of the FastAPI backend.
"""

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_check():
    """Verify that the health check endpoint returns 200 OK and status ok."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "timestamp" in data


def test_list_incidents():
    """Verify that the incidents endpoint returns items and a total count."""
    response = client.get("/api/v1/incidents")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "items" in data
    assert isinstance(data["items"], list)


def test_analytics_summary():
    """Verify that the analytics summary endpoint returns aggregated metrics."""
    response = client.get("/api/v1/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_incidents" in data
    assert "by_sector" in data
    assert "by_severity" in data
