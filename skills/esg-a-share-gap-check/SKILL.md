---
name: esg-a-share-gap-check
description: "用于 A股、A-share、上交所、深交所、可持续发展报告、第14号、第17号、ESG报告、社会责任报告和气候披露差距检查。"
metadata:
  version: "0.1.0"
  domain: "ESG"
  last_reviewed_date: "2026-05-18"
  output_language_default: "zh-CN"
  output_language_policy: "Chinese-first unless English or bilingual output is explicitly requested"
  professional_review_required: true
---

# ESG A-share Gap Check

用于 A 股上市公司可持续发展报告、ESG 报告、社会责任报告和气候披露的差距检查与内部工作底稿。此 skill 独立于 HKEX skill，不适用于港股 Part D 判断。参考框架包括上海证券交易所上市公司自律监管指引第14号——可持续发展报告（试行）和深圳证券交易所上市公司自律监管指引第17号——可持续发展报告（试行），但本 skill 不作法律或监管结论。

## When to use

- 用户提到 A股、A-share、上交所、深交所、沪市、深市、可持续发展报告、ESG 报告、社会责任报告、气候披露、第14号、第17号。
- 用户需要对 A 股上市公司公开报告、披露草稿、数据包或议题清单做准备度差距检查。
- 用户需要判断上证180、科创50、深证100、创业板指数样本公司、境内外同时上市公司或其他自愿披露公司相关的披露主体状态。

## When not to use

- 不用于 HKEX、香港上市发行人或 Part D gap check；这些请求应使用 `esg-hkex-gap-check`。
- 不作法律、监管、审计、鉴证、财务或可持续发展报告结论。
- 不直接写“违规”“不合规”“必须披露”或“已符合上交所/深交所要求”，除非用户提供官方规则文本、公司类别、报告期和专业确认。
- 不发明排放数据、董事会监督机制、鉴证状态、ESG 评级、供应商审核结果、净零目标、碳中和或合规状态。

## Required inputs

- 公司名称或匿名标签。
- 交易所、板块、证券代码或上市地，如已知。
- 报告期间和拟使用的报告名称。
- 是否属于上证180、科创50、深证100、创业板指数样本公司、境内外同时上市公司或其他自愿披露公司。
- 用户提供的官方规则文本、公开报告片段、披露草稿、数据包或说明；如没有，明确说明缺失。
- 输出用途：内部工作底稿、董事会预读、证券部审核材料、对外披露支持或监管申报支持。

## Language policy

Default output language: Chinese (`zh-CN`). Use these rules unless the user explicitly requests otherwise:

- If the user writes in Chinese, output in Chinese.
- If the user writes in mixed Chinese/English, output in Chinese while retaining useful ESG, IR, framework, and rating terminology such as SSE, SZSE, A-share, ESG, Scope 1, Scope 2, Scope 3, 上证180, 科创50, 深证100, and 创业板指数.
- If the user writes in English but does not specify output language, prefer a Chinese summary and Chinese work product, retaining English technical terms where useful.
- Output in English only when the user explicitly requests English, an English version, English answer, investor roadshow wording in English, or board-ready English wording.
- Output bilingual content only when the user explicitly requests bilingual output.
- 默认证据状态采用中文优先标签：`已验证（Verified）`、`需确认（Needs confirmation）`、`缺数据（Missing data）`、`不得声称（Do not claim）`。
- If English or bilingual output is explicitly requested, preserve evidence status labels and risk flags in the requested output language.

## Workflow

1. Classify the request as A 股可持续发展报告 / ESG 报告 / 社会责任报告 / 气候披露差距检查；如用户实际询问 HKEX 或 Part D，转向 `esg-hkex-gap-check`。
2. Open local placeholders for [上交所第14号](references/framework-sse-sustainability-reporting-guideline.md) and [深交所第17号](references/framework-szse-sustainability-reporting-guideline.md), and state that they are not legal checklists.
3. Capture assumptions: exchange, board, report period, index constituent status, domestic-and-overseas listing status, and whether the user supplied official source text.
4. Classify the disclosure subject status before describing gaps: 上证180、科创50、深证100、创业板指数样本公司、境内外同时上市公司、其他自愿披露公司、或适用性待确认。
5. Classify each item by A 股义务层级 cautiously. If exchange, index constituent status, domestic-and-overseas listing status, report period, or rule applicability is not confirmed, default to `义务层级：适用性待确认`.
6. Map user-provided disclosures into the [A 股差距检查模板](assets/templates/a-share-gap-check-template.md).
7. Assign one evidence status to every claim and gap.
8. Convert unsupported regulatory or future-commitment wording into `不得声称（Do not claim）` or `需确认（Needs confirmation）`.
9. Classify whether the output is a draft, internal working paper, board pre-read, external disclosure support, regulatory filing support, investor response, customer response, or provider submission.
10. Apply the Chinese-first language policy; use English or bilingual output only when explicitly requested.
11. End with reviewer handoff for 证券部 / 董办 / 法务 / ESG / 财务 and any relevant operations, EHS, or procurement owner.

