# Day 29: Keep Codex context small and useful

**Thu Oct 25**

**Time spent: 02:30 PM to 3:0 PM**

## Commands I practiced

Recorded in the experiment, rather than re-created terminal output:

```text
git diff --check
python3 scripts/validate_curriculum.py
```

The experiment reports that both prompt runs passed `git diff --check`.
Test A also reports a successful curriculum validation. The focused request
asked for a diff, and the corrected focused run in this session displayed it.
These records do not establish every command used during the original runs.

While preparing this note, the agent used `rtk` as required by the workspace
instructions. From the course repository root, it ran:


## Task result

Objective: give a coding agent useful context deliberately, then compare a
vague request with a focused request on a small documentation change.

The Day 29 curriculum asks for a short `AGENTS.md` covering project layout,
safe commands, conventions, and definition of done. The existing project file
contains those sections. I used it as context; its original creation history
is not verified here, and it was not changed while preparing this note.

`AGENTS.md` supplies reusable project rules. The individual prompt supplies
the outcome, relevant path, current evidence or error, constraints, and exact
verification. For this task there was no recorded runtime error: the evidence
was the sentence explaining the system report. I did not need to paste the
whole repository or share secrets to explain that task.

### What did I do today?

Tool: Codex. The model used for the original experiment is not verified here.

Test A prompt:

> Improve the documentation in this project so it is clearer and easier for beginners to understand. Inspect the repository and make the improvements you think are needed. Verify your work afterward.

Test B context: clarify only the system-report sentence in
`ticket-classifier/README.md`, especially line 81, while preserving its meaning.
Read the relevant section and project instructions; change no script or other
file; show the diff, run `git diff --check`, and report inspected and changed
files. Dependencies and secret contents were outside the task.

| Evidence | Test A: vague | Test B: focused |
| --- | --- | --- |
| Reported changes | README and daily notes for Days 21, 22, and 23 | README only |
| Inspection | Multiple files, directories, and screenshots | Relevant README section and instructions were reported in the corrected run |
| Whitespace check | `git diff --check` reported passed | `git diff --check` reported passed |
| Meaning review | Broad revisions required review | First focused edit omitted details that needed to be preserved |

Right: naming the target, one-sentence scope, constraints, and verification
made the focused change easier to review. The observed change scope narrowed
from four existing documentation files to one.

Wrong / limitations: the first focused edit omitted required details. A narrow
diff and a passing whitespace check do not prove that the meaning is correct.
The corrected sentence in the current README retains the user, host/computer
name, date, disk, memory, project size, processes using the most memory, and
the promise not to change the machine.

Test A ran in the main working tree, not an isolated worktree. Its changes
must be preserved and reviewed rather than discarded to reset the experiment.
The available logs do not establish a complete file-read count, so I cannot
claim an exact reduction in reads. This is an observational comparison, not a
fully controlled experiment; Test B's isolation is unverified.

The experiment note has stale Test B placeholders saying it is not completed,
alongside later limitations and conclusions describing its result. This note
uses those later observations and the corrected focused run in this session.
The placeholders were not filled or changed by this documentation task.

A current command-documentation lookup was attempted with
`rtk proxy npx --no ctx7@latest library Git` and a detailed query. It exited 1
because the requested CLI package was not cached and installation was disabled.
No dependencies were installed; current external documentation was not fetched.

What I learned: useful context reduces ambiguity about what may change.
Paths and targeted search results can be enough. I still need to inspect the
diff for omitted requirements and distinguish a reported result from a check
I actually ran.

Practical steps for the next task:

1. Locate the relevant file with a limited directory listing or search.
2. Read the project instructions and the section needed for the change.
3. State the outcome, path, evidence, constraints, and verification command.
4. Review the changed files and every accepted line against the original meaning.
5. Record actual check results and limitations; use a separate clean worktree
   for a future comparison. That isolation step was not performed here.

Acceptance:

* [x] Identify the Day 29 objective and relevant project instructions.
* [x] Compare vague and focused prompts using the recorded evidence.
* [x] Explain which context helped narrow the reported changes.
* [x] Record the omitted-details problem and the limits of file-read evidence.
* [x] Distinguish executed commands from recommendations.
* [ ] Resolve stale Test B placeholders in the experiment note (outside this request).
* [ ] Verify an isolated comparison and a complete file-read count.

## Proof

Commit, file, screenshot, command output, or URL:

* Task: [Day 29 curriculum](../../curriculum/phase-3-git-github-codex.md#day-29-keep-codex-context-small-and-useful).
* Evidence: [context experiment](context-experiment.md).
* Project rules: [AGENTS.md](../AGENTS.md).
* Previous format: [Day 28](day-28.md).
* Corrected sentence: [project README](../README.md).
* Test A's recorded validator result: 60 formatted days, tracker items, and
  local links across 23 Markdown files. This is historical evidence, not the
  count from today's validation.

## Can I explain it without AI?

* [ ] Yes
* [ ] Not yet; repeat this day
