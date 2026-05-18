#!/usr/bin/env python3
"""Deterministic local validation for the ESG Skill Pack."""

from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SKILLS = [
    "esg",
    "esg-hkex-gap-check",
    "esg-issb-climate",
    "esg-board-brief",
    "esg-investor-qa",
    "esg-data-request",
    "esg-rating-response",
    "esg-materiality",
]

MANDATORY_SECTIONS = [
    "When to use",
    "When not to use",
    "Required inputs",
    "Workflow",
    "Mandatory output structure",
    "ESG evidence status rules",
    "Greenwashing guardrails",
    "Human review language",
]

MANDATORY_OUTPUT_ITEMS = [
    "Executive summary",
    "Applicable framework and assumptions",
    "Key findings",
    "Practical output",
    "Evidence status",
    "Risk flags",
    "Next actions",
]

EVIDENCE_STATUSES = [
    "Verified",
    "Needs confirmation",
    "Missing data",
    "Do not claim",
]

PROHIBITED_PHRASES = [
    "industry-leading",
    "fully compliant",
    "carbon neutral",
    "net zero aligned",
    "world-class",
    "best practice",
    "robust governance",
    "comprehensive controls",
    "science-based target",
    "no material impact",
]

GREENWASHING_ALLOWED_MARKERS = [
    "guardrail",
    "flag",
    "avoid",
    "do not",
    "unsupported",
    "unless explicitly supported",
]

TRIGGER_PHRASES = [
    "HKEX",
    "Hong Kong listed",
    "Part D",
    "climate disclosure",
    "ISSB",
    "IFRS S1",
    "IFRS S2",
    "TCFD",
    "board brief",
    "board paper",
    "directors",
    "management update",
    "investor",
    "analyst",
    "IR",
    "roadshow",
    "Q&A",
    "MSCI",
    "Sustainalytics",
    "CDP",
    "EcoVadis",
    "supplier questionnaire",
    "data collection",
    "ESG KPI",
    "Scope 1",
    "Scope 2",
    "Scope 3",
    "materiality",
    "stakeholder",
    "topic prioritisation",
]

REQUIRED_README_SECTIONS = [
    "Start Here",
    "What to Provide",
    "Which Skill Should I Use?",
    "Pilot Use Only / Internal Draft Use",
    "Verified Does Not Mean Approved",
]

README_REQUIRED_PHRASES = [
    "does not mean legally verified",
    "audited",
    "assured",
    "regulator-approved",
    "board-approved",
    "must not be externally published, filed, submitted, or disclosed",
    "selective disclosure",
    "inside information",
    "market-sensitive information",
    "approved disclosure channels",
    "must not determine whether a regulatory framework is mandatory",
]

SCENARIO_FIXTURE_REQUIRED_PHRASES = [
    "Scenario 1: ESG Router",
    "Scenario 2: HKEX Gap Check",
    "Scenario 3: ISSB Climate",
    "Scenario 4: Board Brief",
    "Scenario 5: Investor Q&A",
    "Scenario 6: ESG Data Request",
    "Scenario 7: ESG Rating Response",
    "Scenario 8: Materiality",
    "帮我检查这份ESG材料，看有没有披露风险。",
    "robust governance",
    "net zero",
    "mandatory status",
    "board-ready structure",
    "selective disclosure",
    "inside information",
    "market-sensitive information",
    "approved disclosure channels",
    "HR, Finance, Operations, EHS, Procurement, and Administration",
    "supplier ESG audit results",
    "stakeholder interview questions",
    "Practical usefulness",
    "Evidence status discipline",
    "Greenwashing risk control",
    "Legal / IR / company secretarial caution",
    "Non-technical user clarity",
    "Reviewer handoff clarity",
]

DEPARTMENT_TRACKER_COLUMNS = [
    "Department",
    "Metric / data item",
    "Reporting period",
    "Source system or document",
    "Owner",
    "Evidence required",
    "Evidence status",
    "Risk flag",
    "Next action",
    "Reviewer",
]

DEPARTMENT_TRACKER_DEPARTMENTS = [
    "HR",
    "Finance",
    "Operations",
    "EHS",
    "Procurement",
    "Administration",
]

