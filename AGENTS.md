# Project Engineering Instructions

## 1. Project Mission


Build Industrial Incident Intelligence, a reproducible and secure platform that integrates data engineering, analytical modeling, and full-stack software development to support evidence-based industrial safety decisions.

All project documentation, code comments, technical specifications, commit messages, and user-facing application text must be written in English unless a specific external requirement states otherwise.

## 2. Engineering Principles

* Prefer simple, maintainable, modular solutions over unnecessary complexity.
* Define requirements and acceptance criteria before implementation.
* Reuse components when their behavior and requirements are compatible.
* Keep analytical experiments separate from production application code.
* Never claim that a feature, test, deployment, or requirement is complete without verifiable evidence.
* Document assumptions, limitations, risks, and unresolved questions.
* Never fabricate datasets, metrics, citations, experiment results, or test outcomes.

## 3. Data Governance

* Document every dataset's source, license, permitted use, schema, and limitations before use.
* Never commit credentials, private information, or restricted course materials.
* Do not publish raw or processed datasets unless their licenses and privacy implications permit it.
* Record data quality checks, transformation rules, and reproducibility instructions.
* Maintain a clear distinction between raw, validated, and processed data.
* Detect duplicates, missing values, inconsistent types, invalid records, and potential target leakage.
* Fit preprocessing transformations on training data only, then apply them to validation and test data.
* Preserve appropriate separation between training, validation, and final evaluation.

## 4. Analytical Integrity

* Define the analytical question, intended users, target variable, and evaluation criteria before modeling.
* Establish a simple baseline before testing more complex models.
* Choose metrics appropriate to the problem and explain why they are useful.
* Evaluate errors, class imbalance, uncertainty, and potential bias.
* Record experiment configurations, random seeds where appropriate, and results.
* Never describe classification of recorded incidents as forecasting future accidents without evidence and a suitable prediction design.
* Treat model outputs as decision support, not as a replacement for professional safety judgment.

## 5. Application Architecture

* Maintain a clear separation between frontend, backend, data processing, model evaluation, and persistence.
* Define and maintain an OpenAPI contract for the backend API.
* Validate inputs at system boundaries.
* Use explicit schemas and meaningful error responses.
* Implement persistent storage with documented migrations or initialization procedures.
* Keep configuration separate from application logic.
* Provide a safe example configuration file without real secrets.
* Document architecture decisions when they materially affect the system.

## 6. Testing and Quality Assurance

* Add automated tests for important business rules and data transformations.
* Test API behavior, validation failures, and persistence.
* Add integration and end-to-end tests as the application matures.
* Test data pipelines and model evaluation logic independently.
* Use representative test fixtures without exposing sensitive data.
* Run applicable checks before accepting a change.
* Report failed, skipped, and unexecuted tests honestly.
* Never state that tests passed unless their actual results are available.

## 7. Security and Operations

* Apply least-privilege access and secure configuration practices.
* Never expose tokens, passwords, private keys, or production credentials.
* Review dependencies and document known security limitations.
* Use containerization and automated delivery checks as implementation progresses.
* Separate development and production configuration.
* Document deployment, rollback, backups, troubleshooting, and operational limitations.
* Provide observability appropriate to the maturity and scale of the application.
* Restrict automated agents to the minimum permissions needed for their tasks.

## 8. AI-Assisted Development

* Give coding agents explicit context, scope, constraints, and acceptance criteria.
* Divide large tasks into small, independently verifiable changes.
* Review generated code instead of accepting it automatically.
* Use independent verification for important changes.
* Record meaningful AI assistance, human review, and verification in the project documentation.
* Document agent capabilities, tools, permissions, and guardrails.
* Do not allow agents to publish secrets, deploy unreviewed changes, or perform destructive actions without appropriate authorization.

## 9. Documentation and Traceability

* Maintain a requirements traceability matrix.
* Link each requirement to its implementation location, verification method, evidence, and status.
* Distinguish planned, in-progress, blocked, implemented, and verified work.
* Keep the README aligned with the actual state of the application.
* Document setup, execution, testing, data provenance, model evaluation, and deployment.
* Keep analytical reports and business claims supported by reproducible evidence.

## 10. Definition of Done

A task can be marked verified only when:

1. Its purpose and acceptance criteria are documented.
2. The implementation exists in the repository.
3. Relevant tests or other appropriate verification have been executed.
4. Results and limitations are recorded.
5. Documentation is updated.
6. No known critical security or data-governance issue is left undisclosed.

If a requirement cannot be verified, mark it as pending or blocked and explain what is missing.

## 11. Change Management

* Prefer small, focused commits with descriptive messages.
* Avoid unrelated changes in a single commit.
* Review changes for regressions, security issues, and accidental data exposure.
* Preserve reproducibility and backward compatibility where practical.
* Do not remove evidence or overwrite important work without understanding its purpose.

## 12. Working Rule

Before implementing a new feature, inspect the relevant requirements, repository structure, existing code, and tests. Propose the smallest sound implementation, apply it, verify it, and document the outcome. Do not invent missing requirements; record questions that require confirmation.

