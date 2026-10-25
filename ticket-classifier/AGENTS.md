# Agent Instructions

## Project layout
- `../README.md` describes the overall 60-day learning path.
- `README.md` describes the Ticket Classifier project.
- `scripts/system-report.sh` reports system information.
- `notes/` contains daily learning notes and evidence.
- `../scripts/validate_curriculum.py` validates curriculum structure and Markdown links; run it from the repository root.

## Safe commands
- Inspect relevant files with `sed`, `rg`, and `find`.
- Review changes from the repository root with `git status --short` and `git diff`.
- Run `python3 scripts/validate_curriculum.py` from the repository root to validate curriculum changes.
- Run `bash -n ticket-classifier/scripts/system-report.sh` from the repository root to check shell syntax.
- Run `bash scripts/system-report.sh` from `ticket-classifier/` when the system report is relevant.
- Never print or expose `.env`, credentials, private keys, or other secrets.

## Conventions
- Keep changes small, beginner-friendly, and limited to the requested task.
- Preserve the existing project structure and learning sequence.
- Use synthetic data and placeholders, never real customer data or credentials.
- Inspect relevant files before editing; avoid unrelated reads and changes.
- Do not install dependencies or modify unrelated files unless explicitly needed and approved.

## Definition of done
- Changes are limited to the intended files.
- Relevant verification commands have been run and their results reported.
- Review `git status --short` and the diff for unintended changes.
- Clearly report remaining errors or unverified behavior.