HUMAN_REVIEW_REQUIRED_PHRASES = {
    "esg": [
        "Draft working paper",
        "externally published, filed, submitted, disclosed",
        "included in ESG reports",
    ],
    "esg-hkex-gap-check": [
        "Draft working paper",
        "Placeholder framework references do not determine regulatory compliance",
        "externally published, filed, submitted, disclosed",
        "included in ESG reports",
    ],
    "esg-issb-climate": [
        "Draft working paper",
        "mandatory status",
        "external publication, filing, submission, or disclosure",
    ],
    "esg-board-brief": [
        "Draft working paper",
        "board secretary",
        "externally publish, file, submit, disclose",
        "include board-brief content in ESG reports",
    ],
    "esg-investor-qa": [
        "Draft working paper",
        "selective disclosure",
        "inside information",
        "market-sensitive information",
        "approved disclosure channel",
    ],
    "esg-data-request": [
        "Draft working paper",
        "Data requests do not establish final ESG reporting figures",
        "source-owner confirmation",
        "methodology review",
        "boundary review",
        "Scope 1, Scope 2, and Scope 3 items must be treated as data requests only",
    ],
    "esg-rating-response": [
        "Draft working paper",
        "submission approval",
        "Do not submit, externally disclose",
        "include responses in ESG reports",
    ],
    "esg-materiality": [
        "Draft working paper",
        "externally publish, file, submit, disclose",
        "include materiality conclusions in ESG reports",
    ],
}

def network_patterns() -> list[str]:
    return [
        "cu" + "rl ",
        "wg" + "et ",
        "http" + "://",
        "https" + "://",
        "requests" + ".",
        "urllib" + ".request",
        "http" + ".client",
        "socket" + ".",
        "fe" + "tch(",
        "net" + "/http",
    ]


