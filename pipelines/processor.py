import pandas as pd
import os

REQUIRED_COLUMNS = [
    "incident_id", "date", "department", "work_shift", "incident_type",
    "injury_type", "permit_to_work", "severity_level", "description",
    "worker_experience_months", "hours_into_shift", "activity"
]

def process_and_validate_incidents(raw_csv_path, output_rejected_path="data/rejected/rejected_incidents.csv"):
    df = pd.read_csv(raw_csv_path)
    
    # 1. Validar columnas obligatorias
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Faltan columnas requeridas en el CSV: {missing_cols}")

    # 2. Identificar filas inválidas (Nulos, Rango de Severidad fuera de 1-4, Horas inválidas)
    invalid_mask = (
        df[REQUIRED_COLUMNS].isnull().any(axis=1) |
        (~df["severity_level"].between(1, 4)) |
        (df["hours_into_shift"] < 0) |
        (df["worker_experience_months"] < 0)
    )
    
    # Separar rechazados antes de deduplicar
    rejected_df = df[invalid_mask].copy()
    valid_df = df[~invalid_mask].copy()

    if not rejected_df.empty:
        os.makedirs(os.path.dirname(output_rejected_path), exist_ok=True)
        rejected_df.to_csv(output_rejected_path, index=False)

    # 3. Eliminar duplicados de las filas válidas
    valid_df = valid_df.drop_duplicates(subset=["incident_id"])
    
    # 4. Asegurar tipos de datos
    valid_df["date"] = pd.to_datetime(valid_df["date"]).dt.strftime("%Y-%m-%d")
    valid_df["permit_to_work"] = valid_df["permit_to_work"].astype(bool)
    valid_df["severity_level"] = valid_df["severity_level"].astype(int)
    valid_df["worker_experience_months"] = valid_df["worker_experience_months"].astype(int)
    valid_df["hours_into_shift"] = valid_df["hours_into_shift"].astype(float)

    return valid_df, len(rejected_df)
