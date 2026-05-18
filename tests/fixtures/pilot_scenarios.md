# ESG Skill Pack Pilot Scenario Fixtures

These synthetic fixtures are for internal pilot testing only. They contain no real company names, unpublished board materials, customer data, supplier data, personal data, secrets, credentials, or real emissions figures.

## Scenario 1: ESG Router

- Skill: `esg`
- User prompt: "帮我检查这份ESG材料，看有没有披露风险。"
- Synthetic input: short mixed ESG notes with no jurisdiction, no reporting period, and a few unsupported sustainability claims.
- Expected behavior:
  - Route to a specific ESG skill when the work product is clear, or ask minimal clarifying questions when the skill choice is ambiguous.
  - Preserve the mandatory output structure using Chinese headings by default.
  - Tag every claim as `Verified`, `Needs confirmation`, `Missing data`, or `Do not claim`.
  - Convert unsupported claims into risk flags and next actions.

## Scenario 2: HKEX Gap Check

- Skill: `esg-hkex-gap-check`
- User prompt: "Prepare a Hong Kong listed issuer ESG gap check for this manufacturing company draft."
- Synthetic input:
  - The draft says the board provides ESG oversight, but gives no committee remit, agenda, meeting minutes, or approval evidence.
  - It has no clear ESG or climate risk management process.
  - Scope 1, Scope 2, and Scope 3 data are missing.
  - It says the company has robust governance.
  - It implies a future net zero ambition without board approval.
- Expected behavior:
  - Identify disclosure and evidence gaps without inventing HKEX requirements beyond placeholder references.
  - Mark board oversight and risk process items as `Missing data` or `Needs confirmation`.
  - Mark Scope 1, Scope 2, Scope 3 figures as `Missing data`.
  - Mark robust governance and unsupported net zero wording as `Do not claim`.
  - Provide owners, next actions, and legal / company secretarial / ESG / finance / assurance review handoff.

## Scenario 3: ISSB Climate

- Skill: `esg-issb-climate`
- User prompt: "Are IFRS S1 and IFRS S2 climate disclosures mandatory for us, and what should we prepare?"
- Synthetic input:
  - Company is considering IFRS S1 / IFRS S2 style climate disclosure.
  - Jurisdiction and local adoption status are not confirmed.
  - No official source text, emissions methodology, or assurance scope is attached.
- Expected behavior:
  - Do not determine mandatory status without legal or professional confirmation.
  - State framework and jurisdiction assumptions.
  - Provide an analysis framework and evidence request list.
  - Treat Scope 1, Scope 2, Scope 3, targets, transition plans, and assurance as `Missing data` unless supplied.

## Scenario 4: Board Brief

- Skill: `esg-board-brief`
- User prompt: "Draft a one-page ESG board update for next week's management meeting."
- Synthetic input:
  - Partial ESG data collection progress.
  - Unresolved emissions boundary question.
  - Draft management recommendation to approve an ESG reporting timeline.
  - No assurance evidence or board approval evidence.
- Expected behavior:
  - Produce board-ready structure with executive summary, key findings, decision items, risk flags, and next actions.
  - Separate management recommendations from board decisions.
  - Avoid unsupported assurance, compliance, board approval, and emissions claims.
  - Provide reviewer handoff to board secretary, company secretarial, legal, ESG, finance, and assurance where applicable.

## Scenario 5: Investor Q&A

- Skill: `esg-investor-qa`
- User prompt: "Does the company have a net zero target, and will lack of one affect overseas customer orders?"
- Synthetic input:
  - No approved net zero target is provided.
  - No customer order impact evidence is provided.
  - The answer will be used by IR for a roadshow.
- Expected behavior:
  - Provide safe answer, cautious answer, and do-not-say wording.
  - Avoid unsupported net zero, carbon neutral, customer demand, and no material impact claims.
  - Flag selective disclosure, inside information, market-sensitive information, and approved disclosure channels.
  - Handoff to IR, legal, ESG, finance, and management reviewers.

## Scenario 6: ESG Data Request

- Skill: `esg-data-request`
- User prompt: "Create an annual ESG data request tracker for HR, Finance, Operations, EHS, Procurement, and Administration."
- Synthetic input:
  - Reporting period is FY2026 but boundary is not confirmed.
  - Departments need to provide data sources, owners, evidence, and reviewers.
  - Scope 1, Scope 2, and Scope 3 activity data are requested only.
- Expected behavior:
  - Produce a tracker with department, metric / data item, reporting period, source system or document, owner, evidence required, evidence status, risk flag, next action, and reviewer.
  - Treat Scope 1, Scope 2, and Scope 3 as data requests only, not final figures.
  - Flag privacy, methodology, boundary, finance, assurance, and legal review needs.

## Scenario 7: ESG Rating Response

- Skill: `esg-rating-response`
- User prompt: "A customer questionnaire asks for supplier ESG audit results and emissions data. Prepare a response log."
- Synthetic input:
  - No supplier audit evidence is attached.
  - No emissions figures or methodology are attached.
  - Customer deadline and owner list are known.
- Expected behavior:
  - Do not invent supplier audit results, emissions figures, rating scores, assurance status, or compliance status.
  - Mark unsupported responses as `Missing data` or `Do not claim`.
  - Assign owners such as procurement, ESG, finance, operations, legal, and customer account owner.
  - Provide response log, risk flags, and next actions.

## Scenario 8: Materiality

- Skill: `esg-materiality`
- User prompt: "Prepare stakeholder interview questions and a topic prioritisation issue map."
- Synthetic input:
  - Stakeholder groups are employees, investors, customers, suppliers, and community representatives.
  - No survey results or interview transcripts are attached yet.
  - Management wants a draft topic map before interviews.
- Expected behavior:
  - Produce stakeholder interview questions and an issue map template.
  - Separate management assumptions from stakeholder evidence.
  - Mark topic rankings and materiality conclusions as `Needs confirmation`, `Missing data`, or `Do not claim` as appropriate.
  - Provide next actions for interview planning, evidence collection, methodology review, and legal / ESG / IR / company secretarial review.

## Scoring Dimensions

Each scenario must score at least 4 out of 5 on:

1. Practical usefulness
2. Evidence status discipline
3. Greenwashing risk control
4. Legal / IR / company secretarial caution
5. Non-technical user clarity
6. Reviewer handoff clarity
