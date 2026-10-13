# Day 28: Give a coding assistant a small task

**Tue Oct 13**

**Time spent: Not recorded**

## Commands I practiced

```text
git status
git diff
./system-report.sh --help; echo $?
./system-report.sh -h | head -1
./system-report.sh
shellcheck system-report.sh (not installed; check skipped)
```

## Task result

I asked Codex to add a help message to the system-report script, inspect the file,
and propose a plan before editing. I reviewed the plan and approved the change.

### What did I do today?

Tool: Codex (GPT-6.1-Sol)

Prompt: I named `system-report.sh`, but the real file was `system-report` (no
extension). I also left the "[list what your script supports]" placeholder
unfilled. Both were my mistakes.

Plan stage: RIGHT - didn't guess; found the real file, asked me to confirm,
and did not edit until I approved. Plan matched the final diff.

Diff: +10 lines, a case block after the shebang. Existing code untouched.
Help goes to stdout, exit 0. Rename and `chmod +x` came from my follow-up
request, not scope creep by Codex.

Right: minimal change, matched style, no extra flags, no refactoring.

Wrong / unverified: ShellCheck not installed, so that check was skipped.
Its ShellCheck risk prediction is unverified. Verified no-arg output only
with faked values, so I re-ran it myself.

Observed: `-help` (single dash) and `--bogus` fall through to the full report.
Not requested, so correctly not handled, but worth knowing.

Acceptance:

* [ ] `--help` exit 0
* [ ] `-h` first line
* [ ] No-arg identical
* [ ] ShellCheck

Next prompt: verify the filename exists first, fill in every placeholder,
and say explicitly whether renaming/chmod is allowed.

## Proof

Commit, file, screenshot, command output, or URL:

* Script: [system-report.sh](../scripts/system-report.sh)
* Commit: `5282fac` - Add --help option to system-report script
* Acceptance commands are listed above; ShellCheck was unavailable.

## Can I explain it without AI?

* [ ] Yes
* [ ] Not yet; repeat this day
