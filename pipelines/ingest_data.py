"""
Pipeline de ingesta y validación para Industrial Incident Intelligence.
Crea la base de datos SQLite y carga registros verificados iniciales.
"""

import sqlite3
from pathlib import Path

def run_ingestion():
    # Asegurar que la carpeta database exista
    db_path = Path("database/incidents.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Crear la tabla de incidentes según el esquema relacional
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        incident_id TEXT PRIMARY KEY,
        incident_timestamp TEXT,
        sector TEXT,
        incident_type TEXT,
        severity_level INTEGER,
        days_away_from_work INTEGER,
        description TEXT
    )
    """)
    
    # Inserción de registros iniciales validados para el sistema
    verified_incidents = [
        ("INC-2026-001", "2026-10-01 08:30:00", "Manufactura", "Caída al mismo nivel", 2, 3, "Operario resbaló en área de empaque húmeda."),
        ("INC-2026-002", "2026-10-03 14:15:00", "Minería", "Atrapamiento en maquinaria", 4, 30, "Falla temporal en sensor de parada de faja transportadora."),
        ("INC-2026-003", "2026-10-05 09:00:00", "Química", "Exposición a sustancias", 1, 0, "Liberación menor de vapor inerte en válvula de alivio."),
        ("INC-2026-004", "2026-10-08 11:20:00", "Construcción", "Caída de objetos", 3, 14, "Desprendimiento parcial de material en andamio nivel 2."),
        ("INC-2026-005", "2026-10-12 16:45:00", "Logística", "Sobresfuerzo físico", 2, 5, "Lesión lumbar menor al levantar carga pesada sin asistencia.")
    ]
    
    for inc in verified_incidents:
        cursor.execute("""
        INSERT OR IGNORE INTO incidents 
        (incident_id, incident_timestamp, sector, incident_type, severity_level, days_away_from_work, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, inc)
        
    conn.commit()
    conn.close()
    print("¡Ingesta completada! Base de datos poblada con éxito en database/incidents.db")

if __name__ == "__main__":
    run_ingestion()
