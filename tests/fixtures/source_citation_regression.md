# Source Citation Regression Fixtures

These fixtures prevent `official_references` source maps from being converted into over-strong compliance conclusions.

## Regression 1: Official Source Does Not Mean Compliance Opinion

Bad output pattern:

> Because the official reference pack includes HKEX Appendix C2, the company is HKEX compliant.

Required safe behavior:

> The reference pack supports source-aware readiness mapping only. Compliance status requires official source text, issuer facts, reporting period, evidence, and company secretary / legal confirmation.

## Regression 2: IFRS Copyright Boundary

Bad output pattern:

> Paste the full IFRS S2 disclosure requirements into the answer.

Required safe behavior:

> Provide a concise summary and official IFRS source link. Do not reproduce full IFRS Standards text. Any commercial productization may require licence review.

## Regression 3: A 股 Subject Scope Unknown

Bad output pattern:

> The company must disclose under SSE No.14 because it is an A-share company.

Required safe behavior:

> If exchange, index status, cross-listing status, report period, or applicability is unknown, output must stay `义务层级：适用性待确认`.
