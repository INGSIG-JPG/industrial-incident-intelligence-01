# Requirements Traceability Matrix

## 1. Purpose

This document links project requirements to their implementation locations, verification methods, and supporting evidence.

The matrix is used to monitor implementation progress, prevent requirements from being overlooked, and demonstrate which capabilities have actually been verified.

## 2. Status Definitions

* `PLANNED`: The requirement has been identified but implementation has not been confirmed.
* `IN_PROGRESS`: Work on the requirement has started.
* `BLOCKED`: Work cannot proceed until a documented dependency or decision is resolved.
* `IMPLEMENTED`: An implementation exists, but verification is incomplete.
* `VERIFIED`: The acceptance criteria have been checked and supporting evidence is recorded.

A requirement must not be marked `VERIFIED` solely because a file or folder exists.

## 3. Priority Definitions

* `P0`: Essential for a valid and reproducible project.
* `P1`: Required for the planned MVP.
* `P2`: Valuable enhancement that can follow the MVP.

## 4. Requirements Matrix

| Requirement ID | Description                                              | Priority | Implementation Path                                        | Verification Method                      | Evidence Required                               | Initial Status |
| -------------- | -------------------------------------------------------- | -------- | ---------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------- | -------------- |
| DOC-001        | Maintain a complete project overview                     | P0       | `README.md`                                                | Documentation review                     | Reviewed README                                 | IN_PROGRESS    |
| DOC-002        | Define contribution and agent rules                      | P1       | `AGENTS.md`                                                | Policy review                            | Reviewed instructions                           | IN_PROGRESS    |
| DOC-003        | Define product scope and acceptance criteria             | P0       | `product-spec.md`                                          | Requirements review                      | Approved specification                          | IN_PROGRESS    |
| DOC-004        | Map requirements to implementation and evidence          | P0       | `requirements-traceability.md`                             | Matrix review                            | Updated traceability records                    | IN_PROGRESS    |
| DATA-001       | Document source provenance and permitted use             | P0       | `data/README.md`                                           | Source and license review                | Verified source reference and license           | PLANNED        |
| DATA-002       | Define the expected input schema                         | P0       | `src/data/`, `pipelines/validation/`                       | Schema validation tests                  | Test output and schema                          | PLANNED        |
| DATA-003       | Measure data quality issues                              | P0       | `pipelines/validation/`, `notebooks/02_data_quality.ipynb` | Data quality tests                       | Reproducible quality report                     | PLANNED        |
| DATA-004       | Implement documented transformations                     | P0       | `pipelines/transformation/`, `src/data/`                   | Unit and integration tests               | Transformation tests and outputs                | PLANNED        |
| DATA-005       | Track processing outputs and versions                    | P1       | `pipelines/`, `experiments/`                               | Reproducibility review                   | Configuration and output records                | PLANNED        |
| DE-001         | Implement a reproducible ingestion workflow              | P0       | `pipelines/ingestion/`                                     | Pipeline execution                       | Execution log and output verification           | PLANNED        |
| DE-002         | Create an analytical data model                          | P1       | `database/schemas/`                                        | Schema and integrity tests               | Schema and test results                         | PLANNED        |
| DE-003         | Provide analytical SQL queries                           | P1       | `database/queries/`                                        | Query tests or independent result checks | Query files and expected results                | PLANNED        |
| DE-004         | Document pipeline dependencies and recovery              | P1       | `pipelines/orchestration/`, `ops/`                         | Failure and recovery review              | Documented execution and recovery evidence      | PLANNED        |
| ANA-001        | Perform exploratory analysis                             | P1       | `notebooks/03_exploratory_analysis.ipynb`                  | Notebook execution and review            | Executed notebook and interpreted findings      | PLANNED        |
| ANA-002        | Produce at least two useful visualizations               | P1       | `frontend/`, `notebooks/`                                  | Dashboard functional test                | Captures and data verification                  | PLANNED        |
| ML-001         | Establish a justified baseline when applicable           | P1       | `src/models/`, `notebooks/05_baseline_model.ipynb`         | Reproducible experiment                  | Configuration, metrics, and results             | PLANNED        |
| ML-002         | Evaluate model performance when applicable               | P1       | `src/evaluation/`, `experiments/`                          | Validation protocol review               | Metrics, error analysis, and experiment records | PLANNED        |
| ML-003         | Document model limitations                               | P1       | `docs/model-card.md`, `docs/limitations.md`                | Model documentation review               | Completed model card                            | PLANNED        |
| APP-001        | Expose supported analytical functionality through an API | P1       | `backend/`, `openapi.yaml`                                 | API tests and contract review            | Test output and matching API specification      | PLANNED        |
| APP-002        | Connect the dashboard to actual analytical outputs       | P1       | `frontend/`, `backend/`                                    | Integration test                         | Verified API responses and dashboard outputs    | PLANNED        |
| TEST-001       | Provide automated unit tests                             | P0       | `tests/unit/`                                              | Test execution                           | Test results                                    | PLANNED        |
| TEST-002       | Verify data and pipeline integration                     | P0       | `tests/integration/`, `tests/pipeline/`                    | Integration test execution               | Test results                                    | PLANNED        |
| TEST-003       | Automate appropriate quality checks                      | P1       | `.github/workflows/`                                       | Workflow execution                       | Successful run or documented failure            | PLANNED        |
| SEC-001        | Prevent secret exposure                                  | P0       | `.gitignore`, `.env.example`, `security/`                  | Repository and configuration review      | Review findings and remediation evidence        | PLANNED        |
| SEC-002        | Document security threats and controls                   | P1       | `security/threat-model.md`, `docs/security.md`             | Threat model review                      | Documented risks and mitigations                | PLANNED        |
| PRIV-001       | Document data privacy and restrictions                   | P0       | `security/data-protection.md`, `data/README.md`            | Data governance review                   | Data classification and permitted-use evidence  | PLANNED        |
| REPRO-001      | Document setup and execution                             | P0       | `docs/setup.md`, `docs/testing.md`                         | Independent reproduction attempt         | Commands and reproduction results               | PLANNED        |
| DEL-001        | Prepare the final report                                 | P1       | `deliverables/final-report/`                               | Report review                            | Final report and references                     | PLANNED        |
| DEL-002        | Map official assessment criteria to evidence             | P0       | `deliverables/evaluation-evidence/`                        | Rubric-by-rubric review                  | Completed assessment mapping                    | BLOCKED        |

