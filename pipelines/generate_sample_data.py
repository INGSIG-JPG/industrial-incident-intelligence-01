import csv
import random
from datetime import datetime, timedelta

NUM_RECORDS = 400
OUTPUT_FILE = "data/raw/incidents_dataset.csv"

DEPARTMENTS = ["Operations", "Maintenance", "Logistics", "Extraction", "Processing Plant"]
WORK_SHIFTS = ["Morning", "Afternoon", "Night"]
ACTIVITIES = ["Maintenance Work", "Heavy Lifting", "Machine Operation", "Height Work", "Chemical Handling"]

def generate_data():
    random.seed(42)
    start_date = datetime(2025, 1, 1)
    records = []

    for i in range(1, NUM_RECORDS + 1):
        incident_id = f"INC-2025-{i:04d}"
        days_offset = random.randint(0, 300)
        incident_date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
        
        department = random.choice(DEPARTMENTS)
        work_shift = random.choice(WORK_SHIFTS)
        activity = random.choice(ACTIVITIES)
        
        # Factores antecedentes (sin fuga de información)
        worker_tenure_years = round(random.uniform(0.5, 15.0), 1)
        hours_into_shift = round(random.uniform(0.1, 10.5), 1)
        permit_to_work = random.choice([True, True, False]) # True: Permiso vigente, False: Sin permiso / deficiente
        
        # Cálculo de severidad basado en factores de riesgo con ruido aleatorio
        risk_score = 0.0
        if not permit_to_work:
            risk_score += 1.5
        if hours_into_shift > 7.0: # Fatiga acumulada
            risk_score += 1.0
        if worker_tenure_years < 1.0: # Personal nuevo
            risk_score += 0.8
        if activity in ["Height Work", "Chemical Handling"]:
            risk_score += 1.2
            
        # Añadir ruido aleatorio
        risk_score += random.uniform(0.0, 1.5)
        
        # Mapeo a severidad de 1 (Leve) a 4 (Crítico)
        if risk_score < 2.0:
            severity_level = 1
        elif risk_score < 3.5:
            severity_level = 2
        elif risk_score < 5.0:
            severity_level = 3
        else:
            severity_level = 4

        records.append({
            "incident_id": incident_id,
            "date": incident_date,
            "department": department,
            "work_shift": work_shift,
            "activity": activity,
            "worker_tenure_years": worker_tenure_years,
            "hours_into_shift": hours_into_shift,
            "permit_to_work": permit_to_work,
            "severity_level": severity_level,
            "description": f"Incident recorded during {activity.lower()} in {department} ({work_shift} shift)."
        })

    fieldnames = [
        "incident_id", "date", "department", "work_shift", "activity",
        "worker_tenure_years", "hours_into_shift", "permit_to_work",
        "severity_level", "description"
    ]
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Successfully generated {NUM_RECORDS} leak-free SST incident records at '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    generate_data()
