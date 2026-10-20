# Operations Runbook

## 1. Local Startup Guide
To run the platform locally from scratch:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r backend/requirements.txt
python pipelines/generate_sample_data.py
python pipelines/ingest_data.py
uvicorn backend.app.main:app --reload
