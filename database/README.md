# Database Architecture & Schema

## 1. Overview
The platform uses a lightweight relational database (SQLite for local/development and PostgreSQL-ready for production) to persist validated industrial incident records. This ensures that the FastAPI backend queries real stored data instead of hardcoded dummy dictionaries.

## 2. Relational Schema (`incidents`)

```sql
CREATE TABLE IF NOT EXISTS incidents (
    incident_id TEXT PRIMARY KEY,
    incident_timestamp TEXT NOT NULL,
    sector TEXT NOT NULL,
    incident_type TEXT NOT NULL,
    severity_level INTEGER CHECK (severity_level BETWEEN 1 AND 4),
    days_away_from_work INTEGER CHECK (days_away_from_work >= 0),
    corrective_action_taken BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## 3. Indexes for Performance
To support fast filtering and pagination required by the API contract:
- Index on `sector` for category filtering.
- Index on `severity_level` for risk analytics and prioritization.
