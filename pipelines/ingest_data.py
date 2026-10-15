"""
Industrial Incident Intelligence - Data Ingestion & Validation Pipeline
Handles raw data validation against the authorized schema and persists to SQLite.
"""

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("database/incidents.db")
RAW_DATA_PATH = Path("data/raw/incidents_sample.csv")

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            incident_id TEXT PRIMARY KEY,
            incident_timestamp TEXT NOT NULL,
            sector TEXT NOT NULL,
            incident_type TEXT NOT NULL,
            severity_level INTEGER CHECK (severity_level BETWEEN 1 AND 4),
            days_away_from_work INTEGER CHECK (days_away_from_work >= 0),
            corrective_action_taken BOOLEAN NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
