# Repository Instructions for Codex

This repository contains Agent Skills-compatible ESG skills. Keep it ready for internal pilot use across Codex, Claude Code, OpenClaw, Hermes, and other `SKILL.md`-compatible agents.

## ESG Rules

- Do not invent ESG regulatory requirements, disclosure obligations, exchange rules, standards, rating methodology requirements, or legal conclusions.
- Keep skills instruction-first. Put long background material in `references/`.
- Prefer templates, checklists, trackers, and tables over free-form prose.
- Keep every ESG claim tagged with one evidence status: `Verified`, `Needs confirmation`, `Missing data`, or `Do not claim`.
- Apply greenwashing guardrails before drafting external-facing language.
- Require human professional review for all outputs before external use.

## Repository Rules

- Maintain exactly the eight MVP skill directories under `skills/`: `esg`, `esg-hkex-gap-check`, `esg-issb-climate`, `esg-board-brief`, `esg-investor-qa`, `esg-data-request`, `esg-rating-response`, and `esg-materiality`.
- Each skill must be self-contained after installation, with its own local `references/`, `assets/templates/`, and any needed `examples/`.
- Do not make installed skills depend on `shared/` or another skill directory.
- Keep shared canonical material under `shared/` only as source material for maintainers.
- Do not include real company confidential information, unpublished board materials, secrets, credentials, or private examples.
- Do not make network calls in the MVP.
- Do not add telemetry, registry publishing, remote script execution, or `curl | bash` patterns.

## Change Workflow

- Before editing, identify the affected skill, template, reference, script, or installer file.
- After modifying skills, templates, references, scripts, or `install.sh`, run:

```sh
python3 -m unittest discover -s tests
```

- If tests fail, fix the source problem rather than loosening guardrails.
- Keep `SKILL.md` files concise and trigger-oriented.
