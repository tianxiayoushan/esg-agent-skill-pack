---
name: esg-hkex-gap-check
description: "Use for HKEX, Hong Kong listed, Part D, and climate disclosure ESG gap checks with evidence status and cautious regulatory assumptions."
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
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

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as HKEX, ISSB, IFRS S1, IFRS S2, TCFD, Scope 1, Scope 2, Scope 3, MSCI, CDP, EcoVadis, and Sustainalytics.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- Preserve evidence status labels and risk flags in the requested output language; keep the four evidence status labels exactly as `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` unless the user asks for translated labels.

## Workflow

1. Open [HKEX placeholder reference](references/framework-hkex-esg-code.md) and confirm it is not a legal checklist.
2. Capture framework assumptions and ask the user to verify official source text before regulatory use.
3. Map each user-provided disclosure or missing area into the [HKEX gap check template](assets/templates/hkex-gap-check-template.md).
4. Assign one evidence status to every claim and gap.
5. Convert unsupported compliance wording into `Do not claim` or `Needs confirmation`.
6. Classify whether the output is a draft gap review, internal working paper, board pre-read, external disclosure support, or regulatory filing support.
7. Apply the Chinese-first language policy; use English board or IR wording only when explicitly requested, preserving evidence status labels and risk flags.
8. Classify each HKEX / Part D item by obligation level before describing the gap.
9. Use readiness wording unless issuer category, reporting period, and obligation level are confirmed.
10. Highlight owners, due dates, and professional review needs.

## HKEX obligation-level taxonomy

Classify each HKEX / Part D item as one of:

- `Mandatory`
- `Comply-or-explain`
- `Voluntary`
- `Applicability to confirm`
- `Not assessed`

Do not write `Part D non-compliance`, `mandatory disclosure`, or `must disclose` unless issuer category, reporting period, and obligation level are confirmed. Default to `Potential disclosure gap`, `Part D readiness gap`, `Obligation level to confirm`, `Comply-or-explain / implementation relief may apply`, and `Requires company secretary / legal confirmation`.

For Part D schedule nuance, state the assumptions cautiously:

- Part D climate disclosures apply from financial years commencing on or after 1 January 2025.
- Scope 1 and Scope 2 requirements may be mandatory depending on issuer category and HKEX timetable.
- Other Part D requirements may be comply-or-explain for non-LargeCap Main Board issuers unless mandatory status is confirmed.
- LargeCap status must be confirmed before using mandatory language.
- GEM and other issuers may have different treatment.
- Do not determine regulatory status without company secretary / legal confirmation.

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
- `Needs confirmation`: plausible but requires legal, company secretarial, ESG, assurance, or management confirmation.
- `Missing data`: required source or company evidence is absent.
- `Do not claim`: compliance, assurance, emissions, target, or governance wording is unsupported.

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

Add this notice: Draft working paper for internal review only. Placeholder framework references do not determine regulatory compliance. Outputs must not be externally published, filed, submitted, disclosed, or included in ESG reports until approved by responsible internal reviewers and professional advisers, including legal, company secretarial, IR, ESG, finance, and assurance reviewers where applicable.

## Local resources

- Reference: [HKEX source placeholder](references/framework-hkex-esg-code.md)
- Template: [HKEX gap check template](assets/templates/hkex-gap-check-template.md)
- Example: [example HKEX gap check](examples/example-hkex-gap-check.md)
