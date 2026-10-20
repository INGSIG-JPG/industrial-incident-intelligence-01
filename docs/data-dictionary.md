# Data Dictionary - Industrial Incident Intelligence

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `incident_id` | VARCHAR / PK | Unique identifier for each incident record. |
| `date` | DATE | Date when the incident or near miss occurred. |
| `department` | VARCHAR | Operational sector (Operations, Maintenance, Logistics, etc.). |
| `work_shift` | VARCHAR | Shift timing (Morning, Afternoon, Night). |
| `incident_type` | VARCHAR | Categorization (Near Miss, First Aid, Medical Treatment, Lost Time Injury). |
| `injury_type` | VARCHAR | Specific injury classification or None. |
| `permit_to_work` | BOOLEAN | Status of work permit (PETS compliance: True/False). |
| `severity_level` | INTEGER | Target variable ranging from 1 (Low) to 4 (Critical). |
| `description` | TEXT | Narrative details of the event. |
| `worker_experience_months` | INTEGER | Tenure of the involved worker in months. |
| `hours_into_shift` | FLOAT | Hours elapsed in the work shift prior to the incident. |
| `activity` | VARCHAR | Specific high-risk activity being performed. |
