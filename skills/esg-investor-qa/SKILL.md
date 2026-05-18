---
name: esg-investor-qa
description: "Use for ESG investor, analyst, IR, roadshow, and Q&A preparation with approved messages, safer fallbacks, and evidence status."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
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

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Use the [investor Q&A template](assets/templates/investor-qa-template.md).
2. Separate public facts from internal assumptions.
3. Draft concise answers with one evidence status each.
4. Create safer fallback wording for unsupported or sensitive questions.
5. Flag selective disclosure, unverified metric, target, certification, rating, or assurance risks.
6. Classify the output as draft Q&A, internal working paper, approved message candidate, external investor response, or regulatory filing support.
7. Apply the Chinese-first language policy; use English IR wording only when explicitly requested, preserving evidence status labels and risk flags.
8. Limit safe answers to publicly disclosed information, approved channels, and approved public channels.
9. Flag comparative claims such as "among the most comprehensive in our industry" unless source-supported and approved.
10. Avoid `Risk flags: None`; use `No material risk identified from provided materials, but IR/legal review required`.
11. Mark questions needing legal, IR, company secretary, or management approval.

## Output style policy

Follow the local [output style policy](references/output-style-policy.md). Default to institutional memo style: Chinese-first, no greeting, no polite filler, no explanatory preface, no decorative language, no marketing tone, and no unsupported comparative praise. Use concise headings, short bullets, and compact tables. Prioritize safe answer, evidence status, risk flag, next action, and reviewer handoff. Investor Q&A outputs should be one-page friendly by default; if longer detail is necessary, provide the executive summary first.

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
- `Needs confirmation`: answer requires IR, legal, ESG, finance, or management approval.
- `Missing data`: required source is not available.
- `Do not claim`: answer is unsupported, promotional, market-sensitive, or could mislead.

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

Add this notice: Draft working paper for internal review only. Confirm all ESG investor messaging with IR, legal, ESG, finance, and management reviewers before external publication, filing, submission, or disclosure, including selective disclosure, inside information, market-sensitive information, and approved disclosure channel checks.

## Official reference layer

When repository access is available, use `references/official_references/reference_registry.yaml` to identify HKEX, A-share, ISSB, and crosswalk readiness source-map assumptions behind investor-facing ESG claims. Use official references to keep answers source-aware, not to create new investor disclosures or compliance conclusions. Investor Q&A must remain limited to approved public sources and reviewer-approved channels.

## Local resources

- Reference: [output style policy](references/output-style-policy.md)
- Template: [investor Q&A template](assets/templates/investor-qa-template.md)
- Example: [example investor Q&A](examples/example-investor-qa.md)
