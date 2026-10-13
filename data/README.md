# Data Documentation

## 1. Purpose

This directory contains documentation and authorized data artifacts used by the Industrial Incident Intelligence project.

Data must be handled according to its source license, redistribution conditions, privacy restrictions, and intended analytical purpose.

## 2. Dataset Selection

**Dataset name:** To be confirmed.

**Publisher:** To be confirmed.

**Original source URL:** To be confirmed.

**License:** To be verified before use.

**Access or download date:** To be recorded.

**Observation period:** To be confirmed.

**Geographic coverage:** To be confirmed.

**Record count:** To be measured.

**Field count:** To be measured.

No dataset should be treated as approved until its provenance and permitted use have been reviewed.

## 3. Directory Conventions

* `raw/`: Original data, preserved without intentional modification when storage and licensing conditions permit.
* `interim/`: Intermediate outputs required for documented processing steps.
* `processed/`: Validated and transformed outputs used for analysis.
* `sample/`: Small, authorized, or synthetic examples used for development and testing.

Directory names describe intended roles. Actual contents and processing status must be documented.

## 4. Data Provenance

For each dataset, document:

1. Dataset title and publisher.
2. Original source and retrieval method.
3. License and redistribution restrictions.
4. Access or download date.
5. File format and encoding.
6. Dataset version or file checksum when appropriate.
7. Schema and data dictionary.
8. Known limitations and quality concerns.
9. Permitted and prohibited uses.
10. Required attribution.

## 5. Data Quality

The data quality process should evaluate, where applicable:

* Missing values.
* Duplicate records.
* Invalid data types.
* Invalid dates and ranges.
* Inconsistent categories.
* Referential integrity.
* Unexpected schema changes.
* Contradictory or impossible values.
* Missing or unreliable target labels.

Each check must have a documented rule and a reproducible verification method.

Do not remove or modify records silently. Document exclusion criteria, transformations, and their effects on the analytical dataset.

## 6. Privacy and Security

Do not commit identifiable worker records, confidential company reports, credentials, or restricted data.

Before using a dataset, evaluate whether it contains personal, sensitive, confidential, or otherwise restricted information.

Apply data minimization and use synthetic examples when real records are unnecessary for development or testing.

If the source license prohibits redistribution, document how authorized users can obtain the data without committing prohibited copies.

## 7. Reproducibility

The project should document how to obtain the authorized source data, validate its integrity, execute transformations, and reproduce the processed output.

Record relevant dependency versions, configuration, processing rules, and data versions.

Do not commit large or restricted files merely to make the repository appear self-contained.

## 8. Data Dictionary

A data dictionary must be created after the selected dataset has been inspected.

For each field, document:

* Field name.
* Data type.
* Business meaning.
* Unit, if applicable.
* Allowed values or range.
* Missing-value policy.
* Source field or transformation.
* Privacy classification, where relevant.
* Whether the field is eligible for analysis or modeling.

Do not assume that similarly named fields have the same meaning across different sources.

## 9. Target Variable and Modeling Suitability

A prediction target must not be selected until its definition, quality, and availability have been examined.

Document the target's meaning, valid values, class distribution where applicable, and limitations.

Do not claim that historical incident records support future accident forecasting unless the data structure and evaluation design support that objective.

## 10. Current Status

Dataset selection, licensing verification, schema inspection, and quality assessment must be recorded as completed only after supporting evidence is available.

