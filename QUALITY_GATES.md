# ESG Skill Pack Quality Gates

These gates define the minimum automated acceptance standard for v0.1.6 internal-pilot candidates. They are not legal, regulatory, audit, assurance, financial, or sustainability reporting conclusions.

## Gate 1: No Unsupported Legal Or Regulatory Conclusions

Forbidden in default outputs unless the phrase is inside an explicit guardrail, forbidden phrase, do-not-say, 不得表述, 禁用措辞, caution, quality gate, or regression fixture section:

- 违规
- 不合规
- 必须披露
- 已符合
- HKEX compliant
- ISSB compliant
- fully compliant
- fully met
- no material gaps
- industry-leading
- world-class
- best practice

Default replacement language:

- 潜在披露差距
- 准备度差距
- 适用性待确认
- 基于已提供材料，未识别出重大准备度差距；这不是合规结论。
- 需公司秘书 / 董办 / 证券部 / 法务 / ESG / 财务确认。

## Gate 2: No Unapproved Future Disclosure Commitments

Forbidden in default examples, templates, and sample outputs unless the sentence explicitly says the wording is prohibited, not to be used by default, or allowed only when the user provides an approved timetable:

- 将在后续报告期披露
- 将在数据条件成熟后补充披露
- 计划披露
- 预计披露
- 将披露
- 保证
- 承诺

Required replacement:

> 公司可评估是否、何时以及以何种范围披露相关信息；任何披露时间表须经管理层、证券部/公司秘书/董办、法务及相关审核人确认后方可对外使用。

If no approved plan exists, use:

> 正在评估。

## Gate 3: A 股 Unknown Status Rule

If exchange, index sample status, domestic-and-overseas listing status, report period, or rule applicability is unknown, the obligation level must stay:

> 义务层级：适用性待确认

Use this cautious explanation:

> 若公司落入适用交易所规则所列披露主体范围，相关报告义务、报告期和披露范围需由证券部、董办及法务确认。

## Gate 4: HKEX Unknown Status Rule

If issuer category, report period, LargeCap status, GEM status, Main Board status, or Part D applicability is unknown, the obligation level must stay:

> 义务层级：适用性待确认

Use this cautious explanation:

> 发行人类别、报告期、LargeCap / GEM / Main Board 状态及 Part D 义务层级需由公司秘书 / 法务确认后，方可使用强制披露或不遵守就解释等标签。

## Gate 5: Evidence Status Chinese-First

Default evidence labels must be:

- 已验证（Verified）
- 需确认（Needs confirmation）
- 缺数据（Missing data）
- 不得声称（Do not claim）

`已验证（Verified）` only means supported by user-provided or public report material. It does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error.

## Gate 6: Output Language

- Default output language is Chinese.
- English output only when the user explicitly requests English.
- Bilingual output only when the user explicitly requests bilingual output.
- Professional terms may be Chinese-first with English in brackets.

## Gate 7: Reviewer Handoff

Every work product must include reviewer handoff or equivalent reviewer routing:

- ESG
- IR
- 公司秘书 / 董办 / 证券部
- 法务
- 财务
- EHS / 运营 / 采购 where applicable
- 管理层 / 董事会 where applicable

## Gate 8: Listed-Company IR And External-Use Controls

Investor-facing outputs must include approved public channels, selective disclosure risk, inside information risk, market-sensitive information risk, and IR / legal / company secretary review.

External-use language must state that outputs are internal draft working papers and must not be externally published, filed, submitted, disclosed, included in ESG reports, or used as investor responses until responsible reviewers approve them.

## Gate 9: Institutional Memo Style

Default outputs must follow the shared output style policy:

- Chinese-first.
- No greeting.
- No polite filler.
- No explanatory preface.
- No decorative language.
- No marketing tone.
- No unsupported comparative praise.
- Use concise headings, short bullets, and compact tables.
- Prioritize conclusion, evidence status, risk flag, next action, and reviewer handoff.
- Board brief and investor Q&A outputs should be one-page friendly by default.

Forbidden filler examples may appear only inside explicit forbidden examples, 不得表述, red-team, regression, caution, or quality gate contexts.

## Gate 10: Optional Company Profile Safety

Company profile files are optional. `company_profile.local.yaml` must stay local and ignored by git.

Profile fields can reduce repeated questions but must not override professional confirmation. If a field lacks `source`, `last_reviewed`, or `confirmed_by`, outputs must treat it as an assumption, not a verified fact. Company profile data must not make skill outputs final legal, regulatory, audit, assurance, financial, sustainability reporting, or compliance conclusions.
