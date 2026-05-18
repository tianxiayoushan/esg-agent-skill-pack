---
name: esg-data-request
description: "Use for ESG data collection, ESG KPI, Scope 1, Scope 2, Scope 3, owner requests, evidence trackers, and reporting data gaps."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
  professional_review_required: true
---

# ESG Data Request

Create practical ESG data request trackers that identify owners, source systems, evidence status, and follow-up actions.

## When to use

- The user asks for ESG data collection, ESG KPI tracking, emissions data requests, source evidence, or owner follow-up.
- The request involves Scope 1, Scope 2, Scope 3, HR, safety, supplier, finance, operations, or governance data.

## When not to use

- Do not calculate emissions or KPIs without approved methodology and data.
- Do not ask for personal or sensitive data without noting privacy and legal review needs.
- Do not infer supplier audit results, diversity metrics, or safety metrics.

## Required inputs

- Reporting period and boundary.
- Framework or questionnaire driving the request.
- Data topics, KPIs, or disclosure questions.
- Known owners, departments, source systems, and due dates.
- Privacy, confidentiality, and review constraints.

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Use the [data request tracker](assets/templates/data-request-tracker.csv).
2. Translate each disclosure or questionnaire item into a specific data or evidence request.
3. Assign owner, department, source system, due date, and reviewer where known.
4. Mark evidence status for each row.
5. Flag privacy, methodology, boundary, assurance, and missing-source risks.
6. Classify the tracker as an internal working paper and state that it does not establish final ESG figures.
7. Apply the Chinese-first language policy; use an English tracker only when explicitly requested, preserving evidence status labels and risk flags.
8. End with a short owner follow-up message if requested.

## Mandatory output structure

Use these headings:

1. 执行摘要
2. 适用框架与假设
3. 关键发现
4. 实用输出：草拟措辞、表格、清单或追踪表
5. 证据状态
6. 风险提示
7. 下一步行动

## ESG evidence status rules

- `Verified`: supported by user-provided or public report material only, such as source file, system export, owner confirmation, and methodology evidence.
- `Needs confirmation`: owner or reviewer must confirm boundary, method, or source.
- `Missing data`: requested metric or source is not supplied.
- `Do not claim`: data is unsupported, unaudited beyond stated evidence, or not approved for use.

`Verified` does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error. If a metric is externally assured, state the assurance level separately, such as reasonable assurance, limited assurance, or assurance status not provided.

## Greenwashing guardrails

Do not invent or imply emissions data, Scope 1, Scope 2, Scope 3 figures, board oversight mechanisms, assurance status, ESG rating scores, supplier audit results, net zero targets, carbon neutrality, compliance status, customer demand impact, diversity metrics, or safety metrics.

- Flag unsupported phrase: industry-leading
- Flag unsupported phrase: fully compliant
- Flag unsupported phrase: carbon neutral
- Flag unsupported phrase: net zero aligned
- Flag unsupported phrase: world-class
- Flag unsupported phrase: best practice
- Flag unsupported phrase: robust governance
- Flag unsupported phrase: comprehensive controls
- Flag unsupported phrase: science-based target
- Flag unsupported phrase: no material impact

## Human review language

Add this notice: Draft working paper for internal review only. Data requests do not establish final ESG reporting figures. Final figures require source-owner confirmation, methodology review, boundary review, and where applicable finance, assurance, and legal review. Scope 1, Scope 2, and Scope 3 items must be treated as data requests only unless supported by approved methodology and source evidence.

## Local resources

- Template: [data request tracker](assets/templates/data-request-tracker.csv)
- Example: [example data request](examples/example-data-request.md)
- Department example: [department-filled data tracker example](examples/example-data-request-departments.md)
