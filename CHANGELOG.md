# Changelog

## v0.1.4 Internal Pilot Candidate - Unreleased

### Added

- Added `esg-a-share-gap-check` as a separate A 股可持续发展报告 / ESG 报告 / 社会责任报告 / 气候披露差距检查 skill.
- Added cautious placeholder references for 上交所《上市公司自律监管指引第14号——可持续发展报告（试行）》 and 深交所《上市公司自律监管指引第17号——可持续发展报告（试行）》.
- Added A 股差距检查 template and example with Chinese-first evidence status, A 股披露主体判断, 议题差距表, 更审慎表述, and 审核交接.

### Improved

- Updated the ESG router, README, and PILOT_GUIDE to separate 港股 HKEX work from A 股上交所/深交所 work.
- Added validator checks for the ninth skill, A 股 trigger phrases, A 股 obligation-level labels, self-contained resources, and HKEX/A-share separation.

## v0.1.3 Internal Pilot Candidate - Unreleased

### Improved

- Reworked README to start from a non-technical business-user perspective, with 30-second overview, copy-ready Chinese prompts, safe-material guidance, and plain-language output interpretation.
- Added Telegram / Hermes user guidance, OpenClaw quick install, and a non-technical FAQ to the README.
- Made HKEX default evidence labels Chinese-first: 已验证（Verified）, 需确认（Needs confirmation）, 缺数据（Missing data）, and 不得声称（Do not claim）.
- Made HKEX obligation labels Chinese-first: 强制披露（Mandatory）, 不遵守就解释（Comply-or-explain）, 自愿披露（Voluntary）, 适用性待确认（Applicability to confirm）, and 未评估（Not assessed）.
- Reduced forward-looking wording in HKEX outputs by requiring approved disclosure timetables before using timing language.
- Reduced regulatory-style conclusions in HKEX outputs by replacing bare mandatory or failure language with applicability, boundary, and obligation-level confirmation wording.
- Replaced unnatural promotional-wording terminology with Chinese alternatives such as 包装性表述, 宣传性表述, and 未经支持的概括性表述.

### Validation

- Validator now checks HKEX Chinese-first evidence and obligation mappings, the Voluntary spelling, and default-output regressions such as English-first evidence labels or bare English obligation-level labels.

## v0.1.2 Internal Pilot Candidate - Unreleased

### Added

- Real-company public report testing notes for Linklogis-style HKEX Part D wording risk and Lenovo-style ISSB, board, investor Q&A, rating response, and materiality output risks.
- HKEX / Part D obligation-level taxonomy requiring each item to be classified as Mandatory, Comply-or-explain, Voluntary, Applicability to confirm, or Not assessed.
- Real-company output issue fixture documenting over-strong wording patterns and safer replacements.

### Improved

- Changed default output strategy to Chinese-first across skills, templates, examples, and validation. English or bilingual output is reserved for explicit user requests.
- Strengthened `Verified` across skills: source-supported only, not legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error.
- Added anti-overclaim wording for readiness reviews, replacing unqualified compliance labels with readiness-only language and professional review handoff.
- Clarified HKEX Part D schedule nuance, including financial years commencing on or after 1 January 2025, issuer category, LargeCap status, and company secretary / legal confirmation.
- Hardened ISSB readiness discipline by separating readiness, alignment, and compliance, and by requiring Scope 3 category coverage, methodology, data quality, and assumptions.
- Clarified materiality language: CSRD/ESRS uses double materiality, GRI is impact-oriented, and ISSB is investor-focused / financial materiality baseline.
- Strengthened investor Q&A controls for approved channels, selective disclosure, inside information, market-sensitive information, and comparative claim risk.
- Improved rating response discipline for ESG rating agency/date/scope/source fields and supplier audit wording.

### Validation

- Validator now checks HKEX obligation-level taxonomy, global `Verified` language, ISSB/CSRD materiality distinction, investor caution language, real-company output issue fixture coverage, and unqualified overclaim phrases.

### Known Limitations

- v0.1.2 remains an internal pilot candidate and does not provide legal, regulatory, audit, assurance, financial, or sustainability reporting conclusions.
- Public-company report testing improves workflow realism but does not convert outputs into compliance opinions or external disclosure-ready text.

## v0.1.1 Internal Pilot Candidate - Unreleased

### Added

- Public-source research map for realistic ESG workflow design, with official and public-source citations and caution notes.
- Realistic work scenario fixture covering HKEX gap review, investor roadshow Q&A, board pre-read, ESG data collection, customer questionnaire response, materiality planning, multilingual output, and low-AI-maturity use.

### Improved

- Added output-use classification guidance to skills: draft, internal working paper, board pre-read, external disclosure, regulatory filing, investor response, customer response, or provider submission.
- Added bilingual drafting guidance so Chinese prompts can produce English board or IR wording while preserving evidence status labels and risk flags.
- Strengthened validation for realistic scenario coverage, public-source research map coverage, and workflow realism.

### Notes

- No new skills, dependencies, network runtime, data integrations, legal checklists, or carbon calculation engines were added.
- Public sources remain reference aids only and do not determine legal, regulatory, audit, assurance, financial, or sustainability reporting conclusions.

## v0.1.0 Internal Pilot - 2026-05-18

Initial internal pilot release of the ESG Skill Pack for listed companies and large companies.

### Eight MVP Skills

- `esg`
- `esg-hkex-gap-check`
- `esg-issb-climate`
- `esg-board-brief`
- `esg-investor-qa`
- `esg-data-request`
- `esg-rating-response`
- `esg-materiality`

### Safety Controls

- Requires every ESG claim to use one evidence status: `Verified`, `Needs confirmation`, `Missing data`, or `Do not claim`.
- Clarifies that `Verified` means source-supported within provided materials only, not legally verified, audited, assured, regulator-approved, board-approved, or externally publishable.
- Includes greenwashing guardrails for unsupported emissions, Scope 1 / Scope 2 / Scope 3 figures, board oversight, assurance, ESG ratings, supplier audit results, net zero, carbon neutrality, compliance status, customer impact, diversity metrics, and safety metrics.
- Requires human professional review before external publication, filing, submission, disclosure, or ESG report inclusion.
- Uses cautious framework placeholders rather than invented regulatory checklists.
- Makes no network calls in the MVP.

### Installer Support

- Supports `--target codex`, `--target claude-code`, `--target openclaw`, `--target hermes`, and `--target all`.
- Supports `--scope project`, `--scope user`, `--scope workspace`, `--scope personal`, and `--scope managed`.
- Supports `--dry-run` and `--force`.
- Installs only real skill directories containing `SKILL.md`.
- Does not overwrite existing skill directories unless `--force` is used.
- Keeps installed skills self-contained with local references, templates, and examples.

### Validation Coverage

- Validates required skill directories and `SKILL.md` frontmatter.
- Validates required metadata, sections, evidence statuses, trigger phrases, framework placeholders, examples, and README safety language.
- Validates no-network and dynamic shell-injection guardrails.
- Validates installer dry-run behavior, target/scope matrix, controlled temp installs, and `--force` overwrite behavior.
- Validates pilot scenario fixtures across all eight skills.
- Validates the department-filled ESG data request example.

### Known Limitations

- Framework references are placeholders and must be verified against official source text before regulatory use.
- The pack does not provide legal, regulatory, audit, assurance, financial, or sustainability reporting advice.
- Outputs are draft working papers only.
- The pack does not determine mandatory regulatory status.
- The pack does not calculate emissions, ESG KPIs, ratings, assurance conclusions, or compliance status without user-provided methodology and evidence.
- Internal pilot users must use synthetic, public-style, or authorized materials only.
