"""
Sample Data Generator
Generates reproducible, anonymized industrial safety incident records 
compliant with the project data dictionary and governance rules.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os


def generate_sample_incidents(num_records: int = 100) -> pd.DataFrame:
    """Generates synthetic incident records for development and testing."""
    np.random.seed(42)

    sectors = ["Manufacturing", "Mining", "Logistics", "Construction", "Energy"]
    incident_types = [
        "Equipment Failure",
        "Slip/Trip/Fall",
        "Chemical Exposure",
        "Electrical",
        "Ergonomic",
    ]
    severity_levels = [1, 2, 3, 4]

    start_date = datetime.now() - timedelta(days=365)

    data = {
        "incident_id": [f"INC-{1000 + i}" for i in range(num_records)],
        "incident_timestamp": [
            (start_date + timedelta(days=int(np.random.randint(0, 365)))).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            for _ in range(num_records)
        ],
        "sector": np.random.choice(sectors, size=num_records),
        "incident_type": np.random.choice(incident_types, size=num_records),
        "severity_level": np.random.choice(
            severity_levels, size=num_records, p=[0.5, 0.3, 0.15, 0.05]
        ),
        "days_away_from_work": [
            int(np.random.choice([0, 0, 1, 3, 7, 14])) for _ in range(num_records)
        ],
        "corrective_action_taken": np.random.choice(
            [True, False], size=num_records, p=[0.8, 0.2]
        ),
    }

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    os.makedirs("data/sample", exist_ok=True)
    df_sample = generate_sample_incidents(150)
    output_path = "data/sample/incidents_sample.csv"
    df_sample.to_csv(output_path, index=False)
    print(f"Sample data successfully generated and saved to {output_path}")
