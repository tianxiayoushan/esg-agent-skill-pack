---
name: esg
description: "Use for practical ESG work products for listed companies and large companies; route to HKEX, A股, 上交所, 深交所, ISSB, board, investor, rating, data, or materiality skills."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
  professional_review_required: true
---

# ESG

Use this general skill to create practical ESG work products when the user has not selected a more specific ESG skill. Prefer the specific skill when the request clearly matches HKEX, A 股, 上交所, 深交所, ISSB, board, investor, data, rating, or materiality work.

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
- Reporting period, business boundary, and any explicit output-language request. Default is Chinese.

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Clarify the work product and select the most specific ESG skill if appropriate.
   - Route A股、A-share、上交所、深交所、可持续发展报告、第14号、第17号、ESG报告、社会责任报告或 A 股气候披露差距检查 to `esg-a-share-gap-check`.
   - Route HKEX、Hong Kong listed、Part D or 香港上市发行人 climate disclosure gap checks to `esg-hkex-gap-check`.
2. Read local references only as needed: [evidence policy](references/evidence-status-policy.md), [greenwashing guardrails](references/greenwashing-guardrails.md), and relevant framework placeholders.
3. Extract claims from user-provided materials and tag each claim with evidence status.
4. Convert unsupported claims into data requests, risk flags, or safer draft wording.
5. Use a local template from [assets/templates](assets/templates/board-brief-template.md) when it matches the request.
6. Classify the requested use as draft, internal working paper, board pre-read, external disclosure, regulatory filing, or investor response, and apply the strictest review language needed.
7. Apply the Chinese-first language policy; use English or bilingual output only when explicitly requested.
8. Keep assumptions separate from findings.
9. End with professional review language.

## Mandatory output structure

Use these headings for all ESG work products:

1. 执行摘要
2. 适用框架与假设
3. 关键发现
4. 实用输出：草拟措辞、表格、清单或追踪表
5. 证据状态
6. 风险提示
7. 下一步行动

## ESG evidence status rules

- `Verified`: supported by user-provided or public report material only.
- `Needs confirmation`: plausible but awaiting source, owner, legal, assurance, or management confirmation.
- `Missing data`: the required evidence is not provided.
- `Do not claim`: unsupported, promotional, misleading, or outside the provided evidence.

`Verified` does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error. If a metric is externally assured, state the assurance level separately, such as reasonable assurance, limited assurance, or assurance status not provided. Do not upgrade an item to `Verified` from general knowledge alone.

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

- Templates: [A 股 gap check](assets/templates/a-share-gap-check-template.md), [HKEX gap check](assets/templates/hkex-gap-check-template.md), [ISSB climate check](assets/templates/issb-climate-check-template.md), [board brief](assets/templates/board-brief-template.md), [investor Q&A](assets/templates/investor-qa-template.md), [data request tracker](assets/templates/data-request-tracker.csv), [rating response log](assets/templates/rating-response-log.md), [materiality issue map](assets/templates/materiality-issue-map.md).
- Examples: [A 股 gap check](examples/example-a-share-gap-check.md), [HKEX gap check](examples/example-hkex-gap-check.md), [board brief](examples/example-board-brief.md), [investor Q&A](examples/example-investor-qa.md), [data request](examples/example-data-request.md), [rating response](examples/example-rating-response.md).
