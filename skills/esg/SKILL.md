---
name: esg
description: "Use for practical ESG work products for listed companies and large companies; route to HKEX, ISSB, board, investor, rating, data, or materiality skills."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: user-language
  professional_review_required: true
---

# ESG

Use this general skill to create practical ESG work products when the user has not selected a more specific ESG skill. Prefer the specific skill when the request clearly matches HKEX, ISSB, board, investor, data, rating, or materiality work.

## When to use

- The user asks for an ESG workplan, disclosure draft, evidence tracker, gap summary, review memo, or cross-functional action list.
- The request involves listed companies or large companies and needs practical output, not generic ESG explanation.
- The user needs help choosing among the specialized ESG skills.

## When not to use

- Do not use this as a substitute for legal, assurance, audit, regulatory, or professional advice.
- Do not make compliance conclusions unless the user supplies official source text and professional confirmation.
- Do not invent data, targets, ratings, assurance, board oversight, or operational performance.

## Required inputs

- Company name or anonymized label.
- Jurisdiction, listing venue, or selected framework if known.
- Work product needed and audience.
- Source materials, notes, or explicit statement that data is unavailable.
- Reporting period, business boundary, and desired output language.

## Workflow

1. Clarify the work product and select the most specific ESG skill if appropriate.
2. Read local references only as needed: [evidence policy](references/evidence-status-policy.md), [greenwashing guardrails](references/greenwashing-guardrails.md), and relevant framework placeholders.
3. Extract claims from user-provided materials and tag each claim with evidence status.
4. Convert unsupported claims into data requests, risk flags, or safer draft wording.
5. Use a local template from [assets/templates](assets/templates/board-brief-template.md) when it matches the request.
6. Keep assumptions separate from findings.
7. End with professional review language.

## Mandatory output structure

Use these headings for all ESG work products:

1. Executive summary
2. Applicable framework and assumptions
3. Key findings
4. Practical output: draft wording, table, checklist, or tracker
5. Evidence status
6. Risk flags
7. Next actions

## ESG evidence status rules

- `Verified`: the user supplied evidence and the wording follows it.
- `Needs confirmation`: plausible but awaiting source, owner, legal, assurance, or management confirmation.
- `Missing data`: the required evidence is not provided.
- `Do not claim`: unsupported, promotional, misleading, or outside the provided evidence.

Do not upgrade an item to `Verified` from general knowledge alone.

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

Add this notice when output may be used internally or externally: Draft working paper for internal review only. Confirm all ESG, regulatory, legal, investor, assurance, financial, operational, and company-specific claims with the responsible professional owner. Outputs must not be externally published, filed, submitted, disclosed, or included in ESG reports until approved for the intended use.

## Local resources

- Templates: [HKEX gap check](assets/templates/hkex-gap-check-template.md), [ISSB climate check](assets/templates/issb-climate-check-template.md), [board brief](assets/templates/board-brief-template.md), [investor Q&A](assets/templates/investor-qa-template.md), [data request tracker](assets/templates/data-request-tracker.csv), [rating response log](assets/templates/rating-response-log.md), [materiality issue map](assets/templates/materiality-issue-map.md).
- Examples: [HKEX gap check](examples/example-hkex-gap-check.md), [board brief](examples/example-board-brief.md), [investor Q&A](examples/example-investor-qa.md), [data request](examples/example-data-request.md), [rating response](examples/example-rating-response.md).
