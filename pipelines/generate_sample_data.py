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
        
        # Factores previos (sin fuga de información para el modelo)
        worker_experience_months = random.randint(3, 120)
        hours_into_shift = round(random.uniform(0.5, 10.5), 1)
        permit_to_work = random.choice([True, True, False])
        
        # Cálculo de severidad basado en riesgo previo + ruido aleatorio
        risk_score = 0.0
        if not permit_to_work:
            risk_score += 1.5
        if hours_into_shift > 7.0:
            risk_score += 1.0
        if worker_experience_months < 12:
            risk_score += 0.8
        if work_shift == "Night":
            risk_score += 0.5
        if activity in ["Height Work", "Chemical Handling"]:
            risk_score += 1.2
            
        risk_score += random.uniform(0.0, 1.5)
        
        if risk_score < 2.0:
            severity_level = 1
        elif risk_score < 3.5:
            severity_level = 2
        elif risk_score < 5.0:
            severity_level = 3
        else:
            severity_level = 4

        # Derivación descriptiva posterior (no se usan como features predictivas)
        if severity_level == 1:
            incident_type = "Near Miss"
            injury_type = "None"
        elif severity_level == 2:
            incident_type = "First Aid"
            injury_type = random.choice(["Cut/Laceration", "Contusion"])
        elif severity_level == 3:
            incident_type = "Medical Treatment"
            injury_type = random.choice(["Burn", "Fracture"])
        else:
            incident_type = "Lost Time Injury"
            injury_type = random.choice(["Fracture", "Chemical Exposure"])

        description = f"Incident recorded during {activity.lower()} in {department} sector ({work_shift} shift)."

        records.append({
            "incident_id": incident_id,
            "date": incident_date,
            "department": department,
            "work_shift": work_shift,
            "incident_type": incident_type,
            "injury_type": injury_type,
            "permit_to_work": permit_to_work,
            "severity_level": severity_level,
            "description": description,
            "worker_experience_months": worker_experience_months,
            "hours_into_shift": hours_into_shift,
            "activity": activity
        })

    fieldnames = [
        "incident_id", "date", "department", "work_shift", "incident_type", 
        "injury_type", "permit_to_work", "severity_level", "description", 
        "worker_experience_months", "hours_into_shift", "activity"
    ]
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Generated {NUM_RECORDS} leak-free records with unified schema at '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    generate_data()
