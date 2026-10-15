from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import Optional

app = FastAPI(
    title="Industrial Incident Intelligence API",
    version="1.0.0",
    description="API para la gestión y análisis de incidentes industriales (v1)"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect("../database/incidents.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/v1/health")
def health_check():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/incidents")
def get_incidents(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    severity: Optional[str] = None
):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM incidents"
    params = []
    
    if severity:
        query += " WHERE severity = ?"
        params.append(severity)
        
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

@app.get("/api/v1/analytics/summary")
def get_analytics_summary():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as total FROM incidents")
    total = cursor.fetchone()["total"]
    
    cursor.execute("SELECT severity, COUNT(*) as count FROM incidents GROUP BY severity")
    by_severity = {row["severity"]: row["count"] for row in cursor.fetchall()}
    
    conn.close()
    return {
        "total_incidents": total,
        "by_severity": by_severity
    }
