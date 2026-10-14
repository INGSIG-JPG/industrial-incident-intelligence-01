"""
Data Processing Module
Handles data loading, schema validation against the data dictionary, 
and preprocessing for industrial incident records.
"""

import pandas as pd
import numpy as np
from typing import Tuple, Optional


class IncidentDataProcessor:
    """Processes raw industrial safety incident datasets with strict validation rules."""

    def __init__(self, filepath: Optional[str] = None):
        self.filepath = filepath
        self.df: Optional[pd.DataFrame] = None

    def load_data(self) -> pd.DataFrame:
        """Loads dataset from CSV file."""
        if not self.filepath:
            raise ValueError("Filepath is not provided.")
        self.df = pd.read_csv(self.filepath)
        return self.df

    def validate_schema(self, df: pd.DataFrame) -> bool:
        """Validates essential columns against the project data dictionary."""
        required_columns = [
            "incident_id",
            "incident_timestamp",
            "sector",
            "incident_type",
            "severity_level",
        ]
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing mandatory columns: {missing_cols}")
        return True

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Performs data cleaning: handles missing values and standardizes formats."""
        cleaned_df = df.copy()
        
        # Ensure timestamp is datetime format
        if "incident_timestamp" in cleaned_df.columns:
            cleaned_df["incident_timestamp"] = pd.to_datetime(
                cleaned_df["incident_timestamp"], errors="coerce"
            )

        # Impute categorical missing values
        if "sector" in cleaned_df.columns:
            cleaned_df["sector"] = cleaned_df["sector"].fillna("Unknown")

        if "incident_type" in cleaned_df.columns:
            cleaned_df["incident_type"] = cleaned_df["incident_type"].fillna("Unclassified")

        # Drop rows where critical primary key or severity is missing
        cleaned_df = cleaned_df.dropna(subset=["incident_id", "severity_level"])

        return cleaned_df
