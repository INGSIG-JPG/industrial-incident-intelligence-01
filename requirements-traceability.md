# Requirements Traceability Matrix

## 1. Purpose

This matrix tracks project requirements from definition through implementation, verification, and evidence. A requirement must not be marked as verified solely because a related file exists.

## 2. Status Definitions

* **PLANNED:** Defined but not implemented.
* **IN_PROGRESS:** Implementation has started.
* **BLOCKED:** Progress depends on an unresolved issue.
* **IMPLEMENTED:** Implementation exists but verification is incomplete.
* **VERIFIED:** Acceptance criteria have been checked and supporting evidence is available.
* **NOT_APPLICABLE:** A documented reason explains why the requirement does not apply.

## 3. Requirements Matrix

| ID      | Requirement                                                  | Planned location                            | Verification method                                               | Evidence                              | Initial status |
| ------- | ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------- | -------------- |
| GOV-01  | Document project scope and expected behavior                 | `README.md`, `product-spec.md`              | Review required sections                                          | Committed documents                   | IN_PROGRESS    |
| GOV-02  | Maintain durable engineering instructions                    | `AGENTS.md`                                 | Review instructions against project workflow                      | Committed file                        | IMPLEMENTED    |
| GOV-03  | Trace requirements to implementation and tests               | `requirements-traceability.md`              | Review every requirement and evidence link                        | This matrix and linked evidence       | IN_PROGRESS    |
| DATA-01 | Document dataset source and permitted use                    | `data/README.md`, `docs/data-dictionary.md` | Verify provenance and license                                     | Source record and license reference   | PLANNED        |
| DATA-02 | Define data schema and data dictionary                       | `docs/data-dictionary.md`                   | Compare documented fields with actual data                        | Data dictionary and validation output | PLANNED        |
| DATA-03 | Detect missing, duplicate, invalid, and inconsistent records | `src/data/`, `tests/`                       | Run data quality checks                                           | Test output and quality report        | PLANNED        |
| DATA-04 | Implement reproducible transformations                       | `pipelines/`, `src/data/`                   | Re-run pipeline from documented inputs                            | Run instructions and output checks    | PLANNED        |
| DATA-05 | Prevent target leakage and invalid evaluation                | `src/features/`, `src/evaluation/`          | Review split strategy and preprocessing boundaries                | Evaluation protocol and tests         | PLANNED        |
| ANA-01  | Document business context and analytical question            | `docs/business-analysis.md`                 | Review problem, users, decisions, and evidence                    | Business analysis                     | PLANNED        |
| ANA-02  | Perform exploratory data analysis                            | `notebooks/`                                | Run notebook and inspect interpretations                          | Executed notebook and plots           | PLANNED        |
| ANA-03  | Establish a baseline model where appropriate                 | `src/models/`, `experiments/`               | Reproduce baseline evaluation                                     | Configuration and evaluation results  | PLANNED        |
| ANA-04  | Compare appropriate model alternatives                       | `experiments/`, `src/evaluation/`           | Verify consistent evaluation protocol                             | Experiment comparison                 | PLANNED        |
| ANA-05  | Document metrics, errors, and limitations                    | `docs/model-card.md`                        | Review metrics and error analysis                                 | Model card and results                | PLANNED        |
| ANA-06  | Prepare analytical presentation and references               | `deliverables/final-assignment/`            | Validate format and reproducibility against official instructions | Presentation, notebook, references    | PLANNED        |
| CMP-01  | Identify the official competition target and metric          | `deliverables/competition/`                 | Compare against the official activity instructions                | Requirement record                    | BLOCKED        |
| CMP-02  | Validate submission schema and required columns              | `deliverables/competition/`                 | Run schema and format checks                                      | Validation output                     | BLOCKED        |
| CMP-03  | Keep competition experiments reproducible                    | `experiments/`, `deliverables/competition/` | Re-run documented experiment                                      | Configuration and results             | PLANNED        |
| CMP-04  | Validate final submission package                            | `deliverables/competition/`                 | Check exact official file names, format, and package rules        | Package checklist                     | BLOCKED        |
| APP-01  | Define the application API contract                          | `openapi.yaml`                              | Validate the specification and endpoint schemas                   | Contract validation result            | PLANNED        |
| APP-02  | Implement backend behavior                                   | `backend/`                                  | Execute backend and API tests                                     | Test results                          | PLANNED        |
| APP-03  | Implement persistent storage                                 | `database/`, `backend/`                     | Verify creation, storage, retrieval, and error behavior           | Persistence test results              | PLANNED        |
| APP-04  | Implement the frontend                                       | `frontend/`                                 | Test main user workflow and error states                          | Screenshots and test results          | PLANNED        |
| APP-05  | Integrate frontend and backend                               | `frontend/`, `backend/`                     | Execute integration tests                                         | Integration test output               | PLANNED        |
| QA-01   | Implement automated unit tests                               | `tests/`                                    | Run unit test suite                                               | Test output                           | PLANNED        |
| QA-02   | Implement integration and API tests                          | `tests/`                                    | Run integration and API checks                                    | Test output                           | PLANNED        |
| QA-03   | Provide reproducible setup instructions                      | `README.md`, `docs/`                        | Follow instructions in a clean environment                        | Setup verification record             | PLANNED        |
| DEV-01  | Containerize the application                                 | `Dockerfile`, `docker-compose.yml`          | Build and run containers                                          | Build and runtime logs                | PLANNED        |
| DEV-02  | Add continuous integration                                   | `.github/workflows/`                        | Trigger workflow and inspect results                              | Successful workflow run               | PLANNED        |
| DEV-03  | Document and verify deployment                               | `docs/deployment.md`, `ops/`                | Follow deployment procedure and test deployed service             | Deployment URL and smoke test         | PLANNED        |
| OPS-01  | Document operational risks and troubleshooting               | `ops/`                                      | Review operational procedures                                     | Operational documentation             | PLANNED        |
| OPS-02  | Add appropriate logs, metrics, and alerts                    | `ops/`                                      | Verify instrumentation and alert behavior                         | Test evidence and configuration       | PLANNED        |
| SEC-01  | Keep secrets and private data out of version control         | `.gitignore`, `.env.example`, `security/`   | Inspect tracked files and configuration                           | Security review record                | PLANNED        |
| SEC-02  | Validate external inputs and handle errors safely            | `backend/`, `tests/`                        | Execute validation and negative tests                             | Test results                          | PLANNED        |
| SEC-03  | Review dependencies and security risks                       | `security/`, CI configuration               | Run appropriate security checks                                   | Scan results and remediation notes    | PLANNED        |
| AI-01   | Document AI-assisted development and review                  | `docs/ai-usage-report.md`, `AGENTS.md`      | Review representative changes and verification evidence           | AI usage report                       | PLANNED        |
| AI-02   | Implement reusable agent capabilities                        | `agent-capabilities/`                       | Execute and review the documented workflow                        | Example execution and review          | PLANNED        |
| AI-03   | Implement a specialized subagent                             | `custom-agent/`                             | Test its scope, output, and boundaries                            | Test record                           | PLANNED        |
| AI-04   | Implement an MCP tool or server                              | `mcp-server/`                               | Run protocol and tool behavior tests                              | Test output and documentation         | PLANNED        |
| AI-05   | Implement agent hooks or guardrails                          | `agent-hooks/`                              | Test allowed and blocked behavior                                 | Verification record                   | PLANNED        |
| AI-06   | Document agent permissions and limitations                   | `security/`, `custom-agent/`                | Review permissions and safeguards                                 | Security review                       | PLANNED        |
| PORT-01 | Provide a clear project demonstration                        | `docs/demo.md`                              | Follow the demonstration steps                                    | Demo instructions and evidence        | PLANNED        |
| PORT-02 | Keep documentation consistent with implementation            | `README.md`, `docs/`                        | Review links, commands, and actual behavior                       | Documentation review                  | PLANNED        |

