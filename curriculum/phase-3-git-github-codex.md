# Phase 3: Git, GitHub, and Coding Assistants

**Days 21–30 · Result:** you can save understandable history, collaborate through a pull request, and use Codex or another coding assistant on a small task without flooding it with irrelevant context.

Git now starts tracking the exact project you used for Linux and troubleshooting practice.

## Day 21: Start tracking with Git

**Goal:** Understand the working tree, repository, and Git status.

**Commands:** `git init`, `git rev-parse --show-toplevel`, `git status`, `git diff`.

**Task:** From the course-repository root, use `git rev-parse --show-toplevel` to confirm that the fork/clone is already a repository. Do **not** run `git init` inside `ticket-classifier`; that would create an unwanted nested repository. Change one note, inspect the unstaged diff, and run `git status`.

**Done when:** You can identify untracked and modified files and explain that Git has not saved either one yet.

**Resource:** [Pro Git: getting a repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Day 22: Make useful commits

**Goal:** Save one logical change with a message that explains it.

**Commands:** `git add`, `git diff --staged`, `git commit`, `git log --oneline`, `git show`.

**Task:** Make one small improvement to the system-report script and one separate documentation correction. Stage, inspect, and commit each logical change separately.

**Done when:** `git log --oneline` shows two focused commits and `git show` explains each without unrelated changes.

**Resource:** [Pro Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

## Day 23: Ignore secrets and generated files

**Goal:** Know what belongs in Git and what must stay local.

**Commands:** `nano .gitignore`, `git check-ignore -v`, `git status`.

**Task:** Inspect the supplied root and `ticket-classifier/.gitignore` files. Confirm that `.env`, private keys, Python cache, virtual environments, logs, and trained model artifacts are ignored while `.env.example` and synthetic data can be tracked. Add any missing safe rule and test it with `git check-ignore -v`.

**Done when:** `git status` contains no log, secret, private key, cache, or virtual-environment file.

**Resource:** [GitHub: ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)

## Day 24: Work on a branch

**Goal:** Isolate a small change before merging it.

**Commands:** `git switch -c`, `git branch`, `git diff main...HEAD`, `git switch`, `git merge`.

**Task:** From your current `phase-3` branch, create `practice-readme`, add a short troubleshooting section, review the branch diff, switch back to `phase-3`, and merge it. Keep `main` unchanged until the Day 30 checkpoint review.

**Done when:** The change is on `main`, the branch history is understandable, and the working tree is clean.

**Resource:** [Pro Git: branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

## Day 25: Resolve a conflict and undo safely

**Goal:** Treat conflicts and mistakes as inspectable states, not emergencies.

**Commands:** `git status`, `git diff`, `git restore`, `git revert`, `git reflog`.

**Task:** On two practice branches, edit the same line and merge to create a conflict. Read the markers, keep the intended result, stage it, and finish the merge. Restore one uncommitted practice edit and use `git revert` on a harmless practice commit.

**Done when:** `notes/git-recovery.md` explains conflict resolution, restoring an uncommitted file, and reverting a shared commit.

**Resource:** [GitHub: resolving merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts)

## Day 26: Connect Git to GitHub

**Goal:** Understand local versus remote repositories.

**Commands:** `git remote -v`, `git push -u origin main`, `git fetch`, `git pull --ff-only`, `git clone`.

**Task:** Inspect the `origin` and `upstream` configured during onboarding. Fetch both, push the current phase branch, and clone your fork into a separate temporary directory to prove the remote contains your work. Self-study students who want tracking can switch to the fork workflow now.

**Done when:** The GitHub page shows the commits and the fresh clone contains the same files without copied secrets.

**Resource:** [GitHub: adding locally hosted code](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

## Day 27: Use issues and pull requests

**Goal:** Connect a problem, proposed change, review, and merge.

**Commands:** Git commands from Days 21–26; GitHub web or `gh` is optional.

**Task:** Open an issue to improve the system-report output. Create a branch, make the smallest change, push it, and open a pull request that says what changed and how you checked it. Review the diff before merging.

**Done when:** The issue links to a merged pull request and the PR contains a command/output proving the change works.

**Resource:** [GitHub Skills: introduction](https://github.com/skills/introduction-to-github)

## Day 28: Give a coding assistant a small task

**Goal:** Ask for one bounded outcome instead of “improve my project.”

**Commands/tools:** Codex, Claude Code, or another assistant; `git status`, `git diff`.

**Task:** Ask the assistant to add a `--help` message to `system-report.sh`. Provide the desired behavior, relevant file, constraints, and the exact command that should pass. Ask it to inspect and propose a plan before editing.

**Done when:** You understand every changed line, reject unrelated changes, run the script yourself, and record what the assistant got right or wrong.

**Resources:** [Official Codex quickstart](https://learn.chatgpt.com/codex/quickstart) · [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)

## Day 29: Keep Codex context small and useful

**Goal:** Supply relevant context deliberately so the assistant spends attention on the task.

**Commands/tools:** `tree` or `find`, `rg`, `git diff`, a short `AGENTS.md`.

**Task:** Write an `AGENTS.md` with only the project layout, safe commands, conventions, and definition of done. Give Codex the outcome, relevant path or file, current error, constraints, and verification command. Compare this result with a vague prompt on a harmless task.

**Done when:** The focused request causes fewer irrelevant file reads or changes, and `notes/context-experiment.md` explains which context helped. Do not paste the whole repository when paths and search results are enough.

**Resources:** [Official Codex prompting](https://learn.chatgpt.com/codex/prompting) · [Official Codex `AGENTS.md` guide](https://learn.chatgpt.com/codex/agent-configuration/agents-md)

## Day 30: Checkpoint complete an assisted pull request

**Goal:** Use an assistant inside the same issue → branch → plan → edit → verify → review → PR flow used by a human.

**Task:** Open an issue for one small improvement to `system-report.sh`. Ask the assistant for a plan, allow only the needed edit, inspect the diff, run ShellCheck if available, test one success and one error case, and open a pull request.

**Done when:** The merged PR links the issue, states what context was provided, shows test evidence, and contains no unexplained code.

**Resource:** [AI-assisted development guide](../guides/ai-assisted-development.md)

### Phase checkpoint

From a clean working tree, make a branch and small change, inspect it, commit it, push it, and explain the pull request. Then show exactly what context an AI assistant would need for that change—and what it does not need.
