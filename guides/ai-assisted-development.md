# Simple Guide to AI-Assisted Coding

Use Codex, Claude Code, or a similar tool after you can perform the basic command yourself. The assistant may suggest a change; you still own the decision and verification.

## Give five pieces of context

For most small tasks, provide only:

1. **Outcome:** what should work when finished.
2. **Relevant path:** the file or small directory to inspect.
3. **Current evidence:** an error message, failing command, or current behavior.
4. **Constraints:** what must not change, including security limits.
5. **Check:** the exact command or behavior that proves success.

Example:

```text
Add a --help message to scripts/system-report.sh.
Inspect that file first and propose a short plan.
Do not install dependencies or change other files.
Keep the script read-only and compatible with Bash.
Done means `bash scripts/system-report.sh --help` exits 0 and normal output still works.
```

## Keep context useful

- Start with the task and relevant paths; do not paste the entire repository.
- Give the exact error, but remove secrets and private data.
- Use `rg`, `find`, a small tree, or file references to help locate code.
- Put stable project facts and commands in a short `AGENTS.md`.
- Keep temporary task details in the prompt, not in permanent instructions.
- Start a separate task when the goal changes substantially.
- Ask the assistant to inspect and plan before a broad edit.

This follows the current [official Codex prompting guidance](https://learn.chatgpt.com/codex/prompting): state the desired outcome and add useful context such as relevant files, components, errors, and constraints. See the official [`AGENTS.md` guide](https://learn.chatgpt.com/codex/agent-configuration/agents-md) for repository instructions.

## Review every result

After an edit:

```bash
git status
git diff
```

Then ask:

- Did it change only the intended files?
- Can I explain every changed line?
- Did it invent a command, file, or library?
- Did it expose a secret or weaken permissions?
- Does the original error disappear for the expected reason?
- Do the relevant tests and manual checks pass?

Never accept “it should work” as proof. Run the command yourself.

## Useful roles for an assistant

- explain one error message after you have read it;
- locate relevant code in an unfamiliar repository;
- propose a short plan for a bounded issue;
- suggest tests and edge cases;
- review a small diff for mistakes;
- improve documentation after the code works.

Avoid asking it to design the entire system, run destructive commands, handle secrets, or make a large unexplained rewrite.

## Official starting points

- Codex: [quickstart](https://learn.chatgpt.com/codex/quickstart), [prompting](https://learn.chatgpt.com/codex/prompting), and [`AGENTS.md`](https://learn.chatgpt.com/codex/agent-configuration/agents-md)
- Claude Code: [overview](https://docs.anthropic.com/en/docs/claude-code/overview) and [common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)

