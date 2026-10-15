"""
Unit tests for Industrial Incident Intelligence FastAPI backend (v1).
"""

import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Configurar la ruta para que Python encuentre el módulo app dentro de backend
backend_path = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_path))

from app.main import app

client = TestClient(app)

def test_health_check():
    """Valida el endpoint de salud con el contrato /api/v1/health."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["database_connected"] is True

def test_get_incidents_structure():
    """Valida la estructura del listado de incidentes en /api/v1/incidents."""
    response = client.get("/api/v1/incidents")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "data" in data
    assert isinstance(data["data"], list)

def test_analytics_summary():
    """Valida el endpoint de resumen analítico /api/v1/analytics/summary."""
    response = client.get("/api/v1/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "severity_breakdown" in data
    assert "sector_breakdown" in data