## 4. Official Requirement Verification

Before marking course-specific or competition-specific requirements as verified:

1. Read the current official instructions.
2. Record the exact deliverable, file format, metric, and deadline where applicable.
3. Update the relevant requirement row.
4. Add the implementation path and verification method.
5. Link the actual evidence.
6. Re-check the requirement before submission.

The competition target, evaluation metric, submission columns, package name, and archive structure must not be guessed.

## 5. Evidence Policy

Acceptable evidence may include:

* Committed source files.
* Automated test results.
* Reproducible notebook outputs.
* Data quality reports.
* Model evaluation reports.
* API contract validation.
* Successful CI workflow runs.
* Deployment verification.
* Screenshots or recordings of real application behavior.
* Official submission receipts where relevant.

Evidence must correspond to the actual version being reviewed.

## 6. Release Gate

The project is ready for a release review only when:

* All mandatory requirements have a documented status.
* All applicable acceptance criteria have been evaluated.
* Blocking issues are resolved or explicitly disclosed.
* Data provenance and permitted use are documented.
* Relevant tests and security checks have been run.
* Documentation matches the actual implementation.
* Required deliverables match their official submission specifications.

A release review does not guarantee a particular competition ranking, academic grade, or external approval.

## 7. Current Project Status

The repository is in its initial documentation and architecture phase.

Most implementation, testing, deployment, analytical, and submission requirements remain planned. The matrix must be updated as evidence becomes available.
