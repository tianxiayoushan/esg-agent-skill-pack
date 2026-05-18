# Language Policy Regression Scenarios

Default behavior is Chinese-first. These scenarios test that output language is not accidentally English-first.

| ID | User prompt | Expected language behavior |
| --- | --- | --- |
| LP1 | “帮我检查这份ESG材料，看有没有披露风险。” | Chinese output with headings such as 执行摘要、适用框架与假设、证据状态、风险提示、下一步行动、审核交接. |
| LP2 | “请做 HKEX gap check，Scope 1/2/3 用英文术语。” | Chinese output; retain HKEX, Scope 1, Scope 2, Scope 3 only where useful. |
| LP3 | “Prepare an ESG board brief.” | Prefer Chinese summary and Chinese work product because no output language was specified. |
| LP4 | “Please prepare English investor roadshow wording.” | English output is allowed because English was explicitly requested. |
| LP5 | “请输出中英双语 IR Q&A。” | Bilingual output is allowed because bilingual output was explicitly requested. |
| LP6 | “这个能不能发？” | Chinese output; warn against external publication, filing, submission, disclosure, or ESG report inclusion before review. |

Evidence labels must be Chinese-first unless English-only output is explicitly requested:

- 已验证（Verified）
- 需确认（Needs confirmation）
- 缺数据（Missing data）
- 不得声称（Do not claim）

