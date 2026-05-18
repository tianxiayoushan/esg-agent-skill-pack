---
name: esg-investor-qa
description: "Use for ESG investor, analyst, IR, roadshow, and Q&A preparation with approved messages, safer fallbacks, and evidence status."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: user-language
  professional_review_required: true
---

# ESG Investor Q&A

Prepare cautious ESG Q&A for investor relations, analysts, roadshows, and management meetings.

## When to use

- The user mentions investor, analyst, IR, roadshow, results call, investor day, or ESG Q&A.
- The output needs approved messaging, safer fallback wording, or risk review.

## When not to use

- Do not disclose non-public or confidential information.
- Do not invent ESG metrics, targets, rating scores, customer demand impact, assurance status, or compliance status.
- Do not create market-sensitive answers without legal and IR review, including review for selective disclosure, inside information, market-sensitive information, and approved disclosure channels.

## Required inputs

- Audience and event context.
- Approved public disclosures or source pack.
- Topics likely to be raised.
- Messaging boundaries and prohibited topics.
- Review owners for IR, legal, ESG, finance, and management.

## Workflow

1. Use the [investor Q&A template](assets/templates/investor-qa-template.md).
2. Separate public facts from internal assumptions.
3. Draft concise answers with one evidence status each.
4. Create safer fallback wording for unsupported or sensitive questions.
5. Flag selective disclosure, unverified metric, target, certification, rating, or assurance risks.
6. Mark questions needing legal, IR, or management approval.

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

- `Verified`: supported by approved public disclosure or user-provided source evidence.
- `Needs confirmation`: answer requires IR, legal, ESG, finance, or management approval.
- `Missing data`: required source is not available.
- `Do not claim`: answer is unsupported, promotional, market-sensitive, or could mislead.

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

Add this notice: Draft working paper for internal review only. Confirm all ESG investor messaging with IR, legal, ESG, finance, and management reviewers before external publication, filing, submission, or disclosure, including selective disclosure, inside information, market-sensitive information, and approved disclosure channel checks.

## Local resources

- Template: [investor Q&A template](assets/templates/investor-qa-template.md)
- Example: [example investor Q&A](examples/example-investor-qa.md)
