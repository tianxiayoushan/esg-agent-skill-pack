# ESG Skill Pack

Practical ESG skills for listed companies and large companies. The pack is designed for ESG, investor relations, company secretarial, legal, finance, sustainability, and operations teams using Codex, Claude Code, OpenClaw, Hermes, or another agent that can read `SKILL.md` folders.

The skills help draft work products such as gap checks, board briefs, investor Q&A, data request trackers, rating responses, and materiality maps. They do not replace professional judgment, legal advice, assurance work, or review against official regulatory text.

## Start Here

Use this pack when you need an internal ESG draft, checklist, tracker, board brief, investor Q&A, or data request that clearly separates supported claims from missing evidence. Start by choosing the closest skill below, then paste your source notes, report extracts, questionnaire, or meeting context into your agent.

## Pilot Use Only / Internal Draft Use

This v0.1 pack is for internal pilot use and draft working papers only. It does not provide legal, regulatory, audit, assurance, financial, or sustainability reporting advice. Outputs must not be externally published, filed, submitted, or disclosed until approved by the responsible internal owners and professional reviewers.

Listed-company IR users must consider selective disclosure, inside information, market-sensitive information, and approved disclosure channels before using any output externally.

The skills must not determine whether a regulatory framework is mandatory for a company without legal or professional confirmation.

## What to Provide

- Company name or anonymized label.
- Jurisdiction, listing venue, framework, questionnaire, or audience if known.
- Source materials: report extracts, policies, data files, board or committee context, investor questions, or stakeholder notes.
- Reporting period, business boundary, owner names, and due dates if available.
- Any wording that is already approved, prohibited, confidential, market-sensitive, or still under review.

If evidence is not available, say so. The skills should mark the item as `Missing data` or `Needs confirmation` rather than filling the gap.

## Which Skill Should I Use?

| If your request mentions... | Use this skill |
| --- | --- |
| HKEX / Hong Kong listed / Part D / climate disclosure | `esg-hkex-gap-check` |
| ISSB / IFRS S1 / IFRS S2 / TCFD | `esg-issb-climate` |
| Board / directors / management update | `esg-board-brief` |
| Investor / analyst / IR / roadshow / Q&A | `esg-investor-qa` |
| ESG KPI / Scope 1 / Scope 2 / Scope 3 / data collection | `esg-data-request` |
| MSCI / CDP / EcoVadis / supplier questionnaire | `esg-rating-response` |
| Materiality / stakeholder / topic prioritisation | `esg-materiality` |
| General ESG workplan or unsure which skill applies | `esg` |

## Verified Does Not Mean Approved

`Verified` means source-supported within the materials provided to the agent only. It does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, or suitable for filing or submission.

Treat every output as a draft until the responsible ESG, IR, company secretarial, legal, finance, sustainability, operations, assurance, and management reviewers approve it for the intended use.

## Skills Included

- `esg` - general ESG work product router and drafting support
- `esg-hkex-gap-check` - HKEX and Hong Kong listed issuer gap checks
- `esg-issb-climate` - ISSB, IFRS S1, IFRS S2, and TCFD climate disclosure support
- `esg-board-brief` - board briefs, board papers, director updates, and management updates
- `esg-investor-qa` - investor, analyst, IR, roadshow, and Q&A preparation
- `esg-data-request` - ESG KPI and Scope 1, Scope 2, Scope 3 data collection trackers
- `esg-rating-response` - MSCI, Sustainalytics, CDP, EcoVadis, and supplier questionnaire responses
- `esg-materiality` - materiality, stakeholder, and topic prioritisation work

## Install

Run commands from this repository root.

Codex project install:

```sh
./install.sh --target codex --scope project
```

Codex user install:

```sh
./install.sh --target codex --scope user
```

Claude Code project install:

```sh
./install.sh --target claude-code --scope project
```

Claude Code user install:

```sh
./install.sh --target claude-code --scope user
```

OpenClaw workspace install:

```sh
./install.sh --target openclaw --scope workspace
```

OpenClaw managed install:

```sh
./install.sh --target openclaw --scope managed
```

Hermes user install:

```sh
./install.sh --target hermes --scope user
```

Preview without copying files:

```sh
./install.sh --target all --dry-run
```

Overwrite an existing installed skill folder:

```sh
./install.sh --target codex --scope user --force
```

The installer copies only directories under `skills/` that contain a `SKILL.md`. Each installed skill is self-contained and includes its own references, templates, and examples.

## Copy-Paste Usage Examples

General ESG drafting:

```text
Use the esg skill. Create a practical ESG disclosure workplan from the source notes below. Tag every claim with evidence status and list follow-up data requests.
```

HKEX gap check:

```text
Use the esg-hkex-gap-check skill. Prepare a Hong Kong listed issuer ESG gap check using the company notes below. Do not claim compliance unless the evidence supports it.
```

ISSB climate disclosure:

```text
Use the esg-issb-climate skill. Draft an IFRS S2 climate disclosure readiness checklist from our provided documents. Mark Scope 1, Scope 2, and Scope 3 items as Missing data unless evidence is supplied.
```

Board brief:

```text
Use the esg-board-brief skill. Draft a two-page board brief for directors on ESG reporting readiness, with risk flags and next actions.
```

Investor Q&A:

```text
Use the esg-investor-qa skill. Prepare investor and analyst Q&A for a roadshow. Separate approved messaging from answers that need confirmation.
```

Data request:

```text
Use the esg-data-request skill. Create an ESG KPI data request tracker for finance, operations, HR, legal, and sustainability owners.
```

Rating response:

```text
Use the esg-rating-response skill. Help prepare a response tracker for MSCI, Sustainalytics, CDP, EcoVadis, and supplier questionnaire requests.
```

Materiality:

```text
Use the esg-materiality skill. Build a stakeholder issue map and topic prioritisation draft from the interview notes below.
```

## Evidence Statuses

Every ESG claim must be tagged with one of these statuses:

- `Verified` - the user provided source evidence and the claim follows that evidence.
- `Needs confirmation` - the claim may be reasonable but needs owner, legal, assurance, or source confirmation.
- `Missing data` - the claim cannot be made because the necessary input has not been provided.
- `Do not claim` - the wording is unsupported, risky, promotional, misleading, or outside the available evidence.

## What This Pack Cannot Do

- It cannot verify current law or stock exchange rules without official source text.
- It cannot provide legal advice, assurance, audit opinions, or regulatory sign-off.
- It cannot invent emissions data, Scope 1, Scope 2, Scope 3 figures, board oversight mechanisms, ESG rating scores, supplier audit results, net zero targets, assurance status, or compliance status.
- It cannot safely use confidential company information unless the user provides it in the current working context and is authorized to do so.
- It does not make network calls in the MVP.

## Human Review Required

Outputs are draft working papers for professional review. Before external use, have the relevant owner review and approve the output, such as ESG, IR, company secretarial, legal, finance, sustainability, operations, assurance provider, management, or board secretary.

## Maintenance

For developers and skill maintainers:

```sh
python3 -m unittest discover -s tests
```

The tests validate skill metadata, mandatory sections, evidence statuses, greenwashing guardrails, framework placeholders, installer options, self-contained skill files, examples, and no-network constraints.

When updating a framework reference, keep the file cautious and include:

- `framework_name`
- `jurisdiction`
- `applicable_companies`
- `source_placeholder`
- `last_reviewed_date`
- `status`
- `update_notes`

Do not turn placeholder references into legal checklists unless the official source text has been reviewed and cited.
