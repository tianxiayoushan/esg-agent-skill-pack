#!/usr/bin/env bash
set -euo pipefail

TARGET="codex"
SCOPE=""
DRY_RUN=0
FORCE=0
DESTINATION=""
DEFAULT_SCOPE=""

SCRIPT_PATH="${BASH_SOURCE[0]}"
SCRIPT_DIR="${SCRIPT_PATH%/*}"
if [ "${SCRIPT_DIR}" = "${SCRIPT_PATH}" ]; then
  SCRIPT_DIR="."
fi

case "${SCRIPT_DIR}" in
  /*) ROOT_DIR="${SCRIPT_DIR}" ;;
  *) ROOT_DIR="${PWD}/${SCRIPT_DIR}" ;;
esac
SOURCE_SKILLS="${ROOT_DIR}/skills"

usage() {
  cat <<'USAGE'
Usage: ./install.sh --target codex|claude-code|openclaw|hermes|all [--scope project|user|workspace|personal|managed] [--dry-run] [--force]

Defaults:
  codex user        -> $HOME/.agents/skills
  codex project     -> .agents/skills
  claude-code user  -> $HOME/.claude/skills
  claude-code project -> .claude/skills
  openclaw workspace -> $PWD/skills
  openclaw project  -> $PWD/.agents/skills
  openclaw personal -> $HOME/.agents/skills
  openclaw managed  -> $HOME/.openclaw/skills
  hermes user       -> $HOME/.hermes/skills
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --scope)
      SCOPE="${2:-}"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

destination_for() {
  local target="$1"
  local scope="$2"
  DESTINATION=""

  case "${target}:${scope}" in
    codex:project) DESTINATION="${PWD}/.agents/skills" ;;
    codex:user) DESTINATION="${HOME}/.agents/skills" ;;
    claude-code:project) DESTINATION="${PWD}/.claude/skills" ;;
    claude-code:user) DESTINATION="${HOME}/.claude/skills" ;;
    openclaw:workspace) DESTINATION="${PWD}/skills" ;;
    openclaw:project) DESTINATION="${PWD}/.agents/skills" ;;
    openclaw:personal) DESTINATION="${HOME}/.agents/skills" ;;
    openclaw:managed) DESTINATION="${HOME}/.openclaw/skills" ;;
    hermes:user) DESTINATION="${HOME}/.hermes/skills" ;;
    *) return 1 ;;
  esac
}

default_scope_for() {
  DEFAULT_SCOPE=""
  case "$1" in
    codex) DEFAULT_SCOPE="user" ;;
    claude-code) DEFAULT_SCOPE="user" ;;
    openclaw) DEFAULT_SCOPE="personal" ;;
    hermes) DEFAULT_SCOPE="user" ;;
    *) return 1 ;;
  esac
}

install_one_target() {
  local target="$1"
  local requested_scope="$2"
  local scope="${requested_scope}"
  local destination
  local skill_name
  local source_dir
  local target_dir
  local installed_names=()
  local skipped_names=()

  if [ -z "${scope}" ]; then
    default_scope_for "${target}"
    scope="${DEFAULT_SCOPE}"
  fi

  if ! destination_for "${target}" "${scope}"; then
    echo "Unsupported target/scope: ${target}/${scope}" >&2
    return 2
  fi
  destination="${DESTINATION}"

  echo "Target: ${target} (${scope})"
  echo "Destination: ${destination}"

  if [ "${DRY_RUN}" -eq 0 ]; then
    mkdir -p "${destination}"
  fi

  for source_dir in "${SOURCE_SKILLS}"/*; do
    if [ ! -d "${source_dir}" ] || [ ! -f "${source_dir}/SKILL.md" ]; then
      continue
    fi
    skill_name="${source_dir##*/}"
    target_dir="${destination}/${skill_name}"

    if [ "${source_dir}" = "${target_dir}" ]; then
      echo "Already in place: ${skill_name}"
      installed_names+=("${skill_name}")
      continue
    fi

    if [ -e "${target_dir}" ] && [ "${FORCE}" -eq 0 ]; then
      echo "Skip existing skill without --force: ${skill_name}"
      skipped_names+=("${skill_name}")
      continue
    fi

    if [ "${DRY_RUN}" -eq 1 ]; then
      echo "Would install: ${skill_name}"
    else
      if [ -e "${target_dir}" ]; then
        rm -rf "${target_dir}"
      fi
      cp -R "${source_dir}" "${target_dir}"
      echo "Installed: ${skill_name}"
    fi
    installed_names+=("${skill_name}")
  done

  echo
  echo "Installed or available skills:"
  if [ "${#installed_names[@]}" -gt 0 ]; then
    for skill_name in "${installed_names[@]}"; do
      echo "  - ${skill_name}"
    done
  else
    echo "  (none installed in this run)"
  fi

  if [ "${#skipped_names[@]}" -gt 0 ]; then
    echo "Skipped existing skills:"
    for skill_name in "${skipped_names[@]}"; do
      echo "  - ${skill_name}"
    done
  fi

  echo
  echo "Usage examples:"
  echo "  Use the esg-board-brief skill to draft a board update with evidence status and risk flags."
  echo "  Use the esg-hkex-gap-check skill to prepare a Hong Kong listed issuer ESG gap check."
  echo "  Use the esg-data-request skill to create an ESG KPI data request tracker."
  echo
}

case "${TARGET}" in
  codex|claude-code|openclaw|hermes)
    install_one_target "${TARGET}" "${SCOPE}"
    ;;
  all)
    install_one_target "codex" "${SCOPE:-user}"
    install_one_target "claude-code" "${SCOPE:-user}"
    install_one_target "openclaw" "${SCOPE:-personal}"
    install_one_target "hermes" "${SCOPE:-user}"
    ;;
  *)
    echo "Unsupported target: ${TARGET}" >&2
    usage >&2
    exit 2
    ;;
esac