## A 股义务层级分类

Use these Chinese-first labels:

- `强制披露`
- `鼓励披露`
- `自愿披露`
- `适用性待确认`
- `未评估`

When company exchange, index constituent status, domestic-and-overseas listing status, report period, or rule applicability is not confirmed, do not output `义务层级：强制披露`, `义务层级：鼓励披露`, or `义务层级：自愿披露`. Default to `义务层级：适用性待确认`.

If describing a potential situation, use: `若公司确认为相关交易所规则所列强制披露主体，则该议题可能属于重点披露项；具体适用性需由证券部、董办、法务确认。`

Do not write `违规`, `不合规`, `必须披露`, or `已符合上交所/深交所要求` unless official source text, company category, report period, and professional confirmation are provided.

Default to:

- `可能需要披露`
- `潜在披露差距`
- `准备度差距`
- `适用性待确认`
- `需证券部 / 董办 / 法务 / ESG / 财务确认`

## Timing and A-share terminology controls

- Do not write fixed trading-day, day-count, or calendar-deadline language unless the user explicitly provides it.
- Use: `在主体状态确认前，所有义务层级判断均应保持为“适用性待确认”。`
- Do not write `将在后续报告期披露`, `计划于 [X] 年内实现首次披露`, `将披露`, or `预计披露` unless the user provides an approved timetable.
- Use: `公司可评估是否、何时以及以何种范围披露相关信息。`
- Use: `任何披露时间表须经管理层、证券部、董办、法务及相关审核人确认后方可对外使用。`
- If no approved plan exists, write only: `正在评估`.
- Do not default to HK-style English explain-or-comply terminology as A 股 terminology. Use `原因说明`, `改进计划`, `后续披露安排`, or `适用规则要求下的解释性说明` where relevant.
- Add this instruction in A 股 gap outputs: `不得直接判断合规或不合规。`

## Mandatory output structure

Use these headings:

1. 使用的 skill
2. 输出用途分类
3. 适用框架与假设
4. A 股披露主体判断
5. 议题差距表
6. 证据状态
7. 风险提示
8. 更审慎表述
9. 下一步行动
10. 审核交接

Also preserve the common ESG work product headings where useful: 执行摘要, 适用框架与假设, 关键发现, 实用输出, 证据状态, 风险提示, 下一步行动.

## ESG evidence status rules

- `已验证（Verified）`: supported by user-provided or public report material only.
- `需确认（Needs confirmation）`: plausible but requires securities affairs, board office, legal, ESG, finance, assurance, or management confirmation.
- `缺数据（Missing data）`: required source, methodology, boundary, issuer status, or company evidence is absent.
- `不得声称（Do not claim）`: compliance, assurance, emissions, target, governance, rating, supplier audit, or regulatory wording is unsupported.

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

Add this notice: Draft working paper for internal review only. Placeholder framework references do not determine regulatory applicability or compliance. Outputs must not be externally published, filed, submitted, disclosed, or included in sustainability, ESG, or social responsibility reports until approved by responsible reviewers, including 证券部、董办、法务、ESG、财务、管理层 and assurance reviewers where applicable.

## Local resources

- References: [上交所第14号占位参考](references/framework-sse-sustainability-reporting-guideline.md), [深交所第17号占位参考](references/framework-szse-sustainability-reporting-guideline.md)
- Template: [A 股差距检查模板](assets/templates/a-share-gap-check-template.md)
- Example: [A 股差距检查示例](examples/example-a-share-gap-check.md)
