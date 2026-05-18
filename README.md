# ESG Skill Pack

## Start Here

这是一个给 ESG、IR、公司秘书、法务、财务、运营、EHS、采购团队使用的 ESG 工作助手包。你不需要懂 Git、终端或 Agent Skills 才能理解它能做什么。

它可以帮你把公开 ESG 报告片段、披露草稿、投资者问题、客户问卷或跨部门数据收集需求，整理成中文优先的工作底稿，并明确标出：

- 哪些说法有资料支持。
- 哪些说法还需要确认。
- 哪些数据缺失。
- 哪些话不应该对外说。
- 下一步该找谁补资料或审核。

它不能替代法律意见、监管意见、审计、鉴证、财务意见、可持续发展报告专业判断、公司秘书确认或董事会批准。所有输出都是内部工作底稿。

最常用的 3 个任务：

1. 检查 ESG / 气候披露有没有潜在缺口。
2. 准备投资者 ESG Q&A 或董事会 ESG 简报。
3. 生成跨部门 ESG 数据收集 tracker 或客户/评级问卷回复日志。

不要上传：未披露财务数据、董事会材料、客户/供应商机密资料、员工个人信息、未发布 ESG 报告全文、内幕消息、市场敏感信息、密码、token、密钥或合同敏感条款。

For pilot rollout instructions, see [PILOT_GUIDE.md](PILOT_GUIDE.md). For release notes and known limitations, see [CHANGELOG.md](CHANGELOG.md).

CI note for technical owners: GitHub Actions runs the same local validation commands on push and pull request.

## v0.2 Official Rules Reference Pack

v0.2 adds an official rules reference pack under [official_references](official_references/). It tracks official source metadata, `last_reviewed_date`, source URLs, topic maps, obligation matrices, and crosswalks for HKEX, A 股, and ISSB.

It helps the agent ask fewer repeated framework questions, but it is still not legal advice, regulatory advice, audit advice, assurance advice, financial advice, sustainability reporting advice, a filing opinion, or a compliance conclusion.

Packaging note: installed skills include local official source-map copies under each skill's `references/official_references/` folder, so Hermes, Codex, Claude Code, and OpenClaw do not need access to the repository root at runtime.

Important boundaries:

- HKEX, A 股, and ISSB references are separated.
- 港股 / HKEX work should use `esg-hkex-gap-check`.
- A 股 / 上交所 / 深交所 work should use `esg-a-share-gap-check`.
- ISSB / IFRS S1 / IFRS S2 work should use `esg-issb-climate`.
- A 股 and HKEX rules must not be mixed.
- Official source summaries are source-map support only. They must be checked against official source text and professional reviewers before external use.

## 30 秒理解

这是一个 ESG 工作助手包，不是 ESG 合规意见。你可以把公开 ESG 报告片段、草稿、投资者问题或数据收集需求发给 AI Agent，它会输出中文优先的工作底稿、证据状态、风险提示和下一步行动。

## Pilot Use Only / Internal Draft Use

本 v0.1 版本只用于内部试点和工作底稿。它不提供法律、监管、审计、鉴证、财务或可持续发展报告意见。所有输出必须先由负责的内部人员和专业审核人批准，才可以对外发布、提交、披露或放入 ESG 报告。

保留英文安全边界：Outputs must not be externally published, filed, submitted, or disclosed until approved by the responsible internal owners and professional reviewers.

上市公司 IR 用户在对外使用任何内容前，必须考虑选择性披露（selective disclosure）、内幕消息（inside information）、市场敏感信息（market-sensitive information）和获批准披露渠道（approved disclosure channels）。

这些 skills 不能在没有法律或专业确认的情况下判断某个监管框架是否对公司强制适用。The skills must not determine whether a regulatory framework is mandatory for a company without legal or professional confirmation.

可以用真实上市公司的公开 ESG 报告测试，但输出仍然只是内部工作底稿，不是合规意见。

## 我该用哪个功能？

