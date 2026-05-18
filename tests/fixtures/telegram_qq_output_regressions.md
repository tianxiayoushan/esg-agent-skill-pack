# Telegram / QQ Output Regression Fixtures

These fixtures capture generated-output patterns that must not reappear in default work products. They are regression examples, not approved output language.

## Regression 1: A 股 Premature Obligation Label

Bad generated-output excerpt:

> 义务层级（暂定）: 强制披露

Required replacement:

> 义务层级：适用性待确认

Rationale: if exchange, index sample status, domestic-and-overseas listing status, reporting period, or rule applicability is unknown, the obligation level must remain unconfirmed.

## Regression 2: Unsupported Future Disclosure Commitment

Bad generated-output excerpt:

> 公司将在后续报告期披露相关气候数据，并将在数据条件成熟后补充披露 Scope 3。

Required replacement:

> 公司可评估是否、何时以及以何种范围披露相关信息；任何披露时间表须经管理层、证券部/公司秘书/董办、法务及相关审核人确认后方可对外使用。

## Regression 3: Unsupported Fixed Timing

Bad generated-output excerpt:

> 公司应在 5 个交易日内确认并补充披露。

Required replacement:

> 在主体状态确认前，所有义务层级判断均应保持为“适用性待确认”；内部时间安排需由管理层和相关审核人确认。

## Regression 4: A 股 HK-Style Terminology

Bad generated-output excerpt:

> This item is comply-or-explain.

Required replacement:

> 如需解释性说明，A 股场景优先使用原因说明、改进计划、后续披露安排或适用规则要求下的解释性说明。

## Regression 5: English-First Evidence Label

Bad generated-output excerpt:

> Evidence status: Missing data

Required replacement:

> 证据状态：缺数据（Missing data）

## Regression 6: Investor Risk Flags None

Bad generated-output excerpt:

> Risk flags: None

Required replacement:

> 未从已提供材料识别出重大风险，但仍需 IR/法务/公司秘书复核。

