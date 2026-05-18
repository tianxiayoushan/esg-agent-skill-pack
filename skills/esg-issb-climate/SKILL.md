---
name: esg-issb-climate
description: "Use for ISSB, IFRS S1, IFRS S2, TCFD, climate disclosure, and Scope 1, Scope 2, Scope 3 readiness work."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
  professional_review_required: true
---

# ESG ISSB Climate

Prepare ISSB-oriented climate readiness work products with cautious assumptions and clear evidence status.

## When to use

- The user mentions ISSB, IFRS S1, IFRS S2, TCFD, climate disclosure, climate readiness, or emissions data.
- The user needs a climate checklist, readiness gap table, board or management update, or data request list.

## When not to use

- Do not create a regulatory checklist from memory.
- Do not determine whether ISSB, IFRS S1, IFRS S2, TCFD, or any climate disclosure framework is mandatory without legal or professional confirmation.
- Do not claim adoption, alignment, target status, transition plan completeness, or assurance status without supplied evidence.
- Do not calculate or estimate Scope 1, Scope 2, or Scope 3 figures unless the user provides an approved method and data.

## Required inputs

- Company name or anonymized label.
- Jurisdiction and whether ISSB is mandatory, voluntary, or under consideration.
- Official source text or instruction to use placeholders only.
- Climate governance, strategy, risk, metrics, targets, and data source notes.
- Reporting period, boundary, and required output type.

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Review local placeholders for [IFRS S1](references/framework-issb-ifrs-s1.md), [IFRS S2](references/framework-issb-ifrs-s2.md), and [TCFD](references/framework-tcfd.md).
2. State source and adoption assumptions before drafting.
3. Use the [ISSB climate check template](assets/templates/issb-climate-check-template.md).
4. Separate governance, strategy, risk management, metrics, and targets only as organizing labels, not invented requirements.
5. Mark unsupported emissions, targets, scenario analysis, transition plan, or assurance claims as `Missing data` or `Do not claim`.
6. Classify whether the output is a draft readiness review, internal working paper, board pre-read, external disclosure support, or regulatory filing support.
7. Apply the Chinese-first language policy; use English board or IR wording only when explicitly requested, preserving evidence status labels and risk flags.
8. Distinguish readiness, alignment, and compliance; use readiness assessment wording unless the user explicitly asks for a binary checklist and every relevant evidence item is reviewed.
9. For Scope 3, request category coverage, materiality rationale, data quality, methodology assumptions, and omitted-category explanations.
10. Distinguish qualitative scenario discussion from quantified financial effects.
11. Do not assume financed emissions applicability unless financial activities are material and confirmed.
12. Convert gaps into owner-specific next actions.

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
- `Needs confirmation`: requires sustainability, finance, risk, legal, assurance, or management confirmation.
- `Missing data`: activity data, methodology, boundary, or source support is absent.
- `Do not claim`: the wording implies unsupported alignment, target, assurance, emissions, or compliance status.

`Verified` does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error. If a metric is externally assured, state the assurance level separately, such as reasonable assurance, limited assurance, or assurance status not provided.

Avoid `fully met`, `fully aligned`, or `compliant with ISSB`. Use `appears substantially prepared based on the provided public materials`, `no major readiness gap identified from the provided excerpts`, `strong evidence in provided materials`, `readiness assessment only`, `not a compliance conclusion`, and `requires professional review`.

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

Add this notice: Draft working paper for internal review only. Confirm climate framework applicability, mandatory status, emissions data, methodologies, targets, assurance status, filing implications, and regulatory use with ESG, finance, risk, legal, and assurance reviewers before external publication, filing, submission, or disclosure.

## Local resources

- References: [IFRS S1 placeholder](references/framework-issb-ifrs-s1.md), [IFRS S2 placeholder](references/framework-issb-ifrs-s2.md), [TCFD placeholder](references/framework-tcfd.md)
- Template: [ISSB climate check template](assets/templates/issb-climate-check-template.md)
