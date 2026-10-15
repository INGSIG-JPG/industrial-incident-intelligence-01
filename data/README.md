# Data Governance & Source Specification

## 1. Authorized Dataset Source
- **Dataset Name**: Industrial Safety and Incident Reports (OSHA / Public Workplace Safety Benchmarks)
- **Original Source**: Public repository / Open Data portal (e.g., Kaggle / OSHA Severe Injury Reports)
- **License**: Public Domain / Open Data Commons Attribution License (ODC-By)
- **Access Date**: October 2026
- **Period Covered**: Historical 3-year trailing window (2023–2026)
- **Data Governance Policy**: Raw data is stored immutably in `data/raw/`. No synthetic data will be used for final academic evaluation or metric reporting; synthetic generators (`pipelines/generate_sample_data.py`) are strictly restricted to software unit testing and CI smoke tests.

## 2. Dataset Schema Overview
- `incident_id`: Unique string identifier for each safety record.
- `incident_timestamp`: ISO-8601 formatted timestamp of the event.
- `sector`: Industrial sector classification (Manufacturing, Mining, Construction, Logistics, Energy).
- `incident_type`: Nature of the safety breach or hazard category.
- `severity_level`: Target ordinal variable representing incident severity (Scale 1 to 4).
- `days_away_from_work`: Quantified impact metric on workforce productivity.
- `corrective_action_taken`: Boolean flag indicating immediate containment compliance.
