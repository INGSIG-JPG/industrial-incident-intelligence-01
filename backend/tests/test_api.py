"""
Unit tests for Industrial Incident Intelligence FastAPI backend.
"""

import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Configurar la ruta para que Python encuentre el módulo app dentro de backend
backend_path = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_path))

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["database_connected"] is True

def test_get_incidents_structure():
    response = client.get("/api/incidents")
    assert response.status_code == 200
    data = response.json()
    assert "count" in data
    assert "data" in data
    assert isinstance(data["data"], list)
