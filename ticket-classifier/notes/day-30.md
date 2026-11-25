# Day 30: Checkpoint - complete an assisted pull request

**Date: <fill in>**
**Time spent: <start> to <end>**

## Commands I practiced

```text
git checkout -b <branch-name>
git status
git diff
shellcheck system-report.sh   # <ran / not installed; check skipped>
./system-report.sh            # success case
./system-report.sh <bad-arg>  # error case; echo $?
git add system-report.sh
git commit -m "<message>"
git push -u origin <branch-name>
gh pr create                  # or opened via the GitHub web UI
```

## Task result

I used an assistant inside the same flow a human would follow:
issue -> branch -> plan -> edit -> verify -> review -> PR.


### What did I do today?

Tool: <assistant codex 5.6>

Context provided: <files, issue text, constraints, what I told it to leave alone>

Prompt: <Read system-report.sh. I want to implement issue #2: add a --help flag and reject unknown flags. Do not edit any files yet. Give me a short plan: what lines change, what you will add, and what you will not touch.>


## Proof

Commit, file, screenshot, command output, or URL:

* Issue: <link>
* PR: <link>
* Script: [system-report.sh](../scripts/system-report.sh)

## Next prompt

<what I would change next time: verify filenames first, fill every placeholder, state allowed/forbidden actions>

## Can I explain it without AI?

* [*] Yes
