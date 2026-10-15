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
        return {"status": "online", "database_connected": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/incidents")
def get_incidents(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    severity_level: Optional[int] = None,
    sector: Optional[str] = None
):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM incidents WHERE 1=1"
    params = []
    
    if severity_level is not None:
        query += " AND severity_level = ?"
        params.append(severity_level)
        
    if sector:
        query += " AND sector = ?"
        params.append(sector)
        
    # Calcular el total para la paginación
    count_query = f"SELECT COUNT(*) as total FROM ({query})"
    cursor.execute(count_query, params)
    total = cursor.fetchone()["total"]
    
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    return {
        "total": total,
        "data": [dict(row) for row in rows]
    }

@app.get("/api/v1/analytics/summary")
def get_analytics_summary():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) as total_incidents, SUM(days_lost) as total_days_lost FROM incidents")
    summary_row = cursor.fetchone()
    
    cursor.execute("SELECT severity_level, COUNT(*) as count FROM incidents GROUP BY severity_level")
    severity_breakdown = [{"severity_level": row["severity_level"], "count": row["count"]} for row in cursor.fetchall()]
    
    cursor.execute("SELECT sector, COUNT(*) as count FROM incidents GROUP BY sector")
    sector_breakdown = [{"sector": row["sector"], "count": row["count"]} for row in cursor.fetchall()]
    
    conn.close()
    
    return {
        "summary": {
            "total_incidents": summary_row["total_incidents"] or 0,
            "total_days_lost": summary_row["total_days_lost"] or 0
        },
        "severity_breakdown": severity_breakdown,
        "sector_breakdown": sector_breakdown
    }
