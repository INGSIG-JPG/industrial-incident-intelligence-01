# Architecture Specification — Industrial Incident Intelligence

## 1. System Overview
The Industrial Incident Intelligence platform is designed around a modular, end-to-end architecture separating data pipelines, persistent storage, backend API services, and an interactive frontend interface.

## 2. Architectural Components and Responsibilities
- **Data Ingestion & Pipelines (`pipelines/`)**: Responsible for reading raw safety logs, executing validation rules against the data dictionary, performing reproducible transformations, and loading cleaned data into the analytical warehouse layer.
- **Persistence Layer (`database/`)**: Stores structured incident records and analytical summaries, supporting reliable queries and state persistence across application restarts.
- **Backend API (`backend/`)**: Built to expose RESTful endpoints adhering to the OpenAPI specification (`openapi.yaml`), handling business logic, input validation, and secure database queries.
- **Frontend Interface (`frontend/`)**: Provides users with a responsive dashboard featuring data summaries, filterable incident records, and at least two core data visualizations.

## 3. Data Flow
1. Raw data is ingested into `data/raw/`.
2. Pipeline validation and transformations process records through `data/interim/` to `data/processed/`.
3. Processed data populates the database persistence layer.
4. The backend API queries the database and serves structured responses to the frontend.
