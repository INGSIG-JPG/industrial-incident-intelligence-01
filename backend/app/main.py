from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from typing import Optional

app = FastAPI(
    title="Industrial Incident Intelligence API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.abspath(os.path.join(base_dir, "../../database/incidents.db"))
    conn = sqlite3.connect(db_path)
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
    severity_level: Optional[str] = None
):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM incidents"
    params = []
    
    if severity_level:
        query += " WHERE severity_level = ?"
        params.append(severity_level)
        
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
    
    cursor.execute("SELECT severity_level, COUNT(*) as count FROM incidents GROUP BY severity_level")
    by_severity = {row["severity_level"]: row["count"] for row in cursor.fetchall()}
    
    conn.close()
    return {
        "total_incidents": total,
        "by_severity": by_severity
    }
