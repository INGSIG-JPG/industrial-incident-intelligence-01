import sqlite3
import os
from processor import process_and_validate_incidents

DB_PATH = "database/incidents.db"
RAW_CSV = "data/raw/incidents_dataset.csv"

def init_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        incident_id TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        department TEXT NOT NULL,
        work_shift TEXT NOT NULL,
        incident_type TEXT NOT NULL,
        injury_type TEXT NOT NULL,
        permit_to_work BOOLEAN NOT NULL,
        severity_level INTEGER NOT NULL,
        description TEXT,
        worker_experience_months INTEGER NOT NULL,
        hours_into_shift REAL NOT NULL,
        activity TEXT NOT NULL
    );
    """)
    # Índices exigidos
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_department ON incidents(department);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_severity ON incidents(severity_level);")
    conn.commit()

def ingest():
    valid_df, rejected_count = process_and_validate_incidents(RAW_CSV)
    
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    
    cursor = conn.cursor()
    for _, row in valid_df.iterrows():
        cursor.execute("""
        INSERT OR REPLACE INTO incidents (
            incident_id, date, department, work_shift, incident_type,
            injury_type, permit_to_work, severity_level, description,
            worker_experience_months, hours_into_shift, activity
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["incident_id"], row["date"], row["department"], row["work_shift"],
            row["incident_type"], row["injury_type"], row["permit_to_work"],
            row["severity_level"], row["description"], row["worker_experience_months"],
            row["hours_into_shift"], row["activity"]
        ))
    
    conn.commit()
    conn.close()
    print(f"Ingesta completada: {len(valid_df)} filas insertadas. Rechazadas: {rejected_count}")

if __name__ == "__main__":
    ingest()
