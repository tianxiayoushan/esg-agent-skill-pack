# Official Reference Scenario Fixtures

These synthetic scenarios test source-map-aware outputs. They contain no private company data and do not ask for legal or compliance conclusions.

## Scenario 1: HKEX Appendix C2 Source-Aware Gap Check

- Skill: `esg-hkex-gap-check`
- Prompt: "请按 HKEX Appendix C2 / Part D 做准备度检查，但不要作合规结论。"
- Expected behavior:
  - Cite official source-map layer: `official_references/hkex/`.
  - Use `潜在披露差距`, `准备度差距`, and `义务层级：适用性待确认`.
  - Ask for issuer category, reporting period, LargeCap / GEM / Main Board status, and company secretary / legal confirmation.
  - Do not write non-compliant, must disclose, or mandatory unless status is confirmed.

## Scenario 2: A 股 No.14 / No.17 Source-Aware Gap Check

- Skill: `esg-a-share-gap-check`
- Prompt: "请按 A 股第14号/第17号做准备度检查，但不要作合规结论。"
- Expected behavior:
  - Cite official source-map layer: `official_references/a_share/`.
  - Separate SSE No.14 and SZSE No.17.
  - Use `义务层级：适用性待确认` when exchange, index status, cross-listing status, report period, or applicability is unknown.
  - Do not use HKEX comply-or-explain terminology by default.

## Scenario 3: ISSB Source-Aware Climate Readiness

- Skill: `esg-issb-climate`
- Prompt: "请按 IFRS S1 / IFRS S2 做 climate readiness review，不要写 ISSB compliant。"
- Expected behavior:
  - Cite official source-map layer: `official_references/issb/`.
  - Distinguish readiness, alignment, and compliance.
  - State IFRS S1 and IFRS S2 are designed to be applied together.
  - Request Scope 3 category coverage, materiality rationale, methodology, data quality, and assurance status.

## Scenario 4: Crosswalk Output

- Skill: `esg`
- Prompt: "请比较 HKEX、A 股和 ISSB 对气候治理、Scope 1/2/3 和 materiality 的差异。"
- Expected behavior:
  - Use `official_references/crosswalks/`.
  - Explain obligation-level differences.
  - Say ISSB is investor-focused / financial materiality baseline.
  - Say CSRD/ESRS uses double materiality and GRI is impact-oriented where relevant.
  - Do not say ISSB uses double materiality.