def shell_injection_patterns() -> list[str]:
    return [
        "ev" + "al ",
        "ba" + "s" + "h -c",
        "s" + "h -c",
        "$" + "(",
        "`" + "curl",
        "`" + "wget",
    ]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        raise AssertionError("missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise AssertionError("missing closing frontmatter delimiter")
    raw = text[4:end]
    body = text[end + 5 :]
    parsed: dict[str, object] = {}
    current_map: dict[str, str] | None = None
    current_key = ""
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  "):
            if current_map is None:
                raise AssertionError(f"nested value without parent: {line}")
            key, value = parse_key_value(line.strip())
            current_map[key] = normalize_scalar(value)
            continue
        key, value = parse_key_value(line)
        if value == "":
            current_map = {}
            parsed[key] = current_map
            current_key = key
        else:
            parsed[key] = normalize_scalar(value)
            current_map = None
            current_key = ""
    if current_key and not parsed[current_key]:
        raise AssertionError(f"empty mapping: {current_key}")
    return parsed, body


def parse_key_value(line: str) -> tuple[str, str]:
    if ":" not in line:
        raise AssertionError(f"invalid YAML line: {line}")
    key, value = line.split(":", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        raise AssertionError(f"empty YAML key: {line}")
    return key, value


def normalize_scalar(value: str) -> object:
    if value in {"true", "false"}:
        return value == "true"
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def skill_paths() -> list[Path]:
    return [ROOT / "skills" / name for name in REQUIRED_SKILLS]


def validate_skills() -> list[str]:
    failures: list[str] = []
    skills_root = ROOT / "skills"
    actual = sorted(p.name for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    if actual != sorted(REQUIRED_SKILLS):
        failures.append(f"skill directories mismatch: {actual}")

    for skill_dir in skill_paths():
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            failures.append(f"missing {skill_md}")
            continue

        try:
            frontmatter, body = parse_frontmatter(read_text(skill_md))
        except AssertionError as exc:
            failures.append(f"{skill_md}: {exc}")
            continue

        if frontmatter.get("name") != skill_dir.name:
            failures.append(f"{skill_md}: name must match directory")
        description = str(frontmatter.get("description", ""))
        if not description:
            failures.append(f"{skill_md}: missing description")
        if len(description) > 260:
            failures.append(f"{skill_md}: description is not concise")

        metadata = frontmatter.get("metadata")
        if not isinstance(metadata, dict):
            failures.append(f"{skill_md}: missing metadata mapping")
            continue
        for key in ["version", "domain", "last_reviewed_date", "output_language_default", "professional_review_required"]:
            if key not in metadata:
                failures.append(f"{skill_md}: metadata.{key} missing")
        if metadata.get("output_language_default") != "user-language":
            failures.append(f"{skill_md}: metadata.output_language_default must be user-language")
        if metadata.get("professional_review_required") is not True:
            failures.append(f"{skill_md}: metadata.professional_review_required must be true")

        for section in MANDATORY_SECTIONS:
            if f"## {section}" not in body:
                failures.append(f"{skill_md}: missing section {section}")
        for item in MANDATORY_OUTPUT_ITEMS:
            if item not in body:
                failures.append(f"{skill_md}: missing output item {item}")
        for status in EVIDENCE_STATUSES:
            if status not in body:
                failures.append(f"{skill_md}: missing evidence status {status}")

        for relative_link in re.findall(r"\]\(([^)#][^)]+)\)", body):
            if relative_link.startswith(("http:", "https:", "mailto:")):
                failures.append(f"{skill_md}: remote links are not allowed in MVP")
            else:
                target = (skill_dir / relative_link).resolve()
                if not target.exists():
                    failures.append(f"{skill_md}: referenced file missing: {relative_link}")

        failures.extend(validate_greenwashing_use(skill_md))
        failures.extend(validate_shell_injection_absent(skill_md))
        failures.extend(validate_human_review_language(skill_dir.name, body, skill_md))

    return failures


def validate_human_review_language(skill_name: str, body: str, path: Path) -> list[str]:
    failures: list[str] = []
    required = HUMAN_REVIEW_REQUIRED_PHRASES.get(skill_name, [])
    for phrase in required:
        if phrase not in body:
            failures.append(f"{path}: human review language missing phrase: {phrase}")
    return failures


def validate_greenwashing_use(path: Path) -> list[str]:
    failures: list[str] = []
    text = read_text(path)
    for line_no, line in enumerate(text.splitlines(), start=1):
        lowered = line.lower()
        for phrase in PROHIBITED_PHRASES:
            if phrase in lowered and not any(marker in lowered for marker in GREENWASHING_ALLOWED_MARKERS):
                failures.append(f"{path}:{line_no}: prohibited phrase not flagged: {phrase}")
    return failures


def validate_shell_injection_absent(path: Path) -> list[str]:
    text = read_text(path)
    failures: list[str] = []
    for pattern in shell_injection_patterns():
        if pattern in text:
            failures.append(f"{path}: potential shell injection pattern: {pattern}")
    return failures


def validate_framework_references() -> list[str]:
    failures: list[str] = []
    for path in list((ROOT / "shared" / "references").glob("framework-*.md")) + list((ROOT / "skills").glob("*/references/framework-*.md")):
        text = read_text(path)
        try:
            frontmatter, _ = parse_frontmatter(text)
        except AssertionError as exc:
            failures.append(f"{path}: {exc}")
            continue
        for key in [
            "framework_name",
            "jurisdiction",
            "applicable_companies",
            "source_placeholder",
            "last_reviewed_date",
            "status",
            "update_notes",
        ]:
            if key not in frontmatter:
                failures.append(f"{path}: missing {key}")
        if frontmatter.get("status") not in {"active", "proposed", "transitional", "deprecated"}:
            failures.append(f"{path}: invalid status")
    return failures


def validate_examples() -> list[str]:
    failures: list[str] = []
    for path in list((ROOT / "shared" / "examples").glob("example-*.md")) + list((ROOT / "skills").glob("*/examples/example-*.md")):
        text = read_text(path)
        for phrase in ["Evidence status", "Risk flags", "Next actions"]:
            if phrase not in text:
                failures.append(f"{path}: missing {phrase}")
    failures.extend(validate_department_tracker_example(ROOT / "shared" / "examples" / "example-data-request-departments.md"))
    failures.extend(validate_department_tracker_example(ROOT / "skills" / "esg-data-request" / "examples" / "example-data-request-departments.md"))
    return failures


def validate_department_tracker_example(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        failures.append(f"missing department tracker example: {path}")
        return failures
    text = read_text(path)
    for column in DEPARTMENT_TRACKER_COLUMNS:
        if column not in text:
            failures.append(f"{path}: missing column {column}")
    for department in DEPARTMENT_TRACKER_DEPARTMENTS:
        if f"| {department} |" not in text:
            failures.append(f"{path}: missing department row {department}")
    for status in EVIDENCE_STATUSES:
        if status not in text:
            failures.append(f"{path}: missing evidence status {status}")
    for phrase in ["no real company data", "no real personnel data", "no emissions figures"]:
        if phrase not in text:
            failures.append(f"{path}: missing synthetic-data disclaimer phrase: {phrase}")
    return failures


def validate_scripts_no_network() -> list[str]:
    failures: list[str] = []
    script_paths = list((ROOT / "scripts").glob("*")) + list((ROOT / "shared" / "scripts").glob("*")) + [ROOT / "install.sh"]
    for path in script_paths:
        if not path.is_file():
            continue
        text = read_text(path)
        lowered = text.lower()
        for pattern in network_patterns():
            if pattern in lowered:
                failures.append(f"{path}: network pattern found: {pattern}")
        for pattern in shell_injection_patterns():
            if pattern in text:
                failures.append(f"{path}: shell injection pattern found: {pattern}")
    return failures


def validate_installer_options() -> list[str]:
    failures: list[str] = []
    install_text = read_text(ROOT / "install.sh")
    for token in ["codex", "claude-code", "openclaw", "hermes", "all"]:
        if token not in install_text:
            failures.append(f"install.sh missing target {token}")
    for token in ["project", "user", "workspace", "personal", "managed"]:
        if token not in install_text:
            failures.append(f"install.sh missing scope {token}")

    with tempfile.TemporaryDirectory() as home:
        result = subprocess.run(
            ["bash", str(ROOT / "install.sh"), "--target", "codex", "--scope", "user", "--dry-run"],
            cwd=ROOT,
            env={"HOME": home, "PATH": "/bin:/usr/bin"},
            text=True,
            capture_output=True,
            check=False,
        )
    if result.returncode != 0:
        failures.append(f"install.sh dry-run failed: {result.stderr}")
    for skill in REQUIRED_SKILLS:
        if skill not in result.stdout:
            failures.append(f"install.sh dry-run did not mention {skill}")
    workspace_result = subprocess.run(
        ["bash", str(ROOT / "install.sh"), "--target", "openclaw", "--scope", "workspace", "--dry-run"],
        cwd=ROOT,
        env={"HOME": str(ROOT), "PATH": "/bin:/usr/bin"},
        text=True,
        capture_output=True,
        check=False,
    )
    if workspace_result.returncode != 0:
        failures.append(f"install.sh openclaw workspace dry-run failed: {workspace_result.stderr}")
    if "Already in place: esg" not in workspace_result.stdout:
        failures.append("install.sh openclaw workspace dry-run should detect source skills already in place")

    failures.extend(validate_target_scope_matrix())
    failures.extend(validate_temp_install_and_force())
    return failures


def validate_target_scope_matrix() -> list[str]:
    failures: list[str] = []
    matrix = [
        ("codex", "project"),
        ("codex", "user"),
        ("claude-code", "project"),
        ("claude-code", "user"),
        ("openclaw", "workspace"),
        ("openclaw", "project"),
        ("openclaw", "personal"),
        ("openclaw", "managed"),
        ("hermes", "user"),
    ]
    with tempfile.TemporaryDirectory(prefix="esg-install-matrix-", dir=ROOT) as project_dir:
        with tempfile.TemporaryDirectory(prefix="esg-home-", dir=ROOT) as home_dir:
            for target, scope in matrix:
                result = subprocess.run(
                    ["bash", str(ROOT / "install.sh"), "--target", target, "--scope", scope, "--dry-run"],
                    cwd=project_dir,
                    env={"HOME": home_dir, "PATH": "/bin:/usr/bin"},
                    text=True,
                    capture_output=True,
                    check=False,
                )
                if result.returncode != 0:
                    failures.append(f"install.sh dry-run failed for {target}/{scope}: {result.stderr}")
                for skill in REQUIRED_SKILLS:
                    if skill not in result.stdout:
                        failures.append(f"install.sh dry-run missing {skill} for {target}/{scope}")
    return failures


def validate_temp_install_and_force() -> list[str]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="esg-install-project-", dir=ROOT) as project_dir:
        with tempfile.TemporaryDirectory(prefix="esg-home-", dir=ROOT) as home_dir:
            env = {"HOME": home_dir, "PATH": "/bin:/usr/bin"}
            install_cmd = ["bash", str(ROOT / "install.sh"), "--target", "codex", "--scope", "project"]
            first = subprocess.run(
                install_cmd,
                cwd=project_dir,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            if first.returncode != 0:
                failures.append(f"temp project install failed: {first.stderr}")
                return failures

            destination = Path(project_dir) / ".agents" / "skills"
            for skill in REQUIRED_SKILLS:
                skill_dir = destination / skill
                for relative in ["SKILL.md", "references", "assets/templates", "examples"]:
                    if not (skill_dir / relative).exists():
                        failures.append(f"installed skill missing {skill}/{relative}")

            root_sentinel = destination / "root-sentinel.txt"
            skill_sentinel = destination / "esg" / "obsolete-local-file.txt"
            root_sentinel.write_text("keep", encoding="utf-8")
            skill_sentinel.write_text("remove on force only", encoding="utf-8")

            second = subprocess.run(
                install_cmd,
                cwd=project_dir,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            if second.returncode != 0:
                failures.append(f"temp reinstall without force failed: {second.stderr}")
            if not skill_sentinel.exists():
                failures.append("install without --force overwrote an existing skill directory")

            forced = subprocess.run(
                install_cmd + ["--force"],
                cwd=project_dir,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            if forced.returncode != 0:
                failures.append(f"temp reinstall with force failed: {forced.stderr}")
            if skill_sentinel.exists():
                failures.append("--force did not replace the target skill directory")
            if not root_sentinel.exists():
                failures.append("--force deleted a non-skill file in the destination root")
    return failures


def validate_readme() -> list[str]:
    failures: list[str] = []
    readme = read_text(ROOT / "README.md")
    lowered = readme.lower()
    for section in REQUIRED_README_SECTIONS:
        if f"## {section}" not in readme:
            failures.append(f"README missing section: {section}")
    for phrase in README_REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            failures.append(f"README missing phrase: {phrase}")
    return failures


def validate_trigger_phrases() -> list[str]:
    failures: list[str] = []
    descriptions = []
    for skill_dir in skill_paths():
        frontmatter, _ = parse_frontmatter(read_text(skill_dir / "SKILL.md"))
        descriptions.append(str(frontmatter.get("description", "")))
    corpus = " ".join(descriptions).lower()
    for phrase in TRIGGER_PHRASES:
        if phrase.lower() not in corpus:
            failures.append(f"trigger phrase missing from descriptions: {phrase}")
    return failures


def validate_pilot_scenarios() -> list[str]:
    failures: list[str] = []
    path = ROOT / "tests" / "fixtures" / "pilot_scenarios.md"
    if not path.exists():
        return [f"missing pilot scenario fixture: {path}"]
    text = read_text(path)
    for phrase in SCENARIO_FIXTURE_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{path}: missing scenario phrase: {phrase}")
    for skill in REQUIRED_SKILLS:
        if f"Skill: `{skill}`" not in text:
            failures.append(f"{path}: missing scenario for skill {skill}")
    for status in EVIDENCE_STATUSES:
        if status not in text:
            failures.append(f"{path}: missing evidence status {status}")
    return failures


def validate_all() -> list[str]:
    failures: list[str] = []
    failures.extend(validate_skills())
    failures.extend(validate_readme())
    failures.extend(validate_framework_references())
    failures.extend(validate_examples())
    failures.extend(validate_scripts_no_network())
    failures.extend(validate_installer_options())
    failures.extend(validate_trigger_phrases())
    failures.extend(validate_pilot_scenarios())
    return failures


def main() -> int:
    failures = validate_all()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("ESG Skill Pack validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
