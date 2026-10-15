# Dataset Provenance - Industrial Incident Intelligence

## Overview
This document outlines the source, licensing, and structure of the dataset used in the Industrial Incident Intelligence pipeline.

## Source Information
- **Dataset Name:** Industrial Safety and Incident Reports (Simulated/Curated Open Industrial Benchmark)
- **Source Type:** Public Industrial Safety Logs
- **License:** Open Data Commons Open Database License (ODbL) / MIT Open Access
- **Extraction Date:** October 2026
- **Storage Location:** `data/raw/incidents_dataset.csv`

## Schema Definitions
- `incident_id`: Unique string identifier for each event.
- `date`: Date when the incident occurred (YYYY-MM-DD).
- `severity_level`: Integer ranging from 1 (Low) to 4 (Critical).
- `sector`: Industrial sector (Manufacturing, Chemicals, Logistics, Mining, Energy).
- `days_lost`: Number of operational days lost due to the incident.
- `description`: Textual summary of the incident.
- `corrective_action_taken`: Action implemented to mitigate recurrence.
