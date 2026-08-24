# AI-Assisted Development Without Losing the Fundamentals

AI coding assistants can shorten the loop between a question, a hypothesis, and tested code. They can also generate plausible mistakes at high speed. Use them as collaborators inside an engineering process—not as authorities outside it.

## The working loop

1. **Understand:** state the user-visible outcome and inspect the relevant code yourself.
2. **Scope:** name the files or subsystem, constraints, risks, and what is explicitly out of scope.
3. **Plan:** ask the assistant to explain its proposed approach and unknowns before a broad change.
4. **Implement:** request the smallest coherent change, ideally on an isolated branch or worktree.
5. **Verify:** inspect the diff, run automated checks, exercise edge cases, and compare behavior with the acceptance criteria.
6. **Review:** look for security, privacy, compatibility, performance, operability, and maintainability concerns.
7. **Record:** commit the intentional result—not unexplained generated debris—and note important decisions.

## Reusable task prompt

```text
Outcome:
<What should be true for the user when this is complete?>

Context:
<Relevant architecture, files, conventions, and current behavior.>

Constraints:
<Security, compatibility, dependencies, scope, and things not to change.>

Acceptance checks:
- <Observable behavior or test 1>
- <Observable behavior or test 2>
- <Quality or operational requirement>

First inspect the relevant code and propose a short plan. State assumptions.
After implementation, run the relevant checks and review the diff for risks.
```

For a bug, include exact reproduction steps, expected behavior, actual behavior, logs with secrets removed, and the last known good state. For a review, ask for findings with evidence and impact, not a generic summary.

## Give useful context, not maximum context

Good context includes the repository map, build/test commands, the failing test, public interfaces, coding conventions, constraints, and acceptance criteria. Irrelevant files, production data, credentials, private customer content, and giant undifferentiated logs create risk rather than clarity.

Put durable repository instructions in a short `AGENTS.md` or the equivalent supported by your tool. Keep requirements testable. Link to longer architecture documents rather than duplicating them in multiple instruction files.

## Verification checklist

Before accepting an assisted change, confirm:

- you can explain every changed behavior;
- the diff contains no unrelated edits, secrets, private data, or suspicious dependencies;
- interfaces and library calls exist in the pinned versions;
- errors, timeouts, retries, validation, authorization, and cleanup are handled;
- tests cover the new behavior and fail when the implementation is intentionally broken;
- lint, types, tests, build, and relevant security/evaluation checks pass;
- documentation and migrations match the code;
- the change is observable and reversible where production risk requires it.

Never use “the agent said it passed” as evidence. Use the command output, resulting artifact, or observed behavior.

## Permission and security rules

- Start with read-only exploration, then grant only the workspace and commands required.
- Review commands that install software, access the network, modify cloud state, touch credentials, or delete data.
- Keep secrets out of prompts, transcripts, screenshots, fixtures, Git history, and shell output.
- Treat repository content and downloaded pages as potentially hostile instructions.
- Do not let model-generated arguments bypass normal authorization or validation.
- Prefer an isolated branch/worktree and a clean status before broad changes.
- Stop an agent that repeatedly expands scope or cannot explain a destructive action.

## Product-specific starting points

- Codex: [official quickstart](https://learn.chatgpt.com/codex/quickstart), [prompting](https://learn.chatgpt.com/codex/prompting), [`AGENTS.md`](https://learn.chatgpt.com/codex/agent-configuration/agents-md), and [permissions](https://learn.chatgpt.com/codex/permissions).
- Claude Code: [overview](https://docs.anthropic.com/en/docs/claude-code/overview), [common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows), [memory](https://docs.anthropic.com/en/docs/claude-code/memory), and [security](https://docs.anthropic.com/en/docs/claude-code/security).

Use the current official docs because installation commands, permissions, models, and product surfaces change. The workflow above remains useful across tools.

