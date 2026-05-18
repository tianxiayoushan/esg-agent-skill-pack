# Changelog

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
