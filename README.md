# acAIberry Foundations Learning Path

> A project-first, 60-day path from a blank terminal to a deployed, observable AI application.

AI engineering is more than calling a model API. A production AI engineer must be able to navigate Linux, collaborate with Git, write maintainable software, build APIs and interfaces, work with data, evaluate model behavior, package services, automate delivery, and operate what they ship. This learning path connects those skills through one continuous capstone instead of teaching them as isolated tutorials.

## What you will build

Over 60 days, you will build **Grounded**: a source-citing AI knowledge assistant for a document collection you choose. It begins as a command-line utility and grows into a full-stack service with:

- a typed Python ingestion pipeline;
- a FastAPI backend and React/TypeScript interface;
- PostgreSQL persistence and vector retrieval;
- model-provider integration, structured outputs, tools, and RAG;
- automated tests, evaluations, security checks, and observability;
- Docker-based local environments and GitHub Actions CI/CD;
- a staged cloud deployment with monitoring, rollback, and a runbook.

The model provider and cloud platform are replaceable. The engineering practices are not.

## Who this is for

This path is designed for early-career developers, self-taught programmers, and software engineers moving into applied AI. You should be comfortable using a computer and reading basic code. Prior Linux, cloud, or machine-learning experience is not required.

Plan for **2–3 focused hours per day**, six days per week. If a day takes longer, split it. Understanding and a working artifact matter more than the calendar.

## The 60-day map

| Phase | Days | Focus | Milestone |
| --- | ---: | --- | --- |
| [1. Developer foundations](curriculum/phase-1-developer-foundations.md) | 1–10 | Linux, shell, networking, Git, GitHub, AI coding tools | A tested environment-diagnostics CLI |
| [2. Python engineering](curriculum/phase-2-python-engineering.md) | 11–20 | Python, types, testing, tooling, configuration, packages | A reliable document-ingestion package |
| [3. Full-stack systems](curriculum/phase-3-full-stack-systems.md) | 21–30 | HTTP, FastAPI, SQL, PostgreSQL, auth, React, async work | A database-backed web application |
| [4. Applied AI systems](curriculum/phase-4-applied-ai.md) | 31–40 | ML/LLM concepts, APIs, prompting, tools, embeddings, RAG | A source-citing AI assistant |
| [5. Production readiness](curriculum/phase-5-production-readiness.md) | 41–50 | Evals, safety, observability, performance, Docker, cloud | A measured, containerized release candidate |
| [6. Delivery and operations](curriculum/phase-6-delivery-operations.md) | 51–60 | CI/CD, deployment, SLOs, resilience, load, releases | A deployed capstone and engineering case study |

See the [complete curriculum](CURRICULUM.md) for the day-by-day index.

## How each day works

Every day has four parts:

1. **Learn** — study a small set of concepts from primary documentation or a high-quality course.
2. **Build** — apply the concept to the capstone or a focused exercise.
3. **Ship** — leave evidence: a commit, test, diagram, benchmark, decision record, or deployment.
4. **Reflect** — write three lines: what changed, what failed, and what you would do differently.

Use the [daily log template](templates/daily-log.md). Keep changes small enough to review. End milestone days by tagging the repository (`day-10`, `day-20`, and so on).

## Production rules from day one

- Never commit credentials. Use environment variables, a secret manager, and a checked-in `.env.example`.
- Prefer small, reviewable commits and pull requests, even when working alone.
- Treat generated code as untrusted until you can explain it, test it, and inspect its diff.
- Validate data at every system boundary. Time out network calls and handle failure explicitly.
- Add a test when fixing a bug. Record important architectural choices in an ADR.
- Measure model quality with a versioned evaluation set; do not judge it only by a few demos.
- Keep development reproducible: lock dependencies, automate checks, and document commands.
- Optimize only after measuring latency, quality, and cost.

## Set up your learning repository

Create a separate repository for your capstone so this curriculum stays clean:

```bash
mkdir grounded-ai && cd grounded-ai
git init
mkdir -p apps/api apps/web packages/ingestion tests docs/adr
touch README.md .gitignore .env.example
git add . && git commit -m "chore: initialize capstone"
```

Choose supported versions of Python, Node.js, Git, and Docker for your operating system. Record the versions in the capstone README instead of relying on whatever happens to be installed globally.

## Using AI coding assistants well

Codex, Claude Code, and similar tools are part of the curriculum, but they are not substitutes for the fundamentals. Use them to explore an unfamiliar repository, propose a plan, implement a bounded change, write tests, or review a diff. You remain responsible for requirements, verification, security, and the final decision.

Start with the [AI-assisted development guide](guides/ai-assisted-development.md). It includes a reusable task prompt, review checklist, and links to the official Codex and Claude Code documentation.

## Completion standard

You have completed the path when you can demonstrate all of the following without hiding behind a tutorial:

- explain the request path from browser to API, database, retrieval system, model, and back;
- reproduce the application locally from a fresh clone with documented commands;
- make a change through a branch, tested pull request, and automated deployment;
- show an evaluation report and explain where the AI system fails;
- find a production problem using logs, metrics, and traces;
- restore or roll back the service using a written runbook;
- explain the security, privacy, latency, quality, and cost tradeoffs you made.

The detailed acceptance criteria are in the [capstone brief](projects/capstone.md).

## Repository guide

```text
.
├── curriculum/       # Six detailed 10-day phases
├── guides/           # Working practices used throughout the path
├── projects/         # Capstone specification and checkpoints
├── resources/        # Curated reference library
├── templates/        # Daily logs, ADRs, and incident reviews
└── scripts/          # Dependency-free curriculum validation
```

## Scope

This is an **applied AI engineering foundation**, not a complete data-science or model-training degree. It teaches enough ML theory to reason about data, metrics, embeddings, and LLM behavior, then concentrates on building dependable products around models. Distributed training, advanced mathematics, CUDA kernels, and research-level model architecture are valuable next steps, but intentionally outside these 60 days.

## Contributing

Corrections and resource improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Prefer stable, accessible, primary sources and explain which learning objective a new resource improves.

