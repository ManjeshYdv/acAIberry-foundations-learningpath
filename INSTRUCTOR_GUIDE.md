# Instructor Guide

The course repository should remain the shared curriculum. Student work should stay in student-owned forks or GitHub Classroom repositories.

## Choose the tracking model

### One to five students

Use forks:

1. Each student forks and clones the course.
2. Each student shares their fork URL.
3. Each student completes one branch and PR per 10-day phase inside their fork.
4. Each student submits six checkpoint issues to this repository using the supplied issue form.
5. You review the PR, ask for a short demonstration, and close the submission issue as approved or revision requested.

For a private student repository, the student must invite you as a collaborator.

### Larger or private cohorts

Use [GitHub Classroom](https://classroom.github.com/) rather than manually managing many forks. Create an individual assignment from a frozen course version and use the Classroom roster/dashboard. Keep the same daily tracker and six checkpoint reviews.

## Freeze a cohort version

Avoid changing instructions while a student is completing a phase. Before a cohort starts, tag the curriculum:

```bash
git switch main
git pull --ff-only origin main
git tag course-YYYY-MM
git push origin course-YYYY-MM
```

Tell students which tag or start date applies. Publish urgent corrections clearly and have students sync only after their current checkpoint is merged.

## Maintain a simple roster

Use a GitHub Project or a small private spreadsheet with these columns:

| Student | Fork/Classroom repo | Current day | Latest checkpoint PR | Review status | Last activity | Blocker |
| --- | --- | ---: | --- | --- | --- | --- |

Recommended review statuses are `Not started`, `In progress`, `Needs review`, `Needs revision`, and `Complete`.

The checkpoint issues in this repository provide a central submission queue. Add them to a [GitHub Project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) if you are tracking several students.

## Review only six checkpoints

| Days | Required demonstration |
| ---: | --- |
| 1–10 | Navigate, edit with Nano, search with grep, inspect `htop`, and run the system report |
| 11–20 | Find a PID/port, reproduce an HTTP error, locate its log, and explain the cause |
| 21–30 | Show branch, commits, PR, and what context was given to the coding assistant |
| 31–40 | Sync dependencies, run tests, train the model, start the API, and call `/predict` |
| 41–50 | SSH to Azure, inspect resources, show the container/logs, and use the SSH tunnel |
| 51–60 | Show passing CI, identify the deployed image, redeploy it, and diagnose one failure |

## Checkpoint rubric

Mark each category `Pass` or `Revise`:

- **Completion:** required tracker days and checkpoint artifact are present.
- **Evidence:** commands, logs, tests, or screenshots support the claim.
- **Understanding:** the student can explain the command and output without reading an AI answer.
- **Git practice:** commits are understandable and the PR is reviewable.
- **Safety:** no secret, private key, customer data, unsafe permission, or uncontrolled cloud cost.
- **Recovery:** the student can correct one small mistake or explain the next diagnostic step.

Approve the checkpoint when all six pass. Give a specific repeat task for anything marked `Revise`.

## What not to use as the main score

- number of commits or lines changed;
- time spent online;
- a polished README without a working demonstration;
- AI-generated explanations the student cannot reproduce;
- completion speed compared with other students.

The strongest check is a five-to-ten-minute live demonstration with one small variation chosen by the instructor.

## Instructor review comment

```text
Checkpoint:
Result: Pass / Revise

What worked:
-

Repeat or fix:
-

Live demonstration:
-

Next phase approved: Yes / No
```
