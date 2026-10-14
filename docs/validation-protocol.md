# Validation Protocol — Industrial Incident Intelligence

## 1. Overview
This document defines the validation strategy, data splitting boundaries, and evaluation metrics for machine learning models and data pipelines within the Industrial Incident Intelligence platform.

## 2. Data Splitting & Prevention of Data Leakage
- **Train-Test Split**: Datasets will be partitioned into training (e.g., 70-80%) and testing (e.g., 20-30%) subsets to ensure unbiased generalization.
- **Temporal/Stratified Sampling**: Where temporal data or class imbalances exist, stratification or chronological splits will be applied to prevent future leakage into past observations.
- **Preprocessing Isolation**: Imputation, scaling, and feature encoding parameters must be computed strictly on the training subset and applied transformatively to validation and test subsets.

## 3. Evaluation Metrics
- **Classification Metrics**: For incident severity or categorical prediction tasks, performance will be measured using:
  - **Precision**: Minimizing false positives in high-severity predictions.
  - **Recall**: Ensuring critical safety incidents are not overlooked (minimizing false negatives).
  - **F1-Score**: Harmonic mean balancing precision and recall, particularly critical for imbalanced industrial safety logs.
- **Baseline Comparison**: All models will be evaluated against a naive or rule-based baseline to prove analytical value.

## 4. Error Analysis Protocol
- Systematic inspection of false positives and false negatives will be conducted to identify operational blind spots, data collection biases, or domain-specific limitations.
