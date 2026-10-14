# Data Dictionary — Industrial Incident Intelligence

## 1. Overview and Purpose
This document establishes the official schema, data types, business meanings, allowed ranges, and missing-value handling policies for the datasets processed within the Industrial Incident Intelligence data engineering and analytical platform. It satisfies requirements for data governance, quality validation, and reproducible feature engineering.

## 2. Dataset Schema Definition
Each ingested record conforms to the following structural specification across raw, interim, and processed storage layers:

| Field Name | Data Type | Business Meaning / Description | Unit / Format | Allowed Values / Range | Missing Value Policy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `incident_id` | String (UUID / Alphanumeric) | Unique primary identifier for each safety incident record. | N/A | Non-null unique strings | Reject record (mandatory primary key) |
| `incident_timestamp` | Timestamp | Date and time when the safety incident or near-miss occurred. | ISO 8601 (`YYYY-MM-DD HH:MM:SS`) | Past timestamps up to current ingestion time | Reject record if missing |
| `sector` | Categorical String | Industrial sector or operational department where the incident took place. | N/A | `Manufacturing`, `Mining`, `Logistics`, `Construction`, `Energy` | Impute as `Unknown` with audit flag |
| `incident_type` | Categorical String | Classification of the primary event nature. | N/A | `Equipment Failure`, `Slip/Trip/Fall`, `Chemical Exposure`, `Electrical`, `Ergonomic` | Impute as `Unclassified` |
| `severity_level` | Integer / Categorical | Evaluated severity scale of the incident (Target Variable). | Ordinal Scale (1 to 4) | `1` (Minor), `2` (Moderate), `3` (Severe), `4` (Critical) | Exclude from training if missing; mandatory for supervised learning |
| `days_away_from_work` | Integer | Total number of lost workdays resulting from the incident. | Days | Integer $\ge 0$ | Impute with `0` for minor/non-lost-time incidents |
| `corrective_action_taken` | Boolean | Indicator whether immediate safety mitigation or corrective action was logged. | Boolean (`True` / `False`) | `True`, `False` | Default to `False` |

## 3. Data Quality and Validation Rules
- **Schema Enforcement**: Ingestion pipelines must validate incoming column headers and data types against this dictionary using automated validation checks (e.g., Great Expectations or Pydantic schemas).
- **Anomaly Detection**: Out-of-range timestamps, negative lost workdays, or unrecognized severity levels trigger pipeline warnings or record quarantine in the `interim/` layer.
- **Privacy Protection**: No personally identifiable information (PII) such as worker names, ID numbers, or specific personal health records are permitted in the dataset. All records must remain anonymized.
