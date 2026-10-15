# Data Dictionary: Industrial Incident Intelligence

This document defines the official data schema, field types, constraints, and target definitions for the authorized datasets used in the Industrial Incident Intelligence platform.

## Field Specifications

| Field Name | Data Type | Constraint / Domain | Description |
| :--- | :--- | :--- | :--- |
| `incident_id` | String | PK, Non-null | Unique alpha-numeric identifier generated for each individual safety record. |
| `incident_timestamp` | Datetime | ISO-8601 UTC | Exact timestamp indicating when the safety incident or hazard was logged. |
| `sector` | Category | Enum: [Manufacturing, Mining, Construction, Logistics, Energy] | Industrial sector classification where the incident occurred. |
| `incident_type` | Category | String, Non-null | Nature of the safety breach, equipment failure, or hazard category. |
| `severity_level` | Integer (Ordinal) | Range: [1, 2, 3, 4] | **Target Variable**. Quantified severity tier (1: Minor / Near Miss, 2: Moderate Injury, 3: Severe Injury, 4: Critical / Fatality). |
| `days_away_from_work` | Integer | Range: $\ge 0$ | Quantified impact metric measuring productivity downtime or lost workdays. |
| `corrective_action_taken` | Boolean | True / False | Flag indicating whether immediate containment and safety compliance protocol was deployed. |

## Data Quality Rules & Validation Constraints
- **Null Handling**: Missing values in `severity_level` or `incident_timestamp` will cause ingestion records to fail validation checks and route to `data/rejected/`.
- **Primary Key Uniqueness**: `incident_id` must be unique across all ingestion batches to prevent duplication skew in downstream models.
