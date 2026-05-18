---
name: esg-rating-response
description: "Use for MSCI, Sustainalytics, CDP, EcoVadis, supplier questionnaire, ESG rating response logs, and evidence-backed answers."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: user-language
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

## Workflow

1. Review [rating questionnaire placeholder](references/framework-rating-questionnaires.md).
2. Use the [rating response log](assets/templates/rating-response-log.md).
3. Convert each request into a response row with source, owner, evidence status, and next action.
4. Mark unsupported answers as `Missing data` or `Do not claim`.
5. Flag rating score, supplier audit, assurance, target, and confidentiality risks.
6. Draft owner follow-up requests for missing evidence.

## Mandatory output structure

Use these headings:

1. Executive summary
2. Applicable framework and assumptions
3. Key findings
4. Practical output: draft wording, table, checklist, or tracker
5. Evidence status
6. Risk flags
7. Next actions

## ESG evidence status rules

- `Verified`: supported by the exact questionnaire request and user-provided source evidence.
- `Needs confirmation`: response requires owner, legal, IR, sustainability, procurement, or customer-review confirmation.
- `Missing data`: evidence or approved wording has not been supplied.
- `Do not claim`: answer implies unsupported score, audit result, certification, target, assurance, or compliance status.

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
