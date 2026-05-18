---
name: esg-rating-response
description: "Use for MSCI, Sustainalytics, CDP, EcoVadis, supplier questionnaire, ESG rating response logs, and evidence-backed answers."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
  professional_review_required: true
---

# ESG Rating Response

Prepare evidence-backed response trackers for ESG ratings, investor questionnaires, customer requests, and supplier questionnaires.

## When to use

- The user mentions MSCI, Sustainalytics, CDP, EcoVadis, supplier questionnaire, customer ESG questionnaire, or rating response.
- The output needs a response log, evidence map, data request, or safer draft wording.

## When not to use

- Do not predict or invent ESG rating scores or methodology outcomes.
- Do not imply supplier audit results, target validation, assurance, or compliance status without evidence.
- Do not submit final answers without owner and professional review.

## Required inputs

- Questionnaire or request text.
- Provider, customer, investor, or requester name.
- Deadline, submission format, and owner list.
- Source documents or approved public disclosures.
- Review and confidentiality constraints.

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Review [rating questionnaire placeholder](references/framework-rating-questionnaires.md).
2. Use the [rating response log](assets/templates/rating-response-log.md).
3. Convert each request into a response row with source, owner, evidence status, and next action.
4. Mark unsupported answers as `Missing data` or `Do not claim`.
5. Flag rating score, supplier audit, assurance, target, and confidentiality risks.
6. Classify the response as a draft, internal working paper, customer response candidate, provider submission, or external disclosure support.
7. Apply the Chinese-first language policy; use English customer or rating response wording only when explicitly requested, preserving evidence status labels and risk flags.
8. For ESG rating scores, require rating agency, date or period, scope, and source.
9. State that ratings do not imply absence of ESG risk or regulatory compliance.
10. Do not add internal estimates or forward-looking statements unless approved.
11. For supplier audit wording, distinguish all suppliers, key suppliers, relevant suppliers, audited suppliers, and supplier self-assessment or questionnaire responses.
12. Draft owner follow-up requests for missing evidence.

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

- `Verified`: supported by user-provided or public report material only.
- `Needs confirmation`: response requires owner, legal, IR, sustainability, procurement, or customer-review confirmation.
- `Missing data`: evidence or approved wording has not been supplied.
- `Do not claim`: answer implies unsupported score, audit result, certification, target, assurance, or compliance status.

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

Add this notice: Draft working paper for internal review only. Confirm questionnaire interpretation, evidence, confidentiality, legal review, customer or provider submission requirements, and submission approval with the responsible professional owners before sending. Do not submit, externally disclose, or include responses in ESG reports until approved for that use.

## Local resources

- Reference: [rating questionnaire placeholder](references/framework-rating-questionnaires.md)
- Template: [rating response log](assets/templates/rating-response-log.md)
- Example: [example rating response](examples/example-rating-response.md)
