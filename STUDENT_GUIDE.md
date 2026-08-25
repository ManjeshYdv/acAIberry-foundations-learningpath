# Student Guide

This repository contains the lessons. Your practical work belongs in the included [`ticket-classifier/`](ticket-classifier/) directory. Its README shows exactly what you build, which files should exist at each checkpoint, and which commands must work.

Choose one setup mode before starting.

## Mode A: Clone for self-study

Use this when you only want to learn locally and do not need an instructor to review your progress.

```bash
git clone https://github.com/AtuLxCE/acAIberry-foundations-learningpath.git
cd acAIberry-foundations-learningpath
ls
cd ticket-classifier
```

You may commit locally, but you cannot push to the instructor's repository. If you later want remote tracking, create your own GitHub repository or start again with Mode B.

## Mode B: Fork for tracked learning

Use this when an instructor will review your work. A **fork** is your copy on GitHub. A **clone** is the copy of your fork on your computer.

### 1. Fork the course

Open <https://github.com/AtuLxCE/acAIberry-foundations-learningpath>, select **Fork**, keep only the `main` branch, and create the fork under your GitHub account.

Your fork should be:

```text
https://github.com/YOUR_USERNAME/acAIberry-foundations-learningpath
```

### 2. Clone your fork

HTTPS works without SSH setup:

```bash
git clone https://github.com/YOUR_USERNAME/acAIberry-foundations-learningpath.git
cd acAIberry-foundations-learningpath
```

If your GitHub SSH key already works, you may use:

```bash
git clone git@github.com:YOUR_USERNAME/acAIberry-foundations-learningpath.git
cd acAIberry-foundations-learningpath
```

Replace `YOUR_USERNAME` with your GitHub username. Do not type angle brackets around it.

### 3. Add the course repository as upstream

Your fork is `origin`; the instructor's course is `upstream`.

```bash
git remote add upstream https://github.com/AtuLxCE/acAIberry-foundations-learningpath.git
git remote -v
```

Expected shape:

```text
origin    https://github.com/YOUR_USERNAME/acAIberry-foundations-learningpath.git
upstream  https://github.com/AtuLxCE/acAIberry-foundations-learningpath.git
```

Do not sync curriculum changes during a phase unless your instructor asks. Finish and merge the current checkpoint first to avoid tracker conflicts.

### 4. Create the first phase branch

```bash
git switch -c phase-1
git push -u origin phase-1
```

The commands below are a workflow recipe. Days 21–30 explain what Git is doing in detail.

## Start Day 1

The `ticket-classifier/` directory already exists so its location is obvious. Create the working directories inside it:

```bash
mkdir -p ticket-classifier/{notes,scripts,data,logs}
cd ticket-classifier
pwd
ls -la
```

Return to the repository root before updating the tracker or using Git:

```bash
cd ..
```

## Daily workflow

### 1. Read only today's lesson

Open [CURRICULUM.md](CURRICULUM.md), select the next unchecked day, and follow its link. Use the [`ticket-classifier` workspace guide](ticket-classifier/README.md) to see how today's task fits into the final application.

### 2. Create a daily log

For Day 1:

```bash
cp templates/daily-log.md ticket-classifier/notes/day-01.md
nano ticket-classifier/notes/day-01.md
```

Use `day-02.md`, `day-03.md`, and so on for later days. Record commands, results, one error, and the fix. Never paste secrets or private keys.

### 3. Update the progress tracker

```bash
nano CURRICULUM.md
```

Change only the completed item. Example:

```text
- [x] Day 1 ... — proof: ticket-classifier/notes/day-01.md
```

Do not mark a task complete until its **Done when** statement is true.

### 4. Validate and review

```bash
python3 scripts/validate_curriculum.py
git status --short
git diff
```

Check that `.env`, logs, credentials, private SSH keys, virtual environments, and model artifacts are not listed for commit.

### 5. Commit and push

Stage the tracker and student-work directory explicitly:

```bash
git add CURRICULUM.md ticket-classifier
git diff --staged
git commit -m "day-01: inspect Linux workstation"
git push
```

Change the day number and message each day. Push at the end of the session so the instructor can see the latest commit.

If Git says there is nothing to commit, check `git status` and confirm that you saved the files in this repository.

## Checkpoint workflow every 10 days

At Days 10, 20, 30, 40, 50, and 60:

1. Run the phase checkpoint and repository validator.
2. Push the phase branch.
3. Open a pull request **inside your fork**.
4. Set the base repository to your fork, base branch to `main`, and compare branch to `phase-N`.
5. Fill in the checkpoint PR template and share its URL with the instructor.

Do not open personal-coursework pull requests against `AtuLxCE/acAIberry-foundations-learningpath`; that repository contains the shared curriculum.

After the instructor approves and you merge the PR:

```bash
git switch main
git pull --ff-only origin main
git switch -c phase-2
git push -u origin phase-2
```

Use `phase-3`, `phase-4`, and so on after later checkpoints.

Finally, submit the checkpoint through the **Phase checkpoint submission** issue form in the instructor repository. Include the URL of the PR in your fork.

## If the instructor publishes a correction

Sync only from a clean `main` after your current phase PR is merged:

```bash
git switch main
git status
git fetch upstream
git merge upstream/main
git push origin main
```

If Git reports a conflict, stop and ask the instructor before discarding anything. Never use a destructive reset command just to make the message disappear.

## What the instructor reviews

- completed tracker items with proof paths;
- daily logs and focused commits;
- the phase checkpoint artifact;
- a passing content validator;
- absence of secrets and private data;
- your ability to explain and demonstrate the commands.

The instructor is tracking understanding, not how many lines you wrote or how quickly you finished.

## Help checklist

Before asking for help, send:

```text
Day:
Goal:
Command run:
Exact error:
Expected result:
What I already checked:
```

Remove secrets and private data. An exact error is more useful than “it does not work.”

## References

- [GitHub: fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
- [GitHub: syncing a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)
- [GitHub: about pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
