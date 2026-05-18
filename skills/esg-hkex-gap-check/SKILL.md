---
name: esg-hkex-gap-check
description: "Use for HKEX, Hong Kong listed, Part D, and climate disclosure ESG gap checks with evidence status and cautious regulatory assumptions."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: user-language
  professional_review_required: true
---

# ESG HKEX Gap Check

Prepare practical HKEX-oriented ESG gap checks for Hong Kong listed issuers. This skill structures evidence and gaps; it does not create a legal checklist.

## When to use

- The user mentions HKEX, Hong Kong listed issuers, Part D, ESG report gaps, or climate disclosure readiness.
- The user needs a gap matrix, evidence tracker, management action list, or board-ready summary.

## When not to use

- Do not use for non-HKEX frameworks unless the user asks for comparison.
- Do not state that the company is compliant unless official source text, company evidence, and professional review support that conclusion.
- Do not invent emissions, governance, assurance, or target disclosures.

## Required inputs

- Issuer name or anonymized label.
- Reporting period and listing context.
- User-provided HKEX source text or instruction to use the local placeholder only.
- ESG report draft, data pack, board paper, policies, or source notes.
- Desired output type: gap table, checklist, action tracker, or board summary.

## Workflow

1. Open [HKEX placeholder reference](references/framework-hkex-esg-code.md) and confirm it is not a legal checklist.
2. Capture framework assumptions and ask the user to verify official source text before regulatory use.
3. Map each user-provided disclosure or missing area into the [HKEX gap check template](assets/templates/hkex-gap-check-template.md).
4. Assign one evidence status to every claim and gap.
5. Convert unsupported compliance wording into `Do not claim` or `Needs confirmation`.
6. Highlight owners, due dates, and professional review needs.

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

- `Verified`: supported by user-provided HKEX source mapping and company evidence.
- `Needs confirmation`: plausible but requires legal, company secretarial, ESG, assurance, or management confirmation.
- `Missing data`: required source or company evidence is absent.
- `Do not claim`: compliance, assurance, emissions, target, or governance wording is unsupported.

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

Add this notice: Draft working paper for internal review only. Placeholder framework references do not determine regulatory compliance. Outputs must not be externally published, filed, submitted, disclosed, or included in ESG reports until approved by responsible internal reviewers and professional advisers, including legal, company secretarial, IR, ESG, finance, and assurance reviewers where applicable.

## Local resources

- Reference: [HKEX source placeholder](references/framework-hkex-esg-code.md)
- Template: [HKEX gap check template](assets/templates/hkex-gap-check-template.md)
- Example: [example HKEX gap check](examples/example-hkex-gap-check.md)
