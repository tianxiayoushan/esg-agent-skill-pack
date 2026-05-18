---
name: esg-board-brief
description: "Use for ESG board brief, board paper, directors, and management update drafting with decisions, risk flags, and evidence status."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: user-language
  professional_review_required: true
---

# ESG Board Brief

Create concise ESG board and management materials that separate facts, assumptions, risks, decisions, and next actions.

## When to use

- The user asks for a board brief, board paper, directors' update, committee paper, or management update.
- The output needs decision points, risk flags, or a practical meeting-ready summary.

## When not to use

- Do not invent board oversight mechanisms, approvals, committee mandates, or minutes.
- Do not present management plans as approved board decisions.
- Do not draft external disclosure conclusions unless the user supplies approved evidence.

## Required inputs

- Audience: board, committee, directors, or management.
- Meeting purpose, date if known, and requested decision or discussion.
- Source notes, policies, reporting timetable, or ESG workstream update.
- Framework assumptions and review owners.
- Desired length and output language.

## Workflow

1. Identify the decision, discussion, or update the board needs.
2. Use the [board brief template](assets/templates/board-brief-template.md).
3. Convert source notes into short findings with evidence status.
4. Separate management recommendations from board decisions.
5. List risk flags for unsupported claims, missing metrics, external disclosure sensitivity, and assurance needs.
6. Classify the paper as a draft, internal working paper, board pre-read, external disclosure support, or regulatory filing support.
7. If the user asks in Chinese but needs English board wording, draft in English while preserving evidence status labels and risk flags.
8. Add next actions with owners.

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

- `Verified`: supported by user-provided board, management, policy, or source evidence.
- `Needs confirmation`: requires management, company secretarial, legal, ESG, finance, or assurance confirmation.
- `Missing data`: the source needed for board-level discussion is absent.
- `Do not claim`: the wording implies unsupported approval, oversight, performance, target, or compliance status.

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

Add this notice: Draft working paper for internal review only. Confirm board remit, meeting context, management recommendations, legal implications, disclosure sensitivity, and any proposed board decision wording with the board secretary, company secretarial, legal, ESG, and finance owners. Do not externally publish, file, submit, disclose, or include board-brief content in ESG reports until approved for that use.

## Local resources

- Template: [board brief template](assets/templates/board-brief-template.md)
- Example: [example board brief](examples/example-board-brief.md)