| 你想做什么 | 使用哪个 skill | 你可以怎么问 |
| --- | --- | --- |
| 检查香港上市公司 ESG / 气候披露缺口 | `esg-hkex-gap-check` | 请检查这段 ESG 披露是否有 HKEX gap |
| 检查 A 股可持续发展报告 / ESG 报告差距 | `esg-a-share-gap-check` | 请检查这段 A 股可持续发展报告是否有上交所/深交所准备度差距 |
| 检查 ISSB / IFRS S2 气候披露准备度 | `esg-issb-climate` | 请按 ISSB S2 检查这段气候披露 |
| 做董事会 ESG 简报 | `esg-board-brief` | 请把这份 ESG 报告整理成董事会预读材料 |
| 准备投资者 ESG Q&A | `esg-investor-qa` | 请基于这份报告生成投资者问答 |
| 收集跨部门 ESG 数据 | `esg-data-request` | 请生成年度 ESG 数据收集 tracker |
| 回复评级 / 客户 ESG 问卷 | `esg-rating-response` | 请生成客户 ESG 问卷回复日志 |
| 做重大性议题分析 | `esg-materiality` | 请重构重大性议题池和访谈问题 |
| 不知道该用哪个 | `esg` | 请帮我判断该用哪个 ESG 工作流 |

## Which Skill Should I Use?

| If your request mentions... | Use this skill |
| --- | --- |
| HKEX / Hong Kong listed / Part D / climate disclosure | `esg-hkex-gap-check` |
| A股 / A-share / 上交所 / 深交所 / 可持续发展报告 / 第14号 / 第17号 | `esg-a-share-gap-check` |
| ISSB / IFRS S1 / IFRS S2 / TCFD | `esg-issb-climate` |
| Board / directors / management update | `esg-board-brief` |
| Investor / analyst / IR / roadshow / Q&A | `esg-investor-qa` |
| ESG KPI / Scope 1 / Scope 2 / Scope 3 / data collection | `esg-data-request` |
| MSCI / CDP / EcoVadis / supplier questionnaire | `esg-rating-response` |
| Materiality / stakeholder / topic prioritisation | `esg-materiality` |
| General ESG workplan or unsure which skill applies | `esg` |

## 直接复制使用的例子

港股用 `esg-hkex-gap-check`；A 股用 `esg-a-share-gap-check`。通用工作流、证据状态、风险提示和审核交接原则可以共用，但不要把 HKEX Part D 和 A 股上交所/深交所规则混在一个 skill 里判断。

投资者问答：

```text
请使用 esg-investor-qa。投资者问：公司是否有净零目标？如果没有，会不会影响海外客户订单？请输出稳妥回答、不得表述、证据状态、风险提示和审核交接。
```

HKEX gap check：

```text
请使用 esg-hkex-gap-check。以下是一段 ESG 披露草稿，请检查潜在 HKEX / Part D 准备度差距。不要直接判断合规或不合规。
```

A 股 gap check：

```text
请使用 esg-a-share-gap-check。以下是一段 A 股可持续发展报告草稿，请检查潜在上交所第14号 / 深交所第17号准备度差距。不要直接判断违规、不合规或必须披露。
```

董事会简报：

```text
请使用 esg-board-brief。请把以下公开 ESG 报告片段整理成一页式董事会 ESG 预读材料。
```

数据收集：

```text
请使用 esg-data-request。请帮我生成 2025 年度 ESG 数据收集 tracker，覆盖 HR、Finance、Operations、EHS、Procurement、Administration。
```

评级问卷：

```text
请使用 esg-rating-response。客户 ESG 问卷要求 Scope 1/2/3、供应商审核、人权政策、反腐败、碳中和和 ESG rating，请生成回复日志和不得声称事项。
```

重大性：

```text
请使用 esg-materiality。请基于以下 ESG 报告片段重构重大性议题池、利益相关方访谈问题和下一步行动。
```

## Copy-Paste Usage Examples

If your AI Agent or team prefers English prompts, explicitly ask for English output:

```text
Use the esg-investor-qa skill. Please answer in English. Prepare investor Q&A from the public report excerpts below, separating safe answers, do-not-say language, evidence status, risk flags, and reviewer handoff.
```

## 如果你通过 Telegram / Hermes 使用

