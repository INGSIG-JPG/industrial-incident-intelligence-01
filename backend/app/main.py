"""
Main Backend Application
Implements FastAPI endpoints aligned with the OpenAPI specification 
for the Industrial Incident Intelligence platform.
"""

from fastapi import FastAPI, Query
from typing import Optional, Dict, Any
from datetime import datetime

app = FastAPI(
    title="Industrial Incident Intelligence API",
    description="REST API for safety incident querying and analytical reporting.",
    version="1.0.0"
)


@app.get("/api/v1/health")
def health_check() -> Dict[str, Any]:
    """Returns the operational status of the service."""
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


@app.get("/api/v1/incidents")
def list_incidents(
    sector: Optional[str] = Query(None, description="Filter by industrial sector"),
    severity_level: Optional[int] = Query(None, description="Filter by severity level"),
    limit: int = Query(20, description="Number of items to return"),
    offset: int = Query(0, description="Offset for pagination")
) -> Dict[str, Any]:
    """Retrieves a paginated list of incident records."""
    # Placeholder response structure matching openapi.yaml
    sample_items = [
        {
            "incident_id": "123e4567-e89b-12d3-a456-426614174000",
            "incident_timestamp": "2026-10-13T14:30:00Z",
            "sector": sector or "Manufacturing",
            "incident_type": "Equipment Failure",
            "severity_level": severity_level or 2,
            "days_away_from_work": 3,
            "corrective_action_taken": True
        }
    ]
    return {
        "total": len(sample_items),
        "items": sample_items
    }


@app.get("/api/v1/analytics/summary")
def analytics_summary() -> Dict[str, Any]:
    """Returns aggregated metrics for dashboard visualizations."""
    return {
        "total_incidents": 250,
        "by_sector": {
            "Manufacturing": 120,
            "Mining": 80,
            "Logistics": 50
        },
        "by_severity": {
            "1": 100,
            "2": 90,
            "3": 40,
            "4": 20
        }
    }
