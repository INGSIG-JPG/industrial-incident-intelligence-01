import csv
import random
from datetime import datetime, timedelta

NUM_RECORDS = 400
OUTPUT_FILE = "data/raw/incidents_dataset.csv"

DEPARTMENTS = ["Operations", "Maintenance", "Logistics", "Extraction", "Processing Plant"]
WORK_SHIFTS = ["Morning", "Afternoon", "Night"]
INCIDENT_TYPES = ["Near Miss", "First Aid", "Medical Treatment", "Lost Time Injury"]
INJURY_TYPES = ["None", "Cut/Laceration", "Contusion", "Burn", "Fracture", "Chemical Exposure"]
PERMIT_REQUIRED = [True, False]

def generate_data():
    random.seed(42)
    start_date = datetime(2025, 1, 1)
    records = []

    for i in range(1, NUM_RECORDS + 1):
        incident_id = f"INC-2025-{i:04d}"
        days_offset = random.randint(0, 300)
        incident_date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
        department = random.choice(DEPARTMENTS)
        shift = random.choice(WORK_SHIFTS)
        inc_type = random.choice(INCIDENT_TYPES)
        injury = random.choice(INJURY_TYPES) if inc_type != "Near Miss" else "None"
        pets_valid = random.choice([True, True, False])  # 66% compliant
        
        # Determine realistic severity level (1: Low to 4: Critical)
        if inc_type == "Near Miss":
            severity = 1
        elif inc_type == "First Aid":
            severity = 2
        elif inc_type == "Medical Treatment":
            severity = 3
        else:
            severity = 4

        records.append({
            "incident_id": incident_id,
            "date": incident_date,
            "department": department,
            "work_shift": shift,
            "incident_type": inc_type,
            "injury_type": injury,
            "permit_to_work": pets_valid,
            "severity_level": severity,
            "description": f"Industrial safety report for {inc_type.lower()} in {department} sector."
        })

    fieldnames = ["incident_id", "date", "department", "work_shift", "incident_type", "injury_type", "permit_to_work", "severity_level", "description"]
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Successfully generated {NUM_RECORDS} SST synthetic incident records at '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    generate_data()
