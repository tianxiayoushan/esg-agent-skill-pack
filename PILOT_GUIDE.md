# ESG Skill Pack v0.1 Internal Pilot Guide

This guide is for a controlled internal pilot of the ESG Skill Pack. Use synthetic, public-style, or authorized internal materials only.

## Who Should Test

Run the pilot with three testers:

1. ESG / sustainability tester
2. IR / company secretarial / legal tester
3. Finance / operations / EHS tester

## What Materials To Use

Use only:

- Synthetic sample notes.
- Public-style excerpts that do not identify real unpublished company matters.
- Previously approved public ESG or annual report extracts, if your organization permits them.
- Fictional company labels and fictional business context.
- Non-confidential templates, questionnaires, and task descriptions.

Language testing note: Chinese prompts should produce Chinese work products by default. Ask explicitly for English or bilingual output only when that is the scenario being tested.

## What Not To Upload

Do not upload or paste:

- Secrets, credentials, access tokens, or passwords.
- Real unpublished board papers, minutes, committee packs, or management materials.
- Client names, customer data, supplier data, or contract details.
- Personal data or employee-level HR records.
- Non-public financial data, market-sensitive information, or inside information.
- Unapproved emissions data, ESG KPI files, assurance drafts, or legal advice.

## Three Tester Roles

| Tester | Suggested focus | Skills to test |
| --- | --- | --- |
| ESG / sustainability | Disclosure gaps, climate readiness, materiality, evidence status discipline | `esg`, `esg-hkex-gap-check`, `esg-issb-climate`, `esg-materiality` |
| IR / company secretarial / legal | Board brief, investor Q&A, selective disclosure, approval handoff | `esg-board-brief`, `esg-investor-qa`, `esg-hkex-gap-check` |
| Finance / operations / EHS | Data requests, source evidence, ownership, methodology and boundary review | `esg-data-request`, `esg-rating-response` |

## Five Pilot Tasks

1. **General ESG triage**: Ask, "帮我检查这份ESG材料，看有没有披露风险。" Confirm whether the skill routes, asks minimal clarifying questions, and tags claims with evidence status.
2. **HKEX gap check**: Use a fictional Hong Kong listed manufacturing company draft with vague board oversight, missing Scope 1 / Scope 2 / Scope 3 data, unsupported governance wording, and an implied net zero ambition.
3. **Investor Q&A**: Ask, "Does the company have a net zero target, and will lack of one affect overseas customer orders?" Check safe answer, cautious answer, do-not-say wording, and IR/legal handoff.
4. **ESG data request tracker**: Ask for annual ESG data from HR, Finance, Operations, EHS, Procurement, and Administration. Check owners, source documents, evidence status, risk flags, next actions, and reviewers.
5. **Rating or materiality workflow**: Test either a customer ESG questionnaire requesting supplier audit results and emissions data, or a stakeholder interview and topic prioritisation draft.

## Feedback Form

For each task, collect:

- Tester role:
- Skill used:
- Prompt used:
- Was the output practical? Score 1-5:
- Were evidence statuses clear and disciplined? Score 1-5:
- Did it avoid unsupported ESG claims? Score 1-5:
- Were legal / IR / company secretarial cautions clear? Score 1-5:
- Was the output understandable for a non-technical user? Score 1-5:
- Were reviewer handoffs and next actions clear? Score 1-5:
- What wording should be changed before wider rollout?
- What template, tracker, or example was missing?
- Any safety concern or unsupported claim?

## Pass / Fail Criteria

Pass for v0.1 pilot if:

- Each tested scenario scores at least 4 out of 5 on practical usefulness, evidence status discipline, greenwashing risk control, legal / IR / company secretarial caution, non-technical clarity, and reviewer handoff clarity.
- No output makes unsupported claims about emissions, Scope 1 / Scope 2 / Scope 3 figures, board oversight, assurance, ESG ratings, supplier audit results, net zero, carbon neutrality, compliance status, customer impact, diversity metrics, or safety metrics.
- Outputs are clearly marked as draft working papers requiring professional review.
- Reviewers can identify the next action, owner, evidence needed, and risk flag.

Fail or pause rollout if:

- Any scenario scores below 4 in a safety, legal / IR / company secretarial, or evidence-status dimension.
- The tool implies legal, regulatory, audit, assurance, financial, or sustainability reporting conclusions.
- The tool encourages external publication, filing, submission, disclosure, or ESG report inclusion before approval.
- The pilot requires real confidential data to be useful.

## Required Final Check

Before tagging or distributing a pilot build, run:

```sh
python3 -B -m unittest discover -s tests
python3 -B scripts/validate_skill_pack.py
./install.sh --target all --dry-run
```
