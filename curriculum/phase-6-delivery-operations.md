# Phase 6: Delivery and Operations

**Days 51–60 · Outcome:** automate trustworthy delivery, deploy the capstone, operate it against explicit reliability targets, recover from failure, and communicate the work as an engineering case study.

Create a `phase-6` branch. Use a staging environment first. Production deployment is optional if it would expose data, create unacceptable cost, or violate an organization's policy.

## Day 51: Continuous integration with GitHub Actions

**Learn:** Workflows, events, jobs, runners, steps, actions, artifacts, matrices, caches, required checks, least-privilege tokens, and the difference between continuous integration, delivery, and deployment.

**Build:** Add CI triggered by pull requests and pushes to `main`. Run formatting/lint checks, types, unit tests, API integration tests with service containers, frontend tests, and the deterministic AI evaluation subset. Upload useful reports on failure.

**Ship:** Protect `main` so the workflow must pass before merge. Intentionally break one check and capture evidence that CI blocks it.

**Check:** CI uses declared dependencies from a clean environment and does not require paid model calls or repository secrets for forked pull requests.

**Resources:** [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) · [Building and testing Python](https://docs.github.com/en/actions/how-tos/use-cases-and-examples/building-and-testing/building-and-testing-python) · [GitHub Actions service containers](https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)

## Day 52: Fast, trustworthy, and secure CI

**Learn:** Dependency caching versus artifacts, job parallelism, cancellation, flaky tests, action pinning, token permissions, OpenID Connect, dependency review, secret scanning, code scanning, SBOMs, provenance, and untrusted pull-request threats.

**Build:** Split independent CI work into parallel jobs, cache using lockfile keys, cancel superseded runs, set explicit timeouts and minimal `permissions`, and pin third-party actions to reviewed commit SHAs where feasible. Add dependency and secret checks appropriate to repository visibility.

**Ship:** Measure cold and warm CI duration. Add a short workflow threat model covering untrusted code, credentials, artifact integrity, and dependency changes.

**Check:** No privileged deployment secret is exposed to arbitrary PR code; cache misses affect speed, not correctness.

**Resources:** [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) · [GitHub dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) · [GitHub artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations)

## Day 53: Continuous delivery and rollbacks

**Learn:** Environments, promotion, approvals, immutable artifacts, build-once/promote-many, database migration compatibility, expand/contract changes, canary/blue-green/rolling deployment, feature flags, smoke tests, and rollback versus roll-forward.

**Build:** Design a workflow that builds immutable images on a version tag, scans them, records digests, deploys those exact digests to staging, runs migrations and smoke tests, and requires approval for production. Authenticate to cloud using OIDC where supported.

**Ship:** Write and rehearse a rollback plan for application code, configuration, and a backward-compatible database change. Add a deployment checklist with stop conditions.

**Check:** Re-running a deployment is idempotent; a failed smoke test halts promotion and leaves an observable event.

**Resources:** [GitHub deployment environments](https://docs.github.com/en/actions/reference/deployments-and-environments) · [GitHub OIDC for cloud](https://docs.github.com/en/actions/concepts/security/openid-connect) · [Martin Fowler: blue-green deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html)

## Day 54: Deploy to staging

**Learn:** Platform configuration, managed database connections, secrets, DNS, TLS, reverse proxies, process scaling, migrations, static assets, and smoke testing in a real environment.

**Build:** Deploy Grounded to staging through the delivery workflow. Configure an HTTPS URL, restricted CORS, managed secrets, database backups, log/trace export, health probes, and minimum/maximum scaling or spending limits. Seed only synthetic data.

**Ship:** A deployment record with commit SHA, image digests, migration version, config version, smoke-test result, and rollback target. Store no secret values in the record.

**Check:** A new checkout can discover the URL and deployment procedure; direct database access is restricted; application and worker can be rolled independently when safe.

**Resources:** Use your selected platform's official deployment guide · [Let's Encrypt: how it works](https://letsencrypt.org/how-it-works/) · [The Twelve-Factor App: processes](https://12factor.net/processes)

## Day 55: SLOs, alerts, and runbooks

**Learn:** Service-level indicators, objectives and agreements, availability and latency, error budgets, symptoms versus causes, actionable alerts, burn rates, on-call handoff, and runbooks.

**Build:** Define a small set of user-centered SLIs: successful API requests, successful grounded answers, p95 latency, and ingestion completion. Set initial SLOs from observed staging behavior. Build a dashboard and two symptom-based alerts with enough context to act.

**Ship:** Write a runbook for “answers are failing or slow” with impact, triage queries, dependency checks, mitigations, escalation, recovery verification, and links—not passwords.

**Check:** Trigger a safe synthetic failure and use the alert plus runbook to identify it. Tune noisy or unactionable signals.

**Resources:** [Google SRE workbook: SLOs](https://sre.google/workbook/implementing-slos/) · [Google SRE: practical alerting](https://sre.google/sre-book/practical-alerting/) · [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/)

## Day 56: Failure drills, backups, and recovery

**Learn:** Failure modes, fault injection, graceful degradation, recovery point objective (RPO), recovery time objective (RTO), backup versus replication, restore testing, disaster recovery, incident roles, and blameless review.

**Build:** Safely simulate one dependency timeout, worker termination, bad deployment/configuration, and database restore into a disposable environment. Verify the UI degrades clearly and jobs remain recoverable. Measure actual recovery time and data loss.

**Ship:** Complete the [incident review template](../templates/incident-review.md) for the most instructive drill and update the runbook with what was missing.

**Check:** A backup is not considered valid until a restore is verified; the drill never targets real user data.

**Resources:** [Google SRE: postmortem culture](https://sre.google/sre-book/postmortem-culture/) · [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) · [Principles of chaos engineering](https://principlesofchaos.org/)

## Day 57: Load testing and capacity

**Learn:** Workload models, throughput, concurrency, saturation, percentiles, coordinated omission, warm-up, bottlenecks, rate limiting, queue depth, capacity envelopes, and cost under load.

**Build:** Define a realistic read/write/question mix with synthetic data. Load test staging gradually, stop at a safe budget/limit, and observe API, database, queue, retrieval, and model-provider behavior. For paid model calls, substitute a latency/error-controlled fake for most load.

**Ship:** A capacity report with environment, workload, p50/p95/p99, error rate, saturation point, bottleneck, cost projection, and next scaling action.

**Check:** The test has explicit stop conditions and does not accidentally test a third-party service or exceed provider limits.

**Resources:** [k6 documentation](https://grafana.com/docs/k6/latest/) · [Locust documentation](https://docs.locust.io/) · [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/)

## Day 58: Releases, documentation, and decisions

**Learn:** Semantic versioning, changelogs, release notes, deprecation, architecture decision records, user versus operator documentation, reproducible demos, and communicating limitations honestly.

**Build:** Audit onboarding from a clean clone. Write concise architecture, local development, testing, deployment, operations, API, evaluation, data/privacy, and troubleshooting sections. Close or label stale assumptions. Turn noteworthy choices into ADRs.

**Ship:** Prepare `v1.0.0` release notes containing capabilities, evidence, known limitations, upgrade/migration notes, rollback target, and image digests. Generate an SBOM if your build platform supports it.

**Check:** Ask another person—or a fresh environment—to follow the README without oral instructions and record every point of friction.

**Resources:** [Semantic Versioning](https://semver.org/) · [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · [Architecture Decision Records](https://adr.github.io/)

## Day 59: Production readiness review

**Learn:** Release gates, risk acceptance, launch criteria, ownership, support boundaries, rollback signals, and why unresolved high-severity findings outweigh a deadline.

**Build:** Review the capstone against the [definition of done](../projects/capstone.md#definition-of-done). Run all tests/evals/scans, restore from backup, verify dashboards and alerts, inspect permissions and costs, rotate a practice credential, and rehearse deployment plus rollback.

**Ship:** Sign a dated readiness review listing evidence links, open risks with owners, launch decision, and rollback triggers. Fix blockers; do not relabel them as documentation issues.

**Check:** Someone other than the author can operate the service using the repository and runbook.

**Resources:** [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [Production readiness checklist ideas](https://gruntwork.io/devops-checklist/) · [Google SRE workbook](https://sre.google/workbook/table-of-contents/)

## Day 60: Launch, teach, and plan the next 90 days

**Build:** Promote the reviewed artifact to your chosen final environment, or run a production-like local launch if public deployment is unsafe or unaffordable. Execute smoke tests, observe it, and roll back if a launch criterion fails.

**Ship:** Tag `v1.0.0` and `day-60`. Publish a short case study covering the problem, architecture, hardest tradeoff, evaluation evidence, incident lesson, cost/latency result, security posture, limitations, and live/demo links. Record a five-minute engineering walkthrough.

**Teach:** Explain one subsystem to another learner without slides. Answer questions using code, diagrams, logs, and measurements.

**Continue:** Write a 90-day plan driven by your gaps: deeper ML/math, data engineering, Kubernetes/Terraform, a cloud certification, open-source contribution, or a second domain-specific AI product. Choose one—not all.

**Check:** The portfolio tells an evidence-based engineering story, not “I followed a tutorial.” Tear down unused cloud resources and keep budget alerts enabled.

**Resources:** [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) · [Diátaxis documentation framework](https://diataxis.fr/) · [Google technical writing courses](https://developers.google.com/tech-writing)

## Phase 6 exit ticket

Deploy a known artifact, identify it by commit and digest, observe a request, explain the SLO, diagnose a synthetic failure, restore or roll back, and show the evaluation evidence. If you can do that, you have moved beyond a demo into production-minded AI engineering.

