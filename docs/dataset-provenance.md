# Dataset Provenance & Data Quality

## Source
* **Type:** 100% Synthetic Data.
* **Generator:** `pipelines/generate_sample_data.py`
* **Seed:** 42 (Reproducible).
* **Record Count:** 400 rows.

## Data Generation Rules
Incident severity is modeled using antecedent OHS risk factors (work permit compliance, shift timing, worker experience, high-risk activity) with random noise to prevent target leakage.