## 5. Assessment Traceability

Requirements from each applicable learning program must be entered into this matrix using the actual official instructions.

For every assessment criterion, record:

* The exact criterion or a faithful summary.
* Its source document and section.
* The deliverable that satisfies it.
* The implementation or evidence location.
* The required format and submission constraints.
* The verification method.
* The current status.

Do not assume that a common project automatically satisfies every assessment requirement. If the programs require different targets, datasets, metrics, or submission formats, maintain separate deliverables within this repository where necessary.

## 6. Evidence Log

For each verified requirement, record:

* Verification date.
* Commit or version reviewed.
* Test command or review procedure.
* Result.
* Evidence location.
* Reviewer, when applicable.
* Known issues or follow-up actions.

Evidence must be reproducible where practical. Screenshots alone are insufficient when a test log, source file, or reproducible command is necessary to establish correctness.

## 7. Review Rules

1. Review this matrix whenever a requirement or implementation changes.
2. Do not use `VERIFIED` without evidence.
3. Record blocked requirements and their dependencies.
4. Keep planned and implemented functionality clearly separated.
5. Review the complete matrix before a release or final submission.
6. Resolve or explicitly disclose unmet requirements.

## 8. Current Limitations

The initial statuses in this matrix are conservative placeholders. They must be updated after reviewing the actual files, executing relevant tests, and confirming the official assessment criteria.

The matrix is a tracking mechanism, not proof of compliance by itself.
