# Phase 1: Developer Foundations

**Days 1–10 · Outcome:** work confidently from a Linux terminal, explain how a web request travels, collaborate through GitHub, and use an AI coding assistant without surrendering engineering judgment.

Create a `phase-1` branch in your capstone repository. Merge it only after the Day 10 milestone passes.

## Day 1: Your engineering workstation

**Learn:** Understand the roles of the operating system, shell, terminal, editor, runtime, package manager, and source-control client. Learn why teams pin tool versions and automate setup.

**Build:** Install or verify Git, Python, a Python environment/package tool, Node.js, Docker, and an editor. Create the capstone repository structure from the root README. Add a `.gitignore` and a README section containing setup commands and exact tool versions.

**Ship:** Commit a `docs/environment.md` inventory and a short learning contract: available study time, the document domain you chose, and your definition of success.

**Check:** A future teammate could identify every required tool without asking you.

**Resources:** [The Missing Semester: course overview](https://missing.csail.mit.edu/) · [VS Code setup](https://code.visualstudio.com/docs/setup/setup-overview) · [Git installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Day 2: Files, paths, and the shell

**Learn:** Absolute and relative paths, files versus directories, hidden files, globbing, quoting, environment variables, command history, manual pages, and exit codes. Learn what `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `touch`, `head`, `tail`, `less`, and `wc` actually do.

**Build:** Create a small document collection under `data/sample/`. Navigate, copy, rename, inspect, and count its files using only the shell. Write the useful commands and observations in `docs/shell-notes.md`—do not save unexplained command dumps.

**Ship:** Add a safe `scripts/inspect-data.sh` that uses `set -euo pipefail`, quotes variables, accepts a directory argument, and reports file counts and sizes without modifying input.

**Check:** Run it from a directory containing spaces and confirm that a nonexistent path returns a non-zero exit code.

**Resources:** [The Missing Semester: shell](https://missing.csail.mit.edu/2020/course-shell/) · [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html) · [ShellCheck](https://www.shellcheck.net/)

## Day 3: Streams, pipes, and text processing

**Learn:** Standard input, output, and error; redirection; pipelines; command substitution; and why Unix tools compose well. Practice `rg` (or `grep`), `find`, `sort`, `uniq`, `cut`, `tr`, `xargs`, `sed`, and basic `awk`.

**Build:** Given a sample access log, answer: Which paths are most common? Which status codes occur? Which requests are slowest? Build the answer as small pipelines, then explain each stage in `docs/log-analysis.md`.

**Ship:** Save a read-only `scripts/summarize-log.sh` with input validation and a useful help message.

**Check:** The script reads a path argument, sends errors to stderr, and can be used in another pipeline.

**Resources:** [The Missing Semester: shell tools](https://missing.csail.mit.edu/2020/shell-tools/) · [ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) · [Data Wrangling with the Command Line](https://missing.csail.mit.edu/2020/data-wrangling/)

## Day 4: Processes, permissions, and environments

**Learn:** Users and groups, read/write/execute bits, least privilege, foreground/background processes, signals, process IDs, services, logs, package managers, `PATH`, and environment variables. Understand why `chmod 777` and running everything as root are warning signs.

**Build:** Start a local Python HTTP server, inspect it with `ps`, `top` or `htop`, `lsof` or `ss`, and stop it gracefully. Create a non-secret environment variable and read it from a tiny Python program. Inspect permissions on the files it creates.

**Ship:** Add `docs/process-debugging.md` with a decision tree for “the service will not start” and “the port is already in use.”

**Check:** You can identify the process bound to a port and explain `SIGTERM` versus `SIGKILL`.

**Resources:** [Linux Journey: permissions](https://linuxjourney.com/lesson/file-permissions) · [The Missing Semester: command-line environment](https://missing.csail.mit.edu/2020/command-line/) · [systemd service concepts](https://systemd.io/)

## Day 5: Networking, HTTP, DNS, and SSH

**Learn:** IP addresses, ports, DNS, TCP, TLS, HTTP methods/status codes/headers, clients and servers, proxies, and SSH keys. Trace a request from a browser through DNS and TLS to an application and database.

**Build:** Use `curl -v`, `dig` or `nslookup`, `ping`, `traceroute`, and `ss` where available. Inspect request and response headers from a public API. Generate a dedicated practice SSH key, understand its public/private halves, and never print or commit the private key.

**Ship:** Draw `docs/request-path.md` showing browser → DNS → load balancer → API → database/model provider → response. Label trust boundaries, ports, and where TLS terminates.

**Check:** Explain the difference between `401`, `403`, `404`, `429`, and `500`, and why an HTTP timeout is mandatory.

**Resources:** [MDN: how the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) · [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) · [GitHub: SSH authentication](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

## Day 6: Git as a history graph

**Learn:** Repositories, commits, trees, the staging area, branches as pointers, `HEAD`, remotes, and the working tree. Prefer understanding Git's data model over memorizing rescue commands.

**Build:** Make three focused capstone changes. Inspect each with `git status`, `git diff`, `git diff --staged`, `git log --graph`, and `git show`. Amend an unpushed commit and restore one intentionally edited file after inspecting the diff.

**Ship:** A readable history using imperative, specific messages such as `docs: explain local setup`.

**Check:** For any line, use `git blame` and `git show` to explain when and why it changed.

**Resources:** [Pro Git: Git basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) · [Learn Git Branching](https://learngitbranching.js.org/) · [The Missing Semester: version control](https://missing.csail.mit.edu/2020/version-control/)

## Day 7: Branches, conflicts, and recovery

**Learn:** Feature branches, merge versus rebase, fast-forward merges, conflicts, tags, detached `HEAD`, reflog, and the difference between reverting public history and rewriting private history.

**Build:** Create two branches that edit the same lines, cause a conflict, resolve it, and verify the result. Make a disposable commit, remove it from the branch, and recover it with `git reflog`. Tag the end of the exercise.

**Ship:** Add `docs/git-recovery.md` covering uncommitted edits, a bad local commit, a bad public commit, and a deleted branch.

**Check:** You can state when `rebase`, `revert`, and `reset` are appropriate without copying a command blindly.

**Resources:** [Pro Git: branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) · [GitHub: resolving conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts) · [Git reference](https://git-scm.com/docs)

## Day 8: GitHub pull requests and review

**Learn:** Issues, branches, pull requests, draft PRs, review comments, approvals, branch protection, status checks, and why reviews discuss risk and intent rather than formatting alone.

**Build:** Open an issue with acceptance criteria, implement it on a branch, and open a PR. Write a description with context, change summary, verification evidence, risks, and screenshots or command output when useful. Review your own diff before requesting review.

**Ship:** Merge through the PR rather than pushing directly to `main`. Add a PR template to the capstone.

**Check:** The issue describes the problem; the PR describes the solution; the commit history remains understandable.

**Resources:** [GitHub Skills: introduction](https://github.com/skills/introduction-to-github) · [GitHub pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) · [Google engineering practices: code review](https://google.github.io/eng-practices/review/)

## Day 9: AI-assisted development with judgment

**Learn:** A coding agent works best with a clear outcome, relevant repository context, constraints, acceptance checks, and permission boundaries. It can still invent APIs, miss requirements, introduce vulnerabilities, or produce code you cannot maintain.

**Build:** Install or open one assistant such as Codex or Claude Code. Give it a bounded documentation or test task using the prompt in the [AI-assisted development guide](../guides/ai-assisted-development.md). Ask for a plan first. Inspect every changed line, run the checks yourself, and record one useful suggestion and one thing you rejected.

**Ship:** Commit the verified change and `docs/ai-assistant-log.md`; do not commit transcripts containing secrets or private data.

**Check:** You can explain the resulting code without the assistant and can identify exactly which evidence made you trust it.

**Resources:** [Official Codex quickstart](https://learn.chatgpt.com/codex/quickstart) · [Official Codex prompting guide](https://learn.chatgpt.com/codex/prompting) · [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)

## Day 10: Milestone build Dev Doctor

**Build:** Create `dev-doctor`, a small Bash CLI that reports whether the capstone prerequisites are available, prints versions, checks whether required ports are free, and returns a non-zero exit code when a required dependency is missing. It must not install software or change the machine.

**Required quality:** Use functions, quote variables, show `--help`, support at least Linux, avoid leaking environment values, and lint with ShellCheck. Add automated tests using Bats or a simpler test harness that safely changes `PATH` to simulate a missing dependency.

**Ship:** Open and merge a milestone PR containing usage docs, test evidence, and a short retrospective. Tag it `day-10`.

**Demo:** From a fresh shell, run one command that produces a clear pass/fail report. Explain how you would debug a failed tool check and a busy port.

**Resources:** [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) · [ShellCheck wiki](https://www.shellcheck.net/wiki/) · [Bats Core](https://bats-core.readthedocs.io/)

## Phase 1 exit ticket

Without notes, explain: a process, a port, an environment variable, file permissions, an HTTP request, a Git branch, a pull request, and how you verify AI-generated code. If any answer is vague, revisit that day's shipped artifact before continuing.
