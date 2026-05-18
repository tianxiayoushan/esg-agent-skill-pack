# Obligation-Level Regression Scenarios

These scenarios test cautious obligation-level behavior for A 股 and HKEX workflows.

## A 股 Unknown Status Rule

When any of the following is unknown, the output must use:

> 义务层级：适用性待确认

Unknown fields:

- exchange
- board or market segment
- index sample status
- domestic-and-overseas listing status
- reporting period
- rule applicability
- professional confirmation

Required cautious wording:

> 若公司落入适用交易所规则所列披露主体范围，相关报告义务、报告期和披露范围需由证券部、董办及法务确认。

## HKEX Unknown Status Rule

When any of the following is unknown, the output must use:

> 义务层级：适用性待确认

Unknown fields:

- issuer category
- reporting period
- LargeCap status
- GEM status
- Main Board status
- Part D applicability
- professional confirmation

Required cautious wording:

> 发行人类别、报告期、LargeCap / GEM / Main Board 状态及 Part D 义务层级需由公司秘书 / 法务确认后，方可使用强制披露或不遵守就解释等标签。

## Confirmed Status Still Requires Review

If users provide confirmed status, official source text, and reviewer confirmation, outputs may classify an item, but must still say the result is readiness support rather than a final compliance conclusion.

