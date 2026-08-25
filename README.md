# acAIberry Foundations Learning Path

> A simple 60-day path to become comfortable building, deploying, and debugging a small AI/ML service.

This path focuses on the tools an AI/ML engineer uses every day: Linux commands, files, logs, errors, processes, networking, SSH, Git and GitHub, Python with `uv`, basic machine learning, Docker, GitHub Actions, and an Azure virtual machine.

It intentionally avoids advanced RAG, agents, Kubernetes, distributed systems, and complicated frontend work. Learn those after these foundations feel normal.

## What you will build

You will build one connected project: **Ticket Classifier**.

It starts as a folder of sample support tickets. You will inspect the files with Linux commands, track them with Git, train a small scikit-learn text classifier, expose it through FastAPI, run it with PM2, package it with Docker, and deploy it to an Azure VM. The same application supplies the logs, errors, processes, ports, containers, and deployment problems used throughout the course.

No paid model API is required.

## How to follow the path

Plan for **60–90 focused minutes per day**.

Each day has only four parts:

- **Goal:** the one idea to understand.
- **Commands:** the small command set to practice.
- **Task:** one change or investigation connected to Ticket Classifier.
- **Done when:** clear evidence that the task worked.

Use [CURRICULUM.md](CURRICULUM.md) as your progress tracker. Check one box only after completing the task and saving its proof in a commit or [daily log](templates/daily-log.md).

If a day is difficult, repeat it. Do not skip the command-line exercises by asking an AI tool to do them for you.

## The six phases

| Phase | Days | Focus | Checkpoint |
| --- | ---: | --- | --- |
| [1. Linux essentials](curriculum/phase-1-linux-essentials.md) | 1–10 | Files, Nano, grep, pipes, processes, disk and memory | Write a system-report script |
| [2. Logs, errors, networks, and SSH](curriculum/phase-2-logs-network-ssh.md) | 11–20 | Exit codes, logs, services, ports, HTTP, SSH | Diagnose a small local server |
| [3. Git, GitHub, and coding assistants](curriculum/phase-3-git-github-codex.md) | 21–30 | Commits, branches, pull requests, Codex context | Complete one reviewed AI-assisted PR |
| [4. Python, uv, and ML basics](curriculum/phase-4-python-uv-ml.md) | 31–40 | Python project setup, data, tests, classification, API | Serve a trained classifier locally |
| [5. PM2, Docker, and Azure](curriculum/phase-5-docker-azure.md) | 41–50 | Process management, containers, Compose, cloud resources | Run the containerized API on an Azure VM |
| [6. CI/CD and operations](curriculum/phase-6-delivery-operations.md) | 51–60 | GitHub Actions, image delivery, security, monitoring, recovery | Redeploy and troubleshoot from the runbook |

## What you need

- A Linux machine, Linux VM, WSL, or other Ubuntu-like shell
- A GitHub account
- An editor; Nano is taught and VS Code is optional
- Python 3.11 or newer and `uv`
- Docker for the container phase
- An Azure account for Days 47–60
- Codex, Claude Code, or another coding assistant for Days 28–30

Azure resources can cost money. Create the smallest suitable VM, configure a budget alert, use synthetic data, and delete the resource group when finished. If Azure is unavailable, use any Ubuntu VM and keep the same SSH and Docker tasks.

## Ground rules

1. Type foundational commands yourself and explain their output.
2. Never commit passwords, API keys, private SSH keys, or `.env` files.
3. Read the error before searching for a fix.
4. Change one thing at a time, then verify it.
5. Use AI assistants for bounded help; inspect their diff and run the checks yourself.
6. Prefer a small working project over a large unfinished architecture.

## Completion means you can

- move around Linux, edit files, search text, and inspect disk, memory, ports, and processes;
- find a useful error in logs and explain the likely cause;
- connect to a VM with SSH and identify its Azure resources;
- make a Git branch, commit, pull request, merge, and recover from a simple mistake;
- create a Python project with `uv`, test it, and train a basic classifier;
- run and inspect the API with PM2 and Docker;
- use GitHub Actions to test and build the project;
- deploy the same container to Azure and troubleshoot it using a written checklist;
- give Codex or another coding assistant only the context needed for a small task.

See the [project brief](projects/capstone.md), [AI-assistant guide](guides/ai-assisted-development.md), and [resource shelf](resources/README.md) when needed.

