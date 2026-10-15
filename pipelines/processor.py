import pandas as pd
import os

class IncidentDataProcessor:
    def __init__(self, raw_data_path: str):
        self.raw_data_path = raw_data_path

    def process(self):
        if not os.path.exists(self.raw_data_path):
            raise FileNotFoundError(f"Raw data file not found at {self.raw_data_path}")
        
        df = pd.read_csv(self.raw_data_path)
        
        # Validación de duplicados
        df = df.drop_duplicates(subset=["incident_id"])
        
        # Validación de rangos y tipos de severidad (1 al 4)
        df["severity_level"] = pd.to_numeric(df["severity_level"], errors="coerce")
        valid_df = df[(df["severity_level"] >= 1) & (df["severity_level"] <= 4)].copy()
        
        # Enviar registros no válidos a cuarentena/rechazados
        rejected_df = df[~df.index.isin(valid_df.index)]
        if not rejected_df.empty:
            os.makedirs("data/rejected", exist_ok=True)
            rejected_df.to_csv("data/rejected/rejected_incidents.csv", index=False)
            
        return valid_df