如果你的团队已经把 ESG Skill Pack 安装到 Hermes，并通过 Telegram bot 使用，你可以像普通聊天一样发送 prompt：

1. 打开团队提供的 Telegram bot 对话。
2. 直接复制下面的 prompt 发给 bot。
3. 在 prompt 后面粘贴公开报告片段、草稿、问题或数据收集需求。
4. 如果 bot 没有识别到 ESG skills，请在开头明确写：`请使用 esg-hkex-gap-check`、`请使用 esg-investor-qa` 或其他 skill 名称。
5. 不要发送机密资料、未披露财务数据、董事会材料、客户/供应商机密、员工个人信息、内幕消息或市场敏感信息。

Telegram / Hermes 测试 prompt 1：

```text
请使用 esg-hkex-gap-check。以下是一段公开 ESG 报告摘录，请用中文检查潜在 HKEX / Part D 准备度差距，输出证据状态、风险提示和下一步行动。不要判断合规或不合规。
```

Telegram / Hermes 测试 prompt 2：

```text
请使用 esg-investor-qa。投资者问：公司是否有净零目标？如果没有，会不会影响海外客户订单？请只基于公开资料生成稳妥回答、不得表述、证据状态、风险提示和 IR/法务/公司秘书审核交接。
```

Telegram / Hermes 测试 prompt 3：

```text
请使用 esg-data-request。请生成 2025 年度 ESG 数据收集 tracker，覆盖 HR、Finance、Operations、EHS、Procurement、Administration，并列出来源文件、负责人、证据状态、风险提示和下一步行动。
```

## What to Provide

提供资料时，尽量说明：

- 公司名称或匿名标签。
- 上市地、司法辖区、框架、问卷或受众。
- 工作目标：gap check、董事会简报、投资者 Q&A、数据 tracker、评级回复、重大性分析等。
- 来源材料：公开报告摘录、政策、数据表、草稿、投资者问题、客户问卷或访谈笔记。
- 报告期间、业务边界、负责人和截止日期。
- 哪些措辞已经批准、禁止使用、仍在审核或可能涉及市场敏感信息。

如果没有证据，请直接说明没有。不要让 AI 猜数字、猜目标、猜董事会审批或猜合规状态。

## 可选：公司 Profile

公司 Profile 是一个可选的本地 YAML 文件，适合由技术同事、证券部、董办、公司秘书、法务或 ESG owner 准备，用来减少重复提问。

普通用户不需要自己写 profile。你可以让技术同事参考 [company_profile.example.yaml](company_profile.example.yaml)，复制成 `company_profile.local.yaml` 后只放在本地使用。`company_profile.local.yaml` 已加入 `.gitignore`，不应提交到 GitHub。

Profile 可以记录公司名称、股票代码、上市地、板块、财政年度、HKEX / A 股主体状态、默认输出语言、已批准公开资料来源和审核角色。

重要限制：

- Profile 是可选上下文，不是合规结论。
- Profile 不能替代法务、公司秘书、证券部、董办、财务、ESG、鉴证或管理层确认。
- 如果 profile 字段没有 `source`、`last_reviewed` 或 `confirmed_by`，输出必须把它当作假设，而不是已验证事实。
- 即使 profile 字段完整，输出仍然只是内部工作底稿，不能直接对外发布、提交、披露或纳入 ESG 报告。

## 什么资料可以上传 / 不要上传什么

可以用：

- 公开 ESG 报告。
- 已公开年报。
- 虚构材料。
- 已允许内部测试的非敏感资料。
- 已脱敏的报告草稿。

不要用：

- 未披露财务数据。
- 董事会材料、会议纪要、委员会文件或管理层材料。
- 客户 / 供应商机密资料。
- 员工个人信息。
- 未发布 ESG 报告全文。
- 内幕消息或市场敏感信息。
- 密码、token、密钥或访问凭证。
- 合同敏感条款。

## Verified Does Not Mean Approved

输出里的证据状态可以这样理解：

