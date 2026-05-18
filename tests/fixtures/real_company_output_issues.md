# Real-Company Public Report Output Issues Fixture

This fixture records short excerpts from generated internal test outputs based on public-style Linklogis and Lenovo ESG report testing. It does not reproduce confidential company data or long copyrighted report text. It is used to harden wording discipline for v0.1.2.

## Issue 1: Linklogis HKEX Part D Over-Strong Mandatory Wording

Generated-output excerpt to avoid:

> Part D non-compliance: the issuer must disclose quantified climate transition plan metrics.

Why it is risky:

- It states a compliance conclusion without confirming issuer category, reporting period, LargeCap status, obligation level, or implementation relief.
- It uses `must disclose` without company secretary / legal confirmation.

Required safer pattern:

- Use `Potential disclosure gap`, `Part D readiness gap`, or `Obligation level to confirm`.
- Classify each item as Mandatory, Comply-or-explain, Voluntary, Applicability to confirm, or Not assessed.
- Add `Requires company secretary / legal confirmation`.

## Issue 2: Lenovo ISSB Readiness Overclaim Risk

Generated-output excerpt to avoid:

> Fully met: no material gaps; Lenovo is industry-leading and fully aligned with ISSB climate expectations.

Why it is risky:

- `Fully met`, `no material gaps`, `industry-leading`, and `fully aligned` overstate the review result unless every evidence item, boundary, period, and methodology has been reviewed and approved.
- ISSB readiness, alignment, and compliance are different conclusions.

Required safer pattern:

- Use `appears substantially prepared based on the provided public materials`.
- Use `no major readiness gap identified from the provided excerpts` only where supported.
- Add `readiness assessment only`, `not a compliance conclusion`, and `requires professional review`.

## Issue 3: Lenovo Verified Definition Good Example

Generated-output excerpt to preserve:

> Evidence status: Verified, meaning supported by the provided public report material only. This does not mean audited, assured, legally verified, regulator-approved, board-approved, externally publishable, complete, or free from error.

Why it is useful:

- It keeps `Verified` tied to source support, not professional approval.
- If a metric is externally assured, the output must state the assurance level separately, such as reasonable assurance, limited assurance, or assurance status not provided.

## Issue 4: Lenovo Product Carbon Neutrality Cautious Wording Good Example

Generated-output excerpt to preserve:

> Do not claim product carbon neutrality unless the specific product, boundary, standard, certification or assurance evidence, period, and approved disclosure wording are provided.

Why it is useful:

- It avoids treating broad sustainability language as a product-level claim.
- It requires evidence before carbon neutral or net zero wording is used externally.

## Issue 5: Lenovo Materiality Framework Correction

Generated-output excerpt to avoid:

> ISSB emphasizes double materiality and therefore the output can reconstruct final materiality topics from the public report.

Why it is risky:

- CSRD/ESRS uses double materiality.
- GRI is impact-oriented.
- ISSB is investor-focused / financial materiality baseline.
- Final materiality cannot be determined without actual methodology, stakeholder evidence, scoring, and governance approval.

Required safer pattern:

- Describe the output as a materiality reconstruction or planning aid only.
- Mark final topic ranking as Needs confirmation unless methodology, stakeholder records, scoring, and governance approval are provided.
