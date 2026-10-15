"""
Industrial Incident Intelligence - FastAPI Backend (v1)
Strictly aligned with OpenAPI contract: /api/v1/health, /api/v1/incidents, and /api/v1/analytics/summary.
"""

from fastapi import FastAPI, HTTPException, Query
import sqlite3
from pathlib import Path
from typing import Optional

app = FastAPI(
    title="Industrial Incident Intelligence API",
    version="1.1.0",
    description="Production-ready API backed by verified industrial incident datasets."
)

DB_PATH = Path("../database/incidents.db")

def get_db_connection():
    if not DB_PATH.exists():
        alt_path = Path("database/incidents.db")
        if alt_path.exists():
            conn = sqlite3.connect(alt_path)
        else:
            raise HTTPException(status_code=500, detail="Database file not found. Run ingestion pipeline.")
    else:
        conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/v1/health")
def health_check():
    """Verifica el estado del servicio y la conexión real a la base de datos."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        return {
            "status": "online",
            "service": "Industrial Incident Intelligence API",
            "database_connected": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.get("/api/v1/incidents")
def get_incidents(
    sector: Optional[str] = Query(None, description="Filter by industrial sector"),
    severity: Optional[int] = Query(None, description="Filter by severity level (1-4)"),
    limit: int = Query(50, ge=1, le=200, description="Maximum number of records to return"),
    offset: int = Query(0, ge=0, description="Number of records to skip for pagination")
):
    """Obtiene el listado de incidentes con soporte para filtros, límite y paginación (offset)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM incidents WHERE 1=1"
    params = []
    
    if sector:
        query += " AND sector = ?"
        params.append(sector)
    if severity:
        query += " AND severity_level = ?"
        params.append(severity)
        
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Obtener el conteo total para metadatos de paginación
    count_query = "SELECT COUNT(*) as total FROM incidents WHERE 1=1"
    count_params = []
    if sector:
        count_query += " AND sector = ?"
        count_params.append(sector)
    if severity:
        count_query += " AND severity_level = ?"
        count_params.append(severity)
        
    cursor.execute(count_query, count_params)
    total_count = cursor.fetchone()["total"]
    conn.close()
    
    incidents = [dict(row) for row in rows]
    return {
        "total": total_count,
        "limit": limit,
        "offset": offset,
        "count": len(incidents),
        "data": incidents
    }

@app.get("/api/v1/analytics/summary")
def get_analytics_summary():
    """Retorna un resumen estadístico y analítico de los incidentes registrados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Total de incidentes y días perdidos
    cursor.execute("SELECT COUNT(*) as total_incidents, SUM(days_away_from_work) as total_days_lost FROM incidents")
    general_stats = dict(cursor.fetchone())
    
    # Incidentes por nivel de severidad
    cursor.execute("SELECT severity_level, COUNT(*) as count FROM incidents GROUP BY severity_level")
    severity_breakdown = [dict(row) for row in cursor.fetchall()]
    
    # Incidentes por sector industrial
    cursor.execute("SELECT sector, COUNT(*) as count FROM incidents GROUP BY sector")
    sector_breakdown = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return {
        "summary": general_stats,
        "severity_breakdown": severity_breakdown,
        "sector_breakdown": sector_breakdown
    }

# Compatibilidad temporal con la raíz
@app.get("/")
def read_root():
    return {"message": "Welcome to Industrial Incident Intelligence API. Please use /api/v1/health or /api/v1/incidents"}