| 状态 | 意思 | 你应该怎么处理 |
| --- | --- | --- |
| 已验证（Verified） | 用户提供材料或公开报告中有支持。 | 仍需确认引用、范围、期间和用途。 |
| 需确认（Needs confirmation） | 看起来可能合理，但还缺负责人、来源、方法、法律、鉴证或管理层确认。 | 找对应负责人确认后再使用。 |
| 缺数据（Missing data） | 当前材料没有支持这个数据或说法。 | 补数据、补来源，或删除相关说法。 |
| 不得声称（Do not claim） | 说法没有支持、可能误导、过度宣传或风险太高。 | 不要对外使用，改成中性措辞或删除。 |

“已验证（Verified）”只表示用户提供材料或公开报告中有支持，不等于审计、鉴证、法律确认、监管批准、董事会批准或可以对外发布。It does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, free from error, or suitable for filing or submission.

其他输出项：

- 风险提示：告诉你哪些措辞、数据、目标、合规判断或对外披露可能有风险。
- 下一步行动：告诉你要补什么资料、找谁确认、什么时候完成。
- 审核交接：告诉你哪些内容要交给 ESG、IR、公司秘书、法务、财务、运营、EHS、采购、鉴证或管理层复核。

## Default Output Language

默认中文输出（Chinese-first）。只有用户明确要求英文时才输出英文；只有用户明确要求双语时才输出双语。

- 如果你用中文提问，输出应为中文。
- 如果你中英混合提问，输出仍应以中文为主。
- 专业术语可以中英并列，例如 HKEX、ISSB、IFRS S2、Scope 1、Scope 2、Scope 3、MSCI、CDP、EcoVadis。
- 证据状态中文优先，英文括号补充，例如：缺数据（Missing data）。
- Output in English only when the user explicitly requests English.
- Output bilingual content only when the user explicitly requests bilingual output.

## FAQ：非技术用户常见问题

**我不懂 ESG，可以用吗？**
可以。你可以从“我该用哪个功能？”表格里选一个最接近的任务，或直接说“请帮我判断该用哪个 ESG 工作流”。但输出仍需要 ESG、IR、公司秘书、法务、财务或相关负责人复核。

**它会自动判断合规吗？**
不会。它只能做准备度检查、证据整理和风险提示。是否适用某项规则、是否合规、是否需要披露，必须由公司秘书、法务和相关专业人员确认。

**输出可以直接复制进 ESG 报告吗？**
不可以。输出是内部工作底稿。任何对外披露、提交、公告、路演或放入 ESG 报告前，都必须经过负责团队和专业审核人批准。

**为什么输出里有“需确认”“缺数据”？**
这是安全设计。它提醒你当前材料还不足以支持某句话或某个数字，需要补来源、补方法、补边界或找负责人确认。

**可以用真实上市公司公开 ESG 报告测试吗？**
可以使用已经公开的 ESG 报告、年报或公开材料做测试。但输出仍然只是内部工作底稿，不是合规意见，也不代表报告没有风险。

**可以上传公司未发布草稿吗？**
只有在公司明确允许、资料已经脱敏且不含机密、内幕消息、市场敏感信息、客户/供应商资料或个人信息时才可以。不能上传未发布 ESG 报告全文、董事会材料或未披露财务数据。

**为什么默认中文？**
本包面向中文 ESG、IR、公司秘书、法务、财务和运营团队试点，默认中文能降低理解成本。专业术语会保留英文括注。

**如何要求英文输出？**
在 prompt 里明确写“请输出英文版”“Please answer in English”“for investor roadshow in English”或“board-ready English wording”。如果没有明确要求，默认输出中文。

**安装失败怎么办？**
把错误信息、你使用的 agent（Hermes / Codex / Claude Code / OpenClaw）和安装命令发给技术同事。普通业务用户不需要自己排查命令行问题。

## Skills Included

