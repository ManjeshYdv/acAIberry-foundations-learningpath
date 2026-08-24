# Contributing

Thank you for helping improve this learning path. Contributions should make a learner more capable, not merely make the repository larger.

## Before proposing a change

- Open an issue for a new topic, structural change, or replacement of a major resource.
- State the learner problem and the day or outcome affected.
- Prefer stable primary documentation, standards, and maintained practical courses.
- Check that a proposed resource is accessible and does not unexpectedly require payment or account creation.
- Do not add affiliate, referral, tracking, pirated, or scraped-content links.

## Curriculum principles

Every required day should remain achievable in roughly 2–3 focused hours and include:

1. a clear learning objective;
2. a hands-on build tied to the capstone or a focused exercise;
3. reviewable evidence of completion;
4. an observable acceptance check;
5. a small number of directly relevant resources.

Protect the progression: fundamentals before frameworks, deterministic software before probabilistic features, evaluation before optimization, and staging before production.

## Pull requests

Keep changes focused and explain:

- what learner problem the change solves;
- which days/files change and why;
- how you checked technical claims and links;
- whether the expected time, prerequisites, scope, or cost changed.

Run the repository validation before opening a PR:

```bash
python3 scripts/validate_curriculum.py
```

Review rendered Markdown, headings, relative links, day numbering, spelling, and command safety. Never include credentials, private data, or paid-service keys in examples.

## Style

- Use plain language and define jargon on first use.
- Prefer active voice and instructions with observable outcomes.
- Use `Learn`, `Build`, `Ship`, and `Check` consistently in daily lessons.
- Use sentence case for headings.
- Keep vendor-specific choices replaceable unless the lesson teaches that vendor directly.
- Label optional work clearly so it does not hide the core path.

By contributing, you confirm that you have the right to submit the content. A repository license has not been selected in this initial version; maintainers should choose one before accepting substantial external contributions.

