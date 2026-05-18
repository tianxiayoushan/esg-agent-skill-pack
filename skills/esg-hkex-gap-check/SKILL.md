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
- 默认证据状态采用中文优先标签：`已验证（Verified）`、`需确认（Needs confirmation）`、`缺数据（Missing data）`、`不得声称（Do not claim）`。不要默认使用英文优先的 evidence-status 裸标签。
- If English or bilingual output is explicitly requested, preserve the four evidence status labels `Verified`, `Needs confirmation`, `Missing data`, and `Do not claim` in English or bilingual form.

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

- `强制披露（Mandatory）`：仅在发行人类别、报告期和义务层级已确认时使用。
- `不遵守就解释（Comply-or-explain）`
- `自愿披露（Voluntary）`
- `适用性待确认（Applicability to confirm）`
- `未评估（Not assessed）`

Do not write `Part D non-compliance`, `mandatory disclosure`, or `must disclose` unless issuer category, reporting period, and obligation level are confirmed. Default to `潜在披露缺口（Potential disclosure gap）`, `Part D 准备度缺口（Part D readiness gap）`, `义务层级：适用性待确认（Applicability to confirm）`, `不遵守就解释 / 实施宽免可能适用（Comply-or-explain / implementation relief may apply）`, and `需公司秘书 / 法务确认（Requires company secretary / legal confirmation）`.

For Part D schedule nuance, state the assumptions cautiously:

- Part D climate disclosures apply from financial years commencing on or after 1 January 2025.
- Scope 1 and Scope 2 requirements may be mandatory depending on issuer category and HKEX timetable.
- Other Part D requirements may be comply-or-explain for non-LargeCap Main Board issuers unless mandatory status is confirmed.
- LargeCap status must be confirmed before using mandatory language.
- GEM and other issuers may have different treatment.
- Do not determine regulatory status without company secretary / legal confirmation.

## Forward-looking and regulatory-style wording controls

- Do not write `预计于下个报告期披露`, `计划在 [X] 个报告期内实现首次披露`, or `将披露` unless the user provides an approved timetable.
- Use: `公司可评估是否、何时以及以何种范围披露相关信息。`
- Use: `任何披露时间表须经管理层、公司秘书及相关审核人确认后方可对外使用。`
- If no approved plan exists, write only: `正在评估`.
- Do not write `作为主板发行人，八项社会议题均需覆盖`, `A1 要求披露`, `必须披露`, or `无法满足` unless official applicability, reporting boundary, and obligation level are confirmed by company secretary / legal reviewers.
- Use: `通常需要根据适用的 HKEX ESG Reporting Code 条文进行披露或解释，具体适用性、披露范围及义务层级需由公司秘书/法务确认。`
- Use: `可能构成披露范围缺口。`
- Use: `需进一步确认适用条文和报告边界。`
- Use `包装性表述`, `宣传性表述`, or `未经支持的概括性表述（unsupported promotional wording）` for unsupported promotional wording.

## Output style policy

Follow the local [output style policy](references/output-style-policy.md). Default to institutional memo style: Chinese-first, no greeting, no polite filler, no explanatory preface, no decorative language, no marketing tone, and no unsupported comparative praise. Use concise headings, short bullets, and compact tables. Prioritize potential gap, obligation level, evidence status, risk flag, next action, and reviewer handoff. If the gap check is long, provide the executive summary first.

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

- `已验证（Verified）`: supported by user-provided or public report material only.
- `需确认（Needs confirmation）`: plausible but requires legal, company secretarial, ESG, assurance, or management confirmation.
- `缺数据（Missing data）`: required source or company evidence is absent.
- `不得声称（Do not claim）`: compliance, assurance, emissions, target, or governance wording is unsupported.

Default output labels should read `证据状态：缺数据（Missing data）` or `证据状态：不得声称（Do not claim）`, not English-first labels.

`已验证（Verified）` does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error. If a metric is externally assured, state the assurance level separately, such as reasonable assurance, limited assurance, or assurance status not provided.

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

## Official reference layer

When repository access is available, use `references/official_references/hkex/` and `references/official_references/crosswalks/hkex_issb_crosswalk.yaml` as readiness source-map support. These files help identify Appendix C2 / Part D topic areas, obligation-level assumptions, issuer-category cautions, and HKEX ↔ ISSB comparison points. They do not determine HKEX compliance and must not be used for compliance conclusions. If issuer category, reporting period, LargeCap / GEM / Main Board status, Part D applicability, implementation relief, or company secretary / legal confirmation is missing, default to `义务层级：适用性待确认` and readiness wording.

## Local resources

- Reference: [HKEX source placeholder](references/framework-hkex-esg-code.md)
- Reference: [output style policy](references/output-style-policy.md)
- Template: [HKEX gap check template](assets/templates/hkex-gap-check-template.md)
- Example: [example HKEX gap check](examples/example-hkex-gap-check.md)