- `esg` - general ESG work product router and drafting support
- `esg-a-share-gap-check` - A 股、上交所、深交所、可持续发展报告、第14号、第17号差距检查
- `esg-hkex-gap-check` - HKEX and Hong Kong listed issuer gap checks
- `esg-issb-climate` - ISSB, IFRS S1, IFRS S2, and TCFD climate disclosure support
- `esg-board-brief` - board briefs, board papers, director updates, and management updates
- `esg-investor-qa` - investor, analyst, IR, roadshow, and Q&A preparation
- `esg-data-request` - ESG KPI and Scope 1, Scope 2, Scope 3 data collection trackers
- `esg-rating-response` - MSCI, Sustainalytics, CDP, EcoVadis, and supplier questionnaire responses
- `esg-materiality` - materiality, stakeholder, and topic prioritisation work

## Install

### A. 最简单：找技术同事安装

如果你不懂命令行，把这个仓库链接和下面这句话发给技术同事：

```text
请帮我安装 ESG Skill Pack v0.1.3-internal-pilot 到 Hermes / Codex / Claude Code / OpenClaw。安装后请运行 validate_skill_pack.py 确认通过。如果 v0.1.3 tag 尚未创建，请先临时使用 v0.1.2-internal-pilot。
```

### B. 一句话安装 Hermes

适合已经会打开终端的用户。这个命令会下载固定版本、先验证、再安装到 Hermes user scope。`v0.1.3-internal-pilot` tag 创建后使用下面命令；tag 创建前可临时把版本改为 `v0.1.2-internal-pilot`。

```bash
tmp="$(mktemp -d)" && git clone --depth 1 --branch v0.1.3-internal-pilot https://github.com/tianxiayoushan/esg-agent-skill-pack.git "$tmp/esg-agent-skill-pack" && cd "$tmp/esg-agent-skill-pack" && python3 -B scripts/validate_skill_pack.py && ./install.sh --target hermes --scope user
```

### C. 一句话安装 OpenClaw

`v0.1.3-internal-pilot` tag 创建后使用下面命令；tag 创建前可临时把版本改为 `v0.1.2-internal-pilot`。

```bash
tmp="$(mktemp -d)" && git clone --depth 1 --branch v0.1.3-internal-pilot https://github.com/tianxiayoushan/esg-agent-skill-pack.git "$tmp/esg-agent-skill-pack" && cd "$tmp/esg-agent-skill-pack" && python3 -B scripts/validate_skill_pack.py && ./install.sh --target openclaw --scope personal
```

### D. 已有本地仓库时安装

从本仓库根目录运行：

```sh
./install.sh --target hermes --scope user
```

其他 agent：

```sh
./install.sh --target codex --scope user
./install.sh --target claude-code --scope user
./install.sh --target openclaw --scope personal
```

预览安装但不复制文件：

```sh
./install.sh --target all --dry-run
```

覆盖已有 skill 文件夹：

```sh
./install.sh --target codex --scope user --force
```

The installer copies only directories under `skills/` that contain a `SKILL.md`. Each installed skill is self-contained and includes its own references, templates, and examples.

## What This Pack Cannot Do

- It cannot verify current law or stock exchange rules without official source text.
- It cannot provide legal advice, assurance, audit opinions, or regulatory sign-off.
- It cannot invent emissions data, Scope 1, Scope 2, Scope 3 figures, board oversight mechanisms, ESG rating scores, supplier audit results, net zero targets, assurance status, or compliance status.
- It cannot safely use confidential company information unless the user provides it in the current working context and is authorized to do so.
- It does not make network calls in the MVP.

## Human Review Required

Outputs are draft working papers for professional review. Before external use, have the relevant owner review and approve the output, such as ESG, IR, company secretarial, legal, finance, sustainability, operations, assurance provider, management, or board secretary.

## Maintenance

For developers and skill maintainers:

```sh
python3 -m unittest discover -s tests
python3 -B scripts/validate_skill_pack.py
./install.sh --target all --dry-run
```

The tests validate skill metadata, mandatory sections, evidence statuses, greenwashing guardrails, framework placeholders, installer options, self-contained skill files, examples, and no-network constraints.

When updating a framework reference, keep the file cautious and include:

- `framework_name`
- `jurisdiction`
- `applicable_companies`
- `source_placeholder`
- `last_reviewed_date`
- `status`
- `update_notes`

Do not turn placeholder references into legal checklists unless the official source text has been reviewed and cited.
