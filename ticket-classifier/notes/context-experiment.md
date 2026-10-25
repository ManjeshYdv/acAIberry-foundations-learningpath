# Context Experiment: Vague vs. Focused Coding-Agent Prompts

## Objective

Compare a vague coding-agent prompt with a focused prompt to understand how task context affects file inspection, change scope, and verification.

## Test A: Vague prompt

### Prompt used

> Improve the documentation in this project so it is clearer and easier for beginners to understand. Inspect the repository and make the improvements you think are needed. Verify your work afterward.

### Observed evidence

Codex inspected multiple project files and directories, including the project README, daily notes for Days 21–23, `.gitignore`, the curriculum, the student guide, and the system-report script. It also viewed screenshots.

The final output reported these four documentation files changed:

- `ticket-classifier/README.md`
- `ticket-classifier/notes/day-21.md`
- `ticket-classifier/notes/day-22.md`
- `ticket-classifier/notes/day-23.md`

The changes included README revisions, corrections to daily notes, and changes to screenshot descriptions.

### Verification

- `python3 scripts/validate_curriculum.py` — passed; validated 60 formatted days, tracker items, and local links across 23 Markdown files.
- `git diff --check` — passed with no output.
- The agent reported that the Day 23 note still needed dedicated evidence for the ignore-rule check.

### Interpretation

The prompt did not specify a target file, a limited change, or an exact completion condition. Codex therefore made broader documentation changes instead of limiting its work to one small improvement.

The output demonstrates broader-than-needed changes. It does not establish the exact number of unnecessary file reads because the tool output does not provide a complete, independently verified read count.

### Safety deviation

This run was performed in the main working tree rather than a disposable worktree. The resulting changes must be preserved and reviewed; they must not be discarded simply to reset the experiment.

## Test B: Focused prompt

**Status:** Not yet completed.

The planned prompt specifies:
- Outcome: clarify the system-report documentation.
- Target: `ticket-classifier/README.md`, especially line 81.
- Constraints: change only the relevant sentence; do not modify the script or other files.
- Verification: show the diff and run `git diff --check`.
- Reporting: identify inspected files, changed files, and verification results.

After running this test in a separate, clean worktree, record the actual observations below.

### Observed evidence

- Files inspected:
- Files changed:
- Unrelated changes:
- Verification commands and results:

## Comparison

| Measurement | Test A: Vague | Test B: Focused |
|---|---|---|
| Files inspected | Multiple files across the project | To be recorded |
| Files changed | README and three daily notes | To be recorded |
| Scope | Broader than the intended small task | To be recorded |
| Verification | Validator and whitespace check passed | To be recorded |
| Unrelated changes | Several edits outside the intended one-sentence task | To be recorded |

## Lessons learned

A useful coding-agent request should specify the desired outcome, relevant path, current evidence or error, constraints, and verification command.

A short `AGENTS.md` can provide stable project conventions and safety rules. The task prompt should provide the specific change and the files relevant to that task.

The experiment is incomplete until Test B is run and its results are compared with Test A. No claim about improvement from the focused prompt should be made before collecting that evidence.

## Experimental limitations

- Test A ran in the main working tree, not an isolated worktree. Its changes were preserved and reviewed rather than discarded.
- The Codex activity log shows several inspected files, but it does not provide a complete, independently verified count of all file reads.
- Test B changed only the README according to the reported Git status. However, the first proposed sentence omitted details from the original requirement, so a narrow diff alone did not guarantee semantic correctness.
- The final corrected sentence must be checked against the original requirements before the experiment is considered complete.

## Final verification evidence

Record the actual results after correcting the sentence:

- `git diff --check`: [paste the actual result]
- `python3 scripts/validate_curriculum.py`: [paste the actual result]
- `git status --short`: [list the remaining changed and untracked files]
- Diff reviewed manually: [yes/no]
- Original meaning preserved: [yes/no, with a brief explanation]

## Final conclusion

The experiment provides evidence that a focused prompt can constrain the observed change scope. The vague prompt led to changes across four existing documentation files, whereas the focused prompt led to a one-file change.

However, limiting the number of changed files does not automatically guarantee correctness. The focused edit initially omitted required details, demonstrating why semantic review and verification are necessary alongside scope constraints.

Because Test A was not isolated and the exact number of file reads is unknown, these results are an observational comparison rather than a fully controlled experiment.