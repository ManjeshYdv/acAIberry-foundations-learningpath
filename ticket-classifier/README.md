# Ticket Classifier Student Workspace

This directory is where the student completes the practical work from all 60 days. It is intentionally almost empty at the beginning.

The student is building one small application that receives a support message and predicts one of three categories:

```text
Input:  "I was charged twice for my subscription"
Output: "billing"
```

The allowed labels are:

- `billing`
- `account`
- `technical`

No paid AI API, database, frontend, or advanced model is required.

## Do not build everything on Day 1

Follow the linked [60-day tracker](../CURRICULUM.md) in order. The first 30 days prepare the workspace and teach the tools. The Python classifier begins on Day 31.

| Days | What the student does in this directory |
| ---: | --- |
| 1–10 | Creates practice data, Linux notes, and `scripts/system-report.sh` |
| 11–20 | Creates local logs, broken examples, and a server-diagnosis note |
| 21–30 | Tracks the existing work with Git and improves one script through a reviewed PR |
| 31–40 | Builds, tests, trains, and serves the Python ticket classifier |
| 41–50 | Runs the API with PM2, Docker, Compose, and an Azure VM |
| 51–60 | Adds CI/CD at the repository root and practices monitoring and recovery |

## Starting Day 1

Run this from the root of the cloned or forked course repository:

```bash
mkdir -p ticket-classifier/{notes,scripts,data,logs}
cd ticket-classifier
pwd
ls -la
```

The directory should now look like:

```text
ticket-classifier/
├── data/
├── logs/       # ignored by Git
├── notes/
├── scripts/
├── .gitignore
└── README.md
```

Daily notes go in `notes/day-01.md`, `notes/day-02.md`, and so on. Runtime logs stay in `logs/` and are not committed. Copy only small, non-sensitive log excerpts into the daily note when they are useful proof.

## Checkpoint 1: expected by Day 10

```text
ticket-classifier/
├── data/
│   ├── practice/
│   └── tickets.txt
├── notes/
│   ├── day-01.md ... day-10.md
│   ├── label-counts.txt
│   ├── processes.md
│   ├── resources.md
│   └── system-report.txt
└── scripts/
    └── system-report.sh
```

The student should be able to run:

```bash
bash scripts/system-report.sh
```

It should print the user, host, date, disk, memory, project size, and top memory-consuming processes without changing the machine.

## Checkpoint 2: expected by Day 20

Add notes showing that the student can read errors and diagnose a local HTTP server:

```text
ticket-classifier/
├── logs/                       # remains local and ignored
├── notes/
│   ├── error-reading.md
│   ├── service-check.md
│   ├── http.md
│   └── day-20-diagnosis.md
├── scripts/system-report.sh
└── .env.example               # placeholders only
```

The Day 20 diagnosis must connect these facts:

```text
command -> process/PID -> listening port -> HTTP status -> log line -> cause/fix
```

The student also creates an SSH key outside this repository for later Azure access. The private key must never appear here.

## Checkpoint 3: expected by Day 30

The project contents are mostly unchanged, but the student must show good Git practice:

- daily commits on the phase branch;
- tracker proof links;
- a short `AGENTS.md` with project paths, safe commands, and completion checks;
- one issue and pull request for a small script improvement;
- a reviewed `git diff` and command output proving the change works.

Codex or another coding assistant helps with only that bounded change. The student must explain every accepted line.

## Checkpoint 4: build the classifier on Days 31–40

By Day 40, this directory should contain:

```text
ticket-classifier/
├── artifacts/                  # generated and ignored
│   └── model.joblib
├── data/
│   └── tickets.csv
├── src/
│   └── ticket_classifier/
│       ├── __init__.py
│       ├── api.py
│       ├── data.py
│       ├── predict.py
│       ├── text.py
│       └── train.py
├── tests/
│   ├── test_api.py
│   ├── test_data.py
│   └── test_text.py
├── .env.example
├── .gitignore
├── AGENTS.md
├── pyproject.toml
└── uv.lock
```

### Data contract

`data/tickets.csv` contains only synthetic examples:

```csv
text,label
"I was charged twice",billing
"I cannot reset my password",account
"The application keeps crashing",technical
```

Create at least 10 examples for each label. Never use real customer messages.

### Required Python responsibilities

- `text.py`: clean text and reject empty input.
- `data.py`: read/validate CSV columns and rows.
- `train.py`: split the data, train TF-IDF plus logistic regression, print metrics, and save `artifacts/model.joblib`.
- `predict.py`: load the saved model and predict one supplied message.
- `api.py`: expose `GET /health` and `POST /predict`.
- `tests/`: verify text cleanup, invalid data, and API behavior.

### Commands that must work by Day 40

Run these from `ticket-classifier/`:

```bash
uv sync
uv run pytest -q
uv run python -m ticket_classifier.train
uv run python -m ticket_classifier.predict "I cannot sign in"
uv run uvicorn ticket_classifier.api:app --host 127.0.0.1 --port 8000
```

From a second terminal:

```bash
curl --fail http://127.0.0.1:8000/health

curl --fail \
  -X POST http://127.0.0.1:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{"text":"I was charged twice"}'
```

Expected response shape:

```json
{"category":"billing"}
```

The exact confidence value is optional. A missing model or invalid request must return a clear error.

## Checkpoint 5: expected by Day 50

Add these files:

```text
ticket-classifier/
├── Dockerfile
├── .dockerignore
├── compose.yaml
├── ecosystem.config.cjs
└── notes/
    ├── api-process.md
    ├── azure-plan.md
    ├── azure-vm.md
    └── azure-deploy.md
```

The same API is operated in three ways:

1. `uv run uvicorn ...` teaches a normal Linux process.
2. PM2 teaches start, stop, restart, status, and logs for that process.
3. Docker/Compose creates the repeatable deployment used on Azure.

PM2 does not run inside the container.

Required local container commands:

```bash
docker build -t ticket-api:local .
docker compose up -d
docker compose ps
docker compose logs --since 10m
curl --fail http://127.0.0.1:8000/health
docker compose down
```

On Azure, the API port remains bound to the VM loopback interface. The student reaches it from their computer with an SSH tunnel:

```bash
ssh -i PATH_TO_KEY -L 8000:127.0.0.1:8000 USERNAME@VM_PUBLIC_IP
```

Placeholders must be replaced locally; private key contents are never committed.

## Checkpoint 6: expected by Day 60

GitHub Actions workflows belong at the **course repository root**, not inside this directory:

```text
acAIberry-foundations-learningpath/
├── .github/
│   └── workflows/
│       ├── content-quality.yml
│       └── student-ci.yml
└── ticket-classifier/
```

`student-ci.yml` must:

1. run the tests with `ticket-classifier` as its working directory;
2. build the image from `ticket-classifier/`;
3. publish a tagged image to GHCR only after checks pass;
4. use minimal GitHub token permissions.

The final proof is not more code. The student must use the [runbook](../templates/runbook.md) to redeploy a known image, call both endpoints, find the request in logs, inspect VM resources, and diagnose one controlled failure.

## What is not required

Do not add these during the 60 days:

- a frontend;
- a database;
- authentication;
- an LLM or paid API;
- RAG or agent frameworks;
- Kubernetes;
- multiple cloud environments.

Finishing and understanding this small service is the objective.
