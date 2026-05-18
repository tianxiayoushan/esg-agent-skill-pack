# Realistic Work Scenario Pack

These scenarios are synthetic but realistic. They are for testing workflow quality only and contain no real company names, unpublished company data, personal data, supplier data, customer data, board materials, secrets, credentials, emissions figures, or market-sensitive information.

## Scenario 1: Hong Kong Listed Issuer ESG Report Gap Review

- Skill: `esg-hkex-gap-check`
- Sector: fictional Hong Kong listed manufacturing issuer.
- User asks: "Please review this ESG report draft before internal circulation."
- Synthetic facts:
  - Board oversight is described as "the Board oversees ESG matters" with no committee remit, meeting cadence, minutes, reporting line, or responsible management owner.
  - Climate risk process is not described.
  - Environmental table includes partial electricity, water, and waste activity data for selected sites only.
  - Scope 1 and Scope 2 source data are incomplete; Scope 3 is not collected.
  - Draft says "robust governance" and implies a future net zero ambition, but no board approval, target boundary, baseline, or method exists.
- Expected output:
  - Gap table with evidence status.
  - Risk flags for unsupported governance, target, Scope 1 / Scope 2 / Scope 3, and compliance wording.
  - Explicitly identify vague board oversight as an evidence gap.
  - Next actions by company secretarial, ESG, finance, operations, legal, and assurance reviewers.
  - No invented HKEX requirements beyond placeholder source assumptions.

## Scenario 2: Investor Roadshow ESG Question Set

- Skill: `esg-investor-qa`
- User asks: "Prepare ESG Q&A for a roadshow."
- Synthetic questions:
  - Do you have a net zero target?
  - Will the lack of a target affect overseas customer orders?
  - Are your products green or low-carbon?
  - Have suppliers passed ESG audits?
  - Were there any safety incidents this year?
  - Why did your ESG rating change?
- Expected output:
  - Safe answer, cautious answer, and do-not-say list for each question.
  - Evidence status for each answer.
  - Selective disclosure, inside information, market-sensitive information, and approved-channel checks.
  - Reviewer handoff to IR, legal, ESG, finance, EHS, procurement, and management as relevant.

## Scenario 3: Board / ESG Committee Pre-Read

- Skill: `esg-board-brief`
- User asks: "Draft a one-page ESG committee pre-read."
- Synthetic facts:
  - Partial KPI table covers energy, water, waste, safety, training, supplier questionnaire status, and governance policies.
  - Reporting boundary is unresolved for leased offices and selected overseas sites.
  - Assurance decision is pending.
  - Management notes upcoming regulatory changes but has not attached official source text.
- Expected output:
  - One-page board pre-read with executive summary, decision items, watch items, evidence gaps, risk flags, and next actions.
  - Clear distinction between management recommendation and board decision.
  - No unsupported assurance, compliance, board approval, or emissions claims.
  - Handoff to board secretary, company secretarial, legal, ESG, finance, operations, EHS, procurement, and assurance where applicable.

## Scenario 4: ESG Data Collection Cycle

- Skill: `esg-data-request`
- User asks: "Build a data collection tracker for the annual ESG reporting cycle."
- Synthetic facts:
  - HR, Finance, Operations, EHS, Procurement, and Administration must provide data.
  - Some owners are missing.
  - Data periods differ across systems.
  - Reporting boundary is unclear.
  - Evidence quality ranges from system exports to informal emails.
- Expected output:
  - Tracker with department, owner, reporting period, source system or document, evidence required, evidence status, risk flag, next action, and reviewer.
  - Responsibility matrix and methodology review items.
  - Scope 1, Scope 2, and Scope 3 treated as data requests only.
  - Clear instruction that requests do not establish final ESG figures.

## Scenario 5: Customer / Supplier ESG Questionnaire

- Skill: `esg-rating-response`
- User asks: "A customer questionnaire asks for emissions figures, supplier audit results, human rights policy, anti-corruption controls, and product carbon claims. Prepare a response log."
- Synthetic facts:
  - No emissions figures or methodology are attached.
  - Supplier audit tracker is incomplete.
  - A human rights policy and anti-corruption policy may exist but are not attached.
  - Product carbon claims are requested but no product carbon footprint evidence is attached.
- Expected output:
  - Response log with evidence requests, do-not-claim items, and owner assignment.
  - Owners include ESG, finance, operations, procurement, legal, compliance, product, and customer account owner.
  - No invented emissions figures, supplier ESG audit results, product carbon claims, rating scores, assurance, or compliance status.

## Scenario 6: Materiality Assessment Planning

- Skill: `esg-materiality`
- User asks: "Prepare stakeholder interview questions and a topic prioritisation issue map."
- Synthetic stakeholders:
  - Internal stakeholders, investors, customers, suppliers, employees, regulators/community representatives.
- Synthetic facts:
  - No interviews or survey results have been completed.
  - Management proposes an initial issue pool covering climate, energy, water, waste, safety, talent, supply chain, ethics, product responsibility, data privacy, and community impact.
- Expected output:
  - Issue pool, stakeholder questions, prioritisation logic, assumptions, limitations, evidence status, and next actions.
  - Do not claim final materiality or stakeholder consensus.
  - Handoff to ESG, legal, IR, company secretarial, management, HR, procurement, and operations.

## Scenario 7: Multilingual Output

- Skills: `esg-board-brief`, `esg-investor-qa`, or `esg`
- Default Chinese Output check:
  - User asks: "帮我用中文整理这份ESG风险提示和下一步行动。"
  - Expected output: Chinese-first work product using Chinese headings, with English ESG terms retained only where useful.
- User asks in Chinese: "请用英文准备董事会/IR可用的ESG风险措辞，但保留证据状态。"
- Synthetic facts:
  - Source notes are mixed Chinese and English.
  - The output is intended for an English board pre-read or investor Q&A draft.
- Expected output:
  - English-ready drafting only because English was explicitly requested, with evidence statuses preserved.
  - Chinese assumptions or caveats may be summarized if useful for the user unless the user asks for English-only.
  - No loss of `Verified`, `Needs confirmation`, `Missing data`, or `Do not claim` labels.
  - External-use and reviewer approval language remains in English.

## Scenario 8: Low-AI-Maturity User

- Skill: `esg`
- User asks: "帮我看看这个ESG材料能不能发。"
- Synthetic facts:
  - User provides a short draft with unclear audience, no reporting period, no source pack, and promotional ESG claims.
- Expected output:
  - Ask only minimal clarifying questions needed to avoid unsafe output.
  - Warn against external publication, filing, submission, disclosure, or ESG report inclusion before approval.
  - Propose a safe review path: identify audience, source evidence, risk flags, evidence status, reviewers, and next actions.
  - Avoid rewriting the draft as externally usable language until evidence and approval status are clear.

## Scoring Dimensions

Output-use coverage terms: draft, internal working paper, board pre-read, external disclosure, regulatory filing, investor response.

Each scenario must score at least 4 out of 5 on:

1. Practical usefulness
2. Evidence status discipline
3. Greenwashing risk control
4. Listed-company legal / IR / company secretarial caution
5. Non-technical user clarity
6. Reviewer handoff clarity
7. Multilingual usability where relevant
8. Template usefulness
