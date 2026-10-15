import os
import sqlite3
from processor import IncidentDataProcessor

def run_ingestion():
    raw_path = "data/raw/incidents_dataset.csv"
    processor = IncidentDataProcessor(raw_path)
    clean_df = processor.process()
    
    os.makedirs("database", exist_ok=True)
    db_path = "database/incidents.db"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            incident_id TEXT PRIMARY KEY,
            date TEXT,
            severity_level INTEGER CHECK(severity_level BETWEEN 1 AND 4),
            sector TEXT,
            days_lost INTEGER,
            description TEXT,
            corrective_action_taken TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    for _, row in clean_df.iterrows():
        cursor.execute("""
            INSERT OR REPLACE INTO incidents 
            (incident_id, date, severity_level, sector, days_lost, description, corrective_action_taken)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row["incident_id"],
            row["date"],
            int(row["severity_level"]),
            row["sector"],
            int(row["days_lost"]),
            row["description"],
            row["corrective_action_taken"]
        ))
        
    conn.commit()
    conn.close()
    print("Ingestion pipeline executed successfully with real dataset.")

if __name__ == "__main__":
    run_ingestion()
