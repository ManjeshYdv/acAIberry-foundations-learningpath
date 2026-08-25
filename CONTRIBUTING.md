# Contributing

Changes should keep this path simple, connected, and beginner-friendly.

## A good daily task

- teaches one main idea;
- takes roughly 60–90 focused minutes;
- uses the existing Ticket Classifier project;
- names only the commands needed that day;
- has one observable “done when” condition;
- links to one or two stable primary resources.

Do not add an advanced framework because it is popular. Open an issue first if a change adds a new service, cloud product, language, or paid requirement.

## Pull requests

Explain the learner problem, affected day, and how the revision makes the path clearer. Then run:

```bash
python3 scripts/validate_curriculum.py
```

Review every changed link and rendered heading. Examples must use synthetic data and placeholders—never credentials, private SSH keys, real customer data, or paid API keys.

