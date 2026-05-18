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
    "esg-a-share-gap-check",
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
    "执行摘要",
    "适用框架与假设",
    "关键发现",
    "实用输出",
    "证据状态",
    "风险提示",
    "下一步行动",
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

UNQUALIFIED_OVERCLAIM_PHRASES = [
    "fully met",
    "no material compliance gaps",
    "Part D non-compliance",
    "industry-leading",
    "world-class",
    "best practice",
    "fully compliant",
    "HKEX compliant",
    "ISSB compliant",
]

GREENWASHING_ALLOWED_MARKERS = [
    "guardrail",
    "flag",
    "avoid",
    "do not",
    "unsupported",
    "unless explicitly supported",
]

OVERCLAIM_ALLOWED_MARKERS = [
    "avoid",
    "do not",
    "unless",
    "flag",
    "guardrail",
    "prohibited",
    "overclaim",
    "caution",
    "replace",
    "source language",
    "quoting",
    "quoted",
    "not",
    "generated-output excerpt to avoid",
    "not a compliance conclusion",
    "preferred replacements",
    "risky",
]

TRIGGER_PHRASES = [
    "HKEX",
    "Hong Kong listed",
    "Part D",
    "climate disclosure",
    "A股",
    "A-share",
    "上交所",
    "深交所",
    "可持续发展报告",
    "第14号",
    "第17号",
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
    "Default Output Language",
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
    "Chinese-first",
    "Output in English only when the user explicitly requests English",
    "Output bilingual content only when the user explicitly requests bilingual output",
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

REALISTIC_SCENARIO_REQUIRED_PHRASES = [
    "Scenario 1: Hong Kong Listed Issuer ESG Report Gap Review",
    "Scenario 2: Investor Roadshow ESG Question Set",
    "Scenario 3: Board / ESG Committee Pre-Read",
    "Scenario 4: ESG Data Collection Cycle",
    "Scenario 5: Customer / Supplier ESG Questionnaire",
    "Scenario 6: Materiality Assessment Planning",
    "Scenario 7: Multilingual Output",
    "Scenario 8: Low-AI-Maturity User",
    "vague board oversight",
    "supplier ESG audit results",
    "请用英文准备董事会/IR可用的ESG风险措辞",
    "Default Chinese Output",
    "帮我用中文整理",
    "帮我看看这个ESG材料能不能发。",
    "draft",
    "internal working paper",
    "board pre-read",
    "external disclosure",
    "regulatory filing",
    "investor response",
    "Multilingual usability where relevant",
]

RESEARCH_MAP_REQUIRED_PHRASES = [
    "HKEX ESG Academy Rules and Regulations",
    "HKEX Appendix C2",
    "IFRS Introduction to ISSB",
    "GRI 3: Material Topics 2021",
    "CDP Question Bank",
    "EcoVadis supporting documents guidance",
    "MSCI ESG Ratings overview",
    "Morningstar Sustainalytics ESG Risk Ratings overview",
    "Macquarie Sustainability reporting page",
    "Caterpillar sustainability reporting page",
    "not a legal checklist",
    "v0.1",
    "v0.2",
]

DEPARTMENT_TRACKER_COLUMNS = [
    "部门",
    "指标 / 数据项",
    "报告期间",
    "来源系统或文件",
    "负责人",
    "所需证据",
    "证据状态",
    "风险提示",
    "下一步行动",
    "复核人",
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

WORKFLOW_REQUIRED_PHRASES = [
    "Classify",
    "draft",
    "internal working paper",
]

OUTPUT_USE_TERMS = [
    "board pre-read",
    "external",
    "regulatory filing",
    "investor response",
    "customer response",
    "provider submission",
    "ESG report",
]

LANGUAGE_POLICY_REQUIRED_PHRASES = [
    "Default output language: Chinese (`zh-CN`)",
    "If the user writes in Chinese, output in Chinese",
    "If the user writes in mixed Chinese/English, output in Chinese",
    "If the user writes in English but does not specify output language, prefer a Chinese summary",
    "Output in English only when the user explicitly requests English",
    "Output bilingual content only when the user explicitly requests bilingual output",
]

HKEX_OBLIGATION_REQUIRED_PHRASES = [
    "强制披露（Mandatory）",
    "不遵守就解释（Comply-or-explain）",
    "自愿披露（Voluntary）",
    "适用性待确认（Applicability to confirm）",
    "未评估（Not assessed）",
    "Part D climate disclosures apply from financial years commencing on or after 1 January 2025",
    "LargeCap status must be confirmed",
    "需公司秘书 / 法务确认（Requires company secretary / legal confirmation）",
]

HKEX_CHINESE_EVIDENCE_REQUIRED_PHRASES = [
    "已验证（Verified）",
    "需确认（Needs confirmation）",
    "缺数据（Missing data）",
    "不得声称（Do not claim）",
    "证据状态：缺数据（Missing data）",
    "证据状态：不得声称（Do not claim）",
]

HKEX_CHINESE_OBLIGATION_REQUIRED_PHRASES = [
    "强制披露（Mandatory）",
    "不遵守就解释（Comply-or-explain）",
    "自愿披露（Voluntary）",
    "适用性待确认（Applicability to confirm）",
    "未评估（Not assessed）",
    "义务层级：适用性待确认（Applicability to confirm）",
]

GLOBAL_VERIFIED_REQUIRED_PHRASES = [
    "supported by user-provided or public report material only",
    "does not mean legally verified, audited, assured, regulator-approved, board-approved, externally publishable, complete, or free from error",
    "state the assurance level separately",
]

MATERIALITY_REQUIRED_PHRASES = [
    "CSRD/ESRS uses double materiality",
    "GRI is impact-oriented",
    "ISSB is investor-focused / financial materiality baseline",
    "Do not say ISSB emphasizes double materiality",
]

INVESTOR_CAUTION_REQUIRED_PHRASES = [
    "selective disclosure",
    "inside information",
    "market-sensitive information",
    "approved channels",
    "approved public channels",
]

REAL_COMPANY_ISSUE_REQUIRED_PHRASES = [
    "Linklogis HKEX Part D Over-Strong Mandatory Wording",
    "Part D non-compliance",
    "义务层级：适用性待确认（Applicability to confirm）",
    "Lenovo ISSB Readiness Overclaim Risk",
    "Fully met",
    "industry-leading",
    "Lenovo Verified Definition Good Example",
    "supported by the provided public report material only",
    "Lenovo Product Carbon Neutrality Cautious Wording Good Example",
    "Lenovo Materiality Framework Correction",
    "CSRD/ESRS uses double materiality",
    "ISSB is investor-focused / financial materiality baseline",
]

A_SHARE_REQUIRED_PHRASES = [
    "esg-a-share-gap-check",
    "上海证券交易所上市公司自律监管指引第14号",
    "深圳证券交易所上市公司自律监管指引第17号",
    "上证180",
    "科创50",
    "深证100",
    "创业板指数样本公司",
    "境内外同时上市公司",
    "其他自愿披露公司",
    "强制披露",
    "鼓励披露",
    "自愿披露",
    "适用性待确认",
    "未评估",
    "潜在披露差距",
    "准备度差距",
    "需证券部 / 董办 / 法务 / ESG / 财务确认",
]

A_SHARE_OUTPUT_HEADINGS = [
    "使用的 skill",
    "输出用途分类",
    "适用框架与假设",
    "A 股披露主体判断",
    "议题差距表",
    "证据状态",
    "风险提示",
    "更审慎表述",
    "下一步行动",
    "审核交接",
]

A_SHARE_CAUTION_REQUIRED_PHRASES = [
    "义务层级：适用性待确认",
    "证券部 / 董办 / 法务确认",
    "不得直接判断合规或不合规",
    "在主体状态确认前，所有义务层级判断均应保持为“适用性待确认”",
    "任何披露时间表须经管理层、证券部、董办、法务及相关审核人确认后方可对外使用",
    "原因说明",
    "改进计划",
    "后续披露安排",
    "适用规则要求下的解释性说明",
]

A_SHARE_FORBIDDEN_PATTERNS = [
    "5个交易日",
    "5 个交易日",
    "义务层级（暂定）: 强制披露",
]

DEEP_QUALITY_FIXTURES = {
    "deep_quality_scenarios.md": [
        "A1",
        "A8",
        "H1",
        "H8",
        "I5",
        "Q5",
        "B4",
        "D4",
        "R3",
        "M4",
        "L5",
    ],
    "red_team_prompts.md": [
        "A 股 Red Team",
        "HKEX Red Team",
        "ISSB Red Team",
        "Investor / Rating Red Team",
    ],
    "language_policy_scenarios.md": [
        "LP1",
        "LP2",
        "LP3",
        "LP4",
        "LP5",
        "LP6",
    ],
    "obligation_level_scenarios.md": [
        "A 股 Unknown Status Rule",
        "HKEX Unknown Status Rule",
        "义务层级：适用性待确认",
    ],
    "telegram_qq_output_regressions.md": [
        "Regression 1",
        "Regression 6",
        "义务层级（暂定）: 强制披露",
        "将在数据条件成熟后补充披露",
    ],
}

QUALITY_GATE_REQUIRED_PHRASES = [
    "No Unsupported Legal Or Regulatory Conclusions",
    "No Unapproved Future Disclosure Commitments",
    "A 股 Unknown Status Rule",
    "HKEX Unknown Status Rule",
    "Evidence Status Chinese-First",
    "Output Language",
    "Reviewer Handoff",
    "Listed-Company IR And External-Use Controls",
    "义务层级：适用性待确认",
    "已验证（Verified）",
    "需确认（Needs confirmation）",
    "缺数据（Missing data）",
    "不得声称（Do not claim）",
]

QUALITY_REGULATORY_FORBIDDEN = [
    "违规",
    "不合规",
    "必须披露",
    "已符合",
    "HKEX compliant",
    "ISSB compliant",
    "fully compliant",
    "fully met",
    "no material gaps",
    "industry-leading",
    "world-class",
    "best practice",
]

QUALITY_FUTURE_FORBIDDEN = [
    "将在后续报告期披露",
    "将在数据条件成熟后补充披露",
    "计划披露",
    "预计披露",
    "将披露",
    "保证",
    "承诺",
]

QUALITY_ALLOWED_CONTEXT_MARKERS = [
    "guardrail",
    "forbidden",
    "do-not-say",
    "do not",
    "don't",
    "avoid",
    "unless",
    "caution",
    "quality gate",
    "regression",
    "red-team",
    "red team",
    "prompt",
    "expected",
    "bad generated-output excerpt",
    "required replacement",
    "unsupported",
    "replace",
    "不得",
    "不要",
    "避免",
    "禁止",
    "禁用",
    "不得表述",
    "除非",
    "不应",
    "不判断",
    "不作",
    "不构成",
    "不是",
    "未经",
    "未批准",
    "风险提示",
    "更审慎",
    "不用于",
    "不要直接",
    "不得直接",
]

FUTURE_ALLOWED_CONTEXT_MARKERS = [
    "do not",
    "avoid",
    "unless",
    "forbidden",
    "quality gate",
    "regression",
    "red-team",
    "red team",
    "bad generated-output excerpt",
    "required replacement",
    "不得",
    "不要",
    "避免",
    "禁止",
    "禁用",
    "除非",
    "未批准",
    "未经",
    "不应",
    "仅当",
    "without",
    "批准时间表",
    "approved timetable",
]

SAMPLE_OUTPUT_REQUIRED_HEADINGS = [
    "使用的 skill",
    "输出用途分类",
    "适用框架与假设",
    "关键发现 / 差距表",
    "证据状态",
    "风险提示",
    "下一步行动",
    "审核交接",
    "专业审核声明",
]

REVIEWER_HANDOFF_TERMS = [
    "ESG",
    "IR",
    "公司秘书",
    "董办",
    "证券部",
    "法务",
    "财务",
    "EHS",
    "运营",
    "采购",
    "管理层",
    "董事会",
]

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
        for key in ["version", "domain", "last_reviewed_date", "output_language_default", "output_language_policy", "professional_review_required"]:
            if key not in metadata:
                failures.append(f"{skill_md}: metadata.{key} missing")
        if metadata.get("output_language_default") != "zh-CN":
            failures.append(f"{skill_md}: metadata.output_language_default must be zh-CN")
        if metadata.get("output_language_policy") != "Chinese-first unless English or bilingual output is explicitly requested":
            failures.append(f"{skill_md}: metadata.output_language_policy must be Chinese-first")
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
        failures.extend(validate_global_verified_definition(body, skill_md))
        failures.extend(validate_language_policy(body, skill_md))
        failures.extend(validate_shell_injection_absent(skill_md))
        failures.extend(validate_human_review_language(skill_dir.name, body, skill_md))
        failures.extend(validate_workflow_realism(body, skill_md))

    return failures


def validate_workflow_realism(body: str, path: Path) -> list[str]:
    failures: list[str] = []
    lowered = body.lower()
    for phrase in WORKFLOW_REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            failures.append(f"{path}: missing workflow realism phrase: {phrase}")
    if "preserve evidence status labels and risk flags" not in lowered and "preserving evidence status labels and risk flags" not in lowered:
        failures.append(f"{path}: missing bilingual evidence-status preservation phrase")
    if not any(term in body for term in OUTPUT_USE_TERMS):
        failures.append(f"{path}: missing output-use classification term")
    return failures


def validate_language_policy(body: str, path: Path) -> list[str]:
    failures: list[str] = []
    for phrase in LANGUAGE_POLICY_REQUIRED_PHRASES:
        if phrase not in body:
            failures.append(f"{path}: missing Chinese-first language policy phrase: {phrase}")
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


def validate_global_verified_definition(body: str, path: Path) -> list[str]:
    failures: list[str] = []
    lowered = body.lower()
    for phrase in GLOBAL_VERIFIED_REQUIRED_PHRASES:
        if phrase.lower() not in lowered:
            failures.append(f"{path}: missing global Verified definition phrase: {phrase}")
    return failures


def validate_release_hardening() -> list[str]:
    failures: list[str] = []

    hkex = read_text(ROOT / "skills" / "esg-hkex-gap-check" / "SKILL.md")
    for phrase in HKEX_OBLIGATION_REQUIRED_PHRASES:
        if phrase not in hkex:
            failures.append(f"esg-hkex-gap-check missing HKEX obligation phrase: {phrase}")

    materiality = read_text(ROOT / "skills" / "esg-materiality" / "SKILL.md")
    for phrase in MATERIALITY_REQUIRED_PHRASES:
        if phrase not in materiality:
            failures.append(f"esg-materiality missing framework distinction phrase: {phrase}")

    investor = read_text(ROOT / "skills" / "esg-investor-qa" / "SKILL.md").lower()
    for phrase in INVESTOR_CAUTION_REQUIRED_PHRASES:
        if phrase.lower() not in investor:
            failures.append(f"esg-investor-qa missing investor caution phrase: {phrase}")

    failures.extend(validate_unqualified_overclaim_phrases())
    failures.extend(validate_real_company_issue_fixture())
    failures.extend(validate_hkex_chinese_first_labels())
    failures.extend(validate_a_share_skill())
    return failures


def validate_unqualified_overclaim_phrases() -> list[str]:
    failures: list[str] = []
    paths = list((ROOT / "skills").glob("*/SKILL.md"))
    paths += list((ROOT / "shared" / "templates").glob("*.md"))
    paths += list((ROOT / "shared" / "examples").glob("*.md"))
    paths += list((ROOT / "skills").glob("*/assets/templates/*.md"))
    paths += list((ROOT / "skills").glob("*/examples/*.md"))
    paths += [ROOT / "README.md", ROOT / "PILOT_GUIDE.md", ROOT / "CHANGELOG.md"]

    for path in paths:
        if not path.exists():
            continue
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            lowered = line.lower()
            for phrase in UNQUALIFIED_OVERCLAIM_PHRASES:
                if phrase.lower() in lowered and not any(marker in lowered for marker in OVERCLAIM_ALLOWED_MARKERS):
                    failures.append(f"{path}:{line_no}: unqualified overclaim phrase: {phrase}")
    return failures


def validate_real_company_issue_fixture() -> list[str]:
    failures: list[str] = []
    path = ROOT / "tests" / "fixtures" / "real_company_output_issues.md"
    if not path.exists():
        return [f"missing real-company output issue fixture: {path}"]
    text = read_text(path)
    for phrase in REAL_COMPANY_ISSUE_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{path}: missing real-company issue phrase: {phrase}")
    return failures


def hkex_default_output_paths() -> list[Path]:
    paths = [
        ROOT / "skills" / "esg-hkex-gap-check" / "SKILL.md",
        ROOT / "shared" / "templates" / "hkex-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-hkex-gap-check.md",
        ROOT / "tests" / "fixtures" / "real_company_output_issues.md",
        ROOT / "CHANGELOG.md",
    ]
    paths += list((ROOT / "skills").glob("*/assets/templates/hkex-gap-check-template.md"))
    paths += list((ROOT / "skills").glob("*/examples/example-hkex-gap-check.md"))
    return [path for path in paths if path.exists()]


def hkex_forbidden_literal_patterns() -> list[str]:
    return [
        "Vol" + "untry",
        "sug" + "ared wording",
        "Evidence status: Missing data",
        "Evidence status: Do not claim",
        "Obligation level to confirm",
    ]


def validate_hkex_chinese_first_labels() -> list[str]:
    failures: list[str] = []
    required_paths = [
        ROOT / "skills" / "esg-hkex-gap-check" / "SKILL.md",
        ROOT / "shared" / "templates" / "hkex-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-hkex-gap-check.md",
    ]
    for path in required_paths:
        text = read_text(path)
        for phrase in HKEX_CHINESE_EVIDENCE_REQUIRED_PHRASES:
            if phrase not in text:
                failures.append(f"{path}: missing HKEX Chinese-first evidence label: {phrase}")
        for phrase in HKEX_CHINESE_OBLIGATION_REQUIRED_PHRASES:
            if phrase not in text:
                failures.append(f"{path}: missing HKEX Chinese-first obligation label: {phrase}")

    for path in hkex_default_output_paths():
        text = read_text(path)
        for pattern in hkex_forbidden_literal_patterns():
            if pattern in text:
                failures.append(f"{path}: HKEX default-output forbidden phrase found: {pattern}")
    return failures


def validate_a_share_skill() -> list[str]:
    failures: list[str] = []
    skill_path = ROOT / "skills" / "esg-a-share-gap-check" / "SKILL.md"
    if not skill_path.exists():
        return [f"missing A-share skill: {skill_path}"]
    text = read_text(skill_path)

    for phrase in A_SHARE_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{skill_path}: missing A-share phrase: {phrase}")
    for phrase in A_SHARE_OUTPUT_HEADINGS:
        if phrase not in text:
            failures.append(f"{skill_path}: missing A-share output heading: {phrase}")
    for phrase in LANGUAGE_POLICY_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{skill_path}: missing A-share language policy phrase: {phrase}")
    for phrase in ["已验证（Verified）", "需确认（Needs confirmation）", "缺数据（Missing data）", "不得声称（Do not claim）"]:
        if phrase not in text:
            failures.append(f"{skill_path}: missing Chinese-first evidence status: {phrase}")
    for forbidden in ["违规", "不合规", "必须披露", "已符合上交所/深交所要求"]:
        if forbidden in text and "Do not write" not in text:
            failures.append(f"{skill_path}: A-share forbidden regulatory phrase not guarded: {forbidden}")
    if "不用于 HKEX" not in text or "esg-hkex-gap-check" not in text:
        failures.append(f"{skill_path}: missing A-share/HKEX separation language")

    router = read_text(ROOT / "skills" / "esg" / "SKILL.md")
    for phrase in ["A股", "上交所", "深交所", "可持续发展报告", "第14号", "第17号", "esg-a-share-gap-check"]:
        if phrase not in router:
            failures.append(f"esg router missing A-share trigger: {phrase}")

    hkex = read_text(ROOT / "skills" / "esg-hkex-gap-check" / "SKILL.md")
    for phrase in ["A股", "A 股", "上交所", "深交所", "第14号", "第17号"]:
        if phrase in hkex:
            failures.append(f"HKEX skill should not claim A-share scope: {phrase}")

    for path in [
        ROOT / "shared" / "templates" / "a-share-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-a-share-gap-check.md",
        ROOT / "shared" / "references" / "framework-sse-sustainability-reporting-guideline.md",
        ROOT / "shared" / "references" / "framework-szse-sustainability-reporting-guideline.md",
        ROOT / "skills" / "esg-a-share-gap-check" / "assets" / "templates" / "a-share-gap-check-template.md",
        ROOT / "skills" / "esg-a-share-gap-check" / "examples" / "example-a-share-gap-check.md",
        ROOT / "skills" / "esg-a-share-gap-check" / "references" / "framework-sse-sustainability-reporting-guideline.md",
        ROOT / "skills" / "esg-a-share-gap-check" / "references" / "framework-szse-sustainability-reporting-guideline.md",
    ]:
        if not path.exists():
            failures.append(f"missing A-share self-contained resource: {path}")

    a_share_paths = [
        ROOT / "skills" / "esg-a-share-gap-check" / "SKILL.md",
        ROOT / "shared" / "templates" / "a-share-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-a-share-gap-check.md",
        ROOT / "tests" / "fixtures" / "pilot_scenarios.md",
        ROOT / "CHANGELOG.md",
    ]
    a_share_paths += list((ROOT / "skills").glob("*/assets/templates/a-share-gap-check-template.md"))
    a_share_paths += list((ROOT / "skills").glob("*/examples/example-a-share-gap-check.md"))

    for path in a_share_paths:
        if not path.exists():
            continue
        text_for_path = read_text(path)
        for pattern in A_SHARE_FORBIDDEN_PATTERNS:
            if pattern in text_for_path:
                failures.append(f"{path}: A-share forbidden phrase found: {pattern}")
        if "comply-or-explain" in text_for_path and "Do not default to `comply-or-explain`" not in text_for_path and "不要默认使用 `comply-or-explain`" not in text_for_path:
            failures.append(f"{path}: default A-share comply-or-explain wording found")

    combined_a_share_text = "\n".join(read_text(path) for path in a_share_paths if path.exists())
    for phrase in A_SHARE_CAUTION_REQUIRED_PHRASES:
        if phrase not in combined_a_share_text:
            failures.append(f"A-share caution phrase missing: {phrase}")

    readme = read_text(ROOT / "README.md")
    for phrase in ["港股用", "A 股用", "esg-a-share-gap-check", "esg-hkex-gap-check"]:
        if phrase not in readme:
            failures.append(f"README missing A-share/HKEX chooser phrase: {phrase}")

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
        for phrase in ["证据状态", "风险提示", "下一步行动"]:
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
    realistic = ROOT / "tests" / "fixtures" / "realistic_work_scenarios.md"
    if not realistic.exists():
        failures.append(f"missing realistic scenario fixture: {realistic}")
    else:
        realistic_text = read_text(realistic)
        realistic_lowered = realistic_text.lower()
        for phrase in REALISTIC_SCENARIO_REQUIRED_PHRASES:
            if phrase.lower() not in realistic_lowered:
                failures.append(f"{realistic}: missing realistic scenario phrase: {phrase}")
        for status in EVIDENCE_STATUSES:
            if status not in realistic_text:
                failures.append(f"{realistic}: missing evidence status {status}")
    return failures


def validate_research_map() -> list[str]:
    failures: list[str] = []
    path = ROOT / "research" / "public_source_research_map.md"
    if not path.exists():
        return [f"missing public source research map: {path}"]
    text = read_text(path)
    for phrase in RESEARCH_MAP_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{path}: missing research phrase: {phrase}")
    if "http" not in text:
        failures.append(f"{path}: missing public URLs")
    return failures


def quality_scan_paths() -> list[Path]:
    paths: list[Path] = []
    paths += list((ROOT / "skills").glob("*/SKILL.md"))
    paths += list((ROOT / "shared" / "templates").glob("*"))
    paths += list((ROOT / "shared" / "examples").glob("*"))
    paths += list((ROOT / "skills").glob("*/assets/templates/*"))
    paths += list((ROOT / "skills").glob("*/examples/*"))
    paths += list((ROOT / "tests" / "fixtures").glob("*.md"))
    paths += [
        ROOT / "README.md",
        ROOT / "PILOT_GUIDE.md",
        ROOT / "CHANGELOG.md",
        ROOT / "QUALITY_GATES.md",
    ]
    return [path for path in paths if path.exists() and path.is_file()]


def line_has_allowed_context(line: str, markers: list[str]) -> bool:
    lowered = line.lower()
    return any(marker.lower() in lowered for marker in markers)


def validate_quality_gate_file() -> list[str]:
    failures: list[str] = []
    path = ROOT / "QUALITY_GATES.md"
    if not path.exists():
        return [f"missing quality gates file: {path}"]
    text = read_text(path)
    for phrase in QUALITY_GATE_REQUIRED_PHRASES:
        if phrase not in text:
            failures.append(f"{path}: missing quality gate phrase: {phrase}")
    return failures


def validate_deep_quality_fixtures() -> list[str]:
    failures: list[str] = []
    fixture_dir = ROOT / "tests" / "fixtures"
    for filename, required_phrases in DEEP_QUALITY_FIXTURES.items():
        path = fixture_dir / filename
        if not path.exists():
            failures.append(f"missing deep quality fixture: {path}")
            continue
        text = read_text(path)
        for phrase in required_phrases:
            if phrase not in text:
                failures.append(f"{path}: missing deep quality phrase: {phrase}")

    deep_path = fixture_dir / "deep_quality_scenarios.md"
    if deep_path.exists():
        text = read_text(deep_path)
        scenario_count = len(re.findall(r"^\| [A-Z]\d+ ", text, flags=re.MULTILINE))
        if scenario_count < 40:
            failures.append(f"{deep_path}: expected at least 40 scenarios, found {scenario_count}")
        for section in ["## A.", "## B.", "## C.", "## D.", "## E.", "## F.", "## G.", "## H.", "## I."]:
            if section not in text:
                failures.append(f"{deep_path}: missing scenario category {section}")
    return failures


def validate_quality_phrase_gates() -> list[str]:
    failures: list[str] = []
    for path in quality_scan_paths():
        if path.name == "QUALITY_GATES.md":
            continue
        lines = read_text(path).splitlines()
        for index, line in enumerate(lines):
            line_no = index + 1
            context = "\n".join(lines[max(0, index - 3) : min(len(lines), index + 3)])
            for phrase in QUALITY_REGULATORY_FORBIDDEN:
                if phrase.lower() in line.lower() and not line_has_allowed_context(context, QUALITY_ALLOWED_CONTEXT_MARKERS):
                    failures.append(f"{path}:{line_no}: quality gate regulatory phrase outside caution context: {phrase}")
            for phrase in QUALITY_FUTURE_FORBIDDEN:
                if phrase in line and not line_has_allowed_context(context, FUTURE_ALLOWED_CONTEXT_MARKERS):
                    failures.append(f"{path}:{line_no}: future disclosure phrase outside caution context: {phrase}")
    return failures


def validate_unknown_status_defaults() -> list[str]:
    failures: list[str] = []
    a_share_paths = [
        ROOT / "skills" / "esg-a-share-gap-check" / "SKILL.md",
        ROOT / "shared" / "templates" / "a-share-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-a-share-gap-check.md",
        ROOT / "tests" / "fixtures" / "obligation_level_scenarios.md",
        ROOT / "tests" / "fixtures" / "sample_outputs_for_review.md",
    ]
    hkex_paths = [
        ROOT / "skills" / "esg-hkex-gap-check" / "SKILL.md",
        ROOT / "shared" / "templates" / "hkex-gap-check-template.md",
        ROOT / "shared" / "examples" / "example-hkex-gap-check.md",
        ROOT / "tests" / "fixtures" / "obligation_level_scenarios.md",
        ROOT / "tests" / "fixtures" / "sample_outputs_for_review.md",
    ]
    for path in a_share_paths:
        if path.exists() and "义务层级：适用性待确认" not in read_text(path):
            failures.append(f"{path}: missing A-share unknown-status default obligation label")
    for path in hkex_paths:
        if path.exists() and "义务层级：适用性待确认" not in read_text(path):
            failures.append(f"{path}: missing HKEX unknown-status default obligation label")
    return failures


def validate_sample_outputs_for_review() -> list[str]:
    failures: list[str] = []
    path = ROOT / "tests" / "fixtures" / "sample_outputs_for_review.md"
    if not path.exists():
        return [f"missing sample outputs fixture: {path}"]
    text = read_text(path)
    sample_count = len(re.findall(r"^## Sample \d+:", text, flags=re.MULTILINE))
    if sample_count < 8:
        failures.append(f"{path}: expected at least 8 sample outputs, found {sample_count}")
    for heading in SAMPLE_OUTPUT_REQUIRED_HEADINGS:
        if heading not in text:
            failures.append(f"{path}: missing sample output heading: {heading}")
    for status in ["已验证（Verified）", "需确认（Needs confirmation）", "缺数据（Missing data）", "不得声称（Do not claim）"]:
        if status not in text:
            failures.append(f"{path}: missing Chinese-first evidence status: {status}")
    for term in REVIEWER_HANDOFF_TERMS:
        if term not in text:
            failures.append(f"{path}: missing reviewer handoff term: {term}")
    for phrase in [
        "本输出为内部工作底稿",
        "不构成法律、监管、审计、鉴证、财务或可持续发展报告意见",
        "不得在负责审核人批准前对外发布、提交、披露或纳入 ESG 报告",
        "基于已提供材料，未识别出重大准备度差距；这不是合规结论。",
        "未从已提供材料识别出重大风险，但仍需 IR/法务/公司秘书复核。",
    ]:
        if phrase not in text:
            failures.append(f"{path}: missing sample-output risk phrase: {phrase}")
    return failures


def validate_quality_gates() -> list[str]:
    failures: list[str] = []
    failures.extend(validate_quality_gate_file())
    failures.extend(validate_deep_quality_fixtures())
    failures.extend(validate_quality_phrase_gates())
    failures.extend(validate_unknown_status_defaults())
    failures.extend(validate_sample_outputs_for_review())
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
    failures.extend(validate_research_map())
    failures.extend(validate_release_hardening())
    failures.extend(validate_quality_gates())
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
